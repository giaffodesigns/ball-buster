import pygame
import sys
import math
from pygame.locals import *

FPS = 60
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

# Colors
DARKBLUE = (  0,  61, 102)
RED =      (255,   0,   0)

# Defaults
PADDLEMAXSPEED = 5

def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    FPSCLOCK = pygame.time.Clock()                                              # come back to understand classes
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Ball Breaker')

    FONT = pygame.font.Font(None, 24)

    # Create sprite lists
    allsprites = pygame.sprite.Group()

    # Create the player paddle
    paddle = Paddle()
    allsprites.add(paddle)

    # Create the brick
    '''brick = Brick()
    allsprites.add(brick)'''

    # THIS IS JUST A TEST
    ball_image = pygame.image.load('ball.png')
    ball = Ball(ball_image, RED, 200, 200)
    allsprites.add(ball)
    ball = Ball(ball_image, DARKBLUE, 300, 300)
    allsprites.add(ball)
    # THIS IS JUST A TEST

    game_over = False

    while True:
        # Event Loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        # Update object positions on screen
        if not game_over:
            paddle.update()

        # Main Surface Drawing Functions
        DISPLAYSURF.fill(DARKBLUE)
        allsprites.draw(DISPLAYSURF)

        pygame.display.flip()                                                   # draw to surface
        FPSCLOCK.tick(FPS)


class Paddle(pygame.sprite.Sprite):
    speed = 5.0

    bounce_mult = 3         # multiple used to change angle of brick when hitting paddle

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('paddle.png')
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect.x = (WINDOWWIDTH / 2) - (self.width / 2)
        self.rect.y = WINDOWHEIGHT - 50

    def update(self):
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT]:
            self.rect.x += self.speed

        # Make sure the paddle doesn't move off the screen
        if self.rect.x > WINDOWWIDTH - self.width:
            self.rect.x = WINDOWWIDTH - self.width
        elif self.rect.x < 0:
            self.rect.x = 0


class Brick(pygame.sprite.Sprite):
    speed = 5.0

    direction = 200     # Direction of ball (in degrees)

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('brick.png')
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect.x = WINDOWWIDTH / 2
        self.rect.y = WINDOWHEIGHT - 100

    def bounce_x(self):
        self.direction = (180 - self.direction) % 360
    def bounce_y(self, diff):
        self.direction = ((180 - self.direction) % 360) % 360
        if diff:
            v_x = math.cos(math.radians(self.direction))
            v_x = (v_x + (diff * PADDLEMAXSPEED)) / 2
            self.direction = math.degrees(math.acos(v_x))               # include maximmum horizontal angle later






    def update(self):


        if self.rect.y >= WINDOWWIDTH:
            return False
        else:
            return True


class Ball(pygame.sprite.Sprite):
    def __init__(self, ball_image, color, x_pos, y_pos):
        super().__init__()

        self.image = pygame.Surface.copy(ball_image)
        self.image.fill(color, special_flags=BLEND_MULT)
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()


        self.rect.x = x_pos
        self.rect.y = y_pos

    def drawBalls(self, rows, top):
        columns = int(WINDOWWIDTH / self.width) - 1
        margin = (WINDOWWIDTH - (columns * self.width)) / 2


if __name__ == '__main__':
    main()
