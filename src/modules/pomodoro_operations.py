from src.common.models import Pomodoro
from src.modules.task_operations import TaskManager
from src.common.exceptions import PomodoroValidationError, TaskValidationError
from datetime import datetime

class PomodoroManager:

    """
    1. pomodoro_timers is a dict containing all the active pomodoro timers, key -> task_id, value -> Pomodoro object
    2. finished_sessions is a dict containing task_id as a key and number of closed pomodoro timers as a value
    3. total_time shows a total time spent on tasks
    """

    pomodoro_timers = {}
    finished_sessions = {}
    total_time = 0

    @staticmethod
    def start_pomodoro(id: int, pomodoro: Pomodoro):
        try:
            task = TaskManager.get_id_task(id)
        except TaskValidationError as e:
            raise PomodoroValidationError(f'Cannot create this pomodoro timer - {e}!')
        
        if id in PomodoroManager.pomodoro_timers:
                raise PomodoroValidationError('Cannot create another pomodoro timer, there can only be one active!')
            
        """
        Check if the difference between start and end parameters is max. 25 mins
        """
        
        time_difference = (pomodoro.end_time - pomodoro.start_time).total_seconds() / 60
        
        if time_difference > 25:
            extra = time_difference - 25
            raise PomodoroValidationError(f'Given Pomodoro time is longer than 25 minutes by {extra:.1f} min!')

        if pomodoro.completed:
            PomodoroManager.total_time += PomodoroManager.count_pomodoro_time(pomodoro.start_time, pomodoro.end_time)
            PomodoroManager.finished_sessions[id] = PomodoroManager.finished_sessions.get(id, 0)+1
        else:
            PomodoroManager.pomodoro_timers[id] = pomodoro
            task.status = 'in progress'

    @staticmethod
    def close_pomodoro(id: int):
        try:
            TaskManager.get_id_task(id)
        except TaskValidationError as e:
            raise PomodoroValidationError(f'Cannot close this pomodoro timer - {e}!')
        
        if id not in PomodoroManager.pomodoro_timers:
            raise PomodoroValidationError('Seems like the Pomodoro timer you want to close does not exist or got closed already...')
        else:
            start = PomodoroManager.pomodoro_timers[id].start_time
            end = PomodoroManager.pomodoro_timers[id].end_time
            PomodoroManager.total_time += PomodoroManager.count_pomodoro_time(start, end)
            PomodoroManager.pomodoro_timers.pop(id)
            PomodoroManager.finished_sessions[id] = PomodoroManager.finished_sessions.get(id, 0)+1

    @staticmethod
    def count_pomodoro_time(start_time: datetime, end_time: datetime):
        return ((end_time - start_time).total_seconds() / 60)
    
    @staticmethod
    def pomodoro_stats():
        stats = {
            "total_time_spent": PomodoroManager.total_time,
            "finished_sessions": PomodoroManager.finished_sessions
        }
        return stats
        

        
        