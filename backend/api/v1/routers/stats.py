from fastapi import APIRouter, Depends
from database.connection import get_db
from backend.schemas.stats import StatsResponse
from backend.services.stats import StatsService
from backend.api.dependency import get_current_user


router = APIRouter(prefix="/stats", tags=["stats"])
stats_service = StatsService()


@router.get("/", response_model=StatsResponse)
def get_stats(db=Depends(get_db), current_user=Depends(get_current_user)):
    return stats_service.get_user_stats(db, current_user.email)
