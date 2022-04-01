from fastapi import FastAPI

from typing import Optional

from users import users, models as user_models

from database import engine


user_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
