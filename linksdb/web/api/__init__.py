import flask_restful
from .links import LinksResource
from .tags import TagsResource

api = flask_restful.Api()


api.add_resource(LinksResource, '/api/links/')
api.add_resource(TagsResource, '/api/tags/')
