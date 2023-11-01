# Game of Life

import pygame,sys

from gol_util import *

pygame.init()
screen = pygame.display.set_mode((SC_WIDTH_HEIGHT, SC_WIDTH_HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(COLOUR_BG)



    pygame.display.update()

