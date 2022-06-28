from elasticsearch import Elasticsearch
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.settings import settings

engine = create_engine(settings.database_url)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False
)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()


es = Elasticsearch([{'host': settings.es_host, 'port': settings.es_port, 'scheme': ''}])