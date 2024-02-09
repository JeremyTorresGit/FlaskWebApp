from flask import Blueprint, render_template, request, flash, jsonify
#roots and url stored
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__) #name of blueprint

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) # data turned json
    noteId = note['noteId'] #find note
    note = Note.query.get(noteId) #get note
    if note: #true?
        if note.user_id == current_user.id: #correct user?
            db.session.delete(note)
            db.session.commit()

    return jsonify({}) # returns nothing
