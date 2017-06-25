import random, time, pygame, sys 
from pygame.locals import *
import Shapes
from Shapes import *
from variables import *
from bords import *

class Block(object):
	__movement=1

	def __init__(self):
		pass

	def rotate(self,board,fallingpiece):
		temp=Board()
		fallingpiece['rotation']=(fallingpiece['rotation']+1)%len(Shapes.shapes[fallingpiece['shape']])
		if not temp.checkpiecepos(board,fallingpiece):
			fallingpiece['rotation']=(fallingpiece['rotation']-1)%len(Shapes.shapes[fallingpiece['shape']])
		return fallingpiece['rotation']

	def moveleft(self,fallingpiece):
		fallingpiece['x']-=self.__movement
		return fallingpiece['x'],False,True


	def moveright(self,fallingpiece):
		fallingpiece['x']+=self.__movement
		return fallingpiece['x'],True,False

	def draw(self,board,fallingpiece):
		temp=Board()
		for i in range(1,boardheight):
			if not temp.checkpiecepos(board,fallingpiece,adjy=i):
				break;

		fallingpiece['y']+=i-1
		return fallingpiece['y'],False,False,False

	def randomblock(self):
		pass

class S(Block):
	def __init__(self):
		pass
		
	def randomblock(self):
		Sblock = [['#####',
                 	'##X##',
                 	'##XX#',
                 	'###X#',
                 	'#####'],
                 	['#####',
                 	'#####',
                 	'##XX#',
                 	'#XX##',
                 	'#####']]

    		return Sblock

class Z(Block):
	def __init__(self):
		pass
		

	def randomblock(self):
		Zblock = [['#####',
                 '##X##',
                 '#XX##',
                 '#X###',
                 '#####'],
                 ['#####',
                 '#####',
                 '#XX##',
                 '##XX#',
                 '#####']]
      		return Zblock


class I(Block):
	def __init__(self):
		pass
	def randomblock(self):	
		Iblock=[['#####',
                 '#####',
                 'XXXX#',
                 '#####',
                 '#####'],
                 ['##X##',
                 '##X##',
                 '##X##',
                 '##X##',
                 '#####']]
        
    		return Iblock

class O(Block):
	def __init__(self):
		pass
	def randomblock(self):
		Oblock=[['#####',
                 '#####',
                 '#XX##',
                 '#XX##',
                 '#####']]
        
    		return Oblock             

class J(Block):
	def __init__(self):
		pass
	def randomblock(self):
		Jblock=[['#####',
                 '##XX#',
                 '##X##',
                 '##X##',
                 '#####'],
                 ['#####',
                 '#####',
                 '#XXX#',
                 '###X#',
                 '#####'],
                 ['#####',
                 '##X##',
                 '##X##',
                 '#XX##',
                 '#####'],
                 ['#####',
                 '#X###',
                 '#XXX#',
                 '#####',
                 '#####']]

    		return Jblock             


class L(Block):
	def __init__(self):
		pass
	def randomblock(self):
		Lblock=[['#####',
                 '#####',
                 '#XXX#',
                 '#X###',
                 '#####'],
                 ['#####',
                 '#XX##',
                 '##X##',
                 '##X##',
                 '#####'],
				 ['#####',
                 '###X#',
                 '#XXX#',
                 '#####',
                 '#####'],
                 ['#####',
                 '##X##',
                 '##X##',
                 '##XX#',
                 '#####']]

 		return Lblock

class T(Block):
	def __init__(self):
		pass
	def randomblock(self):
		Tblock=[['#####',
                 '#####',
                 '#XXX#',
                 '##X##',
                 '#####'],
                 ['#####',
                 '##X##',
                 '#XX##',
                 '##X##',
                 '#####'],
				 ['#####',
                 '##X##',
                 '#XXX#',
                 '#####',
                 '#####'],
                 ['#####',
                 '##X##',
                 '##XX#',
                 '##X##',
                 '#####']]
       		return Tblock 
class Sp(Block):
	def __init__(self):
		pass
	def randomblock(self):
		Spblock=[['#####',
                 '#####',
                 '##X##',
                 '#####',
                 '#####']]
        	return Spblock