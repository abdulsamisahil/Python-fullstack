from flask import Flask

def init_app(): 
    application = Flask(__name__)
    application.config['SECRET_KEY'] = 'mysecretkeysami'

    from .views import views
    from .auth import auth

    application.register_blueprint(views, url_prefix=('/'))
    application.register_blueprint(auth, url_prefix=('/'))

    return application

