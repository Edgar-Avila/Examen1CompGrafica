import pygame as pg
from scene import Scene, SceneOption
from config import *
from colors import *

class Help(Scene):
    def __init__(self) -> None:
        self.font = pg.font.SysFont('Comic Sans MS', 30)
        lines = [
            "Use the space key to start the match",
            "Use the up and down arrow keys to move",
            "Score a point when the ball goes past",
            "Your opponent goal.",
            "Z - Back"
        ]
        self.lines = [self.font.render(line, False, WHITE) for line in lines]
        self.delay = 20

    def init(self, **kwargs):
        return super().init(**kwargs)

    def update(self):
        if self.delay <= 0:
            if pg.key.get_pressed()[pg.K_z]:
                Scene.changeScene(SceneOption.MENU)
                self.delay = 20
        else:
            self.delay -= 1

    def draw(self, window: pg.surface.Surface):
        for i, line in enumerate(self.lines):
            pos = (MID_X - line.get_width() / 2, MID_Y + i * 30 - len(self.lines) * 30 / 2)
            window.blit(line, pos)

