from database.models.user import User
from database.models.task import Task

def get_all_users(db):
    return db.query(User).all()

def get_users_with_tasks(db):
    users = db.query(User).all()
    for user in users:
        user.tasks = db.query(Task).filter(Task.owner_email == user.email).all()
    return users

def update_user_role(db, email, role):
    user = db.query(User).get(email)
    if user:
        user.role = role
        db.commit()
        db.refresh(user)
    return user
