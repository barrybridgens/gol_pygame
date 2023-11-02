# Game of Life

# inspired by YouTube video from Steve's Coding Lab

import pygame,sys

from gol_util import *

def draw_grid():
    for row in range(TOTAL_ROWS_COLS):
        for col in range(TOTAL_ROWS_COLS):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, COLOUR_GRID, rect, 1)

def display_cells(cells):
    for x in range(TOTAL_ROWS_COLS):
        for y in range(TOTAL_ROWS_COLS):
            if cells[x][y] == ALIVE:
                rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, COLOUR_ALIVE, rect, 0)    

if (__name__ == "__main__"):

    grid_state = [[DEAD for _ in range(TOTAL_ROWS_COLS)]
                  for _ in range(TOTAL_ROWS_COLS)]
    
    pygame.init()
    screen = pygame.display.set_mode((SC_WIDTH_HEIGHT, SC_WIDTH_HEIGHT))

    button = False;
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button = True;
            elif event.type == pygame.MOUSEBUTTONUP:
                button = False
            elif (event.type == pygame.MOUSEMOTION) and button:
                pos = pygame.mouse.get_pos()
                col = pos[0] // CELL_SIZE
                row = pos[1] // CELL_SIZE

                if grid_state[row][col] == DEAD:
                    grid_state[row][col] = ALIVE
                else:
                    grid_state[row][col] = DEAD

                
            

        screen.fill(COLOUR_BG)
        draw_grid()
        
        display_cells(grid_state)
            
        pygame.display.update()

