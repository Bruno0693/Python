from math import *
import numpy as np 
import pygame, sys
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW =(255,255,0)


L = np.linspace(0, 2*pi, 100)
X = np.cos(L)
Y = np.sin(L)
c = 0


pygame.init()

FPS = 20
fpsClock = pygame.time.Clock()


surface = pygame.display.set_mode((600,600))
pygame.display.set_caption("Cercle")

while True:
	surface.fill(BLACK)
	x = 300 + 100*X[c]
	y = 300 - 100*Y[c]
	pygame.draw.circle(surface, WHITE, (300,300), 2, 0)
	pygame.draw.circle(surface, YELLOW, (int(x),int(y)),3, 0)
	pygame.draw.line(surface, YELLOW, (300, 300), (x,y), 1)

	
	c += 1
	if c == len(X) - 1:
		c=0
		
	for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

	pygame.display.flip()
	fpsClock.tick(FPS)
