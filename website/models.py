from . import db 
from flask_login import UserMixin
from sqlalchemy import func

class Note(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    note_text = db.Column(db.String(20000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))



class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    notes = db.relationship('Note')

