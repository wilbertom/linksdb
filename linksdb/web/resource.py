import json
import flask
import flask_restful
from linksdb.database.session import session


class ModelResource(flask_restful.Resource):

    model = None
    fields = {}

    def serialize(self, r):
        data = {}

        for f, rf in self.fields.items():
            data[f] = getattr(r, rf)

        return data

    def list(self):
        return session.query(self.model).all()

    def get(self):

        objects = []
        records = self.list()

        for r in records:
            objects.append(self.serialize(r))

        return {
            'objects': objects,
        }

    def get_post_data(self):
        return json.loads(flask.request.form['data'])

    def post(self):
        data = self.get_post_data()

        inst_data = {}

        for f, rf in self.fields.items():

            if f in data:
                inst_data[rf] = data[f]

        inst = self.model(**inst_data)
        inst.save()

        return {
            'id': inst.id,
        }
