from models import Task
from typing import List
from modules import TaskValidationError

class TaskManager:

    task_counter = 1
    tasks:List[Task] = []

    @staticmethod
    def create_task(task: Task) -> Task:
        task.id = TaskManager.task_counter
        TaskManager.task_counter += 1
        """Data validation:

        1. tittle - min. 3, max. 100 characters long.
        2. description - optional, max. 300 characters long.
        3. status - 'to do', 'in progress', 'finished'; default - 'to do'"""
        
        if len(task.tittle) < 3 or len(task.tittle) > 100:
            raise TaskValidationError('Size of the tittle should be in range of 3-100 letters!')
        if len(task.description) < 0 or len(task.description) > 300:
            raise TaskValidationError('Size of the description should be in range of 0-300 letters!')
        
        TaskManager.tasks.append(task)
        return task

    def get_tasks() -> List[Task]:
        return TaskManager.tasks