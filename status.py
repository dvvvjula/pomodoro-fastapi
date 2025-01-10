from enum import Enum
from modules import TaskValidationError

class Status(Enum):
    TODO = "to do"
    INPROGRESS = "in progress"
    FINISHED = "finished"

    def enum_from_value(enum, value):
        try:
            return enum(value)
        except TaskValidationError:
            raise TaskValidationError(f"Value {value} not found in.")