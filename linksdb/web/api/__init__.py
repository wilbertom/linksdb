import flask_restful
from .links import LinksResource
from .tags import TagsResource
from .link_with_tags import LinkWithTagsResource

api = flask_restful.Api()


api.add_resource(LinkWithTagsResource, '/api/links/')
api.add_resource(TagsResource, '/api/tags/')
