from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .base import Base
from .links_tags import links_tags


class Link(Base):
    __tablename__ = 'links'

    value = Column(String, unique=True, nullable=False)

    tags = relationship(
        'Tag', secondary=links_tags,
    )
