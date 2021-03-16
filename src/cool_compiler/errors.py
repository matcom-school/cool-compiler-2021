from enum import Enum

class ErrorType(Enum):
    SE = "SemanticError"

def errors_compose (pos : tuple,  etype : ErrorType, text : str):
    return f' {pos} {etype} {text}'
