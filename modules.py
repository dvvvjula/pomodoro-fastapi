class TaskValidationError(Exception):
    """Raised when the Task input is invalid"""
    
    def __init__(self, message='Task input is invalid'):
        self.message = message
        super().__init__(self.message)

class PomodoroValidationError(Exception):
    """Raised when the Pomodoro input is invalid"""
    
    def __init__(self, message="Task input is invalid"):
        self.message = message
        super().__init__(self.message)