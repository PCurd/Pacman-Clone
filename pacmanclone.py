import pygame, sys
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels

def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Hello World!')
    while True: # main game loop
     for event in pygame.event.get():
      if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
       pygame.quit()
       sys.exit()
     pygame.display.update()
     FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
