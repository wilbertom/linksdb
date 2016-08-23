from .links import LinksResource
from linksdb.database import Tag


class LinkWithTagsResource(LinksResource):

    def post(self):
        link_o = super(LinkWithTagsResource, self).post()

        link = self.session.query(self.model).get(link_o['id'])
        data = self.get_post_data()

        for tag_name in data['tags']:
            tag = self.session.query(Tag).filter_by(name=tag_name).first()

            if tag is None:
                tag = Tag(name=tag_name)
                self.session.add(tag)

            link.tags.append(tag)

        self.session.commit()

        return link_o
