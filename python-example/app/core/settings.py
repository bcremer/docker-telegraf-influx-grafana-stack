import os

from pydantic import BaseSettings

pg_host = os.environ['POSTGRES_HOST']
pg_port = os.environ['POSTGRES_PORT']
pg_user = os.environ['POSTGRES_USER']
pg_pass = os.environ['POSTGRES_PASSWORD']
pg_db = os.environ['POSTGRES_DB']


class Settings(BaseSettings):
    service_host: str = '0.0.0.0'
    service_port: int = 8000

    database_url: str = f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'

    es_host: str = os.environ['ELASTICSEARCH_HOST']
    es_port: int = os.environ['ELASTICSEARCH_PORT']


settings = Settings()