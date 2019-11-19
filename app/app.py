from flask import Flask
from .models import Base, Post
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

