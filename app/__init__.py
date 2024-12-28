from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
scheduler = APScheduler()

# Ensure that the scheduler is only started once
if not hasattr(app, 'scheduler_started'):
    scheduler.init_app(app)
    scheduler.start()
    app.scheduler_started = True

from app import routes

