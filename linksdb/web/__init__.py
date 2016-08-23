import flask
from .api import api
from .views import views


def create_app():

    app = flask.Flask(__name__)

    app.register_blueprint(views)
    api.init_app(app)

    return app
