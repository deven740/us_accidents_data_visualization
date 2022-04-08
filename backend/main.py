from fastapi import FastAPI, HTTPException, Request, Depends
from typing import Optional
from fastapi.security import OAuth2PasswordBearer

from users import users, schemas,  models as user_models
from database import engine
import auth

user_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
