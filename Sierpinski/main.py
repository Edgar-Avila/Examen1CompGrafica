import pygame as pg
from OpenGL.GL import *
from enum import Enum

# Config
class Mode(Enum):
    Lines = 1,
    Triangles = 2

WIDTH, HEIGHT = (600, 600)
FPS = 60
CLOCK = pg.time.Clock()

MODE = Mode.Triangles
DEPTH = 4

#                 a
#                 /\   
#                /__\ 
#               /\  /\    
#              /__\/__\
#             /\      /\   
#            /__\    /__\ 
#           /\  /\  /\  /\ 
#        d /__\/__\/__\/__\ e
#         /\              /\ 
#        /__\            /__\ 
#       /\  /\          /\  /\
#      /__\/__\        /__\/__\
#     /\      /\      /\      /\  
#    /__\    /__\    /__\    /__\ 
#   /\  /\  /\  /\  /\  /\  /\  /\
#  /__\/__\/__\/__\/__\/__\/__\/__\
# b               f                c

def sierpinski_lines(ax, ay, bx, by, cx, cy, n):
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_LOOP)
    glVertex2f(ax, ay)
    glVertex2f(bx, by)
    glVertex2f(cx, cy)
    glEnd()
    sierpinski_lines_inside(ax, ay, bx, by, cx, cy, n)

def sierpinski_lines_inside(ax, ay, bx, by, cx, cy, n):
    if n <= 0:
        return
    dx, dy = (bx + ax) / 2, (by + ay) / 2
    ex, ey = (cx + ax) / 2, (cy + ay) / 2
    fx, fy = (bx + cx) / 2, (by + cy) / 2
    glBegin(GL_LINE_LOOP)
    glVertex2f(dx, dy)
    glVertex2f(ex, ey)
    glVertex2f(fx, fy)
    glEnd()

    sierpinski_lines_inside(ax, ay, dx, dy, ex, ey, n-1)
    sierpinski_lines_inside(dx, dy, bx, by, fx, fy, n-1)
    sierpinski_lines_inside(ex, ey, fx, fy, cx, cy, n-1)

def sierpinski_triangles(ax, ay, bx, by, cx, cy, n):
    glBegin(GL_TRIANGLES)

    # Triangulo blanco grande
    glColor3f(1, 1, 1)
    glVertex2f(ax, ay)
    glVertex2f(bx, by)
    glVertex2f(cx, cy)
    glEnd()

    # Triangulos negros
    sierpinski_triangles_black(ax, ay, bx, by, cx, cy, n)

def sierpinski_triangles_black(ax, ay, bx, by, cx, cy, n):
    if n <= 0:
        return
    dx, dy = (bx + ax) / 2, (by + ay) / 2
    ex, ey = (cx + ax) / 2, (cy + ay) / 2
    fx, fy = (bx + cx) / 2, (by + cy) / 2

    glBegin(GL_TRIANGLES)
    glColor3f(0, 0, 0)
    glVertex2f(dx, dy)
    glVertex2f(ex, ey)
    glVertex2f(fx, fy)
    glEnd()
    sierpinski_triangles_black(ax, ay, dx, dy, ex, ey, n-1)
    sierpinski_triangles_black(dx, dy, bx, by, fx, fy, n-1)
    sierpinski_triangles_black(ex, ey, fx, fy, cx, cy, n-1)


def main():
    pg.init()
    pg.display.set_mode((WIDTH, HEIGHT), pg.DOUBLEBUF | pg.OPENGL)
    pg.display.set_caption('OpenGL Primitives')

    # Valores iniciales 
    # ax, ay = 0, 1
    # bx, by = -1, -1
    # cx, cy = 1, -1

    ax, ay = 0, 1
    bx, by = -1, -1
    cx, cy = 1, -1

    # Variables
    running = True

    # Main loop
    while running:
        # Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        # Update

        # Draw
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        if MODE == Mode.Lines:
            sierpinski_lines(ax, ay, bx, by, cx, cy, DEPTH)
        elif MODE == Mode.Triangles:
            sierpinski_triangles(ax, ay, bx, by, cx, cy, DEPTH)
        pg.display.flip()

        # Framerate
        CLOCK.tick(FPS)

    pg.quit()


if __name__ == '__main__':
    main()
