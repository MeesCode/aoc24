
def readGrid(file):
    m = {}
    inp = [list(i.strip()) for i in open(file).readlines()]
    for yi, y in enumerate(inp):
        for xi, item in enumerate(y):
            m[(xi, yi)] = item
    return m

grid = readGrid("4i.txt")

count = 0

for (x, y), c in grid.items():

    # first character
    if c == 'M':
        # check if the his the topleft M of a cross
        if (
            ((x+2, y) in grid and grid[(x+2, y)] == 'S') and 
            ((x+1, y+1) in grid and grid[(x+1, y+1)] == 'A') and 
            ((x, y+2) in grid and grid[(x, y+2)] == 'M') and 
            ((x+2, y+2) in grid and grid[(x+2, y+2)] == 'S') 
            or 
            ((x+2, y) in grid and grid[(x+2, y)] == 'M') and 
            ((x+1, y+1) in grid and grid[(x+1, y+1)] == 'A') and 
            ((x, y+2) in grid and grid[(x, y+2)] == 'S') and 
            ((x+2, y+2) in grid and grid[(x+2, y+2)] == 'S') 
            ):
            count = count + 1

    if c == 'S':
        # check if the his the topleft S of a cross
        if (
            ((x+2, y) in grid and grid[(x+2, y)] == 'M') and 
            ((x+1, y+1) in grid and grid[(x+1, y+1)] == 'A') and 
            ((x, y+2) in grid and grid[(x, y+2)] == 'S') and 
            ((x+2, y+2) in grid and grid[(x+2, y+2)] == 'M') 
            or 
            ((x+2, y) in grid and grid[(x+2, y)] == 'S') and 
            ((x+1, y+1) in grid and grid[(x+1, y+1)] == 'A') and 
            ((x, y+2) in grid and grid[(x, y+2)] == 'M') and 
            ((x+2, y+2) in grid and grid[(x+2, y+2)] == 'M') 
            ):
            count = count + 1

print(count)