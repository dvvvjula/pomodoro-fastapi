from fastapi import FastAPI, HTTPException
from models import Task, Pomodoro
from modules import TaskValidationError, PomodoroValidationError
from task_operations import TaskManager

app = FastAPI()

@app.get('/tasks')
async def get_all_tasks():
    return TaskManager.get_tasks()

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task_by_id(task_id: str):
    task = (TaskManager.get_tasks()).get(task_id)

    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    return task

@app.post("/tasks")
async def add_task(task:Task):
    try:
        TaskManager.create_task(task)
    except TaskValidationError as e:
        raise HTTPException(status_code=400, detail=e.message)
