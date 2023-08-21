"""
Defines the model class representing the "Email" table within the database.

Classes
-------
Email:
    Model class representing an email address.
"""

from . import db

class Email(db.Model):
    """
    Model class representing an email address.

    This class defines the structure of the 'Email' table in the database. Each instance of
    this class represents a unique email address.

    Attributes
    ----------
    id : int
        The primary key identifier for the email record.
    address : str
        The email address itself, stored as a string.
        Example: "user@example.com"

    """

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), unique=True, nullable=False)