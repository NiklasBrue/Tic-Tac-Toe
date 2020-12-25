import pygame, sys

'''
- pygame coordinates go from left to right and from top to bottom
- pygame always has to be initialised
'''





#constants
_WIDTH = 600
_HEIGHT = 600
_WHITE = (255, 255, 255)
_BLACK = (0, 0, 0)


#build screen with width and height
screen = pygame.display.set_mode((_WIDTH, _HEIGHT))
#add title
pygame.display.set_caption('Tic Tac Toe')
screen.fill(_WHITE)
#add lines
def draw_lines():
    pygame.draw.line(screen, _BLACK, (0, 200), (600, 200), 10)
    pygame.draw.line(screen, _BLACK, (0, 400), (600, 400), 10)
    pygame.draw.line(screen, _BLACK, (200, 0), (200, 600), 10)
    pygame.draw.line(screen, _BLACK, (400, 0), (400, 600), 10)

draw_lines()