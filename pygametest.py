#!/usr/bin/python

import pygame
from pygame.locals import *

def main():
	# Initialise screen
	pygame.init()
	screen = pygame.display.set_mode((700, 500))
	pygame.display.set_caption('Basic Pygame program')

	# Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((250, 250, 250))

	# Display some text
	font = pygame.font.Font(None, 36)
	text = font.render("Hello There", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)

	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()

	# draw rectangle to screen

	# rectangle = pygame.draw.rect(background, (60,60,100), (0,0,50,50), 5)
	background.fill((60,60,100), rectangle)
	print(rectangle.top, rectangle.left, rectangle.bottom, rectangle.right)
	print(rectangle.size)
	print(rectangle.center)
	rectangle.center = (50,50)
	
	# background.scroll(200,300)
	# rectangle.move(200,300)
	# rectangle = pygame.draw.rect(background, (60,60,100), (50,50,50,50),5)

	# # load images, make sprites
	# img = pygame.image.load('fire_sprite.png')
	# pygame.Player.images = [img, pygame.transform.flip(img, 1, 0)]
	# all = pygame.sprite.RenderUpdates()
	# Player.containers = all
	# player = Player()


	# Event loop
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return

		screen.blit(background, (0, 0))
		pygame.display.flip()

		# rectangle = pygame.draw.rect(background, (60,60,100), (0,0,50,50), 5)
		# background.fill((60,60,100), rectangle)
		# background.scroll(200,300)
		# rectangle.move(200,300)

def move(rectangle, position):
	pass


if __name__ == '__main__': main()