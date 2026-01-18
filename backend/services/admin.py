from sqlalchemy.orm import Session
from backend.crud import admin as admin_crud
from fastapi import HTTPException

class AdminService:
    def get_all_users(self, db: Session):
        return admin_crud.get_all_users(db)

    def get_users_with_tasks(self, db: Session):
        return admin_crud.get_users_with_tasks(db)

    def update_user_role(self, db: Session, email: str, role: str):
        if role not in ["user", "admin"]:
             raise HTTPException(status_code=400, detail="Invalid role")
        
        user = admin_crud.update_user_role(db, email, role)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
