from flask import render_template, request, redirect, url_for, flash, current_app
from app import app, db, scheduler
from app.models import Search
import requests
import smtplib
from email.mime.text import MIMEText

def get_oauth_token():
    token_url = 'https://gw.api.it.umich.edu/um/oauth2/token'
    payload = {
        'grant_type': 'client_credentials',
        'client_id': current_app.config['CLIENT_KEY'],
        'client_secret': current_app.config['CLIENT_SECRET'],
        'scope': current_app.config['SCOPE']
    }
    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(token_url, headers=headers, data=payload, timeout=30)
    response.raise_for_status()
    return response.json()['access_token']

def fetch_class_info(token, class_number):
    url = f"https://gw.api.it.umich.edu/um/Curriculum/SOC/Terms/2510/Classes/{class_number}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    class_info = response.json()
    available_seats = class_info.get('getSOCSectionListByNbrResponse', {}).get('ClassOffered', {}).get('AvailableSeats', 'N/A')
    return available_seats

def send_email(subject, body, to_email):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = current_app.config['FROM_EMAIL']
    msg['To'] = to_email

    with smtplib.SMTP(current_app.config['SMTP_SERVER'], current_app.config['SMTP_PORT']) as server:
        server.starttls()
        server.login(current_app.config['SMTP_USERNAME'], current_app.config['SMTP_PASSWORD'])
        server.sendmail(current_app.config['FROM_EMAIL'], to_email, msg.as_string())
        print(f"Sent email to {to_email}")

def check_seats():
    with app.app_context():
        searches = Search.query.all()
        token = get_oauth_token()
        for search in searches:
            available_seats = fetch_class_info(token, search.class_number)
            send_email("Class Availability Update", f"Available Seats: {available_seats}", search.user_email)

scheduler.add_job(id='Scheduled Task', func=check_seats, trigger='interval', seconds=60)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        class_number = request.form['class_number']
        user_email = request.form['user_email']
        new_search = Search(class_number=class_number, user_email=user_email)
        db.session.add(new_search)
        db.session.commit()
        flash('Your search has been added!', 'success')
        return redirect(url_for('index'))
    return render_template('index.html')