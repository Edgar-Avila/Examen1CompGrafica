import pygame as pg
from random import choice, randint

# General
WIDTH = 600
HEIGHT = 600
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
FPS = 60
TWO_PLAYER = False

# Game
PADDLE_W = 10
PADDLE_H = 80
BALL_RADIUS = 10
POINTS_TO_WIN = 1

# Keys
CANCEL = (pg.K_ESCAPE, pg.K_q)
ACCEPT = (pg.K_SPACE, pg.K_RETURN, pg.K_z)
LEFT = (pg.K_LEFT, pg.K_a)
RIGHT = (pg.K_RIGHT, pg.K_d)
UP = (pg.K_UP, pg.K_w)
DOWN = (pg.K_DOWN, pg.K_s)

# Colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Ball:
    def __init__(self, color):
        self.pos = pg.Vector2(MID_X, MID_Y)
        self.vel = pg.Vector2()
        self.radius = BALL_RADIUS
        self.color = color

    def spawn(self):
        self.pos = pg.Vector2(MID_X, MID_Y)
        self.vel = pg.Vector2()
    
    def start(self):
        opx, opy = choice((True, False)), choice((True, False))
        vx = randint(20, 40) / 10
        vy = randint(20, 40) / 10
        if opx:
            vx *= -1
        if opy:
            vy *= -1
        self.vel = pg.Vector2(vx, vy)

    def move(self):
        self.pos += self.vel
        if self.pos.y < 0 or self.pos.y > HEIGHT:
            self.vel.y *= -1

    def get_bounds(self):
        left = self.pos.x - self.radius
        right = self.pos.x + self.radius
        top = self.pos.y - self.radius
        bottom = self.pos.y + self.radius
        return left, right, top, bottom

    def draw(self, window):
        pg.draw.circle(window, self.color, self.pos, self.radius)

class Paddle:
    def __init__(self, x, color):
        y = MID_Y - PADDLE_H / 2
        self.points = 0
        self.rect = pg.Rect(x, y, PADDLE_W, PADDLE_H)
        self.start = pg.Rect(x, y, PADDLE_W, PADDLE_H)
        self.vel = pg.Vector2()
        self.color = color
        self.timer = 0
        self.sp = 10

    def spawn(self):
        self.rect = pg.Rect(self.start)
        self.vel = pg.Vector2()
    
    def move_input(self):
        self.vel = pg.Vector2()
        pressed = pg.key.get_pressed()
        if True in (pressed[k] for k in DOWN):
            self.vel.y = self.sp
        if True in (pressed[k] for k in UP):
            self.vel.y = -self.sp
        self.rect.move_ip(self.vel)
        self.rect.clamp_ip(0, 0, WIDTH, HEIGHT)

    def auto(self, ball: Ball):
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

    def get_bounds(self):
        left = self.rect.x
        right = self.rect.x + self.rect.w
        top = self.rect.y
        bottom = self.rect.y + self.rect.h
        return left, right, top, bottom
    
    def draw(self, window: pg.surface.Surface):
        pg.draw.rect(window, self.color, self.rect)

def check_collisions(ball, player1, player2):
    ba_l, ba_r, ba_t, ba_b = ball.get_bounds()
    _, p1_r, p1_t, p1_b = player1.get_bounds()
    p2_l, _, p2_t, p2_b = player2.get_bounds()

    ball_collides_p1 = ba_l < p1_r and ba_b > p1_t and ba_t < p1_b
    ball_collides_p2 = ba_r > p2_l and ba_b > p2_t and ba_t < p2_b

    if ball_collides_p1 and ball.vel.x < 0:
        ball.vel.x *= -1
    if ball_collides_p2 and ball.vel.x > 0:
        ball.vel.x *= -1

def check_point(ball, player1, player2):
    if ball.pos.x < 0 or ball.pos.x > WIDTH:
        if ball.pos.x < 0:
            player1.points += 1
        if ball.pos.x > WIDTH:
            player2.points += 1
        ball.spawn()
        player1.spawn()
        player2.spawn()

def draw_points(window, font, player1, player2):
    p1_text = font.render(f'{player1.points}', GREEN)[0]
    p2_text = font.render(f'{player2.points}', RED)[0]
    window.blit(p1_text, (MID_X - p1_text.get_width() - 10, 10))
    window.blit(p2_text, (MID_X + 10, 10))

def check_winner(player1, player2):
    if player1.points >= POINTS_TO_WIN:
        return "player1"
    if player2.points >= POINTS_TO_WIN:
        return "player2"
    return None

def main():
    # Init
    pg.init()
    pg.font.init()

    # Vars
    window = pg.display.set_mode((WIDTH, HEIGHT))
    font = pg.freetype.Font(None, 30)
    pg.display.set_caption('Pong')
    clock = pg.time.Clock()
    running = True
    winner = None

    # Entities
    ball = Ball(WHITE)
    player1 = Paddle(10, GREEN)
    player2 = Paddle(WIDTH - PADDLE_W - 10, RED)

    while running:
        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                # Exit
                if event.key in CANCEL:
                    running = False

                # Start game
                if event.key in ACCEPT:
                    if ball.vel.x == 0 and ball.vel.y == 0:
                        ball.start()
        # Update
        check_collisions(ball, player1, player2)
        check_point(ball, player1, player2)
        winner = check_winner(player1, player2)
        running = running and (winner is None)
        ball.move()
        player1.move_input()
        player2.auto(ball)

        # Draw
        window.fill(BLACK)
        pg.draw.line(window, GRAY, (MID_X, 0), (MID_X, HEIGHT))
        draw_points(window, font, player1, player2)
        player1.draw(window)
        player2.draw(window)
        ball.draw(window)
        pg.display.update()

        clock.tick(FPS)

    if winner is not None:
        if winner == player1:
            print("Ganaste")
        else:
            print("Perdiste")
    pg.quit()

if __name__ == '__main__':
    main()

