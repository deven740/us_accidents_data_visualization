from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi import Request

class Settings(BaseModel):
    authjwt_secret_key: str = "secret"


@AuthJWT.load_config
def get_config():
    return Settings()


def authjwt_exception_handler(request: Request, exc: AuthJWTException):

    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )
