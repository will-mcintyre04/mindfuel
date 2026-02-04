"""
Package to create and configure a Flask app with SQLAlchemy database support.

Sets up a Flask app instance with configuration options specified
by the `config_name`. It initializes the SQLAlchemy database support and creates
database tables for the defined models, and registers blueprints to app.

Functions
---------
create_app(config_name : str)
    Creates and configures a Flask App with SQLAlchemy ORM database support.

Examples
--------
To create a local SQLite database with a specific configuration:

>>> flask shell
>>> from app.extensions import db
>>> from app.models import Email
>>> db.create_all()
>>> exit()

This will create an `app.db` database with an `emails` table within an `instance` directory. 

Then, to run the app:

>>> flask --app app run
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from .config import app_config
from .extensions import db

def create_app(config_name='development'):
    """
    Flask app factory to configure app with SQLAlchemy database support, default to development.

    Configures flask app instance, database connection and blueprint registration.

    Parameters
    ----------
    config_name : str
        The name of the configuration to use for the Flask app ('development' or 'production')

    Returns
    -------
    app : flask.Flask
        A configured Flask app instance with database connectivity.
    """

    load_dotenv()

    # Create Flask app instance and configure based on environment
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)

    from .routes import bp
    app.register_blueprint(bp)

    return app