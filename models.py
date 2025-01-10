from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from status import Status

class Task(BaseModel):
    id: int = None
    tittle: str = Field(..., min_length=3, max_length=100)
    description: Optional[str]
    status: Status

class Pomodoro(BaseModel):
    task_id: int
    start_time: datetime
    end_time: datetime
    completed: bool