from database.models.user import User
from passlib.context import CryptContext
from backend.core.security import get_password_hash


def get_user_by_email(db, email):
    return db.query(User).filter(User.email == email).first()


def create_user(db, user):
    role = "admin" if db.query(User).count() == 0 else "user"
    db_user = User(
        email=user.email, hashed_password=get_password_hash(user.password), role=role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
