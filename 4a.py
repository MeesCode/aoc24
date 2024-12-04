
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
    if c == 'X':

        # look in all directions
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:

                # ignore when no direction
                if dx == 0 and dy == 0:
                    continue

                # assemble string
                teststr = ''
                for i in range(4):
                    k = (x + (dx*i), y + (dy*i))
                    if k in grid:
                        teststr = teststr + grid[k]
                    else:
                        break

                # check if there's a match
                if(teststr == "XMAS"):
                    count = count + 1

print(count)