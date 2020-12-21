# Main file for the flappy bird game

# Imports
import pygame
from FlappyBird.Constants import WIN_HEIGHT, WIN_WIDTH

# Variables and constants
pygame.display.set_mode((WIN_HEIGHT, WIN_WIDTH))
pygame.display.set_caption("Flappy Bird")


# Main function
def main():
    run = True

    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pass

        pygame.display.update()

    pygame.quit()


# Run main loop
main()
