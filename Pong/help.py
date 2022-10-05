import pygame as pg
from scene import Scene, SceneOption
from config import *
from colors import *
import keys

class Help(Scene):
    def __init__(self) -> None:
        self.font = pg.freetype.Font(None, 30)
        title = [
            "Instructions",
            " "
        ]
        controls = [
            "<Confirm> -> [Space, Z, Enter]",
            "<Down> -> [S, Down]",
            "<Up> -> [S, Up]",
            " "
        ]
        instructions = [
            "Press <Confirm> to start the match",
            "Press <Up> and <Down> to move",
            "Score a point when the ball goes past",
            "Your opponent goal.",
            "Press <Confirm> to go back"
        ]
        title = [self.font.render(line, YELLOW, BLACK) for line in title]
        controls = [self.font.render(line, GREEN, BLACK) for line in controls]
        instructions = [self.font.render(line, WHITE, BLACK) for line in instructions]
        self.lines = title + controls + instructions

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
            pos = (20, MID_Y + i * 30 - len(self.lines) * 30 / 2)
            window.blit(line[0], pos)

