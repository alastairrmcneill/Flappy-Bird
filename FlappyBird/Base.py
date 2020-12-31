"""
Base class for the flappy bird game
"""

import pygame
from FlappyBird.Constants import VEL, base_img, FLOOR_HEIGHT

class Base:
    vel = VEL
    img = base_img

    def __init__(self, win):
        """
        Base class for the base of the game
        Arguments:
            win {Surface} -- Surface on to which everything is drawn
        """
        self.win = win
        self.width = self.img.get_width()
        self.x1 = 0
        self.x2 = self.width
        self.x3 = self.x2 + self.width
        self.y = FLOOR_HEIGHT

    def move(self):
        """
        Method moves the base to the left
        """
        self.x1 -= self.vel
        self.x2 -= self.vel
        self.x3 -= self.vel

        if self.x1 + self.width <0:
            self.x1 = self.x3 + self.width

        if self.x2 + self.width <0:
            self.x2 = self.x1 + self.width

        if self.x3 + self.width <0:
            self.x3 = self.x2 + self.width

    def get_mask(self):
        """
        Method returns the mask of the base image
        Returns:
            Mask -- Mask of the base image
        """
        return pygame.mask.from_surface(self.img)


    def draw(self):
        """
        Method draws the base to the screen
        """
        self.win.blit(self.img, (self.x1,self.y))
        self.win.blit(self.img, (self.x2,self.y))
        self.win.blit(self.img, (self.x3,self.y))
