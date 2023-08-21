from flask import Blueprint, request, jsonify
from .models import Email, db

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