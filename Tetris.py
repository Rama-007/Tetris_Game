# pylint: disable=W0511, C0321
from RunGame import *
def main():
	global fpsclock, displaysurf, basicfont, bigfont
	pygame.init()
	displaysurf = pygame.display.set_mode((windowwidth, windowheight))
	fpsclock = pygame.time.Clock()	
	bigfont = pygame.font.Font('bold.ttf', 54)
	basicfont = pygame.font.Font('bold.ttf', 22)
	showtextscreen('Tetris')
	while True:
		rungame()
		showtextscreen('Game Over')

if __name__ == '__main__':
	main()