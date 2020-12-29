## The main game class for the flappy bird game. Stores all the game logic and functionality
import pygame
from flappybird.Constants import bg_img
from flappybird.Bird import Bird
from flappybird.Base import Base
from flappybird.Pipe import Pipe
from flappybird.Constants import WIN_WIDTH, WIN_HEIGHT, FPS, BLACK, smallFont, bigFont, smallestFont, file_path

class Game:
    def __init__(self, win):
        self.win = win
        self.reset()

    def reset(self):
        self.bg_img = bg_img
        self.bird = Bird(self.win)
        self.base = Base(self.win)
        self.pipes = []
        self.pipes.append(Pipe(self.win))
        self.tick_count = 0
        self.score = 0
        self.highScore = 0
        self.get_high_score()
        self.started = False
        self.running = True
        self.ended = False
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
            text = smallFont.render("Press SPACE to start", False, BLACK)
            text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 + 50))
            self.win.blit(text, text_rect)

            pygame.display.update()

    def end_screen(self):
        self.set_high_score()

        run = True
        delay = 50
        message = ""

        while run:
            delay -= 1

            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
            if delay < 0:
                message = "Press SPACE to restart game"
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    run = False
                    self.reset()
                    return

            self.bird.crash()
            self.check_collisions()

            self.win.blit(self.bg_img, (0,0))
            self.bird.draw()
            for pipe in self.pipes:
                pipe.draw()
            self.base.draw()


            text = smallFont.render("Game Over", False, BLACK)
            text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))
            score_text = bigFont.render("Score: " + str(self.score), False, BLACK)
            score_text_rect = score_text.get_rect(center = (WIN_WIDTH/2, WIN_HEIGHT/2 + 50))
            restart_text = smallestFont.render(message, False, BLACK)
            restart_text_rect = restart_text.get_rect(center = (WIN_WIDTH/2, WIN_HEIGHT - 100))


            self.win.blit(restart_text, restart_text_rect)
            self.win.blit(text, text_rect)
            self.win.blit(score_text, score_text_rect)

            pygame.display.update()

    def get_high_score(self):
        try:
            f = open(file_path, "r")
            data = f.read()
            f.close()

            self.highScore = int(data)
        except:
            self.highScore = 0

    def set_high_score(self):
        if self.score > self.highScore:
            f = open(file_path,"w")
            f.write(str(self.score))
            f.close()

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
        if self.bird.y < 0 or self.bird.collide(self.pipes[0], self.base):
            self.ended = True

    def draw(self):
        self.win.blit(self.bg_img, (0,0))
        self.bird.draw()
        for pipe in self.pipes:
            pipe.draw()
        self.base.draw()

        textsurface = bigFont.render(str(self.score), False, (0, 0, 0))
        self.win.blit(textsurface, (10,10))


        pygame.display.update()
