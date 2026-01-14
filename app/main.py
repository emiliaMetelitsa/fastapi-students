from fastapi import FastAPI
from app.api.routes import router
from app.db.session import engine
from app.db.models import Base
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Students API")
app.include_router(router)
