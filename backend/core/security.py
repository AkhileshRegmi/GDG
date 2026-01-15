from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from backend.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(subject):
    now = datetime.utcnow()
    expire_minutes = settings.ACCESS_TOKEN_EXPIRY
    default_delta = timedelta(minutes=expire_minutes)
    expire_time = now + default_delta
    to_encode = {}
    to_encode["exp"] = expire_time
    to_encode["sub"] = str(subject)
    secret = settings.SECRET_KEY
    encoded_jwt = jwt.encode(to_encode, secret)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    is_correct = pwd_context.verify(plain_password, hashed_password)
    return is_correct


def get_password_hash(password):
    hashed_pwd = pwd_context.hash(password)
    return hashed_pwd
