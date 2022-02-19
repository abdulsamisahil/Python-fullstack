from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login(): 
    return "<h2>Login Page</h2>"

@auth.route('/sign-up')
def signup(): 
    return "<h2>Register Page</h2>"

@auth.route('/logout')
def logout(): 
    return "<h2>Logout Page</h2>"