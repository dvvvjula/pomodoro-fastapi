from src.routers.routers_pomodoro import router as router_pomodoro
from src.routers.routers_tasks import router as router_tasks
from fastapi import FastAPI

app = FastAPI()

app.include_router(router_pomodoro)
app.include_router(router_tasks)