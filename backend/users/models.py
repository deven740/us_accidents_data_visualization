from enum import unique
from operator import index
from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)