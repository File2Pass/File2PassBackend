from distutils.command.config import config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    with app.app_context():
        db.init_app(app)

    db.init_app(app)

    return app
