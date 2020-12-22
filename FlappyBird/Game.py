## The main game class for the flappy bird game. Stores all the game logic and functionality
import pygame
from flappybird.Constants import bg_img
from flappybird.Bird import Bird
from flappybird.Base import Base


class Game:
    def __init__(self, win):
        self.win = win
        self.bg_img = bg_img
        self.bird = Bird(self.win)
        self.base = Base(self.win)


    def jump(self):
        self.bird.jump()


    def update(self):
        self.bird.move()
        self.base.move()

        self.win.blit(self.bg_img, (0,0))
        self.bird.draw()
        self.base.draw()

        pygame.display.update()
