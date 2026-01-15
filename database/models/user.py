from sqlalchemy import Column, String
from database.connection import Base


class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")
