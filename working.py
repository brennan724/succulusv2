#platfwork.py

import sys, pygame, random
pygame.init()

size = width, height = 1000, 700
color = 250, 0, 0

screen = pygame.display.set_mode(size)

succulus = pygame.image.load("shitty vacuum.png")
amy = pygame.image.load("amy.gif")
andy = pygame.image.load("andy.gif")
anna = pygame.image.load("anna.gif")
dln = pygame.image.load("dln.gif")
dave = pygame.image.load("dave.gif")
jadrian = pygame.image.load("jadrian.gif")
jeff = pygame.image.load("jeff.gif")
obama = pygame.image.load("obama.gif")
putin = pygame.image.load("putin.gif")
sherri = pygame.image.load("sherri.gif")
steviep = pygame.image.load("stevie_p.gif")

space = pygame.image.load("space.png")
succulusrect = succulus.get_rect()
spacerect = space.get_rect()

amyrect = amy.get_rect()
andyrect = andy.get_rect()
annarect = anna.get_rect()
dlnrect = dln.get_rect()
daverect = dave.get_rect()
jadrianrect = jadrian.get_rect()
jeffrect = jeff.get_rect()
obamarect = obama.get_rect()
putinrect = putin.get_rect()
sherrirect = sherri.get_rect()
stevierect = steviep.get_rect()




font = pygame.font.Font(None, 20)
text = 'Space Vacuum'
size = font.size(text)
ren = font.render(text, 0, color, space)

y = 0
x = 0
x2 = random.randrange(10)
y2 = random.randrange(10)
x3 = random.randrange(10)
y3 = random.randrange(10)
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

    succulusrect = succulusrect.move([x,y])

    amyrect = amyrect.move([x2,y2])
    annarect = annarect.move([x3,y3])
    if amyrect.center[0] - amyrect.w//2 + x < 0 or amyrect.center[0] + amyrect.w//2 + x > width:
        x2 = - x2
    if amyrect.center[1] - amyrect.h//2 + y < 0 or amyrect.center[1] + amyrect.h//2 + y > height:
        y2 = - y2
    if annarect.center[0] - annarect.w//2 + x < 0 or annarect.center[0] + annarect.w//2 + x > width:
        x3 = - x3
    if annarect.center[1] - annarect.h//2 + y < 0 or annarect.center[1] + annarect.h//2 + y > height:
        y3 = - y3
    screen.blit(space, spacerect)
    screen.blit(amy, amyrect)
    screen.blit(anna, annarect)
    #screen.blit(text, textrect)
    screen.blit(succulus, succulusrect)
    pygame.display.flip()
 