import pygame
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
    '''brick = Brick()
    allsprites.add(brick)
    bricks.add(brick)'''

    game_over = False

    while True:
        # Event Loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT]:
            paddle.pos -= paddle.speed
        if keys_pressed[K_RIGHT]:
            paddle.pos += paddle.speed

        # Main Surface Drawing Functions
        DISPLAYSURF.fill(DARKBLUE)
        allsprites.draw(DISPLAYSURF)

        pygame.display.flip()                                                   # draw to surface
        FPSCLOCK.tick(FPS)

class Paddle(pygame.sprite.Sprite):
    speed = 5.0

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('paddle.png')
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.pos = (WINDOWWIDTH / 2) + (self.width / 2)
        self.rect.y = WINDOWHEIGHT - 50

    def update(self):
        self.rect.x = self.pos
        # Make sure the paddle doesn't move off the screen
        if self.rect.x > WINDOWWIDTH - self.width:
            self.rect.x = WINDOWWIDTH - self.width
        elif self.rect.x < WINDOWWIDTH:
            self.rect.x = WINDOWWIDTH


class Brick(pygame.sprite.Sprite):
    speed = 5.0


    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('brick.png')                       # not set as surface

        self.direction = 200

        self.x = WINDOWWIDTH / 2
        self.y = WINDOWHEIGHT - 100

if __name__ == '__main__':
    main()
