import pygame
import sys
import math
import random
from pygame.locals import *

FPS = 60
WINDOWWIDTH = 800
WINDOWHEIGHT = 600

# Colors
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
MAGENTA  = (255,   0, 255)
CYAN     = (  0, 255, 255)
BLACK    = (  0,   0,   0)
GRAY     = (128, 128, 128)
WHITE    = (255, 255, 255)
DARKBLUE = (  0,   0, 128)

# Defaults
PADDLEMAXSPEED = 5
RANDOMCOLORS = (RED, GREEN, BLUE, YELLOW, MAGENTA, CYAN, GRAY, WHITE)


######## MAIN GAME FUNCTION ########
def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    FPSCLOCK = pygame.time.Clock()                                              # come back to understand classes
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Ball Breaker')

    # Initialize fonts
    FONTLARGE = pygame.font.Font("SuperMario256.ttf", 32)
    FONTSMALL = pygame.font.Font("SuperMario256.ttf", 16)

    # Initialize score
    score = 0

    # Create sprite lists
    allsprites = pygame.sprite.Group()
    bricks = pygame.sprite.Group()
    balls = pygame.sprite.Group()

    # Create the player paddle
    paddle = Paddle()
    allsprites.add(paddle)

    # Create the brick
    brick = Brick()
    allsprites.add(brick)
    bricks.add(brick)

    # Create the balls
    ball_image = pygame.image.load('ball.png')
    columns_wide = int(WINDOWWIDTH / ball_image.get_width()) - 1 # Set the number of balls for a wide row
    columns_narrow = columns_wide - 1 # Set the number of balls for a narrow row
    margin_wide = (WINDOWWIDTH - (columns_wide * ball_image.get_width())) / 2 # Center the wide rows
    margin_narrow = (WINDOWWIDTH - (columns_narrow * ball_image.get_width())) / 2 # Center the narrow rows
    top = 30 # Set the top y coordinate of the first row
    rows = 5 # Set number of rows
    # Create the rows, in alternating wide and narrow rows, with random colors for the balls, then add them to the allsprites list
    for i in range(rows):
        if i % 2 == 0:
            for j in range (columns_wide):
                ball = Ball(ball_image, RANDOMCOLORS[random.randint(0, len(RANDOMCOLORS) - 1)], (j * ball_image.get_width() + margin_wide), top)
                allsprites.add(ball)
                balls.add(ball)
        else:
            for k in range (columns_narrow):
                ball = Ball(ball_image, RANDOMCOLORS[random.randint(0, len(RANDOMCOLORS) - 1)], (k * ball_image.get_width() + margin_narrow), top)
                allsprites.add(ball)
                balls.add(ball)
        top += ball_image.get_height()

    game_over = False



##### GAME LOOP #####
    while True:
        # Clear the screen for next frame
        DISPLAYSURF.fill(DARKBLUE)

        # Event Loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()


        # If the player has not lost yet
        if not game_over:
            # Update the positions of objects on the screen
            paddle.update()
            brick.update()

            # ball bounce

            # paddle bounce


            # Update the score display
            scoretext = FONTSMALL.render("Score: " + str(score), True, WHITE)
            DISPLAYSURF.blit(scoretext, (10, 10))

        # If the player loses
        if game_over:
            text = FONTLARGE.render("Game Over", True, RED)
            textpos = text.get_rect(centerx = DISPLAYSURF.get_width()/2)
            textpos.top = 300
            DISPLAYSURF.blit(text, textpos)

        # Main Surface Drawing Functions
        allsprites.draw(DISPLAYSURF)

        pygame.display.flip()                                                   # draw to surface
        FPSCLOCK.tick(FPS)











#### CLASSES ####
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

    direction = 45     # Direction of ball (in degrees)

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('brick.png')
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect.x = WINDOWWIDTH / 2
        self.rect.y = WINDOWHEIGHT - 100

        self.angle_limit = 20                                              # most shallow angle ball can bounce off paddle at
        self.paddle_range = (180-self.angle_limit, self.angle_limit)

    def bounce_y(self):
        self.direction = (180 - self.direction) % 360
    def bounce_x(self):
        self.direction = (360 - self.direction) % 360

        # v_x = math.cos(math.radians(self.direction))
        # v_x = (v_x + (diff * PADDLEMAXSPEED)) / 2
        # self.direction = math.degrees(math.acos(v_x))               # include maximum horizontal angle later
    def bounce_paddle(self, partial):
        # partial expressed as a number between 0 ant 100 expressing a percentage along the paddle's hit range from left to right
        r = self.paddle_range
        if r[1] > r[2]:
            partial = abs(100-partial)      # invert percentage if provided range starts with larger angle number first
        partial = partial/100

        t = []
        for i in range(len(r)):
            t[i] = r[i] - min(r)

        new = max(t) * partial
        self.direction = new + min(r)



    def update(self):
        """ Update the position of the ball. """
        # Sine and Cosine work in degrees, so we have to convert them
        direction_radians = math.radians(self.direction)

        # Change the position (x and y) according to the speed and direction
        self.rect.x += self.speed * math.sin(direction_radians)
        self.rect.y -= self.speed * math.cos(direction_radians)

        if self.rect.x >= WINDOWWIDTH - self.width or self.rect.x <= 0: # Bounce off side walls
            self.bounce_x()

        if self.rect.y <= 0:
            self.bounce_y()
        elif self.rect.y >= WINDOWHEIGHT:           # return if below window for game over signal
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


if __name__ == '__main__':
    main()
