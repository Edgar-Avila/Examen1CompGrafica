import pygame as pg
from scene import Scene
from paddle import Paddle
from ball import Ball
from config import *
from colors import *
from enum import Enum

class GameMode(Enum):
    SINGLE_PLAYER = 0,
    TWO_PLAYER = 1

class GameDifficulty(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2

class Game(Scene):
    def __init__(self) -> None:
        self.player1 = Paddle(10, GREEN)
        self.player2 = Paddle(WIDTH - PADDLE_W - 10, RED)
        self.ball = Ball(WHITE)
        self.p1_points = 0
        self.p2_points = 0
        self.font = pg.font.SysFont('Comic Sans MS', 30)

    def init(self, **kwargs):
        self.difficulty = kwargs.get('mode', GameDifficulty.MEDIUM)
        self.mode = kwargs.get('mode', GameMode.SINGLE_PLAYER)

    def start(self) -> None:
        if self.ball.vel.x == 0 and self.ball.vel.y == 0:
            self.ball.start()

    def check_collisions(self) -> None:
        ba_l, ba_r, ba_t, ba_b = self.ball.get_bounds()
        _, p1_r, p1_t, p1_b = self.player1.get_bounds()
        p2_l, _, p2_t, p2_b = self.player2.get_bounds()

        ball_collides_p1 = ba_l < p1_r and ba_b > p1_t and ba_t < p1_b
        ball_collides_p2 = ba_r > p2_l and ba_b > p2_t and ba_t < p2_b

        if ball_collides_p1 and self.ball.vel.x < 0:
            self.ball.vel.x *= -1
        if ball_collides_p2 and self.ball.vel.x > 0:
            self.ball.vel.x *= -1

    def check_point(self) -> None:
        if self.ball.pos.x < 0 or self.ball.pos.x > WIDTH:
            if self.ball.pos.x < 0:
                self.p2_points += 1
            if self.ball.pos.x > WIDTH:
                self.p1_points += 1
            self.ball.spawn()
            self.player1.spawn()
            self.player2.spawn()

    def draw_points(self, window: pg.surface.Surface) -> None:
        p1_text = self.font.render(f'{self.p1_points}', False, GREEN)
        p2_text = self.font.render(f'{self.p2_points}', False, RED)
        window.blit(p1_text, (MID_X - p1_text.get_width() - 10, 10))
        window.blit(p2_text, (MID_X + 10, 10))

    def update(self) -> None:
        self.check_point()
        self.player1.move_input()
        self.player2.auto(self.ball)
        self.ball.move()
        self.check_collisions()

    def draw(self, window: pg.surface.Surface) -> None:
        pg.draw.line(window, WHITE, (MID_X, 0), (MID_X, HEIGHT))
        self.draw_points(window)
        self.ball.draw(window)
        self.player1.draw(window)
        self.player2.draw(window)
