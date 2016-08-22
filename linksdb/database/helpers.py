from .engine import engine
from .base import Base


def create():
    Base.metadata.create_all(bind=engine)
