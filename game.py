import pygame
import random

import shop
from settings import *
import shop

pygame.mixer.init()

class SnakeGame:

    def __init__(self, display):
        self.display = display
        self.w = W
        self.h = H
        self.clock = pygame.time.Clock()


        self.get_food = pygame.mixer.Sound('assets/sounds/get-food.mp3')
        self.loose = pygame.mixer.Sound('assets/sounds/loose.mp3')

        self.reset()

    def draw_background(self):
        for y in range(0, self.h, BLOCK_SIZE):
            for x in range(0, self.w, BLOCK_SIZE):
                is_even = (x // BLOCK_SIZE + y // BLOCK_SIZE) % 2 == 0
                color = colors["GREEN"] if is_even else colors["LIGHT_GREEN"]
                pygame.draw.rect(self.display, color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

    def reset(self):
        self.direction = Direction.RIGHT

        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head,
                      Point(self.head.x - BLOCK_SIZE, self.head.y),
                      Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]

        self.score = 0
        self.food = None
        self._place_food()
        self.frame_iteration = 0

    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self, score_final):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True, "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if self.direction != Direction.RIGHT:
                        self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if self.direction != Direction.LEFT:
                        self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.direction != Direction.DOWN:
                        self.direction = Direction.UP
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if self.direction != Direction.UP:
                        self.direction = Direction.DOWN

        self._move(self.direction)
        self.snake.insert(0, self.head)

        game_over = False
        if self._is_collision():
            self.loose.play()
            game_over = True
            return game_over, self.score

        if self.head == self.food:
            self.get_food.play()
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()

        self._update_ui(score_final)
        self.clock.tick(SPEED)
        return game_over, self.score

    def _is_collision(self):
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True
        if self.head in self.snake[1:]:
            return True
        return False

    def _update_ui(self, score_final):
        self.draw_background()

        for pt in self.snake:
            pygame.draw.rect(self.display, shop.SKIN1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, shop.SKIN2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))

        pygame.draw.rect(self.display, shop.FRUIT_SKIN, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        text = font.render("Score: " + str(self.score), True, colors["WHITE"])
        text2 = font.render("High Score: " + str(score_final), True, colors["WHITE"])
        self.display.blit(text, [0, 0])
        self.display.blit(text2, [400, 0])
        pygame.display.flip()

    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y)

def startgame(display, gamespeed=10):
    global SPEED
    SPEED = gamespeed

    game = SnakeGame(display)
    score_final = 0
    draw_background(display)

    while True:
        game_over, score = game.play_step(score_final)

        if score == "exit":
            return "exit"

        if game_over == True:
            game.reset()
            if score > score_final:
                score_final = score
            return "game_over"