import pygame as pg
from config import *
from ball import Ball

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
        keys = pg.key.get_pressed()
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            self.vel.y = self.sp
        if keys[pg.K_w] or keys[pg.K_UP]:
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
# def automatico(self, py):
#         self.y += self.vy
#         if self.aut <= 0:
#             medio = self.y + self.h / 2
#             if abs(medio-py) > self.h / 4:
#                 if medio < py:
#                     self.vy = self.sp
#                 else:
#                     self.vy = -self.sp
#             else:
#                 self.vy *= 0.2
#             self.aut = 2
#         else:
#             self.aut -= 1
#         self.bordes()

    def get_bounds(self) -> tuple[float, float, float, float]:
        left = self.rect.x
        right = self.rect.x + self.rect.w
        top = self.rect.y
        bottom = self.rect.y + self.rect.h
        return left, right, top, bottom
    
    def draw(self, window: pg.surface.Surface) -> None:
        pg.draw.rect(window, self.color, self.rect)
