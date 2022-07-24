import numpy as np

grid = [[0 for i in range(9)] for j in range(9)]
# print(np.matrix(grid))
def print_grid(row , col):
    global grid
    grid[row][col] = 'x'
    print(np.matrix(grid))

def input_grid():
    global grid
    for i in range(9):
        for j in range(9):
            
            print_grid(i , j)
            val = input('Enter the number on position of x (q to quit row , x to quit filling)- ')
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

def solve():
    global grid

    for row in range(9):
        for col in range(9):

            if grid[row][col] == 0:
                for num in range(1,10):
                    if possible(row,col,num):
                        grid[row][col] = num
                        solve()
                        grid[row][col] = 0
                return
    print(np.matrix(grid))
    x = input('Do you want more possible solution ?')

input_grid()
print('SOLUTION -----')
solve()
print('No more solution available')