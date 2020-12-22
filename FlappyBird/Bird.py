## Bird class for the flappy bird game
import pygame
from flappybird.Constants import BLACK

class Bird:
    def __init__(self, win):
        self.win = win
        self.y = 100
        self.x = 100

    def jump(self):
        print("jump")

    def move(self):
        pass

    def draw(self):
        pygame.draw.circle(self.win, BLACK, (self.x, self.y), 10)

    def get_mask(self):
        pass