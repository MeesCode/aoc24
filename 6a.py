import time

def readGrid(file):
    m = {}
    inp = [list(i.strip()) for i in open(file).readlines()]
    for yi, y in enumerate(inp):
        for xi, item in enumerate(y):
            if item == '.':
                continue
            m[(xi, yi)] = item
    return m

grid = readGrid("6i.txt")

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction = 0

for p, c in grid.items():
    if c == '^':
        pos = p
        break

# find bounds
maxx = max([x for x, y in grid.keys()])
maxy = max([y for x, y in grid.keys()])
minx = min([x for x, y in grid.keys()])
miny = min([y for x, y in grid.keys()])

visited = set()
visited.add(pos)

while True:

    # determine new position
    newpos = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

    # check if we are on a wall
    if newpos in grid and grid[newpos] == '#':
        direction = (direction + 1) % 4
        continue

    # check if we are out of bounds
    if newpos[0] < minx or newpos[0] > maxx or newpos[1] < miny or newpos[1] > maxy:
        break

    # move
    pos = newpos
    visited.add(pos)

print(len(visited))