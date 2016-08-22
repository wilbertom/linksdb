from ..resource import ModelResource
from linksdb.database import Link


class LinksResource(ModelResource):
    model = Link
    fields = {
        'id': 'id',
        'link': 'value',
    }
