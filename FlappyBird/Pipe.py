## Pipes class for the flappy bird game
import pygame
import random
from flappybird.Constants import pipe_img, VEL, FLOOR_HEIGHT, WIN_WIDTH

class Pipe:
    def __init__(self, win):
        self.win = win
        self.x = WIN_WIDTH + 10
        self.height = 0
        self.vel = VEL
        self.gap = 120

        self.top = 0
        self.bottom = 0

        self.TOP_IMG = pygame.transform.flip(pipe_img, False, True)
        self.BOTTOM_IMG = pipe_img

        self.set_height()

    def set_height(self):
        self.height = random.randint(50, FLOOR_HEIGHT - 50 - self.gap)

        self.top = self.height - self.TOP_IMG.get_height()
        self.bottom = self.height + self.gap

    def move(self):
        self.x -= self.vel

    def draw(self):
        self.win.blit(self.TOP_IMG, (self.x, self.top))
        self.win.blit(self.BOTTOM_IMG, (self.x, self.bottom))
