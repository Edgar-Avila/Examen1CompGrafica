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
        pg.display.set_caption("Pong")
        self.clock = pg.time.Clock()
        self.running = False
        self.scenes = {
            SceneOption.GAME: Game(),
            SceneOption.MENU: Menu(),
            SceneOption.HELP: Help()
        }

    def events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                self.running = False
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
            self.scenes[Scene.current].handle_events(event)

    def update(self) -> None:
        self.scenes[Scene.current].update()

    def draw(self) -> None:
        self.window.fill(BLACK)
        self.scenes[Scene.current].draw(self.window)
        pg.display.update()

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
