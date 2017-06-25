import random, time, pygame, sys 
from pygame.locals import *
import Shapes
from Shapes import *
from variables import *



def selectrandomblock():
	n=random.randint(1,30)
	shape=random.choice(list(Shapes.shapes.keys()))
	while(shape=='Sp'):
		shape=random.choice(list(Shapes.shapes.keys()))
		if(n%4==0 or n%7==0 or n%11==0):
			break
	return shape

def terminate():
	pygame.quit()
	sys.exit()

def checkforquit():
	for event in pygame.event.get(QUIT):
		terminate()
	for event in pygame.event.get(KEYUP):
		if event.key == K_ESCAPE:
			terminate()
		pygame.event.post(event)


def checkforkeypress():
	checkforquit()
	for event in pygame.event.get([KEYDOWN,KEYUP]):
		if event.type == KEYDOWN :
			continue
		return event.key
	return None