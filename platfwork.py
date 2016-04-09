#platfwork.py
import sys, pygame
pygame.init()

size = width, height = 1920, 1080
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("dpad.png")
ballrect = ball.get_rect()

y = 0
x = 0
speed = 1
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
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
 