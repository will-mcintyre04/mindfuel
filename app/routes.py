"""
Flask Blueprint for defining routes.

This module defines routes and associated views for the app.

Blueprint
---------
bp : flask.Blueprint
    A blueprint object representing the main email update routes.

"""

from flask import Blueprint, request, jsonify
from .models import Email, db

# Initialize blueprint within the current module (so Flask knows where to look for templates/static files from)
bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "Welcome to the Email Update App!"

@bp.route('/add_email', methods=['POST'])
def add_email():
    data = request.json
    address = data.get('address')

    if not address:
        return jsonify({'error': 'Email address missing'}), 400

    new_email = Email(address=address)
    db.session.add(new_email)
    db.session.commit()

    return jsonify({'message': 'Email added successfully'}), 201