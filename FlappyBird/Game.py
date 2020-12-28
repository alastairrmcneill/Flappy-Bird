## The main game class for the flappy bird game. Stores all the game logic and functionality
import pygame
from flappybird.Constants import bg_img
from flappybird.Bird import Bird
from flappybird.Base import Base
from flappybird.Pipe import Pipe

pygame.font.init()
myfont = pygame.font.SysFont('Marker Felt', 50)

class Game:
    def __init__(self, win):
        self.win = win
        self.bg_img = bg_img
        self.bird = Bird(self.win)
        self.base = Base(self.win)
        self.pipes = []
        self.pipes.append(Pipe(self.win))
        self.tick_count = 0
        self.score = 0


    def jump(self):
        self.bird.jump()

    def add_pipes(self):
        self.tick_count += 1

        if self.tick_count == 100:
            self.pipes.append(Pipe(self.win))
            self.tick_count = 0

    def get_score(self):
        if not self.pipes[0].passed and self.bird.x > self.pipes[0].right():
            self.score += 1
            self.pipes[0].passed = True


    def update(self):
        if self.pipes[0].off_screen():
            self.pipes.pop(0)

        self.bird.move()
        self.base.move()
        self.add_pipes()
        for pipe in self.pipes:
            pipe.move()

        self.get_score()



    def draw(self):
        self.win.blit(self.bg_img, (0,0))
        self.bird.draw()
        for pipe in self.pipes:
            pipe.draw()
        self.base.draw()

        textsurface = myfont.render(str(self.score), False, (0, 0, 0))
        self.win.blit(textsurface, (10,10))


        pygame.display.update()
