from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi_jwt_auth.exceptions import AuthJWTException


from users import users, models as user_models
from database import engine
import auth

user_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)

app.add_exception_handler(AuthJWTException, auth.authjwt_exception_handler)