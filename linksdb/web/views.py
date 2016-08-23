import flask

views = flask.Blueprint(
    'views', __name__, static_folder='static', template_folder='templates'
)


@views.route('/')
def index():
    return flask.render_template('index.html')
