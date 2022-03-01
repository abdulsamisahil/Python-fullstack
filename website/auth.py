from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login(): 
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    #if user with the typed email found 
    if user: 
        #Check if the db.stored hash pass equals the user typed pass 
        if check_password_hash(user.password, password): 
            flash('Login succeeded', category='success')
            return redirect(url_for('views.home'))        
        else: 
            flash('Password is incorrect', category='error')
    else: 
        flash('No user with this email exists in our system', category='error')
        
    return render_template("login.html", boolean=True)

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if User.query.filter_by(email=email).first(): 
            flash('User with this email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 3:
            flash('Password must be at least 7 characters.', category='error')
        else:

            new_user = User(first_name=first_name, last_name=last_name, 
            email=email, password=generate_password_hash(password1, method='sha256'))

            db.session.add(new_user)
            db.session.commit()

            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign-up.html", user=current_user)

@auth.route('/logout')
def logout(): 
    return "<h2>Logout Page</h2>"