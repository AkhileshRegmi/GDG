from pydantic import BaseModel


class StatsResponse(BaseModel):
    total_tasks: int
    completed_tasks: int
    overdue_tasks: int
    completion_rate: float
    pending_tasks: int
