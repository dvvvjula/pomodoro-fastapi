from pydantic import BaseModel
from datetime import datetime

class Task(BaseModel):
    id: int
    tittle: str
    description: str
    status: str

class Pomodoro(BaseModel):
    task_id: int
    start_time: datetime
    end_time: datetime
    completed: bool