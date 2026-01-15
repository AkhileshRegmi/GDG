from database.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def get_user_by_email(db, email):
    return db.query(User).filter(User.email == email).first()

def create_user(db, user):
    hashed_password = pwd_context.hash(user.password)
    role = "admin" if db.query(User).count() == 0 else "user"
    db_user = User(email=user.email, hashed_password=hashed_password, role=role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user