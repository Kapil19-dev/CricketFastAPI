import numpy as np
from fastapi import FastAPI
from db.models import models
from db.models.models import Matches
from db.postgres.database import engine, SessionLocal
from api import admin, users
from service import update_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# update_db.update_complete_db()
app.include_router(admin.admin_router)
app.include_router(users.user_router)


