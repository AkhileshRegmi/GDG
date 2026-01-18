from fastapi import APIRouter, Depends
from typing import List
from database.connection import get_db
from backend.services.admin import AdminService
from backend.api.dependency import admin_access
from backend.schemas.user import UserResponse, UserWithTasks, UserRoleUpdate

router = APIRouter(prefix="/admin", tags=["admin"])
admin_service = AdminService()

@router.put("/users/{user_email}/role", response_model=UserResponse)
def update_user_role(
    user_email: str, 
    role_update: UserRoleUpdate, 
    db=Depends(get_db), 
    admin=Depends(admin_access)
):
    return admin_service.update_user_role(db, user_email, role_update.role)

@router.get("/users", response_model=List[UserResponse])
def get_all_users(
    db=Depends(get_db), 
    admin=Depends(admin_access)
):
    return admin_service.get_all_users(db)

@router.get("/users-tasks", response_model=List[UserWithTasks])
def get_users_with_tasks(
    db=Depends(get_db), 
    admin=Depends(admin_access)
):
    return admin_service.get_users_with_tasks(db)
