# Game of Life

# inspired by YouTube video from Steve's Coding Lab

import pygame, sys, time, copy

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

def clear_grid():
    for x in range(TOTAL_ROWS_COLS):
        for y in range(TOTAL_ROWS_COLS):
            grid_state[x][y] = DEAD
    new_state = copy.deepcopy(grid_state)

def glider_down_left(x, y):
    grid_state[x][y] = ALIVE
    grid_state[x + 1][y] = ALIVE
    grid_state[x + 1][y + 1] = ALIVE
    grid_state[x + 2][y + 1] = ALIVE
    grid_state[x][y + 2] = ALIVE

def glider_up_right(x, y):
    grid_state[x][y] = ALIVE
    grid_state[x - 1][y] = ALIVE
    grid_state[x - 1][y - 1] = ALIVE
    grid_state[x - 2][y - 1] = ALIVE
    grid_state[x][y - 2] = ALIVE

if (__name__ == "__main__"):

    grid_state = [[DEAD for _ in range(TOTAL_ROWS_COLS)]
                  for _ in range(TOTAL_ROWS_COLS)]
    new_state = copy.deepcopy(grid_state)
    
    pygame.init()
    screen = pygame.display.set_mode((SC_WIDTH_HEIGHT, SC_WIDTH_HEIGHT))

    button = False
    run = False
    stop = False
    running = False
    sleep_time = 0.25
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    run = True
                elif event.key == pygame.K_s:
                    stop = True
                elif event.key == pygame.K_i:
                    sleep_time = sleep_time / 2.0
                elif event.key == pygame.K_d:
                    sleep_time = sleep_time * 2.0
                elif event.key == pygame.K_g:
                    glider_up_right(70,12)
                elif event.key == pygame.K_h:
                    glider_down_left(8,70)
                elif event.key == pygame.K_c:
                    for x in range(TOTAL_ROWS_COLS):
                        for y in range(TOTAL_ROWS_COLS):
                            grid_state[x][y] = DEAD
                        new_state = copy.deepcopy(grid_state)
                elif event.key ==pygame.K_q:
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
                #else:
                #    grid_state[row][col] = DEAD


        screen.fill(COLOUR_BG)
        draw_grid()

        # Game of Life Logic
        if run:
            running = True
            run = False
        elif stop:
            running = False
            stop = False
        
        if running:
            for x in range(TOTAL_ROWS_COLS):
                for y in range(TOTAL_ROWS_COLS):
                    # Count neighbours
                    neighbours = 0
                    # Left
                    if x > 0:
                        if grid_state[x - 1][y] == ALIVE:
                            neighbours = neighbours + 1
                    # Right
                    if x < (TOTAL_ROWS_COLS - 1):
                        if grid_state[x + 1][y] == ALIVE:
                            neighbours = neighbours + 1
                    # Above
                    if y < (TOTAL_ROWS_COLS - 1):
                        if grid_state[x][y + 1] == ALIVE:
                            neighbours = neighbours + 1
                    # Below
                    if y > 0:
                        if grid_state[x][y - 1] == ALIVE:
                            neighbours = neighbours + 1
                    # Down and left
                    if (x > 1) and (y > 0):
                        if grid_state[x - 1][y - 1] == ALIVE:
                            neighbours = neighbours + 1
                    # Up and left
                    if (x > 1) and (y < (TOTAL_ROWS_COLS - 1)):
                        if grid_state[x - 1][y + 1] == ALIVE:
                            neighbours = neighbours + 1
                    # Up and right
                    if (x < (TOTAL_ROWS_COLS - 1)) and (y < (TOTAL_ROWS_COLS - 1)):
                        if grid_state[x + 1][y + 1] == ALIVE:
                            neighbours = neighbours + 1
                    # Down and right
                    if (x < (TOTAL_ROWS_COLS - 1)) and (y > 0):
                        if grid_state[x + 1][y - 1] == ALIVE:
                            neighbours = neighbours + 1

                    # Live / Die / Born Logic
                    if grid_state[x][y] == ALIVE:
                        if neighbours < 2:
                            new_state[x][y] = DEAD
                        elif ((neighbours == 2) or (neighbours == 3)):
                            new_state[x][y] = ALIVE
                        elif neighbours > 3:
                            new_state[x][y] = DEAD
                        else:
                            new_state[x][y] = DEAD
                    elif grid_state[x][y] == DEAD:
                        if neighbours == 3:
                            new_state[x][y] = ALIVE
                    else:
                        new_state[x][y] = DEAD

            grid_state = copy.deepcopy(new_state)

        
        display_cells(grid_state)
            
        pygame.display.update()

        if running:
            time.sleep(sleep_time)

