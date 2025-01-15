from fastapi import APIRouter, HTTPException
from src.common.models import Pomodoro
from src.common.exceptions import PomodoroValidationError
from src.modules.pomodoro_operations import PomodoroManager

router = APIRouter()

@router.post("/pomodoro")
async def create_pomodoro(task_id: int, pomodoro:Pomodoro):
    try:
        PomodoroManager.start_pomodoro(task_id, pomodoro)
    except PomodoroValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)
    
@router.post("/pomodoro/{task_id}/stop")
async def stop_pomodoro(task_id: int):
    try:
        PomodoroManager.close_pomodoro(task_id)
    except PomodoroValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)
    
@router.get("/pomodoro/stats")
async def show_pomodoro_stats():
    return PomodoroManager.pomodoro_stats()