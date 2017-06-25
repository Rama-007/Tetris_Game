import random, time, pygame, sys 
from pygame.locals import *
import Shapes
from Shapes import *
from variables import *

from Blck import *

class Board(object):
	def __init__(self):
		pass


	def checkpiecepos(self,board,piece,adjx=0,adjy=0):
		for x in range(templatewidth):
			for y in range(templateheight):
				#isaboveboard=y+piece['y']+adjy < 0
				rangex=x+piece['x']+adjx
				rangey=y+piece['y']+adjy
				if (rangey<0) or Shapes.shapes[piece['shape']][piece['rotation']][y][x] == blank:
					continue
				if not (rangex>=0 and rangex<boardwidth and rangey<boardheight):
					return False
				if board[rangex][rangey] != blank:
					return False
		return True

	def fillpiecepos(self,board,piece):
		for x in range(templatewidth):
			for y in range(templateheight):
				if Shapes.shapes[piece['shape']][piece['rotation']][y][x] != blank:
					board[x + piece['x']][ y + piece['y']] = 'X'

		return board