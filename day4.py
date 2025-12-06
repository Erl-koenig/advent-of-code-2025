from utils import load_input

example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".splitlines()

data = load_input(4).splitlines()
grid = [list(line) for line in data]
rolls_accessible = 0
rows = len(grid)
cols = len(grid[0])

adjacent_directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != "@":
            continue

        neighbors = 0
        for xr, xc in adjacent_directions:
            yr, yc = r + xr, c + xc
            if not (0 <= yr < rows and 0 <= yc < cols):
                continue
            if grid[yr][yc] == "@":
                neighbors += 1

        if neighbors < 4:
            rolls_accessible += 1


print("part1: ", rolls_accessible)
