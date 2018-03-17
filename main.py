import pygame
import random
import sys
import math
from pygame.locals import *

FPS = 60
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

# Colors
DARKBLUE = (0, 61, 102)

def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    FPSCLOCK = pygame.time.Clock()                                              # come back to understand classes
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Ball Breaker')

    FONT = pygame.font.Font(None, 24)

    # Create sprite lists
    balls = pygame.sprite.Group()
    bricks = pygame.sprite.Group()
    allsprites = pygame.sprite.Group()

    # Create the player paddle
    paddle = Paddle()
    allsprites.add(paddle)

    # Create the brick
    brick = Brick()
    allsprites.add(brick)
    bricks.add(brick)

    game_over = False

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
        allsprites.draw(DISPLAYSURF)

        pygame.display.update()                                                 # draw to surface
        FPSCLOCK.tick(FPS)

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('paddle.png')
        self.rect = self.sprite.get_rect()

        self.rect.x = WINDOWWIDTH / 2
        self.rect.y = WINDOWHEIGHT - 50
        self.speed = 5

class Brick(pygame.sprite.Sprite):


    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('brick.png')                       # not set as surface
        self.speed = 5

        self.direction = 200

        self.x = WINDOWWIDTH / 2
        self.y = WINDOWHEIGHT - 100

if __name__ == '__main__':
    main()
