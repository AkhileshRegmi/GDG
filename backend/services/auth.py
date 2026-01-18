from backend.core.security import verify_password, create_access_token
from backend.crud import user as user_crud
from fastapi import HTTPException


class AuthService:
    def create_user(self, db, user):
        db_user = user_crud.get_user_by_email(db, user.email)
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        db_user = user_crud.create_user(db, user)
        return {"email": db_user.email, "role": db_user.role}

    def authenticate_user(self, db, email, password):
        user = user_crud.get_user_by_email(db, email)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Incorrect email or password")
        access_token = create_access_token(user.email)
        return {"access_token": access_token, "token_type": "bearer", "role": user.role}
