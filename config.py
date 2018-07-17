import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bebasguelah'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root@localhost/isi_krs'
    SQLALCHEMY_TRACK_MODIFICATIONS = False