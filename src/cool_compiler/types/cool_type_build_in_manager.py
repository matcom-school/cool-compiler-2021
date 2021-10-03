from .tools import SemanticError
import inspect
def type_body_def(cls):
    for n, f  in inspect.getmembers(cls, predicate=inspect.ismethod):
        if n == '__init__': continue
        if n in cls.__dict__: f()

class Singleton(type):
    _instances = None
    def __call__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances

def build_in_type(cls):
    manager = CoolTypeBuildInManager()
    manager.dictt[cls.__name__] = cls()
    return cls

class CoolTypeBuildInManager(metaclass=Singleton):
    def __init__(self) -> None:
        self.dictt = {}

    def __iter__(self):
        return self.dictt.__iter__()

    def find(self, name:str):
        try:
            return self.dictt[name]
        except KeyError:
            raise SemanticError(f'Type "{name}" is not defined.')