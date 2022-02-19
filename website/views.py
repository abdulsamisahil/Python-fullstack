from flask import Blueprint, render_template, request
from flask_login import current_user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home(): 
    if request.method == 'POST': 
        note = request.form.get('note')
        print(note)

    return render_template("home.html", user=current_user)