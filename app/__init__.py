from flask import Flask
from .config import app_config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../instance/config.py')

    db.init_app(app) #Connect SQLAlchemy database ORM to the flask app
    with app.app_context():
        db.create_all()#This function scans the defined models (Python classes) that inherit from db.Model and generates the SQL statements required to create the corresponding database tables

    from .routes import bp
    app.register_blueprint(bp)

    return app