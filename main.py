import pygame
import sys
import math
import random
from pygame.locals import *
from bricks import *
from constants import *




######## MAIN GAME FUNCTION ########
def main():
    global FPSCLOCK, DISPLAYSURF

    pygame.init()
    FPSCLOCK = pygame.time.Clock()                                              # come back to understand classes
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Ball Breaker')

    # Initialize fonts
    FONTLARGE = pygame.font.Font("RussoOne-Regular.ttf", 60)
    FONTSMALL = pygame.font.Font("RussoOne-Regular.ttf", 20)

    # Initialize score
    score = 0

    # Create sprite lists
    allsprites = pygame.sprite.Group()
    bricks = pygame.sprite.Group()
    balls = pygame.sprite.Group()

    # Create the player paddle
    paddle = Paddle()
    allsprites.add(paddle)

    # Create the ball
    ball = Ball()
    allsprites.add(ball)
    balls.add(ball)

    # Create the bricks
    # Open the level file and read it line by line
    with open("levels/samplelevel.lvl") as f:
        bricklist = f.read().splitlines()
    f.close() # Close the level file so it's not taking up memory

    # Convert the list values to integers (they are currently strings)
    for i in range(len(bricklist)):
        bricklist[i] = [int(j) for j in bricklist[i].split()]

    # Create each brick from the level file, passing the arguments [bricktype, x, y]
    # Add those bricks to the "bricks" sprite list
    for i in range(len(bricklist)):
        brick = Brick(bricklist[i][0], bricklist[i][1], bricklist[i][2])
        allsprites.add(brick)
        bricks.add(brick)

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
            game_over = ball.update()      # update brick position; ends game if brick falls off screen

            # ball bounce
            brickskilled = pygame.sprite.spritecollide(ball, bricks, True)
            for brick in brickskilled: # Check the list of colliding sprites, and add one to the score for each one
                score += 1
            # If we actually hit a block, bounce the ball
            if len(brickskilled) > 0:
                bouncedirection = get_bounce_direction(brickskilled[0], ball)
                print (bouncedirection)
                if bouncedirection == 1:
                    ball.bounce_x()
                elif bouncedirection == 0:
                    ball.bounce_y()
                # Game ends if all the blocks are gone
                if len(bricks) == 0:
                    game_over = True

            # paddle bounce
            if pygame.sprite.spritecollide(paddle, balls, False):
                ball.bounce_paddle(paddle)



            # Update the score display
            scoretext = FONTSMALL.render("Score: " + str(score), True, WHITE)
            DISPLAYSURF.blit(scoretext, (10, 10))

        # If the player loses
        if game_over:
            text = FONTLARGE.render("Game Over", True, WHITE)
            text_x = (WINDOWWIDTH / 2) - (text.get_width() / 2)
            text_y = (WINDOWHEIGHT / 2) - (text.get_height() / 2)
            DISPLAYSURF.blit(text, (text_x, text_y))

        # Main Surface Drawing Functions
        allsprites.draw(DISPLAYSURF)

        pygame.display.flip()                                                   # draw to surface
        FPSCLOCK.tick(FPS)






#### INTERNAL FUNCTIONS ####
def range_percent(low, high, ref, force_range=False):
    # takes two numbers as a range and the object being analyzed and returns
    # the object's position between the two, with 0.000 being the low number and 1.000 being the high number
    offset = min(low, high)
    percent = (ref-offset)/(high-offset)
    # print(percent)                                                                                                         # TROUBLESHOOT
    if force_range == True:
        if percent > 1: percent = 1
        if percent < 0: percent = 0
    return percent


def get_bounce_direction(ball, brick):
    # brick moving to left
    if ball.rect.right >= brick.rect.left >= ball.rect.right - brick.speed:
        return 1
    # brick moving to right
    elif ball.rect.left <= brick.rect.right <= ball.rect.left + brick.speed:
        return 1
    else:
        return 0



#### CLASSES ####
class Paddle(pygame.sprite.Sprite):
    speed = 5.0

    bounce_mult = 3         # multiple used to change angle of brick when hitting paddle

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("sprites/paddle.png")
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


class Ball(pygame.sprite.Sprite):
    speed = 5.0

    direction = -35    # Direction of ball (in degrees)

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("sprites/ball.png")
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect.x = WINDOWWIDTH / 2
        self.rect.y = WINDOWHEIGHT - 100
        # self.rect.x = 0


        self.angle_limit = 20                                              # most shallow angle ball can bounce off paddle at
        self.paddle_range = (180+self.angle_limit, 360-self.angle_limit)

    def bounce_x(self):
        self.direction = (180 - self.direction) % 360
        # print('current angle: ' + str(self.direction))                                                                                               # TROUBLESHOOT
    def bounce_y(self):
        self.direction = (360 - self.direction) % 360
        # print('current angle: ' + str(self.direction))                                                                                               # TROUBLESHOOT

        # v_x = math.cos(math.radians(self.direction))
        # v_x = (v_x + (diff * PADDLEMAXSPEED)) / 2
        # self.direction = math.degrees(math.acos(v_x))               # include maximum horizontal angle later
    def bounce_paddle(self, paddle_obj):
        # partial expressed as a number between 0 ant 100 expressing a percentage along the paddle's hit range from left to right
        brick_cent = self.rect.x + (self.width/2)
        partial = range_percent(paddle_obj.rect.x, paddle_obj.rect.x + paddle_obj.width, brick_cent, True)        # find position of brick along paddle's full length


        r = self.paddle_range
        if r[0] > r[1]:
            partial = abs(1-partial)      # invert percentage if provided range starts with larger angle number first

        t = list(r)
        offset = min(r)
        for i in range(len(r)):
            t[i] = r[i] - min(r)

        new = max(t) * partial

        print('percent: ' + str(partial), 'new angle: ' + str(new + offset))                                                                        # TROUBLESHOOT
        self.direction = new + offset
        self.rect.bottom = paddle_obj.rect.top - 1             # reposition block to be above paddle and out of collision box
        print('current angle: ' + str(self.direction))                                                                                    # TROUBLESHOOT



    def update(self):
        """ Update the position of the ball. """
        # Sine and Cosine work in degrees, so we have to convert them
        direction_radians = math.radians(self.direction + 90)
        fall = False

        # Change the position (x and y) according to the speed and direction
        self.rect.x += self.speed * math.sin(direction_radians)
        self.rect.y -= self.speed * math.cos(direction_radians)

        if self.rect.right >= WINDOWWIDTH:              # bounce off right wall
            self.bounce_x()
            self.rect.right = WINDOWWIDTH - 1
        elif self.rect.left <= 0:                       # bounce off left wall
            self.bounce_x()
            self.rect.left = 1


         # self.width or self.rect.x <= 0: # Bounce off side walls
         #    self.bounce_x()

        if self.rect.y <= 0:
            self.bounce_y()
        elif self.rect.y >= WINDOWHEIGHT:           # return if below window for game over signal
            fall = True

        return fall


if __name__ == '__main__':
    main()
