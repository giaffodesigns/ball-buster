import pygame
import random
import sys
from pygame.locals import *

FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

# Colors
DARKBLUE = (0, 61, 102)

def main():
    global FPSCLOCK, DISPLAYSURF

    paddle = Paddle()

    pygame.init()
    FPSCLOCK = pygame.time.Clock()                                              # come back to understand classes
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Ball Breaker')

    while True:
        # Event Loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT]:
            paddle.x -= paddle.speed
        if keys_pressed[K_RIGHT]:
            paddle.x += paddle.speed

        # Main Surface Drawing Functions
        DISPLAYSURF.fill(DARKBLUE)
        DISPLAYSURF.blit(paddle.sprite, (paddle.x, paddle.y))                                        # add to DISPLAYSURF surface

        pygame.display.update()                                                     # draw to surface
        FPSCLOCK.tick(FPS)

class Paddle:
    def __init__(self):
        self.sprite = pygame.image.load('paddle.png')
        self.x = WINDOWWIDTH / 2
        self.y = WINDOWHEIGHT - 50
        self.speed = 2

if __name__ == '__main__':
    main()
