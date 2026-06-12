import pygame as pg
from menu import menu_cycle
from game import startgame
from game_over import game_over_cycle
from settings import *
from shop import shop_cycle

def main():
    pg.init()
    display = pg.display.set_mode((W, H))
    pg.display.set_caption('Classic Snake')
    clock = pg.time.Clock()

    state = 'menu'

    while state != "exit":
        if state == "menu":
            state = menu_cycle(display)

        elif state == "game":
            state = startgame(display)

        elif state == "shop":
            state = shop_cycle(display)

        elif state == "game_over":
            state = game_over_cycle(display)

    pg.quit()

if __name__ == "__main__":
    main()