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
        digits = [int(c) for c in bank[:-1]]
        first_digit = max(digits)
        first_digit_idx = digits.index(first_digit)
        second_digit = max([int(c) for c in bank[first_digit_idx + 1 :]])
        result = int(str(first_digit) + str(second_digit))
        total_joltage += result
    return total_joltage


def part2():
    total_joltage = 0

    for bank in data:
        batteries_needed = 12
        result = []
        i = 0

        for position in range(batteries_needed):
            remaining_needed = batteries_needed - position
            look_ahead = len(bank) - i - remaining_needed + 1

            search_end = i + look_ahead
            max_digit = max(bank[i:search_end])
            i = bank.index(max_digit, i, search_end) + 1

            result.append(max_digit)

        total_joltage += int("".join(result))

    return total_joltage


print("part1: ", part1())
print("part1: ", part2())

"""
Part 1:
1. Find largest digit in the sequence that isnt the last digit (pick leftmost if multiple)
2. Find largest digit again in the sequence that appears AFTER the first digit

Part 2:
1. Pick highest available digit greedily at each position (pick leftmost if multiple)
2. Ensure enough digits remain for the remaining positions 
"""
