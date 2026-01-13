from datetime import datetime
from database.models.task import Task

def get_all_user_tasks(db, user_id):
    return db.query(Task).filter(Task.owner_id == user_id).all()

def get_task(db, task_id, user_id):
    return db.query(Task).filter(Task.id == task_id, Task.owner_id == user_id).first()

def create_task(db, task, user_id):
    db_task = Task(**task.model_dump(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task_in_db(db, db_task):
    db_task.updated_at = datetime.utcnow()
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task_from_db(db, db_task):
    db.delete(db_task)
    db.commit()