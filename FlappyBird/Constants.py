## Constants for the Flappy Bird game
import os
import pygame

# Window settings
WIN_HEIGHT = 600
WIN_WIDTH = 400
FLOOR_HEIGHT = 560


# Images
base_path = os.path.dirname(os.path.dirname(__file__))
imgs_path = os.path.join(base_path, "imgs")
bg_img = pygame.transform.scale(pygame.image.load(os.path.join(imgs_path,"bg.png")), (WIN_WIDTH, WIN_HEIGHT))
bird_imgs = [pygame.image.load(os.path.join(imgs_path,"bird1.png")),
            pygame.image.load(os.path.join(imgs_path,"bird2.png")),
            pygame.image.load(os.path.join(imgs_path,"bird3.png"))]
base_img = pygame.image.load(os.path.join(imgs_path,"base.png"))
pipe_img = pygame.image.load(os.path.join(imgs_path,"pipe.png"))

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Game speed
FPS = 30
VEL = 4

# Fonts
pygame.font.init()
largeFont = pygame.font.SysFont('Marker Felt', 50)
mediumFont = pygame.font.SysFont('Marker Felt', 30)
smallFont = pygame.font.SysFont('Marker Felt', 20)


# Init File Path
file_path = os.path.join(base_path, "files/score.txt")
