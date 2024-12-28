from app import db
from datetime import datetime

class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_number = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(120), nullable=False)
    date_searched = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Search {self.class_number}>'
