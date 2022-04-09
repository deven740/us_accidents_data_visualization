from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse

from .models import UserModel
from .schemas import UserSchema
from database import get_db


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


@router.get("/")
async def test(db: Session = Depends(get_db)):
    return db.query(UserModel).all()


@router.post("/register")
async def register_user(user: UserSchema, db: Session = Depends(get_db)):

    user_exists = db.query(UserModel).filter(UserModel.username == user.username).first()
    if user_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User Already Exists")

    user_model = UserModel()
    user_model.username = user.username
    user_model.password = get_password_hash(user.password)

    db.add(user_model)
    db.commit()

    return {
        "status": 201,
        "transaction": "User Created Successfully"
    }


@router.post('/login')
def login(user: UserSchema, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    
    user_exists = db.query(UserModel).filter(UserModel.username == user.username).first()
    if not user_exists:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User Does not exist")

    if verify_password(user.password, user_exists.password):
        # subject identifier for who this token is for example id or username from database
        access_token = Authorize.create_access_token(subject=user.username)
        refresh_token = Authorize.create_refresh_token(subject=user.username)
        return {"access_token": access_token, "refresh_token": refresh_token}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Password do not match")


@router.get('/user')
async def user(Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    return {"user": current_user}

