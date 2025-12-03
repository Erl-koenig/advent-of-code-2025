from utils import load_input

example = """987654321111111
811111111111119
234234234234278
818181911112111
""".splitlines()

data = load_input(3).splitlines()


def part1():
    total_joltage = 0
    for bank in data:
        digits_idx = [(int(c), i) for i, c in enumerate(bank[:-1])]
        first_digit, first_digit_idx = max(digits_idx, key=lambda x: (x[0], -x[1]))
        second_digit = max([int(c) for c in bank[first_digit_idx + 1 :]])
        result = int(str(first_digit) + str(second_digit))
        total_joltage += result
    return total_joltage


print("part1: ", part1())
# print("part1: ", part2())

"""
Part 1:
1. Find largest digit in the sequence that isnt the last digit (pick leftmost if multiple)
2. Find largest digit again in the sequence that appears AFTER the first digit

Part 2:

"""
