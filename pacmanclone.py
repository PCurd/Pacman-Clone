import pygame, sys
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
HALF_WINWIDTH = int(WINDOWWIDTH / 2)
HALF_WINHEIGHT = int(WINDOWHEIGHT / 2)
PACMANSIZE = 31
MOVERATE = 1
BGCOLOUR = pygame.color.Color(0,0,0,0)
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'
gameOverMode = False

DEBUG = 0

def setup():
    global PACMAN_IMG, PACMAN_RECT
    PACMAN_IMG = pygame.image.load('images\sprites\pacman_various_sheet.png')
    PACMAN_RECT = pygame.Rect(398,7,PACMANSIZE,PACMANSIZE)


def main():
    global FPSCLOCK, DISPLAYSURF, pacmanObj
    pygame.init()
    setup()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Hello World!')

    pacmanObj = {'surface': PACMAN_IMG,
                  'facing': RIGHT,
                  'x': HALF_WINWIDTH,
                  'y': HALF_WINHEIGHT,
                 'size': PACMANSIZE}

    
    while True: # main game loop
     RunGame()

def RunGame():
    DoEvents()
    DISPLAYSURF.fill(BGCOLOUR)


    pacmanObj['rect'] = pygame.Rect( (pacmanObj['x'],
                                               pacmanObj['y'],
                                               pacmanObj['size'],
                                               pacmanObj['size']) )
      
    DISPLAYSURF.blit(pacmanObj['surface'], pacmanObj['rect'], PACMAN_RECT)
    if DEBUG == 1:
     print pacmanObj['rect']


    if not gameOverMode:
      #Move Pacman
         for case in switch(pacmanObj['facing']):
             if case(UP):
                pacmanObj['y'] -= MOVERATE
                break
             if case(DOWN):
                pacmanObj['y'] += MOVERATE
                break
             if case(LEFT):
                pacmanObj['x'] -= MOVERATE
                break
             if case(RIGHT):
                pacmanObj['x'] += MOVERATE
                break
             if case(): # default, could also just omit condition or 'if True'
                break

    pygame.display.update()
    FPSCLOCK.tick(FPS)

def DoEvents():
    for event in pygame.event.get():
      if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
       pygame.quit()
       sys.exit()
      elif event.type == KEYDOWN:
                if event.key == K_UP:
                    pacmanObj['facing'] = UP
                if event.key == K_DOWN:
                    pacmanObj['facing'] = DOWN
                if event.key == K_LEFT:
                    pacmanObj['facing'] = LEFT
                if event.key == K_RIGHT:
                    pacmanObj['facing'] = RIGHT


# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

        
if __name__ == '__main__':
    main()




