## Bird class for the flappy bird game
import pygame
from flappybird.Constants import BLACK, WIN_HEIGHT, bird_imgs

class Bird:
    IMGS = bird_imgs

    def __init__(self, win):
        self.win = win
        self.y = WIN_HEIGHT//2
        self.height = self.y
        self.x = 75
        self.vel = 0
        self.tick_count = 0
        self.tilt = 0
        self.img = self.IMGS[0]
        self.rotated_img = self.img
        self.img_count = 0
        self.img_loop = 5
        self.rot_vel = 10
        self.new_rect = None


    def jump(self):
        self.vel = -10
        self.tick_count = 0
        self.height = self.y


    def move(self):
        self.tick_count += 1
        displacement = self.vel*self.tick_count + 0.5*3*self.tick_count**2

        if displacement > 20:
            displacement = 20

        self.y = self.y + displacement

        self.get_rotation(displacement)


    def get_rotation(self, displacement):
        if displacement < 0:
            self.tilt = 20
        else:
            if self.tilt > -80:
                self.tilt -= self.rot_vel


    def get_img(self):
        self.img_count += 1

        if self.img_count < self.img_loop:
            self.img = self.IMGS[0]
        elif self.img_count < self.img_loop * 2:
            self.img = self.IMGS[1]
        elif self.img_count < self.img_loop * 3:
            self.img = self.IMGS[2]
        elif self.img_count < self.img_loop * 4:
            self.img = self.IMGS[1]
        else:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt < -80:
            self.img = self.IMGS[1]
            self.img_count = int(self.img_loop * 1.5)




    def draw(self):
        self.get_img()

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)

        self.win.blit(rotated_image, new_rect.topleft)


    def get_mask(self):
        pass