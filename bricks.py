import pygame
import sys
import math
import random
from pygame.locals import *

RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
MAGENTA  = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)
GRAY     = (128, 128, 128)
WHITE    = (255, 255, 255)

bricks = pygame.sprite.Group()
brick_image = [
    pygame.image.load('brick0.png'),
    pygame.image.load('brick1.png'),
    pygame.image.load('brick2.png'),
    pygame.image.load('brick3.png'),
]

brick_props = [
    #type, color, hits
    [0, WHITE, 1],
    [0, RED, 1],
    [0, GREEN, 1],
    [0, BLUE, 1],
    [0, CYAN, 1],
    [0, MAGENTA, 1],
    [0, YELLOW, 1],
    [0, BLACK, 1],
    [0, GREY, 1],
]


class Brick(pygame.sprite.Sprite):
    def __init__(self, , x_pos, y_pos, brick_image):
        super().__init__()

        self.image = pygame.Surface.copy(brick_image)
        self.image.fill(color, special_flags=BLEND_MULT)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect.x = x_pos
        self.rect.y = y_pos


class Brick_Call(Brick):
    def __init__(shape, type, x_pos, y_pos):






for info in list:
    Brick_Call(shape, type, x_pos, y_pos)
