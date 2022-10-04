import pygame as pg
from random import randint, choice
from config import *

class Ball:
    def __init__(self, color) -> None:
        self.pos = pg.Vector2(MID_X, MID_Y)
        self.vel = pg.Vector2()
        self.radius = BALL_RADIUS
        self.color = color

    def spawn(self) -> None:
        self.pos = pg.Vector2(MID_X, MID_Y)
        self.vel = pg.Vector2()
    
    def start(self) -> None:
        opx, opy = choice((True, False)), choice((True, False))
        vx = randint(20, 40) / 10
        vy = randint(20, 40) / 10
        if opx:
            vx *= -1
        if opy:
            vy *= -1
        self.vel = pg.Vector2(vx, vy)

    def move(self) -> None:
        self.pos += self.vel
        if self.pos.y < 0 or self.pos.y > HEIGHT:
            self.vel.y *= -1

    def get_bounds(self) -> tuple[float, float, float, float]:
        left = self.pos.x - self.radius
        right = self.pos.x + self.radius
        top = self.pos.y - self.radius
        bottom = self.pos.y + self.radius
        return left, right, top, bottom

    def draw(self, window) -> None:
        pg.draw.circle(window, self.color, self.pos, self.radius)

