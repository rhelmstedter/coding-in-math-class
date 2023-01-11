"""In Dungeons and Dragons, a player can gain an advantage by rolling two dice
simultaneously and choosing the higher value. What is the new expected value for an
n-sided die when rolling with an advantage?
"""

from itertools import product
from collections import Counter


def original_expected_value(n=6):
    sides = range(1, n + 1)
    return sum(num for num in sides) / n


def new_expected_value(n=6):
    sides = range(1, n + 1)
    counts = Counter(max(t) for t in product(sides, sides))
    return round(sum(count * value for value, count in counts.items()) / n**2, 3)


if __name__ == "__main__":
    sides = 11
    print(f"Original Expected Value for a D{sides}: {original_expected_value(sides)}")
    print(f"New Expected Value a D{sides}: {new_expected_value(sides)}")
