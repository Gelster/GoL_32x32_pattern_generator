import numpy as np
import copy
import pandas as pd

# Apply Conway's rules
def update(grid):
    # copy grid since we require 8 neighbors
    # for calculation and we go line by line
    N = 32
    newGrid = grid.copy()
    total_sum = 0
    for i in range(N):
        for j in range(N):

            # compute 8-neighbor sum
            # using toroidal boundary conditions - x and y wrap around
            # so that the simulation takes place on a toroidal surface.
            total = int(grid[i, (j - 1) % N]) +\
                    int(grid[i, (j + 1) % N]) +\
                    int(grid[(i - 1) % N, j]) +\
                    int(grid[(i + 1) % N, j]) +\
                    int(grid[(i - 1) % N, (j - 1) % N]) +\
                    int(grid[(i - 1) % N, (j + 1) % N]) +\
                    int(grid[(i + 1) % N, (j - 1) % N]) +\
                    int(grid[(i + 1) % N, (j + 1) % N])

            total_sum += total
            # apply Conway's rules

            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    newGrid[i, j] = 0
            else:
                if total == 3:
                    newGrid[i, j] = 1

    # update data
    grid[:] = newGrid[:]
    return newGrid

# Generate random pattern
def generate(density):
    pattern = np.random.choice([False, True], size=[32,32], p=[1-density, density])
    return pattern

def characterize(pattern):
    sum = np.sum(pattern)
    return sum

def apply_rule_N_times(N,arr):
    for i in range(N):
        arr = update(arr)
    return arr


pattern_folder = 'C:\\Users\\Podhr\\Documents\\GoL\\PatternGenerator\\patterns\\'
char_file = 'C:\\Users\\Podhr\\Documents\\GoL\\PatternGenerator\\characterization.txt'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    char = open(char_file, 'w')
    loops = 1000
    arr = generate(0.5)
    sum = characterize(arr)
    print(sum)
    char.write(str(0) + ": " + str(sum) + "\n")
    print(str(0) + "/" + str(loops))
    for i in range(loops):
        np.savetxt(pattern_folder + str(i) +'.txt', arr, delimiter='\t', fmt="%5i")
        arr = copy.deepcopy(apply_rule_N_times(1, arr))
        sum = characterize(arr)
        print(sum)
        char.write(str(i+1) + ": " + str(sum) + "\n")
        print(str(i+1)+"/"+str(loops))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# data = pd.read_csv(file)