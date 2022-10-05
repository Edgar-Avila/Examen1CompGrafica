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

    def handle_events(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_DOWN, pg.K_s):
                self.down()
            elif event.key in (pg.K_UP, pg.K_w):
                self.up()
            elif event.key in (pg.K_RETURN, pg.K_z, pg.K_SPACE):
                self.run_selected()

    def init(self, **kwargs):
        pass
    
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
        pass

    def down(self) -> None:
        self.selected += 1
        if self.selected >= len(self.options):
            self.selected = 0

    def up(self) -> None:
        self.selected -= 1
        if self.selected < 0:
            self.selected = len(self.options) - 1

    def draw(self, window: pg.surface.Surface) -> None:
        for i, (img, img2) in enumerate(zip(self.imgs, self.imgs_selected)):
            pos = (40 + 20 * i, MID_Y - 20 * len(self.options) + 40 * i)
            if self.selected == i:
                window.blit(img2, pos)
            else:
                window.blit(img, pos)
