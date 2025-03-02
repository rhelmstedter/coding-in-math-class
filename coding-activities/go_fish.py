import random
from collections import Counter

fish = ["green", "blue", "blue", "blue", "yellow", "yellow","yellow", "yellow","yellow", "yellow"]

def calc_exp_prob(trials):
    outcomes = Counter()
    for cast in range(trials):
        outcomes.update([random.choice(fish)])

    yellow_prob = outcomes["yellow"] / trials
    blue_prob = outcomes["blue"] / trials
    green_prob = outcomes["green"] / trials

    print("Experimental Probablity")
    print("-----------------------")
    print(f"Number of trials = {trials:,}")
    print(f"P(yellow) = {yellow_prob:.5}")
    print(f"P(blue) = {blue_prob:.5}")
    print(f"P(green) = {green_prob:.5}")

def calc_theoretical_prob():
    total = len(fish)
    fish_counts = Counter(fish)

    yellow_prob = fish_counts["yellow"] / total
    blue_prob = fish_counts["blue"] / total
    green_prob = fish_counts["green"] / total

    print("Theoretical Probablity")
    print("----------------------")
    print(f"P(yellow) = {yellow_prob:.5}")
    print(f"P(blue) = {blue_prob:.5}")
    print(f"P(green) = {green_prob:.5}")

if __name__ == "__main__":
        calc_theoretical_prob()
        print()
        calc_exp_prob(1000000)
