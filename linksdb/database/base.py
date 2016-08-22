from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .session import session


class _Base(object):

    id = Column(Integer, primary_key=True)

    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated = Column(DateTime, nullable=False, default=datetime.utcnow)

    def save(self):
        self.updated = datetime.utcnow()
        session.add(self)
        session.commit()

        return self


Base = declarative_base(cls=_Base)
