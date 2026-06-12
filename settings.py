import pygame as pg
from enum import Enum
from collections import namedtuple

pg.init()

# all scripts

colors = {
    "WHITE": (255, 255, 255),
    "RED": (200, 0, 0),
    "BLACK": (0, 0, 0),
    "GREEN": (34, 139, 34),
    "LIGHT_GREEN": (50, 205, 50)
}

W=640
H=480

font = pg.font.Font('pixel.otf', 50)
big_font = pg.font.Font('pixel.otf', 100)
small_font = pg.font.Font('pixel.otf', 30)

# game.py

BLOCK_SIZE = 20
SPEED = 10

Point = namedtuple('Point', 'x, y')


class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


# functions

def draw_background(display):
    for y in range(0, H, BLOCK_SIZE):
        for x in range(0, W, BLOCK_SIZE):
            is_even = (x // BLOCK_SIZE + y // BLOCK_SIZE) % 2 == 0
            color = colors["GREEN"] if is_even else colors["LIGHT_GREEN"]
            pg.draw.rect(display, color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

class CreateButton():
    def __init__(self, x, y, w, h, text, button_path, button_hover_path):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.btn_text = text

        self.button = pg.image.load(button_path).convert_alpha()
        self.hover_button = pg.image.load(button_hover_path).convert_alpha()

        self.button = pg.transform.scale(self.button, (w, h))
        self.hover_button = pg.transform.scale(self.hover_button, (w, h))

        self.btn_rect = pg.Rect(x, y, w, h)

        self.text = font.render(self.btn_text, True, colors["WHITE"])
        self.text_rect = self.text.get_rect(center=self.btn_rect.center)

    def is_clicked(self):
        mouse_pos = pg.mouse.get_pos()
        if self.btn_rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0]:
                return True
        return False

    def draw(self, display):
        mouse_pos = pg.mouse.get_pos()
        if self.btn_rect.collidepoint(mouse_pos):
            display.blit(self.hover_button, self.btn_rect)
        else:
            display.blit(self.button, self.btn_rect)
        display.blit(self.text, self.text_rect)