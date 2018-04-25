import pygame
import sys
import math
import random
import easygui
from pygame.locals import *
from bricks import *
from constants import *

WINDOWWIDTH_ACTUAL = WINDOWWIDTH + 350

def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    FPSCLOCK = pygame.time.Clock()                                              # come back to understand classes
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH_ACTUAL, WINDOWHEIGHT))
    pygame.display.set_caption('Ball Buster - Level Builder')

    PLAYSURF = pygame.Surface((WINDOWWIDTH, WINDOWHEIGHT))

##### PROGRAM LOOP #####
    while True:
        # Clear the screen for next frame
        DISPLAYSURF.fill(BLACK)
        PLAYSURF.fill(DARKBLUE)

        # Event Loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        # Main Surface Drawing Functions
        DISPLAYSURF.blit(PLAYSURF, (0, 0))
        #allsprites.draw(DISPLAYSURF)

        pygame.display.flip()
        FPSCLOCK.tick(FPS)

    # palette (sprite group)
        # any click, mouse changes to match, sets a variable
        # to match represented brick
    # mouse objects
    # buttons
        # save level
        # name level
        # load level

if __name__ == '__main__':
    main()
