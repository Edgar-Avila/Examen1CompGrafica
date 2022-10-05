import pygame as pg
from scene import Scene, SceneOption
from config import *
from colors import *
import keys

class Help(Scene):
    def __init__(self) -> None:
        self.font = pg.font.SysFont('Comic Sans MS', 30)
        lines = [
            "Use the space key to start the match",
            "Use the up and down arrow keys to move",
            "Score a point when the ball goes past",
            "Your opponent goal.",
            "Z or Space or Enter -> Back"
        ]
        self.lines = [self.font.render(line, False, WHITE) for line in lines]

    def handle_events(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN:
            if event.key in keys.ACCEPT:
                Scene.changeScene(SceneOption.MENU)

    def init(self, **kwargs):
        return super().init(**kwargs)

    def update(self):
        pass
    def draw(self, window: pg.surface.Surface):
        for i, line in enumerate(self.lines):
            pos = (MID_X - line.get_width() / 2, MID_Y + i * 30 - len(self.lines) * 30 / 2)
            window.blit(line, pos)

