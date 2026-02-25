from os import name
import fastapi
from fastapi import FastAPI
from database.database import engine
import models
from database.database import Base

from routers import users
from routers.doctors import Doctor
app=FastAPI()

from routers import users
from routers import doctors

Base.metadata.create_all(bind=engine)
app.include_router(users.router)
app.include_router(doctors.router)
