import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = 'Clave nueva'
    SESSION_COOKIE_SECURE = False


class DevelopmentCongig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_UTL = 'mysql+pymysql://root:Soporte2003:root@127.0.0.1/bdidgs801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
