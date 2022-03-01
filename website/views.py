from flask import Blueprint, jsonify, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db 
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home(): 
    if request.method == 'POST': 
        note = request.form.get('note')

        if len(note) < 1: 
            flash('Note is very short', category='error')
        else: 
            new_note = Note(note_text=note, uid=current_user.id)
            #print(note)
            db.session.add(new_note)
            db.session.commit()
            flash('New note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note(): 
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note: 
        if note.uid == current_user.id: 
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
