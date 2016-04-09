#platfwork.py
import sys, pygame
pygame.init()

size = width, height = 1000, 800
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("shitty vacuum.png")
space = pygame.image.load("space.png")
ballrect = ball.get_rect()
spacerect = space.get_rect()

y = 0
x = 0
speed = 5
movetab = []

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == 119: #w
                if y >= 0:
                    y -= speed
            elif event.key == 97: #a
                if x >= 0:
                    x -= speed
            elif event.key == 115: #s
                if y <= 0:
                    y += speed
            elif event.key == 100: #d
                if x <= 0:
                    x += speed
        elif event.type == pygame.KEYUP:
            if event.key == 119: #w
                if y <= 0:
                    y += speed
            elif event.key == 97: #a
                if x <= 0:
                    x += speed
            elif event.key == 115: #s
                if y >= 0:
                    y -= speed
            elif event.key == 100: #d
                if x >= 0:
                    x -= speed
    ballrect = ballrect.move([x,y])
    screen.blit(space, spacerect)
    screen.blit(ball, ballrect)
    pygame.display.flip()
 