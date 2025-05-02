from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# Create a Flask application instance
myapp_obj = Flask(__name__)

# Set the base directory path for the application (where this file is located)
basedir = os.path.abspath(os.path.dirname(__file__))

# Configuration settings for the Flask application
myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',  # Secret key for session management and CSRF protection
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),  # SQLite database URI (app.db will be in the base directory)
)

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(myapp_obj)


# Import routes and models after app initialization to avoid circular imports
from app import routes, models