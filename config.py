DEBUG = True

USERNAME = 'adb360'
PASSWORD = '1234'
SERVER = 'localhost'
DB = 'flask_fundamentos'

SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "minha-chave-secreta"

BABEL_DEFAULT_LOCALE = 'pt'

