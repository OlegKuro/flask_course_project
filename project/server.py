import logging

from flask import Flask
from flask_restx import Api

from project.config import get_config
from project.exceptions import BaseProjectException
from project.tools.setup_db import db
from project.views import auth_ns, user_ns

api = Api()


def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(get_config(config_name))
    app.logger.setLevel(logging.DEBUG if app.config['DEBUG'] else logging.INFO)

    db.init_app(app)
    api.init_app(app)

    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)

    @api.errorhandler(BaseProjectException)
    def handle_validation_error(error):
        return error.message, error.code

    return app
