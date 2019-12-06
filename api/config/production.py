# Flask settings
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../data-dev.sqlite')

from app import secrets

DEBUG = False
FLASK_SECRET_KEY = 'paPTvnNME5NBHHuIOlFqG6zS77vHadbo'
SQLALCHEMY_DATABASE_URI = secrets.SQLALCHEMY_DATABASE_URI_PRODUCTION
SQLALCHEMY_BINDS = {
    'cm_db':      os.environ.get('DATABASE_URL') or \
                  'sqlite:///' + db_path
}
SECRET_KEY = 'paPTvnNME5NBHHuIOlFqG6zS77vHadbo'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
ERROR_404_HELP = False
RESTPLUS_JSON = {
    'separators': (',', ':')
}
CELERY_BROKER_URL = 'amqp://admin:mypass@rabbit:5672/'
										 
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
UPLOAD_FOLDER = 'uploaded_file'

user = secrets.prod_user
host = secrets.prod_host
password = secrets.prod_password
port = secrets.prod_port
database = secrets.prod_database

MAIL_USERNAME = secrets.MAIL_USERNAME
MAIL_PASSWORD = secrets.MAIL_PASSWORD
MAIL_DEFAULT_SENDER = secrets.MAIL_USERNAME
MAIL_SERVER = secrets.MAIL_SERVER
MAIL_PORT = secrets.MAIL_PORT
