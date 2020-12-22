## The main game class for the flappy bird game. Stores all the game logic and functionality
import pygame
from flappybird.Constants import bg_img
from flappybird.Bird import Bird
from flappybird.Base import Base
from flappybird.Pipe import Pipe


class Game:
    def __init__(self, win):
        self.win = win
        self.bg_img = bg_img
        self.bird = Bird(self.win)
        self.base = Base(self.win)
        self.pipes = []
        self.pipes.append(Pipe(self.win))
        self.tick_count = 0


    def jump(self):
        self.bird.jump()

    def add_pipes(self):
        self.tick_count += 1

        if self.tick_count == 100:
            self.pipes.append(Pipe(self.win))
            self.tick_count = 0

    def update(self):
        self.bird.move()
        self.base.move()
        self.add_pipes()
        for pipe in self.pipes:
            pipe.move()

    def draw(self):
        self.win.blit(self.bg_img, (0,0))
        self.bird.draw()
        for pipe in self.pipes:
            pipe.draw()
        self.base.draw()


        pygame.display.update()
