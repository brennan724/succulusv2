# succulus.py
# Brennan Kuo, Jordan Sybesma, Sara Canilang, Mikyla Carpenter
# Carlhacks 2016

import sys, pygame, random, os, time,copy
pygame.init()

try: 
    import tkinter as tk
except:
    import Tkinter as tk

root = tk.Tk()

size = width, height = root.winfo_screenwidth()-100, root.winfo_screenheight()-100
color = 250, 250, 250
pygame.mixer.init()
pygame.mixer.music.load("soundtrack.OGG")
pygame.mixer.music.play(-1, 0.0)
start_time = time.clock()

screen = pygame.display.set_mode(size)

succulus = pygame.image.load("shitty vacuum.png") #create image objects
amy = pygame.image.load("amy.gif")
andy = pygame.image.load("andy.gif")
anna = pygame.image.load("anna.gif")
dln = pygame.image.load("dln.gif")
dave = pygame.image.load("dave.gif")
jadrian = pygame.image.load("jadrian.gif")
jeff = pygame.image.load("jeff.gif")
layla = pygame.image.load("layla.png")
obama = pygame.image.load("obama.gif")
putin = pygame.image.load("putin.gif")
sherri = pygame.image.load("sherri.gif")
steviep = pygame.image.load("stevie_p.gif")
schiller = pygame.image.load("schiller.gif")
space = pygame.image.load("space.png") #background

succulusrect = succulus.get_rect()
spacerect = space.get_rect()
amyrect = amy.get_rect() #get rekt
andyrect = andy.get_rect()
annarect = anna.get_rect()
dlnrect = dln.get_rect()
daverect = dave.get_rect()
jadrianrect = jadrian.get_rect()
jeffrect = jeff.get_rect()
laylarect = layla.get_rect()
obamarect = obama.get_rect()
putinrect = putin.get_rect()
sherrirect = sherri.get_rect()
stevieprect = steviep.get_rect()
schillerrect = schiller.get_rect()

profs = [
[amy,amyrect,random.randrange(10),random.randrange(10)],
[andy,andyrect,random.randrange(10),random.randrange(10)],
[dln,dlnrect,random.randrange(10),random.randrange(10)],
[dave,daverect,random.randrange(10),random.randrange(10)],
[jadrian,jadrianrect,random.randrange(10),random.randrange(10)],
[jeff,jeffrect,random.randrange(10),random.randrange(10)],
[layla,laylarect,random.randrange(10),random.randrange(10)],
[obama,obamarect,random.randrange(10),random.randrange(10)],
[putin,putinrect,random.randrange(10),random.randrange(10)],
[sherri,sherrirect,random.randrange(10),random.randrange(10)],
[steviep,stevieprect,random.randrange(10),random.randrange(10)],
[schiller, schillerrect,random.randrange(10),random.randrange(10)]
] #list of images and vectors for later iteration

backup = copy.copy(profs) #so we can restart later

font = pygame.font.Font(None, 150)
text = 'Space Vacuum'
size = font.size(text)
ren = font.render(text, 0, color)
textrect = ren.get_rect()

y = 0
x = 0
speed = 5
movetab = []

succulusrect = succulusrect.move([width-succulusrect.w,succulusrect.h])
screen.blit(succulus,succulusrect)

while 1: 
    #event handling
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
            elif event.key == 121 and len(profs) == 0: #y
                profs = copy.copy(backup)
            elif event.key == 110 and len(profs) == 0: #n
                sys.exit()
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
    
    #collision detection
    for p in profs:
        if succulusrect.colliderect(p[1]):
            #WE ATE U UP/
            profs.remove(p)
    
    #drawing
    if succulusrect.center[0] - succulusrect.w//2 + x < 0 or succulusrect.center[0] + succulusrect.w//2 + x > width:
        if succulusrect.center[1] - succulusrect.h//2 + y < 0 or succulusrect.center[1] + succulusrect.h//2 + y > height:
            succulusrect = succulusrect.move([0,0])
        else:
            succulusrect = succulusrect.move([0,y])
    else:
        if succulusrect.center[1] - succulusrect.h//2 + y < 0 or succulusrect.center[1] + succulusrect.h//2 + y > height:
            succulusrect = succulusrect.move([x,0])
        else:
            succulusrect = succulusrect.move([x,y])
            
    screen.blit(space, spacerect)
    for p in profs:
        if p[1].center[0] - p[1].w//2 + p[2] < 0 or p[1].center[0] + p[1].w//2 + p[2] > width:
            p[2] = - p[2]
        if p[1].center[1] - p[1].h//2 + p[3] < 0 or p[1].center[1] + p[1].h//2 + p[3] > height:
            p[3] = - p[3]
        p[1] = p[1].move([p[2],p[3]])
        screen.blit(p[0],p[1])
    if time.clock() - start_time < 5:
        screen.blit(ren, textrect)
    screen.blit(succulus, succulusrect)
    
    if len(profs) == 0: #display endgame text
        font = pygame.font.Font(None, 150)
        text = 'Restart? (y/n)'
        size = font.size(text)
        endgame = font.render(text, 0, color)
        endgamerect = endgame.get_rect()
        screen.blit(endgame, endgamerect)
    pygame.display.flip() 