import logging

from fastapi import FastAPI, Request, Depends
from fastapi_health import health

from core.database import get_session
from services.track import TrackService

app = FastAPI(title="Test application")
logger = logging.getLogger(__name__)
session = get_session()


@app.get('/')
def index(request: Request,
          service: TrackService = Depends()):
    return service.get(dict(request.query_params))

@app.get('/health')
def is_database_online(session: bool = Depends(get_session)):
    return session