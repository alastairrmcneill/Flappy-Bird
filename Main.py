# Main file for the flappy bird game

# Imports
import pygame
from flappybird.Constants import WIN_HEIGHT, WIN_WIDTH, FPS
from flappybird.Game import Game


# Variables and constants
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Main function
def main():
    run = True
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if not game.started:
            game.start_screen()
        if game.ended:
            game.end_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game.jump()

        game.update()
        game.draw()


    pygame.quit()


# Run main loop
main()
