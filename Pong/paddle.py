import pygame as pg
from typing import Tuple
from config import *
from ball import Ball
import keys

class Paddle:
    def __init__(self, x, color) -> None:
        y = MID_Y - PADDLE_H / 2
        self.rect = pg.Rect(x, y, PADDLE_W, PADDLE_H)
        self.start = pg.Rect(x, y, PADDLE_W, PADDLE_H)
        self.vel = pg.Vector2()
        self.color = color
        self.timer = 0
        self.sp = 10

    def spawn(self) -> None:
        self.rect = pg.Rect(self.start)
        self.vel = pg.Vector2()
    
    def move_input(self) -> None:
        self.vel = pg.Vector2()
        pressed = pg.key.get_pressed()
        if True in (pressed[k] for k in keys.DOWN):
            self.vel.y = self.sp
        if True in (pressed[k] for k in keys.UP):
            self.vel.y = -self.sp
        self.rect.move_ip(self.vel)
        self.rect.clamp_ip(0, 0, WIDTH, HEIGHT)

    def auto(self, ball: Ball) -> None:
        self.rect.move_ip(self.vel)
        mid = self.rect.y + self.rect.h / 2
        if self.timer <= 0:
            if abs(mid - ball.pos.y) > self.rect.h / 4:
                if mid < ball.pos.y:
                    self.vel.y = self.sp
                else:
                    self.vel.y = -self.sp
            else:
                self.vel.y *= 0.2
            self.rect.clamp_ip(0, 0, WIDTH, HEIGHT)

    def get_bounds(self) -> Tuple[float, float, float, float]:
        left = self.rect.x
        right = self.rect.x + self.rect.w
        top = self.rect.y
        bottom = self.rect.y + self.rect.h
        return left, right, top, bottom
    
    def draw(self, window: pg.surface.Surface) -> None:
        pg.draw.rect(window, self.color, self.rect)
