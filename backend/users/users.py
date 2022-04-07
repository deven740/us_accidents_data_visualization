from fastapi import APIRouter, Depends

from .models import UserModel

from .schemas import UserSchema

from sqlalchemy.orm import Session

from database import get_db


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get("/")
async def test(db: Session = Depends(get_db)):
    return db.query(UserModel).all()


@router.post("/register")
async def register_user(user: UserSchema ,db: Session = Depends(get_db)):

    user_model = UserModel()
    user_model.username = user.username
    user_model.password = user.password

    db.add(user_model)
    db.commit()

    return {
        "status": 201,
        "transaction": "Successful"
    }

