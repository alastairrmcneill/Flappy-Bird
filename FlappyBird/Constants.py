## Constants for the Flappy Bird game
import os
import pygame

# Window settings
WIN_HEIGHT = 600
WIN_WIDTH = 400


# Images
base_path = os.path.dirname(os.path.dirname(__file__))
imgs_path = os.path.join(base_path, "imgs")
bg_img = pygame.transform.scale(pygame.image.load(os.path.join(imgs_path,"bg.png")), (WIN_WIDTH, WIN_HEIGHT))


# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
