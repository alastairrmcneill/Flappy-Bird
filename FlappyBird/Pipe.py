import pygame
import random
from FlappyBird.Constants import pipe_img, VEL, FLOOR_HEIGHT, WIN_WIDTH

class Pipe:
    def __init__(self, win):
        """
        Pipe class containing the top and bottom pipes
        Arguments:
            win {Surface} -- The window object on to which we draw
        """
        self.win = win
        self.x = WIN_WIDTH + 10
        self.height = 0
        self.vel = VEL
        self.gap = 150
        self.passed = False

        self.top = 0
        self.bottom = 0

        self.TOP_IMG = pygame.transform.flip(pipe_img, False, True)
        self.BOTTOM_IMG = pipe_img

        self.set_height()

    def set_height(self):
        """
        Method sets the position of the top of the gap between pipes
        """
        self.height = random.randint(50, FLOOR_HEIGHT - 50 - self.gap)

        self.top = self.height - self.TOP_IMG.get_height()
        self.bottom = self.height + self.gap

    def move(self):
        """
        Method moves the pipe towards the bird
        """
        self.x -= self.vel

    def off_screen(self):
        """
        Method checks if pipe is off the screen

        Returns:
            Bool -- True if pipe is off the screen
        """
        return self.x + self.TOP_IMG.get_width() < 0

    def right(self):
        """
        Method gives the right hand edge of pipe

        Returns:
            Int -- x position of the right hand edge
        """
        return self.x + self.TOP_IMG.get_width()

    def get_masks(self):
        """
        Method gives masks of the pipe surface for colision detection
        Returns:
            Mask -- returns both top and bottom masks
        """

        top_mask = pygame.mask.from_surface(self.TOP_IMG)
        bottom_mask = pygame.mask.from_surface(self.BOTTOM_IMG)

        return top_mask, bottom_mask

    def draw(self):
        """
        Method draws the pipes to the screen
        """
        self.win.blit(self.TOP_IMG, (self.x, self.top))
        self.win.blit(self.BOTTOM_IMG, (self.x, self.bottom))
