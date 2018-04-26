import pygame
import sys
import math
import random
from pygame.locals import *
from constants import *

bricks = pygame.sprite.Group()
brick_image = [
    pygame.image.load('sprites/brick0.png'),
    pygame.image.load('sprites/brick1.png'),
    pygame.image.load('sprites/brick2.png'),
    pygame.image.load('sprites/brick3.png'),
]

brick_props = [
    # type, color, hits
    [    0,    WHITE,    1],            #0
    [    0,      RED,    1],            #1
    [    0,    GREEN,    1],            #2
    [    0,     BLUE,    1],            #3
    [    0,     CYAN,    1],            #4
    [    0,  MAGENTA,    1],            #5
    [    0,   YELLOW,    1],            #6
    [    0,    BLACK,    1],            #7
    [    0,     GRAY,    1],            #8
    [    1,    WHITE,    1],            #9
    [    1,      RED,    1],            #10
    [    1,    GREEN,    1],            #11
    [    1,     BLUE,    1],            #12
    [    1,     CYAN,    1],            #13
    [    1,  MAGENTA,    1],            #14
    [    1,   YELLOW,    1],            #15
    [    1,    BLACK,    1],            #16
    [    1,     GRAY,    1],            #17
    [    2,    WHITE,    1],            #18
    [    2,      RED,    1],            #19
    [    2,    GREEN,    1],            #20
    [    2,     BLUE,    1],            #21
    [    2,     CYAN,    1],            #22
    [    2,  MAGENTA,    1],            #23
    [    2,   YELLOW,    1],            #24
    [    2,    BLACK,    1],            #25
    [    2,     GRAY,    1],            #26
    [    3,    WHITE,    1],            #27
    [    3,      RED,    1],            #28
    [    3,    GREEN,    1],            #29
    [    3,     BLUE,    1],            #30
    [    3,     CYAN,    1],            #31
    [    3,  MAGENTA,    1],            #32
    [    3,   YELLOW,    1],            #33
    [    3,    BLACK,    1],            #34
    [    3,     GRAY,    1],            #35
]


class Brick(pygame.sprite.Sprite):
    # ex: brick = Brick({type:}0, {x:}50, {y:}20)
    def __init__(self, type, x_pos, y_pos, brick_image=brick_image, brick_props=brick_props):
        super().__init__()

        props = brick_props[type]   #quick access to specific properties list
        #props = [type, color, hits]

        self.image = pygame.Surface.copy(brick_image[props[0]])
        self.image.fill(props[1], special_flags=BLEND_MULT)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.type = type
        self.health = props[2]

        self.rect.x = x_pos
        self.rect.y = y_pos
