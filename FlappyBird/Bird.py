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
        self.gravity = 1
        self.tick_count = 0
        self.tilt = 0
        self.img = self.IMGS[0]
        self.rotated_img = self.img
        self.img_count = 0
        self.img_loop = 5
        self.rot_vel = 10
        self.new_rect = None
        self.hit_base = False
        self.hit_pipe = False
        self.hit_top = False


    def jump(self):
        self.vel = -4.5
        self.tick_count = 0
        self.height = self.y

    def crash(self):
        self.tilt = -90
        if self.hit_base:
             return
        if self.hit_pipe or self.hit_top:
            self.gravity = 10
            self.move()

    def move(self):
        self.tick_count += 1
        displacement = self.vel*self.tick_count + 0.5*self.gravity*self.tick_count**2

        if displacement > 15:
            displacement = 15
        print(displacement)

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

    def get_mask(self):
        return pygame.mask.from_surface(self.rotated_img)

    def collide(self, pipe, base):
        bird_mask = self.get_mask()

        top_mask, bottom_mask = pipe.get_masks()
        base_mask = base.get_mask()

        top_offset = (pipe.x - self.x, pipe.top - round(self.y))
        bottom_offset = (pipe.x - self.x, pipe.bottom - round(self.y))

        top_intersect = bird_mask.overlap(top_mask, top_offset)
        bottom_intersect = bird_mask.overlap(bottom_mask, bottom_offset)

        # Implement the base collisions
        base_offsets = [(base.x1 - self.x, base.y - round(self.y)), (base.x2 - self.x, base.y - round(self.y)), (base.x3 - self.x, base.y - round(self.y))]

        for offset in base_offsets:
            base_intersect = bird_mask.overlap(base_mask, offset)
            if base_intersect:
                self.hit_base = True
                return True

        if top_intersect or bottom_intersect:
            self.hit_pipe = True
            return True

        return False

    def draw(self):
        self.get_img()

        self.rotated_img = pygame.transform.rotate(self.img, self.tilt)
        new_rect = self.rotated_img.get_rect(center = self.img.get_rect(topleft = (self.x, self.y)).center)

        self.win.blit(self.rotated_img, new_rect.topleft)