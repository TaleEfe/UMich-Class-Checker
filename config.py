import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = os.urandom(24)
    CLIENT_KEY = 'm7fTvj1L5YPhBXZvJuYqAQX0zeAhBwMsfF9eYf4nhTcaux3k'
    CLIENT_SECRET = '7hD4GQOmXxd93hRGIwtqTJC0PPjO3Dn1BarHqMgD2JPe2yUsL2sAZyP3MExgFoYC'
    SCOPE = 'umscheduleofclasses'
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SMTP_USERNAME = 'taleefe@gmail.com'
    SMTP_PASSWORD = 'wiaaacwgwodsdnem'
    FROM_EMAIL = 'taleefe@gmail.com'
