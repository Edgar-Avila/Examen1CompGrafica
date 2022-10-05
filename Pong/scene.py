import pygame as pg
from enum import Enum
from abc import ABC, abstractmethod

class SceneOption(Enum):
    MENU = 0,
    GAME = 1,
    HELP = 2

class Scene(ABC):
    current = SceneOption.MENU

    @staticmethod
    def changeScene(to: SceneOption):
        Scene.current = to

    @abstractmethod
    def handle_events(self, event: pg.event.Event):
        pass

    @abstractmethod
    def init(self, **kwargs):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, window: pg.surface.Surface):
        pass
    
