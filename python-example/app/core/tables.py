import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from core.database import engine

Base = declarative_base()


class Track(Base):
    __tablename__ = 'track'

    id = sa.Column(sa.Integer, primary_key=True)
    at = sa.Column(sa.DateTime, server_default=func.now())
    data = sa.Column(sa.JSON, nullable=True)


Base.metadata.create_all(engine)