from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path 


db = SQLAlchemy() #Next time, will start with handling the db 1.13
db_name = "Notes.db"

def create_app(): 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkeysami'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix=('/'))
    app.register_blueprint(auth, url_prefix=('/'))

    from .models import Note, User

    create_db(app)

    return  app


def create_db(app): 
    if not path.exists('website/' + db_name): 
        db.create_all(app=app)
        print('Databse created')