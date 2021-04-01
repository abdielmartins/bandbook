__version__ = "0.1.0"

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from app.configurations import database, migration
from app import views


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    database.init_app(app)
    migration.init_app(app)
    views.init_app(app)

    return app