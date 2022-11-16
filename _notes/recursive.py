
# https://medium.com/@ekapope.v/learning-recursive-algorithm-with-sudoku-solver-in-python-345623de98ae

# example grid
# the black cells are filled with 0
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
        

def possible(y,x,n):
  global grid
  # n is the number we want to fill in

  # 1st 
  # check if n already existed in vertical (y) axis
  # if exists, return False (not possible)
  for i in range(9):
    if grid[y][i] == n:
      return False

  # 2nd
  # check horizontal (x) axis
  for i in range(9):
    if grid[i][x] == n:
      return False

  # 3rd
  # check the 3x3 local grid
  x0 = (x//3)*3 
  y0 = (y//3)*3
  for i in range(3):
    for j in range(3):
      if grid[y0+i][x0+j] == n:
         return False

  # return true if pass all 3 checks.
  return True

def solve():
  global grid
  for y in range(9):
    for x in range(9):
      # Find blank positions in the grid (value = 0)
      if grid[y][x] == 0:
        # Loop n from 1-9
        for n in range(1,10):
          if possible(y,x,n):
            grid[y][x] = n
            solve()

            # This is where backtracking happens
            # Reset the latest position back to 0 and try with new n value
            grid[y][x] = 0
        return
  print(np.matrix(grid))
  input('More?')
  