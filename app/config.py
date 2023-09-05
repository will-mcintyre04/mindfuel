"""
Flask Application Configuration Settings.

Defines configuration classes dependant on production/development environment.

Classes
-------
Config:
    Base configuration class with shared settings.
DevelopmentConfig:
    Configuration class for the development environment.
ProductionConfig:
    Configuration class for the production environment.

Attributes
----------
app_config : dict
    A dictionary mapping environment names to their corresponding configuration classes.
"""

import os

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

    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """
    Configuration class for development environment.

    This class inherits from the base Config class and provides configuration settings
    specific to the development environment.

    Attributes
    ----------
    DEBUG : bool
        Controls whether the application runs in debug mode.
    SQLALCHEMY_DATABASE_URI : str
        The URI for the SQLite database used in development.
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

class ProductionConfig(Config):
    """
    Configuration class for production environment.

    This class inherits from the base Config class and provides configuration settings
    specific to the production environment.

    Attributes
    ----------
    DEBUG : bool
        Controls whether the application runs in debug mode.
        Note: Debug mode should be turned off in production for security reasons.
    SQLALCHEMY_DATABASE_URI : str
        The URI for the production database obtained from the 'DATABASE_URL' environment variable.
    """
    from dotenv import load_dotenv
    load_dotenv()
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://willymac:will'sdb@willymac.mysql.pythonanywhere-services.com/willymac$emails"
    print(SQLALCHEMY_DATABASE_URI)

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

if __name__ == "__main__":
    test = ProductionConfig()
    print(test.SQLALCHEMY_DATABASE_URI)