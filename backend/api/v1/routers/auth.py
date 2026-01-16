from fastapi import APIRouter, Depends
from database.connection import get_db
from backend.services.auth import AuthService
from backend.schemas.user import UserCreate, UserResponse, UserLogin
from backend.schemas.token import Token

router = APIRouter(prefix="/auth", tags=["auth"])
auth_service = AuthService()


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db=Depends(get_db)):
    return auth_service.create_user(db, user)


@router.post("/login", response_model=Token)
def login(user_credentials: UserLogin, db=Depends(get_db)):
    return auth_service.authenticate_user(
        db, user_credentials.email, user_credentials.password
    )
