"""
The main game class for the flappy bird game. Stores all the game logic and functionality
"""

import pygame
from flappybird.Constants import bg_img
from flappybird.Bird import Bird
from flappybird.Base import Base
from flappybird.Pipe import Pipe
from flappybird.Constants import WIN_WIDTH, WIN_HEIGHT, FPS, BLACK, mediumFont, largeFont, smallFont, file_path

class Game:
    def __init__(self, win):
        """
        Class holds the main game functionality for full game

        Arguments:
            win {surface} -- The surface everything will be drawn on to
        """
        self.win = win
        self.reset()

    def reset(self):
        """
        Method sets or resets all the class information to reset the game
        """
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
        """
        Method is the loop for the start screen, handling the logic
        """
        delay = 10
        run = True

        while run:
            delay -= 1
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if delay < 0:
                    self.started = True
                    run = False

            self.draw_start_screen()

    def draw_start_screen(self):
        """
        Method draws the start screen to the window
        """
        self.win.blit(self.bg_img, (0,0))
        self.bird.draw()


        welcome_message = mediumFont.render("Press SPACE to start", False, BLACK)
        rect = welcome_message.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2 + 50))
        self.win.blit(welcome_message, rect)

        pygame.display.update()

    def end_screen(self):
        """
        Method is the loop for the end game screen, handles the logic to start again
        """
        self.set_high_score()

        run = True
        delay = 30
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

            self.draw_end_screen(message)

    def draw_end_screen(self, message):
        """
        Method draws the end screen to the window
        Arguments:
            message {String} -- The message to the user written on the screen
        """
        self.win.blit(self.bg_img, (0,0))
        for pipe in self.pipes:
            pipe.draw()
        self.bird.draw()
        self.base.draw()


        self.end_game_text(message)

        pygame.display.update()

    def end_game_text(self, message):
        """
        Method writes the message to the screen

        Arguments:
            message {String} -- Stringt o be written to the screen
        """
        game_over_text = mediumFont.render("Game Over", False, BLACK)
        rect = game_over_text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))
        self.win.blit(game_over_text, rect)

        score_text = largeFont.render("Score: " + str(self.score), False, BLACK)
        rect = score_text.get_rect(center = (WIN_WIDTH/2, WIN_HEIGHT/2 + 50))
        self.win.blit(score_text, rect)

        restart_text = smallFont.render(message, False, BLACK)
        rect = restart_text.get_rect(center = (WIN_WIDTH/2, WIN_HEIGHT - 100))
        self.win.blit(restart_text, rect)

        if self.score > self.highScore and self.score > 0:
            high_score_text = largeFont.render("New High Score!", False, BLACK)
        else:
            high_score_text = mediumFont.render("High Score: " + str(self.highScore), False, BLACK)

        rect = high_score_text.get_rect(center = (WIN_WIDTH/2, WIN_HEIGHT/2 - 100))
        self.win.blit(high_score_text, rect)

    def get_high_score(self):
        """
        Method gets the previous high score from file
        """
        try:
            f = open(file_path, "r")
            data = f.read()
            f.close()

            self.highScore = int(data)
        except:
            self.highScore = 0

    def set_high_score(self):
        """
        Method writes the new high score to file
        """
        if self.score > self.highScore:
            f = open(file_path,"w")
            f.write(str(self.score))
            f.close()

    def jump(self):
        """
        Method causes bird to jump
        """
        self.bird.jump()

    def add_pipes(self):
        """
        Method adds pipes every 80 frames
        """
        self.tick_count += 1

        if self.tick_count == 80:
            self.pipes.append(Pipe(self.win))
            self.tick_count = 0

    def get_score(self):
        """
        Adds one to the score if the pipe has been passed
        """
        if not self.pipes[0].passed and self.bird.x > self.pipes[0].right():
            self.score += 1
            self.pipes[0].passed = True


    def update(self):
        """
        Method moves all pipes, bird and base
        """
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
        """
        Method checks if collision between bird and base, ceiling or pipes
        """
        if self.bird.y < 0:
            self.bird.hit_top = True
            self.ended = True

        if self.bird.collide(self.pipes[0], self.base):
            self.ended = True

    def draw(self):
        """
        Method draws the bird, base, pipes and score to the screen
        """
        self.win.blit(self.bg_img, (0,0))
        self.bird.draw()
        for pipe in self.pipes:
            pipe.draw()
        self.base.draw()

        textsurface = largeFont.render(str(self.score), False, (0, 0, 0))
        self.win.blit(textsurface, (10,10))


        pygame.display.update()
