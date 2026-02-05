
import os
import secrets

class Config:
    """
    Base configuration class for Flask application.

    This class defines the base configuration settings that are shared across all environments.
    It provides configuration options for SQLAlchemy and can be inherited by environment-specific
    configuration classes.

    Attributes
    ----------
    SQLALCHEMY_TRACK_MODIFICATIONS : bool
        Controls whether SQLAlchemy should track modifications to database objects.
        Setting this to False can improve performance and memory usage.
    SECRET_KEY : str
        Creates a secret key to allow session management.

    """
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

if __name__ == "__main__":
    test = ProductionConfig()
    print(test.SQLALCHEMY_DATABASE_URI)