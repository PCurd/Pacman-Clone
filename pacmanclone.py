import pygame, sys
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels

def setup():
    global PACMAN_IMG, PACMAN_RECT
    PACMAN_IMG = pygame.image.load('images\sprites\pacman_various_sheet.png')
    PACMAN_RECT = pygame.Rect(398,7,29,31)


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    setup()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Hello World!')
    while True: # main game loop
     for event in pygame.event.get():
      if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
       pygame.quit()
       sys.exit()
     DISPLAYSURF.blit(PACMAN_IMG, (10,100,0,0), PACMAN_RECT)
     pygame.display.update()
     FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
