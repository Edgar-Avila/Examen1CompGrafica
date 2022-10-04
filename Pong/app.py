import pygame as pg
from config import *
from colors import *
from game import Game

class App:
    def __init__(self) -> None:
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = False
        self.game = Game()

    def events(self) -> None:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                if event.key == pg.K_SPACE:
                    self.game.start()

    def update(self) -> None:
        self.game.update()

    def draw(self) -> None:
        self.window.fill(BLACK)
        self.game.draw(self.window)
        pg.display.update()

    def run(self):
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
