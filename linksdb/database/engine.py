import sqlalchemy
from linksdb.configuration import Configuration

engine = sqlalchemy.create_engine(Configuration.SQL_URI)
