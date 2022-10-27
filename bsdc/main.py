import asyncio

from fastapi import FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config
from pydantic import BaseSettings

from bsdc.db import get_session, get_engine
from bsdc.db.models import Base
from bsdc.routers.v1 import root

class Settings(BaseSettings):
    port: int = 2833
    
def app_maker(testing: bool = False):
    app = FastAPI(version="1.0.0")
    app.include_router(root, prefix="/api")
    if not testing:
        
        engine = get_engine()
        Base.metadata.bind = engine
        Base.metadata.create_all()
        session = next(get_session(engine=engine))
        
    return app