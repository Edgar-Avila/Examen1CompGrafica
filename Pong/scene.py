import pygame as pg
from enum import Enum
from abc import ABC, abstractmethod

class SceneOption(Enum):
    MENU = 0,
    GAME = 1,
    HELP = 2

class Scene(ABC):
    current = SceneOption.MENU

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, window: pg.surface.Surface):
        pass
    
