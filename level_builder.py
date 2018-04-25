import pygame
import sys
import math
import random
from pygame.locals import *
from bricks import *
from constants import *


def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    FPSCLOCK = pygame.time.Clock()                                              # come back to understand classes
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Ball Breaker')

    # palette (sprite group)
        # any click, mouse changes to match, sets a variable
        # to match represented brick
    # mouse objects
