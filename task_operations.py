from models import Task
from typing import List
from modules import TaskValidationError
from fastapi import HTTPException
#from status import Status

class TaskManager:

    task_counter = 1
    tasks:List[Task] = []
    status = ['to do', 'in progress', 'finished']

    @staticmethod
    def create_task(task: Task) -> Task:

        """Data validation:

        1. tittle - min. 3, max. 100 characters long, must be unique.
        2. description - optional, max. 300 characters long.
        3. status - 'to do', 'in progress', 'finished'; default - 'to do'"""
        
        if len(task.tittle) < 3 or len(task.tittle) > 100:
            raise TaskValidationError('Size of the tittle should be in range of 3-100 letters!')
        
        for value in TaskManager.tasks:
            if value.tittle == task.tittle:
                raise TaskValidationError('Tittle has to be unique, be creative please')

            
        if len(task.description) < 0 or len(task.description) > 300:
            raise TaskValidationError('Size of the description should be in range of 0-300 letters!')
        
        """Try implementing enum again instead of a status list"""

        if len(task.status)==0:
            task.status = TaskManager.status[0]
        elif task.status not in TaskManager.status:
            raise TaskValidationError(f'Invalid status name. Try those: {[s for s in TaskManager.status]}!')
            
        task.id = TaskManager.task_counter
        TaskManager.task_counter += 1
        TaskManager.tasks.append(task)
        return task
    
    @staticmethod
    def get_tasks() -> List[Task]:
        return TaskManager.tasks
    
    @staticmethod
    def get_id_task(id: int):
        for task in TaskManager.tasks:
            if task.id == id:
                return task
        raise HTTPException(f'There is no task with id {id} in the database!')
    
    @staticmethod
    def get_status_tasks(status: str) -> List[Task]:
        if status in TaskManager.status:
            return [task for task in TaskManager.tasks if task.status.lower() == status.lower()]
        else:
            raise TaskValidationError(f"{status} doesn't exist!")
        
    @staticmethod
    def update_task(id: int, task: Task):
        for value in TaskManager.tasks:
            if value.tittle == task.tittle:
                raise TaskValidationError('Tittle has to be unique, be creative please')

        if len(task.description) == 0 or len(task.description) > 300:
            raise TaskValidationError('Size of the description should be in range of 0-300 letters!')

        if len(task.status) == 0:
            task.status = TaskManager.status[0]
        elif task.status not in TaskManager.status:
            raise TaskValidationError(f'Invalid status name. Try those: {[s for s in TaskManager.status]}!')

        for value in TaskManager.tasks:
            if value.id == id:
                value.tittle = task.tittle
                value.description = task.description
                value.status = task.status
        
    @staticmethod
    def delete_task(id: int) -> None:
        try:
            task = TaskManager.get_id_task(id)
        except HTTPException:
            raise TaskValidationError(status_code=404, detail=f'{id} cannot be deleted from the database!')
        TaskManager.tasks.remove(task)