from os import environ


class Config:
    """Set Flask configuration vars from .env file."""
    # Enable Flask's debugging features. Should be False in production
    DEBUG = True