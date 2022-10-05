import pygame as pg
from scene import Scene, SceneOption
from config import *
from colors import *

class Menu(Scene):
    def __init__(self) -> None:
        self.font = pg.font.SysFont('Comic Sans MS', 30)
        self.options = ['Start', 'Help', 'Exit']
        self.imgs = [self.font.render(option, False, WHITE) for option in self.options]
        self.imgs_selected = [self.font.render(option, False, GREEN) for option in self.options]
        self.selected = 0
        self.delay = 0

    def init(self, **kwargs):
        return super().init()
    
    def run_selected(self) -> None:
        selected_option = self.options[self.selected]
        if selected_option == 'Start':
            Scene.changeScene(SceneOption.GAME)
        elif selected_option == 'Help':
            Scene.changeScene(SceneOption.HELP)
        elif selected_option == 'Exit':
            pg.quit()
            exit()

    def update(self) -> None:
        self.input()

    def down(self) -> None:
        self.selected += 1
        if self.selected >= len(self.options):
            self.selected = 0

    def up(self) -> None:
        self.selected -= 1
        if self.selected < 0:
            self.selected = len(self.options) - 1

    def input(self) -> None:
        if self.delay <= 0:
            keys = pg.key.get_pressed()
            if keys[pg.K_DOWN]:
                self.down()
            elif keys[pg.K_UP]:
                self.up()
            elif keys[pg.K_RETURN] or keys[pg.K_z]:
                self.run_selected()
            self.delay = 10
        else:
            self.delay -= 1

    def draw(self, window: pg.surface.Surface) -> None:
        for i, (img, img2) in enumerate(zip(self.imgs, self.imgs_selected)):
            pos = (40 + 20 * i, MID_Y - 20 * len(self.options) + 40 * i)
            if self.selected == i:
                window.blit(img2, pos)
            else:
                window.blit(img, pos)
