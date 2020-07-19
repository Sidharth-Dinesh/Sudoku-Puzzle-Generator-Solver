'''
SUDOKU SOLVER:
    Using recursion and backtracking. 
    Algorithm - 
    0. Define a solving function.
    1. Search for the first empty slot(0). 
    2. Attempt to fill the empty slot with a number from 1-9.
    3. If the number is already in the row/col/box, change it.
    4. Call the function again. Proceed until sudoku is solved.
    
'''



import random
import time

# bit of tester code, left here for legacy

#grid = [[0,0,6,1,0,2,5,0,0,],
#        [0,3,9,0,0,0,1,4,0,],
#        [0,0,0,0,4,0,0,0,0,],
#        [9,0,2,0,3,0,4,0,1,],
#        [0,8,0,0,0,0,0,7,0,],
#        [1,0,3,0,6,0,8,0,9,],
#        [0,0,0,0,1,0,0,0,0,],
#        [0,5,4,0,0,0,9,1,0,],
#        [0,0,7,5,0,3,2,0,0,],]



#grid = [[5,3,0,0,7,0,0,0,0,],
#        [6,0,0,1,9,5,0,0,0,],
#        [0,9,8,0,0,0,0,6,7,],
#        [8,0,0,0,6,0,0,0,3,],
#        [4,0,0,8,0,3,0,0,1,],
#        [7,0,0,0,2,0,0,0,6,],
#        [0,6,1,0,0,0,2,8,0,],
#        [0,0,0,4,1,9,0,0,5,],
#        [0,0,0,0,8,0,0,7,9,],]
#

# predeclaration of grid
grid = [[0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],
        [0,0,0,0,0,0,0,0,0,],]

# number of empty slots
EMPTIES = 40

##############################################################################
# pull random elements from the grid

def pull_random():
    
    k = EMPTIES
    pulled = []
    while k>0:
        i=random.randint(0,8)
        j=random.randint(0,8)
        if [i,j] not in pulled:
            grid[i][j]=0
            pulled.append([i,j])
            k-=1

##############################################################################

##############################################################################
# Just prints the grid.

def print_grid(t):
    for x in range(9):
        print("")
        if x%3 == 0 and x!=0:
            print("-------------------")
        for y in range(9):
            if y%3 == 0 and y!=0:
                print("|",end="")
            
            print(t[x][y],end=" ")
    
##############################################################################

##############################################################################
# makes a solvable grid
            
def make_question():
    def fill(c=0):
        i, j = divmod(c, 9)
        arr=list(range(1,10))
        random.shuffle(arr)
        for t in arr:
            if (t not in grid[i] and all(row[j] != t for row in grid) and all(t not in row[j-j%3:j-j%3+3] for row in grid[i-i%3:i])): 
                grid[i][j]=t
                if c+1>=81 or fill(c+1):
                    return grid
        else:
            grid[i][j] = 0
            return None

    return fill()



##############################################################################


##############################################################################
# solve a grid using recursive backtracking
    
def sudoku_solver(grid):
    
    if not find_empty():
        return True
        
    else:
        r,c = find_empty()
    
    for x in range(1,10):
        if not is_used(x,r,c):
            grid[r][c] = x
            
            
            if sudoku_solver(grid):
                return True
            
        grid[r][c] = 0
        
    return False

#############################################################################
        
                         
   
##############################################################################
# return a list with coords of empty slot, false if no empty slots
    
def find_empty():
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                return [x,y]
    return False

##############################################################################

##############################################################################
# check if a number is already used in the row-col-block
    
def is_used(n,r,c):
    global grid
    for x in range(9):
        if grid[x][c] == n or grid[r][x] == n:
            return True
        
    
    if r in [0,1,2]:
        for x in [0,1,2]:
            
            if c in[0,1,2]:
                for y in [0,1,2]:
                    if n == grid[x][y]:
                        return True
            if c in[3,4,5]:
                for y in [3,4,5]:
                    if n == grid[x][y]:
                        return True
            if c in[6,7,8]:
                for y in [6,7,8]:
                    if n == grid[x][y]:
                        return True
                    
    elif r in [3,4,5]:
        for x in [3,4,5]:
            
            if c in[0,1,2]:
                for y in [0,1,2]:
                    if n == grid[x][y]:
                        return True
            if c in[3,4,5]:
                for y in [3,4,5]:
                    if n == grid[x][y]:
                        return True
            if c in[6,7,8]:
                for y in [6,7,8]:
                    if n == grid[x][y]:
                        return True
    
    elif r in [6,7,8]:
        for x in [6,7,8]:
            
            if c in[0,1,2]:
                for y in [0,1,2]:
                    if n == grid[x][y]:
                        return True
            if c in[3,4,5]:
                for y in [3,4,5]:
                    if n == grid[x][y]:
                        return True
            if c in[6,7,8]:
                for y in [6,7,8]:
                    if n == grid[x][y]:
                        return True
                    
    return False
            
##############################################################################


##############################################################################
# main
    
# generate question
print("Question is -")
grid=make_question()
pull_random()
print_grid(grid)
print("\n\n")

# solve question
print("Solution is -")
sudoku_solver(grid)
print_grid(grid)
print("") 
time.sleep(20)