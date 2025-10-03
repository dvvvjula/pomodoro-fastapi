# Pomodoro & Task Management API

This project is a **Pomodoro timer and task management system** built with **FastAPI**.  
It provides a backend for managing tasks, starting and closing Pomodoro sessions, and tracking overall productivity statistics.  

The project was developed as part of the university course **Specialized Software Tools**.

---

## Features

- **Task management**: create, retrieve, update, and delete tasks.  
- **Pomodoro sessions**: start and close Pomodoro timers linked to tasks.  
- **Validation rules**:
  - Only one active Pomodoro timer per task.
  - Maximum Pomodoro length: 25 minutes.
- **Statistics**:
  - Total time spent on tasks.
  - Number of finished Pomodoro sessions per task.
- **Interactive API documentation** with Swagger (`/docs`) and ReDoc (`/redoc`).  

---

## Technologies

- [FastAPI](https://fastapi.tiangolo.com/) – web framework for building APIs  
- [Uvicorn](https://www.uvicorn.org/) – ASGI server  
- Python 3.10+  

---

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/dvvvjula/pomodoro-fastapi.git
   cd pomodoro-task-api

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```  

4. Open in browser:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

# 📌 API Endpoints
<img width="1483" height="517" alt="image" src="https://github.com/user-attachments/assets/07a126a5-7556-4541-8ddf-5938b531a18e" />
<img width="1478" height="647" alt="image" src="https://github.com/user-attachments/assets/be732179-2e40-4e30-a30b-a4abb62fd9fd" />

### Pomodoro
  - POST /pomodoro → Create a new Pomodoro timer for a given task
  - POST /pomodoro/{task_id}/stop → Stop and close the Pomodoro timer for the task
  - GET /pomodoro/stats → Show statistics (total time spent, finished sessions per task)
### Tasks
  - GET /tasks → Get tasks filtered by status
  - POST /tasks → Create a new task
  - GET /tasks/{task_id} → Retrieve task by ID
  - PUT /tasks/{task_id} → Update task details
  - DELETE /tasks/{task_id} → Delete task

# Project Structure
  ```bash
  TO-DO/
  │
  ├── src/
  │   ├── common/                 # Models and exceptions
  │   │   ├── exceptions.py       # Custom exceptions
  │   │   ├── models.py           # Data models (Pomodoro, Task)
  │   │   ├── status.py           # Task status definitions
  │   │   └── __init__.py
  │   │
  │   ├── modules/                # Core business logic
  │   │   ├── pomodoro_operations.py  # PomodoroManager logic
  │   │   ├── task_operations.py      # TaskManager logic
  │   │   └── __init__.py
  │   │
  │   ├── routers/                # API routers (endpoints)
  │   │   ├── routers_pomodoro.py # Endpoints for Pomodoro
  │   │   ├── routers_tasks.py    # Endpoints for Tasks
  │   │   └── __init__.py
  │   │
  │   └── main.py                 # FastAPI entry point
  │
  ├── requirements.txt            # Project dependencies
  └── README.md                   # Project description
  ```
<img width="1463" height="561" alt="image" src="https://github.com/user-attachments/assets/5d0a9761-fab3-4c45-96c2-f1b398b255d0" />
