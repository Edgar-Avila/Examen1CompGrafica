from enum import Enum
from abc import ABC, abstractmethod

class SceneOption(Enum):
    MENU = 0,
    GAME = 1,
    HELP = 2

class Scene(ABC):
    current = SceneOption.MENU

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def draw():
        pass
    
