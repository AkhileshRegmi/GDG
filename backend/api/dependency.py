from fastapi import Depends, HTTPException, Request
from jose import jwt
from backend.core.config import settings
from database.connection import get_db
from database.models.user import User


def get_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401)
    return auth_header.split(" ")[1]


def get_current_user(token=Depends(get_token), db=Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY)
        email = payload.get("email")
        if email is None:
            raise HTTPException(status_code=401)
    except:
        raise HTTPException(status_code=401)

    user_email = email
    user = db.query(User).get(user_email)
    if user is None:
        raise HTTPException(status_code=401)

    return user


def admin_access(user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403)
    return user
