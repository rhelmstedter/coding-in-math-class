#! python3
"""Simulate Rolling Two 6-sided dice."""

from random import randint
from collections import Counter
from matplotlib import pyplot

TRIALS: int = 10000


def simulate(n):
    """Simulate rolling two 6-sided dice.

    Parameters
    ----------
    n : int
        Number of trials
    """
    rolls = []
    for trial in range(n):
        trial = randint(1, 6) + randint(1, 6)
        rolls.append(trial)
    return rolls


def plot(counts: Counter):
    """Plot all the results of the simulation.

    Parameters
    ----------
    counts : Counter
        A counter containing the number of times a give sum was rolled
    """
    pyplot.title(f"{TRIALS} Pairs of 6-sided Dice")
    pyplot.xlabel("Sum of Roll")
    pyplot.ylabel("Frequency")
    pyplot.bar(counts.keys(), counts.values())
    pyplot.show()


results = simulate(TRIALS)
counts = Counter(results)
print("(sum, count)")
print(sorted(counts.items()))
plot(counts)
