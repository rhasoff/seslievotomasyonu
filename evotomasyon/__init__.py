  
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '7da0e967-a3e2-4976-96e4-1538c12fd28e'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # ADMINS = ['your-email@example.com']
    # POSTS_PER_PAGE = 25



app = Flask(__name__)
# app.config['SECRET_KEY'] = '7da0e967-a3e2-4976-96e4-1538c12fd28e'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config.from_object(Config)
db = SQLAlchemy(app)

from evotomasyon import routes


