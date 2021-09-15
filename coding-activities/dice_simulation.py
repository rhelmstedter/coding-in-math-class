#! python3
from random import randint
from typing import List
from collections import Counter
from matplotlib import pyplot

TRIALS: int = 1000


def simulate(n: int) -> List[int]:
    rolls: List[int] = []
    for trial in range(n):
        roll = randint(1,6) + randint(1,6)
        rolls.append(roll)
    return rolls

def plot(counts):
    pyplot.title(f"{TRIALS} Dice Rolls")
    pyplot.xlabel("Sum of Roll")
    pyplot.ylabel("Frequency")
    pyplot.bar(counts.keys(), counts.values())
    pyplot.show()

results = simulate(TRIALS)
counts = Counter(results)
print(counts)
plot(counts)
