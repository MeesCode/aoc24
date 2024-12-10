

def readGrid(file):
    m = {}
    inp = [list(i.strip()) for i in open(file).readlines()]
    for yi, y in enumerate(inp):
        for xi, item in enumerate(y):
            if item == '.':
                continue
            m[(xi, yi)] = item
    return m

grid = readGrid("8i.txt")

anetennas = {}
nodes = set()

maxx = len(open("8i.txt").readlines()[0].strip())
maxy = len(open("8i.txt").readlines())

# create a list of all combinations of two positions with the same antenna
for p1, c1 in grid.items():
    for p2, c2 in grid.items():
        if c1 == c2:
            if p1 == p2:
                continue
            if c1 not in anetennas:
                anetennas[c1] = []
            anetennas[c1].append((p1, p2))
    
for antenna, positions in anetennas.items():
    for (pos1, pos2) in positions:

        newx = (pos1[0] - pos2[0]) + pos1[0]
        newy = (pos1[1] - pos2[1]) + pos1[1]

        if newx < 0 or newx >= maxx or newy < 0 or newy >= maxy:
            continue

        nodes.add((newx, newy))
    
print(len(nodes))