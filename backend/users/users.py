from fastapi import APIRouter, Depends

from .models import UserModel

from .schemas import UserSchema

from sqlalchemy.orm import Session

from database import get_db

from passlib.context import CryptContext

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)


@router.get("/")
async def test(db: Session = Depends(get_db)):
    return db.query(UserModel).all()


@router.post("/register")
async def register_user(user: UserSchema ,db: Session = Depends(get_db)):

    user_model = UserModel()
    user_model.username = user.username
    user_model.password = get_password_hash(user.password)

    db.add(user_model)
    db.commit()

    return {
        "status": 201,
        "transaction": "Successful"
    }

