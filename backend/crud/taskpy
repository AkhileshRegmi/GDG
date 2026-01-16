from database.models.task import Task


def get_all_user_tasks(db, user_email):
    return db.query(Task).filter(Task.owner_email == user_email).all()


def get_task(db, task_id):
    return db.query(Task).get(task_id)


def create_task(db, task, user_email):
    db_task = Task(
        title=task.title,
        description=task.description,
        priority=task.priority,
        status=task.status,
        deadline=task.deadline,
        tags=task.tags,
        owner_email=user_email,
    )
    db.add(db_task)
    db.commit()


def update_task_in_db(db, task_id, task):
    db_task = get_task(db, task_id)
    if not db_task:
        return None
    db_task.title = task.title
    db_task.description = task.description
    db_task.priority = task.priority
    db_task.status = task.status
    db_task.deadline = task.deadline
    db_task.tags = task.tags
    db.add(db_task)
    db.commit()


def delete_task_from_db(db, task_id):
    db_task = get_task(db, task_id)
    db.delete(db_task)
    db.commit()
