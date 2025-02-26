from dotenv import load_dotenv
from flask_cors import CORS
from flask import Flask 
from .constants import *
from .extensions import *
from .config import Config

from .error_handler import register_error_handlers



load_dotenv()

def create_app(config_class=Config):

    app = Flask(__name__)

    app.config.from_object(config_class)

    CORS(app)

    register_blueprints(app)

    initialize_extensions(app)

    return app


def initialize_extensions(app):
    database.init_app(app)

    db_migration.init_app(app, database)


def register_blueprints(app):
    app.register_blueprint(routes_blueprint)

