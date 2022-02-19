from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #Next time, will start with handling the db 1.13

def init_app(): 
    application = Flask(__name__)
    application.config['SECRET_KEY'] = 'mysecretkeysami'

    from .views import views
    from .auth import auth

    application.register_blueprint(views, url_prefix=('/'))
    application.register_blueprint(auth, url_prefix=('/'))

    return application

