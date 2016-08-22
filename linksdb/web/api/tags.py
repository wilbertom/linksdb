from ..resource import ModelResource
from linksdb.database import Tag


class TagsResource(ModelResource):
    model = Tag
    fields = {
        'id': 'id',
        'name': 'name',
    }
