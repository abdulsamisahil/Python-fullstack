from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #Next time, will start with handling the db 1.13

def init_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkeysami'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix=('/'))
    app.register_blueprint(auth, url_prefix=('/'))

    return  app
