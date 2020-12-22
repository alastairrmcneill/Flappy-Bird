## Base class for the flappy bird game
import pygame
from flappybird.Constants import VEL, base_img, FLOOR_HEIGHT

class Base:
    vel = VEL
    img = base_img

    def __init__(self, win):
        self.win = win
        self.width = self.img.get_width()
        self.x1 = 0
        self.x2 = self.width
        self.x3 = self.x2 + self.width

    def move(self):
        self.x1 -= self.vel
        self.x2 -= self.vel
        self.x3 -= self.vel

        if self.x1 + self.width <0:
            self.x1 = self.x3 + self.width

        if self.x2 + self.width <0:
            self.x2 = self.x1 + self.width

        if self.x3 + self.width <0:
            self.x3 = self.x2 + self.width


    def draw(self):
        self.win.blit(self.img, (self.x1,FLOOR_HEIGHT))
        self.win.blit(self.img, (self.x2,FLOOR_HEIGHT))
        self.win.blit(self.img, (self.x3,FLOOR_HEIGHT))
