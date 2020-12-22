## The main game class for the flappy bird game. Stores all the game logic and functionality
import pygame
from flappybird.Constants import bg_img
from flappybird.Bird import Bird


class Game:
    def __init__(self, win):
        self.win = win
        self.bg_img = bg_img
        self.bird = Bird(self.win)
        self.pipes = []


    def jump(self):
        self.bird.jump()


    def update(self):
        self.win.blit(self.bg_img, (0,0))
        self.bird.draw()
        pygame.display.update()
