from app import App
import pygame as pg

def main():
    pg.init()
    pg.font.init()
    app = App()
    app.run()

if __name__ == '__main__':
    main()
