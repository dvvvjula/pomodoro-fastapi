from models import Pomodoro
from task_operations import TaskManager
from modules import PomodoroValidationError, TaskValidationError
from datetime import datetime, timedelta

class PomodoroManager:

    """
    1. Pomodoro timers is a dict containing all the active pomodoro timers, key -> task_id, value -> Pomodoro object
    2. Finished sessions is a dict containing task_id as a key and number of closer pomodoro timers as a value
    """

    pomodoro_timers = {}
    finished_sessions = {}

    @staticmethod
    def start_pomodoro(id: int, pomodoro: Pomodoro):
        try:
            TaskManager.get_id_task(id)
        except TaskValidationError as e:
            raise PomodoroValidationError(f'Cannot create this pomodoro timer - {e}!')
        
        for timer in PomodoroManager.pomodoro_timers:
            if timer.id == id:
                raise PomodoroValidationError('Cannot create another pomodoro timer, there can only be one active!')
            
        """
        Check if the difference between start and end parameters is max. 25 mins
        """
        time_difference = (pomodoro.end_time - pomodoro.start_time).total_seconds() / 60
        
        if time_difference > 25:
            extra = time_difference - 25
            raise PomodoroValidationError(f'Given Pomodoro time is longer than 25 minutes by {extra:.1f} min!')

        if not pomodoro.completed:
            PomodoroManager.finished_sessions[id] = PomodoroManager.finished_sessions.get(id, 0)+1
        else:
            PomodoroManager.pomodoro_timers[id] = pomodoro
        
        