from utils import load_input

DIAL_SIZE = 100
idx = 50
data = load_input(1).splitlines()
part1 = 0
part2 = 0

for line in data:
    direction = line[0]
    dist = int(line[1:])

    # part 2
    if direction == "R":
        first = (DIAL_SIZE - idx) % DIAL_SIZE or DIAL_SIZE
    else:
        first = idx if idx > 0 else DIAL_SIZE

    if dist >= first:
        part2 += 1 + (dist - first) // DIAL_SIZE

    # update pos
    if direction == "R":
        idx = (idx + dist) % DIAL_SIZE
    else:
        idx = (idx - dist) % DIAL_SIZE

    # part 1
    if idx == 0:
        part1 += 1

print("part1: ", part1)
print("part2: ", part2)
