import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/webtoons_db'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret'
