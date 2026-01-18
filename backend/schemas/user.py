from typing import List
from pydantic import BaseModel, EmailStr
from backend.schemas.task import TaskResponse


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    role: str



class UserLogin(UserBase):
    password: str


class UserWithTasks(UserResponse):
    tasks: List[TaskResponse]


class UserRoleUpdate(BaseModel):
    role: str
