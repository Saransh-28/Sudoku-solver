import curses
from curses import wrapper
from curses.textpad import rectangle
import time

start_corr_x = 15
start_corr_y = 3

grid = [[0 for i in range(9)] for j in range(9)]

def input_grid(stdscr):
    global grid
    for i in range(9):
        for j in range(9):
            grid[i][j] = '@'
            
            print_grid(stdscr , grid , 0)
            stdscr.addstr(0,0,'Press the number on position of "@"')
            stdscr.addstr(1,0,'**Enter q to quit row , x to quit filling**')
            val = stdscr.getkey()
            if val == 'q' or val == 'x':
                grid[i][j] = 0
                break
            elif val == '':
                val = 0
            grid[i][j] = val
        if val == 'x':
            break

def possible(row,col,num):
    global grid

    for i in range(9):
        if grid[row][i] == num:
            return False

    for i in range(9):
        if grid[i][col] == num:
            return False

    x = (row//3)*3
    y = (col//3)*3
    for i in range(3):
        for j in range(3):
            if grid[x+i][y+j] == num:
                return False
    return True

def solve(stdscr):
    global grid
    global inigird
    for row in range(9):
        for col in range(9):

            if grid[row][col] == 0:
                for num in range(1,10):
                    if possible(row,col,num):
                        grid[row][col] = num
                        print_grid(stdscr , grid , 1)
                        time.sleep(0.01)
                        solve(stdscr)
                        grid[row][col] = 0
                return
    stdscr.clear()
    stdscr.addstr(1,start_corr_x,'------THE SOLUTION OF PUZZLE------')
    print_grid(stdscr , grid , 0)
    stdscr.refresh()
    stdscr.getch()

def print_grid(stdscr ,grid, color):

    curses.init_pair(1,curses.COLOR_GREEN , curses.COLOR_BLACK)
    green_black = curses.color_pair(1)
    curses.init_pair(2,curses.COLOR_RED , curses.COLOR_BLACK)
    red_black = curses.color_pair(2)
    curses.init_pair(3,curses.COLOR_WHITE , curses.COLOR_BLACK)
    white_black = curses.color_pair(3)   

    if color == 1:
        color = green_black
    elif color == 0:
        color = white_black

    stdscr.addstr(start_corr_y + 2,start_corr_x + 4,f'| {grid[0][0]} {grid[0][1]} {grid[0][2]} | {grid[0][3]} {grid[0][4]} {grid[0][5]} | {grid[0][6]} {grid[0][7]} {grid[0][8]} |',color)
    stdscr.addstr(start_corr_y + 3,start_corr_x + 4,f'| {grid[1][0]} {grid[1][1]} {grid[1][2]} | {grid[1][3]} {grid[1][4]} {grid[1][5]} | {grid[1][6]} {grid[1][7]} {grid[1][8]} |',color)
    stdscr.addstr(start_corr_y + 4,start_corr_x + 4,f'| {grid[2][0]} {grid[2][1]} {grid[2][2]} | {grid[2][3]} {grid[2][4]} {grid[2][5]} | {grid[2][6]} {grid[2][7]} {grid[2][8]} |',color)

    stdscr.addstr(start_corr_y + 6,start_corr_x + 4,f'| {grid[3][0]} {grid[3][1]} {grid[3][2]} | {grid[3][3]} {grid[3][4]} {grid[3][5]} | {grid[3][6]} {grid[3][7]} {grid[3][8]} |',color)
    stdscr.addstr(start_corr_y + 7,start_corr_x + 4,f'| {grid[4][0]} {grid[4][1]} {grid[4][2]} | {grid[4][3]} {grid[4][4]} {grid[4][5]} | {grid[4][6]} {grid[4][7]} {grid[4][8]} |',color)
    stdscr.addstr(start_corr_y + 8,start_corr_x + 4,f'| {grid[5][0]} {grid[5][1]} {grid[5][2]} | {grid[5][3]} {grid[5][4]} {grid[5][5]} | {grid[5][6]} {grid[5][7]} {grid[5][8]} |',color)

    stdscr.addstr(start_corr_y + 10,start_corr_x + 4,f'| {grid[6][0]} {grid[6][1]} {grid[6][2]} | {grid[6][3]} {grid[6][4]} {grid[6][5]} | {grid[6][6]} {grid[6][7]} {grid[6][8]} |', color)
    stdscr.addstr(start_corr_y + 11,start_corr_x + 4,f'| {grid[7][0]} {grid[7][1]} {grid[7][2]} | {grid[7][3]} {grid[7][4]} {grid[7][5]} | {grid[7][6]} {grid[7][7]} {grid[7][8]} |', color)
    stdscr.addstr(start_corr_y + 12,start_corr_x + 4,f'| {grid[8][0]} {grid[8][1]} {grid[8][2]} | {grid[8][3]} {grid[8][4]} {grid[8][5]} | {grid[8][6]} {grid[8][7]} {grid[8][8]} |', color)
    
    stdscr.attron(red_black)
    rectangle(stdscr , start_corr_y + 1, start_corr_x + 4, start_corr_y + 13,start_corr_x + 28 )

    rectangle(stdscr , start_corr_y + 1, start_corr_x + 4, start_corr_y + 5,start_corr_x + 12 )
    rectangle(stdscr , start_corr_y + 1, start_corr_x + 20, start_corr_y + 5,start_corr_x + 28 )

    rectangle(stdscr , start_corr_y + 5, start_corr_x + 12, start_corr_y + 9,start_corr_x + 20 )

    rectangle(stdscr , start_corr_y + 9, start_corr_x + 4, start_corr_y + 13,start_corr_x + 12 )
    rectangle(stdscr , start_corr_y + 9, start_corr_x + 20, start_corr_y + 13,start_corr_x + 28 )
    stdscr.attroff(red_black)
    stdscr.refresh()

def main(stdscr):
    global grid
    input_grid(stdscr)
    solve(stdscr)

wrapper(main)
