from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Task(BaseModel):
    id: int = None
    tittle: str
    description: Optional[str]
    status: str

class Pomodoro(BaseModel):
    task_id: int
    start_time: datetime
    end_time: datetime
    completed: bool