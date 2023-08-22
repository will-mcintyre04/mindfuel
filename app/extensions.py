"""
Flask Extensions Configuration.

This module initializes and configures Flask extensions used in the application.
It creates instances of Flask extensions for associations with the Flask app.

Attributes
----------
db : SQLAlchemy
    An instance of SQLAlchemy for database interactions using SQLAlchemy's ORM features.

"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()