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



