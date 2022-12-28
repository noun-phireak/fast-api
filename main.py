from fastapi import FastAPI
from routers.api_v1.api import router
from models import models
import database

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

app.include_router(router, prefix="/api/v1")

