from datetime import datetime
from backend.schemas.stats import StatsResponse
from backend.crud import task as task_crud

class StatsService:
    def get_user_stats(self, db, user_email):
        tasks = task_crud.get_all_user_tasks(db, user_email)
        
        now = datetime.utcnow()
        
        total_tasks = 0
        completed_tasks = 0
        overdue_tasks = 0
        pending_tasks = 0
        
        for t in tasks:
            total_tasks += 1
            
            if t.status != "Completed" and t.status != "Overdue" and t.deadline and t.deadline < now:
                t.status = "Overdue"
            if t.status == "Completed":
                completed_tasks += 1
            elif t.status == "Overdue":
                overdue_tasks += 1
            elif t.status == "Pending":
                pending_tasks += 1
        
        db.commit()
            
        completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0.0
        
        return StatsResponse(
            total_tasks=total_tasks,
            completed_tasks=completed_tasks,
            overdue_tasks=overdue_tasks,
            completion_rate=round(completion_rate, 2),
            pending_tasks=pending_tasks
        )
