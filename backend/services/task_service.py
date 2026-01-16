from fastapi import HTTPException
from backend.crud import task as task_crud


class TaskService:

    def create_task(self, db, task, user_email):
        task_crud.create_task(db, task, user_email)

    def get_tasks(self, db, user_email):
        return task_crud.get_all_user_tasks(db, user_email)

    def get_task(self, db, task_id, user_email):
        db_task = task_crud.get_task(db, task_id)
        if not db_task or db_task.owner_email != user_email:
            raise HTTPException(status_code=404, detail="Task not found")
        return db_task

    def update_task(self, db, task_id, task_update, user_email):
        db_task = self.get_task(db, task_id, user_email)
        if not db_task or db_task.owner_email != user_email:
            raise HTTPException(status_code=404, detail="Task not found")
        if task_update.title is None:
            task_update.title = db_task.title

        if task_update.description is None:
            task_update.description = db_task.description

        if task_update.priority is None:
            task_update.priority = db_task.priority

        if task_update.status is None:
            task_update.status = db_task.status

        if task_update.deadline is None:
            task_update.deadline = db_task.deadline

        if task_update.tags is None:
            task_update.tags = db_task.tags

        task_crud.update_task_in_db(db, task_id, task_update)

    def delete_task(self, db, task_id, user_email):
        db_task = self.get_task(db, task_id, user_email)
        if not db_task:
            raise HTTPException(status_code=404, detail="Task not found")
        task_crud.delete_task_from_db(db, task_id)
