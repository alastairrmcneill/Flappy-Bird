## The main game class for the flappy bird game. Stores all the game logic and functionality
import pygame
from flappybird.Constants import bg_img
from flappybird.Bird import Bird
from flappybird.Base import Base
from flappybird.Pipe import Pipe
from flappybird.Constants import WIN_WIDTH, WIN_HEIGHT, FPS

pygame.font.init()
scoreFont = pygame.font.SysFont('Marker Felt', 50)
startFont = pygame.font.SysFont('Marker Felt', 30)

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
        self.started = False
        self.running = True
        self.clock = pygame.time.Clock()

    def start_screen(self):
        run = True
        while run:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.started = True
                run = False

            self.win.blit(self.bg_img, (0,0))
            self.bird.draw()
            text = startFont.render("Press SPACE to start", False, (0, 0, 0))
            text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 + 50))
            self.win.blit(text, text_rect)

            pygame.display.update()



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

        self.check_collisions()

        self.get_score()

    def check_collisions(self):
        if self.bird.y < 0:
            self.running = False

        if self.bird.collide(self.pipes[0], self.base):
            print("collided")
            self.running = False



    def draw(self):
        self.win.blit(self.bg_img, (0,0))
        self.bird.draw()
        for pipe in self.pipes:
            pipe.draw()
        self.base.draw()

        textsurface = scoreFont.render(str(self.score), False, (0, 0, 0))
        self.win.blit(textsurface, (10,10))


        pygame.display.update()
