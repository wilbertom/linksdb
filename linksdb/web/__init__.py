import flask
from .api import api


def create_app():

    app = flask.Flask(__name__)
    api.init_app(app)

    return app
