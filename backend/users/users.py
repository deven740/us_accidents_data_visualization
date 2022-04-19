from fastapi import APIRouter, Depends, Request, status, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse
from datetime import timedelta

from .models import UserModel, RoleModel
from .schemas import UserSchema, UserResponseModel
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
        
    role = db.query(RoleModel).filter(RoleModel.role == "Supervisor").one()

    user_model = UserModel()
    user_model.username = user.username
    user_model.password = get_password_hash(user.password)
    user_model.role_id = role.id

    db.add(user_model)
    db.commit()

    return {
        "status": 201,
        "transaction": "User Created Successfully"
    }


@router.post('/login')
async def login(user: UserSchema, Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    user_exists = db.query(UserModel).filter(UserModel.username == user.username).first()
    if not user_exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Does not exist")

    if verify_password(user.password, user_exists.password):
        # subject identifier for who this token is for example id or username from database
        access_token = Authorize.create_access_token(subject=user.username,  expires_time=timedelta(seconds=30))
        refresh_token = Authorize.create_refresh_token(subject=user.username, expires_time=timedelta(days=30))
        return {"access_token": access_token, "refresh_token": refresh_token,
                "user": {"username": user.username, "role": user_exists.role.role}}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Password do not match")


@router.get('/user', response_model=UserResponseModel)
async def user(Authorize: AuthJWT = Depends(), db: Session = Depends(get_db)):
    Authorize.jwt_required()

    current_user = Authorize.get_jwt_subject()
    
    user = db.query(UserModel).filter(UserModel.username == current_user).first()

    response = {
        'username': user.username,
        'role': user.role.role
    }

    return response


@router.post('/refresh')
async def refresh(Authorize: AuthJWT = Depends()):
    """
    The jwt_refresh_token_required() function insures a valid refresh
    token is present in the request before running any code below that function.
    we can use the get_jwt_subject() function to get the subject of the refresh
    token, and use the create_access_token() function again to make a new access token
    """
    Authorize.jwt_refresh_token_required()

    current_user = Authorize.get_jwt_subject()
    new_access_token = Authorize.create_access_token(subject=current_user, expires_time=timedelta(minutes=1))
    return {"access_token": new_access_token}
