import pygame, sys
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels
HALF_WINWIDTH = int(WINDOWWIDTH / 2)
HALF_WINHEIGHT = int(WINDOWHEIGHT / 2)
PACMANSIZE = 16
MOVERATE = 1
BGCOLOUR = pygame.color.Color(0,0,0,0)
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'
gameOverMode = False

DEBUG = 0

def setup():
    global TICK
    TICK=0



def main():
    global FPSCLOCK, DISPLAYSURF, pacmanObj
    pygame.init()
    setup()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Pacman Clone!')

    pacmanObj = Pacman()

    
    while True: # main game loop
     RunGame()

def RunGame():
    DoEvents()

    if not gameOverMode:
        DoMoves()
        Animate()
        
    Draw()
    

def DoMoves():
#Move Pacman
     for case in switch(pacmanObj.facing):
         if case(UP):
            pacmanObj.y -= MOVERATE
            break
         if case(DOWN):
            pacmanObj.y += MOVERATE
            break
         if case(LEFT):
            pacmanObj.x -= MOVERATE
            break
         if case(RIGHT):
            pacmanObj.x += MOVERATE
            break
         if case(): # default, could also just omit condition or 'if True'
            break

def Animate():
    global TICK
    TICK +=1
    if TICK ==5:
        TICK=0
        pacmanObj.animation = (0 if pacmanObj.animation == 1 else 1)
            
def DoEvents():
    for event in pygame.event.get():
      if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
       pygame.quit()
       sys.exit()
      elif event.type == KEYDOWN:
                if event.key == K_UP and pacmanObj.facing in (LEFT, RIGHT):
                    pacmanObj.facing = UP
                if event.key == K_DOWN and pacmanObj.facing in (LEFT, RIGHT):
                    pacmanObj.facing = DOWN
                if event.key == K_LEFT and pacmanObj.facing in (UP, DOWN):
                    pacmanObj.facing = LEFT
                if event.key == K_RIGHT and pacmanObj.facing in (UP, DOWN):
                    pacmanObj.facing = RIGHT


def Draw():
    pacmanObj.rect = pygame.Rect( (pacmanObj.x,
                                               pacmanObj.y,
                                               pacmanObj.size,
                                               pacmanObj.size) )
    if DEBUG == 1:
     print pacmanObj.surface

    DISPLAYSURF.fill(BGCOLOUR)
    DISPLAYSURF.blit(pacmanObj.surface, pacmanObj.rect, pacmanObj.FacingRect())
    pygame.display.update()
    FPSCLOCK.tick(FPS)




class Animated(object):
    surface = None
    def FacingRect(self):
        for case in switch(self.facing):
            if case(UP):
                return self.RECT_UP[self.animation]
            if case(DOWN):
                return self.RECT_DOWN[self.animation]
            if case(LEFT):
                return self.RECT_LEFT[self.animation]
            if case(RIGHT):
                return self.RECT_RIGHT[self.animation]
    def SetSurface(self, path):
        self.surface= pygame.image.load(path)

    facing = RIGHT

class Pacman(Animated):
    def __init__(self):
        self.SetSurface('images\sprites\pacman_various_sheet.png')
    RECT_RIGHT = [pygame.Rect(120,0,PACMANSIZE,PACMANSIZE), pygame.Rect(120,30,PACMANSIZE,PACMANSIZE)]
    RECT_LEFT = [pygame.Rect(60,0,PACMANSIZE,PACMANSIZE), pygame.Rect(60,30,PACMANSIZE,PACMANSIZE)]
    RECT_UP = [pygame.Rect(30,0,PACMANSIZE,PACMANSIZE), pygame.Rect(30,30,PACMANSIZE,PACMANSIZE)]
    RECT_DOWN = [pygame.Rect(90,0,PACMANSIZE,PACMANSIZE), pygame.Rect(90,30,PACMANSIZE,PACMANSIZE)]
    x= HALF_WINWIDTH
    y = HALF_WINHEIGHT
    size = PACMANSIZE
    animation = 0
    
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




