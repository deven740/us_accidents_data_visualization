from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi import Depends, APIRouter


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


@AuthJWT.load_config
def get_config():
    return Settings()



# @app.post('/login')
# def login(user: schemas.UserSchema, Authorize: AuthJWT = Depends()):
#     if user.username != "stringst" or user.password != "stringst":
#         raise HTTPException(status_code=401,detail="Bad username or password")

#     # subject identifier for who this token is for example id or username from database
#     access_token = Authorize.create_access_token(subject=user.username)
#     refresh_token = Authorize.create_refresh_token(subject=user.username)
#     return {"access_token": access_token, "refresh_token": refresh_token}


@router.post('/refresh')
def refresh(Authorize: AuthJWT = Depends()):
    """
    The jwt_refresh_token_required() function insures a valid refresh
    token is present in the request before running any code below that function.
    we can use the get_jwt_subject() function to get the subject of the refresh
    token, and use the create_access_token() function again to make a new access token
    """
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user)
    return {"access_token": new_access_token}


# @app.get('/user')
# def user(Authorize: AuthJWT = Depends()):
#     Authorize.jwt_required()

#     current_user = Authorize.get_jwt_subject()
#     return {"user": current_user}


# @app.get('/optional-authorize')
# def user(Authorize: AuthJWT = Depends()):
#     Authorize.jwt_optional()

#     # If no jwt is sent in the request, get_jwt_subject() will return None
#     current_user = Authorize.get_jwt_subject() or "anonymous"
#     return {"user": current_user}


# @app.exception_handler(AuthJWTException)
# def authjwt_exception_handler(request: Request, exc: AuthJWTException):
#     return JSONResponse(
#         status_code=exc.status_code,
#         content={"detail": exc.message}
#     )
