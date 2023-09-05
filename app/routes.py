"""
Flask Blueprint Definitions.

This module defines routes and associated views for the app.

Blueprint
---------
bp : flask.Blueprint
    A blueprint object representing the main email update routes.

"""

from flask import Blueprint, request, redirect, url_for, render_template
from .models import Email, db
import os

# Initialize blueprint within the current module (so Flask
# knows where to look for templates/static files from)
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # GET method, for viewing and input
    success = request.args.get('success', False)
    return render_template('index.html', 
                            github_image=os.path.join("static",
                                                     "images",
                                                     "github.png"),
                            success=success)

@bp.route('/add_email', methods=['POST'])
def add_email():
    # POST method request. Add email to database.
    email = Email(address = request.form['address'])
    db.session.add(email)
    db.session.commit()
    return redirect(url_for('main.index', success=True))

@bp.route('/delete_email/<address>', methods=['GET', 'POST'])
def delete_email(address):
    # If GET, show confirmation
    if request.method == 'GET':
        return render_template('confirm_delete.html', address=address)

    # If POST method, delete from the database
    if request.method == 'POST':
        email = Email.query.filter_by(address=address).first()
        
        if email:
            db.session.delete(email)
            db.session.commit()
        else:
            return redirect(url_for('main.index'))
        return redirect(url_for('main.index'))