from utils import load_input

data = load_input(2).split(",")


def part1():
    total = 0
    for r in data:
        start, end = map(int, r.split("-"))

        for x in range(start, end + 1):
            s = str(x)
            n = len(s)

            if n % 2 != 0:
                continue

            mid = n // 2
            if s[:mid] == s[mid:]:
                total += x

    return total


def part2():
    total = 0
    for r in data:
        start, end = map(int, r.split("-"))
        for x in range(start, end + 1):
            s = str(x)
            n = len(s)
            for pattern_len in range(1, n // 2 + 1):
                if n % pattern_len != 0:  # pattern cant be repeated evenly
                    continue
                pattern = s[:pattern_len]
                if pattern * (n // pattern_len) == s:
                    total += x
                    break

    return total


print("part1: ", part1())
print("part2: ", part2())
