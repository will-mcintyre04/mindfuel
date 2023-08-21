"""
Create and configure a Flask app with SQLAlchemy database support.

Sets up a Flask app instance with configuration options specified
by the `config_name`. It initializes the SQLAlchemy database support and creates
database tables for the defined models.

Functions
---------
create_app(config_name : str)
    Creates and configures a Flask App with SQLAlchemy ORM database support

Examples
--------
To create a local SQLite database with a specific configuration:

>>> from app import create_app, db
>>> app = create_app('development')
>>> with app.app_context():
>>>     db.create_all()

This will create an `app.db` database within an `instance` directory.
"""

from flask import Flask
from .config import app_config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app(config_name="development"):
    """
    Flask app factory to configure app with SQLAlchemy database support, default to development.

    Parameters
    ----------
    config_name : str
        The name of the configuration to use for the Flask app ('development' or 'production')

    Returns
    -------
    app : flask.Flask
        A configured Flask app instance with database connectivity.
    """

    # Load environment variables
    load_dotenv()

    # Create Flask app instance and configure based on environment
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    # Connect SQLAlchemy database ORM to the flask app
    db.init_app(app)

    # Register Blueprint to configure routes and views
    from .routes import bp
    app.register_blueprint(bp)

    return app