from flask import Blueprint, request, redirect, url_for, render_template, flash
from .models import Email, db
import os
from sqlalchemy.exc import IntegrityError

# Initialize blueprint within the current module (so Flask
# knows where to look for templates/static files from)
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # GET method, for viewing and input
    return render_template('index.html')

@bp.route('/add_email', methods=['POST'])
def add_email():
    # POST method request. Add email to the database.
    email_address = request.form.get('address')
    
    try:
        email = Email(address=email_address)
        db.session.add(email)
        db.session.commit()
        flash("Success: Thank you for subscribing!", "success")
    except IntegrityError as e:
        # Rollback the transaction
        db.session.rollback()
        flash("Error: email already exists in the database!", "error")
    
    return redirect(url_for('main.index'))

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