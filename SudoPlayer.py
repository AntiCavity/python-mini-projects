
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

def possible(grid, row, column, number):
    #check the row to see if the number shows up again
    for i in range(0,9):
        if grid[row][i] == number:
            return False
    
    #check the column to see if the number shows up again

    for i in range(0,9):
        if grid[i][column] == number:
            return False

    #check each square to see if the number shows up in the square

    xSection = (row // 3) * 3
    ySection = (column // 3) * 3

    for i in range(0,3):
        for j in range(0,3):
            if grid[i + xSection][j + ySection] == number:
                return False
    
    return True


def solve(grid):
    currentEmpty = find_empty(grid)
    if currentEmpty:
        row, column = currentEmpty
    else:
        return True
    for n in range(1,10):
        if possible(grid, row, column, n):
            grid[row][column] = n
            if solve(grid):
                printGrid(grid)
                print('\n')
                #exit()
            grid[row][column] = 0
    return False

def find_empty(grid):
     for row in range(0,9):
            for column in range(0,9):
                if grid[row][column] == 0:
                    return(row, column)
     return None

def printGrid(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(grid[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(grid[i][j], end="\n")
            else:
                print(str(grid[i][j]) + " ", end="")
    return

solve(grid)              





