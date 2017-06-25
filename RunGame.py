import random, time, pygame, sys 
from pygame.locals import *
import Shapes
from Shapes import *
from variables import *

from bords import *

from functions import *

from drawing import *

from Blck import *

from numbers import *

boardwidth = 30
boardheight = 32




		
class gameplay(Board,Block):
	__maxadd=10
	__leveldiv=500
	__falltime=0.25
	__leveltimedec=0.05
	def __init__(self):
		pass
	def getblankboard(self):
		board=[]
		for i in range(boardwidth):
			board.append([blank] * boardheight)
		return board


	def drawboard(self,board):
		pygame.draw.rect(displaysurf,bordercolor,(xmargin-6,topmargin-10,(boardwidth*boxsize)+8,(boardheight*boxsize)+8),5)	
		for x in range(boardwidth):
			for y in range(boardheight):
				if board[x][y]=='X':
					px=(xmargin+(x*boxsize))
					py=(topmargin+(y*boxsize))
					keysurf,keyrect=maketextobjs("X",basicfont,textcolor)
					keyrect.center=int(px+1/2),int(py+1/2)
					displaysurf.blit(keysurf,keyrect)

	
	def checkrowfull(self,board,y):
		for x in range(boardwidth):
			if board[x][y] == blank:
				return False
		return True

	def checkrowempty(self,board,y):
		for x in range(boardwidth):
			if board[x][y] != blank:
				return False
		return True	

	def calculatelevel(self,score):
		level=int(score/self.__leveldiv)+1
		fallfreq=self.__falltime - (level*self.__leveltimedec)
		if(fallfreq<=0):
			fallfreq=fallfreq + (level*self.__leveltimedec)
		return level,fallfreq

	def updatescore(self,score):
		return score+self.__maxadd


	def removecompletelines(self,board):
		y = boardheight - 1
		numlinesremoved=0
		while y >= 0:
			if self.checkrowfull(board,y):
				pygame.mixer.music.load('rowfull.wav')
				pygame.mixer.music.play(0, 0.0)
				for downy in range(y,0,-1):
					for x in range(boardwidth):
						board[x][downy]=board[x][downy-1]
						downy-=1
			 	for x in range(boardwidth):
			 		board[x][0]=blank
			 	numlinesremoved+=1
			else:
			 	y-=1
		return numlinesremoved*100


	def specialmove(self,board,x):
		pygame.mixer.music.load('special.wav')
		pygame.mixer.music.play(0, 0.0)
		y=boardheight - 1
		n=random.randint(0,1)
		while y>=0:
			x=0
			while(x<boardwidth):
					board[x][y]=blank
					x=x+1
			y-=1


	def selectpiece(self):
		shape=selectrandomblock()
		newpiece={'shape':shape,
			'rotation':random.randint(0,len(Shapes.shapes[shape])-1),
			'x':int(boardwidth/2)-int(templatewidth/2),
			'y': -3}
		return newpiece


def rungame():
	a=gameplay()
	board = a.getblankboard()
	fallingpiece=a.selectpiece()
	nextpeice=a.selectpiece()
	lastfalltime = time.time()
	score=0
	level,fallfreq=a.calculatelevel(score)
	

	while True:
		if fallingpiece == None:
			fallingpiece=nextpeice
			nextpeice=a.selectpiece()
			lastfalltime=time.time()

			if not a.checkpiecepos(board,fallingpiece):
				return

		checkforquit()

		for event in pygame.event.get():
			if event.type == KEYUP:
				if (event.key == K_a):
					movingleft=False
				elif (event.key == K_d):
					movingright=False

				elif (event.key==K_z):
					displaysurf.fill(bg)
					showtextscreen('Game Paused')

			elif event.type == KEYDOWN:
				if(event.key == K_s):
					fallingpiece['rotation']=a.rotate(board,fallingpiece)
				elif(event.key == K_a) and a.checkpiecepos(board,fallingpiece,adjx=-1):
					fallingpiece['x'],movingright,movingleft=a.moveleft(fallingpiece)
					
				elif(event.key == K_d) and a.checkpiecepos(board,fallingpiece,adjx=1):
					fallingpiece['x'],movingright,movingleft=a.moveright(fallingpiece)

				elif(event.key == K_SPACE):
					fallingpiece['y'],movingright,movingleft,movingdown=a.draw(board,fallingpiece)


		if time.time() - lastfalltime > fallfreq:
			if not a.checkpiecepos(board,fallingpiece,adjy=1):
				board = a.fillpiecepos(board,fallingpiece)
				score=a.updatescore(score)

				if(fallingpiece['shape']=='Sp'):
					score+=50
					a.specialmove(board,fallingpiece['x'])
				score+=a.removecompletelines(board)
				level,fallfreq = a.calculatelevel(score)
				fallingpiece=None

			else:
				fallingpiece['y']+=1
				lastfalltime=time.time()

		displaysurf.fill(bg)
		drawstatus(score,level)
		drawnextpiece(nextpeice,board)
		a.drawboard(board)
		if fallingpiece!=None:
			drawpiece(board,fallingpiece)
		pygame.display.update()
		fpsclock.tick(25)
