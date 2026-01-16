from fastapi import APIRouter, Depends
from database.connection import get_db
from backend.services.task_service import TaskService
from backend.api.dependency import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])
task_service = TaskService()


@router.post("/create")
def create_task(task, db=Depends(get_db), current_user=Depends(get_current_user)):
    task_service.create_task(db, task, current_user.email)
    return {"message": "Task created successfully"}


@router.get("/fetch")
def read_tasks(db=Depends(get_db), current_user=Depends(get_current_user)):
    tasks = task_service.get_tasks(db, current_user.email)
    return [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status,
            "deadline": task.deadline,
            "tags": task.tags,
            "created_at": task.created_at,
            "updated_at": task.updated_at,
            "owner_email": task.owner_email,
        }
        for task in tasks
    ]


@router.get("/fetch/{task_id}")
def read_task(task_id: int, db=Depends(get_db), current_user=Depends(get_current_user)):
    task = task_service.get_task(db, task_id, current_user.email)
    return {
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "priority": task.priority,
        "status": task.status,
        "deadline": task.deadline,
        "tags": task.tags,
        "created_at": task.created_at,
        "updated_at": task.updated_at,
        "owner_email": task.owner_email,
    }


@router.put("/update/{task_id}")
def update_task(
    task_id: int,
    task,
    db=Depends(get_db),
    current_user=Depends(get_current_user),
):
    task_service.update_task(db, task_id, task, current_user.email)
    return {"message": "Task updated successfully"}


@router.delete("/delete/{task_id}")
def delete_task(
    task_id: int, db=Depends(get_db), current_user=Depends(get_current_user)
):
    task_service.delete_task(db, task_id, current_user.email)
    return {"message": "Task deleted successfully"}
