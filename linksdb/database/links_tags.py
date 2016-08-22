from sqlalchemy import Table, Column, ForeignKey
from .base import Base

links_tags = Table(
    'links_tags', Base.metadata,
    Column('link_id', ForeignKey('links.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True),
)
