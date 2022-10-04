import pygame as pg
from config import *
from colors import *
from scene import Scene, SceneOption
from game import Game
from menu import Menu
from help import Help

class App:
    def __init__(self) -> None:
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = False
        self.game = Game()
        self.menu = Menu()
        self.help = Help()

    def events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                if event.key == pg.K_SPACE:
                    self.game.start()

    def update(self) -> None:
        if Scene.current == SceneOption.GAME:
            self.game.update()
        elif Scene.current == SceneOption.MENU:
            self.menu.update()
        elif Scene.current == SceneOption.HELP:
            self.help.update()

    def draw(self) -> None:
        self.window.fill(BLACK)
        if Scene.current == SceneOption.GAME:
            self.game.draw(self.window)
        elif Scene.current == SceneOption.MENU:
            self.menu.draw(self.window)
        elif Scene.current == SceneOption.HELP:
            self.help.draw(self.window)
        pg.display.update()

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
