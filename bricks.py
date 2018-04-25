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
    #type, color, hits
    [0, WHITE, 1],          #0
    [0, RED, 1],            #1
    [0, GREEN, 1],          #2
    [0, BLUE, 1],           #3
    [0, CYAN, 1],           #4
    [0, MAGENTA, 1],        #5
    [0, YELLOW, 1],         #6
    [0, BLACK, 1],          #7
    [0, GRAY, 1],           #8
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
