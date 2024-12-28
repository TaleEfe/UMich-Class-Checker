import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = os.urandom(24)
    CLIENT_KEY = 'Key'
    CLIENT_SECRET = 'Secret'
    SCOPE = 'umscheduleofclasses'
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_USERNAME = 'taleefe@gmail.com'
    SMTP_PASSWORD = 'Password'
    FROM_EMAIL = 'taleefe@gmail.com'
