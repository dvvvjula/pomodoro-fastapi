from fastapi import FastAPI, HTTPException
from models import Task, Pomodoro
from modules import TaskValidationError, PomodoroValidationError
from task_operations import TaskManager
from typing import List, Optional

app = FastAPI()

@app.get("/tasks", response_model=List[Task])
async def get_tasks_by_status(status: Optional[str] = None):
    try:
        if status:
            return TaskManager.get_status_tasks(status)
        else:
            return TaskManager.get_tasks()
    except TaskValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task_by_id(task_id: int):
    try:
        return TaskManager.get_id_task(task_id)
    except HTTPException as e:
        raise HTTPException(status_code=400, detail=e.message)

@app.post("/tasks")
async def add_task(task:Task):
    try:
        TaskManager.create_task(task)
    except TaskValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)
    
@app.put("/tasks/{task_id}")
async def update_task_by_id(task_id: int, task: Task):
    try:
        TaskManager.update_task(task_id, task)
    except TaskValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    try:
        TaskManager.delete_task(task_id)
    except TaskValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)
