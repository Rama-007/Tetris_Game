import random, time, pygame, sys 
from pygame.locals import *
import Shapes
from Shapes import *
from variables import *
from functions import *
from Blck import *

pygame.init()
fpsclock=pygame.time.Clock()
displaysurf=pygame.display.set_mode((windowwidth,windowheight))
basicfont=pygame.font.Font('bold.ttf' ,20)
bigfont=pygame.font.Font('bold.ttf', 50)


def drawstatus(score,level):
		scoresurf=basicfont.render('Level: %s'%level,True,textcolor)
		scorerect=scoresurf.get_rect()
		scorerect.topleft=(windowwidth-250,49)
		displaysurf.blit(scoresurf,scorerect)

		scoresurf=basicfont.render('Score: %s'%score,True,textcolor)
		scorerect=scoresurf.get_rect()
		scorerect.topleft=(windowwidth-250,21)
		displaysurf.blit(scoresurf,scorerect)


def drawnextpiece(nextpeice,board):
	nextsurf=basicfont.render('Next:',True,textcolor)
	nextrect=nextsurf.get_rect()
	nextrect.topleft=(windowwidth-250,80)
	displaysurf.blit(nextsurf,nextrect)
	drawpiece(board,nextpeice,px=windowwidth-220,py=200)

def drawpiece(board,piece,px=None,py=None):
	drawshape=shapes[piece['shape']][piece['rotation']]
	if px==None and py==None:
		px=(xmargin+(piece['x']*boxsize))
		py=(topmargin+((piece['y'])*boxsize))
	if piece['shape']=='Sp':
		for x in range(templatewidth):
			for y in range(templateheight):
				if drawshape[y][x]!=blank:
					keysurf,keyrect=maketextobjs("SP",basicfont,specialcolor)
					keyrect.center=int((px+x*boxsize)),int((py+y*boxsize))
					displaysurf.blit(keysurf,keyrect)
	else:
		for x in range(templatewidth):
			for y in range(templateheight):
				if drawshape[y][x]!=blank:
					keysurf,keyrect=maketextobjs("X",basicfont,specialcolor)
					keyrect.center=int((px+x*boxsize)),int((py+y*boxsize))
					displaysurf.blit(keysurf,keyrect)


def maketextobjs(text,font,color):
    surf = font.render(text,True,color)
    return surf,surf.get_rect()




def showtextscreen(text):
	titlesurf,titlerect=maketextobjs(text,bigfont,textcolor)
	titlerect.center=(int(windowwidth/2),int(windowheight/2))
	displaysurf.blit(titlesurf,titlerect)
	keysurf,keyrect=maketextobjs("Press a key to play : Lets Have Some fun!!",basicfont,playcolor)
	keyrect.center=(int(windowwidth/2),int(windowheight/2)+108)
	displaysurf.blit(keysurf,keyrect)
	while checkforkeypress() == None:
		pygame.display.update()
		fpsclock.tick()
