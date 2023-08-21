from flask import Flask
from .config import app_config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../instance/config.py')

    from .routes import bp
    app.register_blueprint(bp)

    return app