"""
Author: Alastair McNeill
Recreate the Flappy Bird game within Python using pygame.
Has ability to restart after crash, pixel perfect collisions and high score tracking
"""

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
    """
    Main game loop that handles inputs
    """
    run = True
    game = Game(WIN)
    pressed = False                     # Means a click is only one click


    while run:
        clock.tick(FPS)

        if not game.started:            # If the game hasn't started yet show the start screen
            game.start_screen()
        if game.ended:                  # If the bird has crashed show the end screen
            game.end_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not pressed:
                        game.jump()
                        pressed = True  # Ensure the event is only registered once per click

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pressed = False     # Reset the button

        game.update()                   # Move all the pieces
        game.draw()                     # Draw all the pieces

    pygame.quit()

# Run main loop
main()
