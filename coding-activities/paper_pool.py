import time
import os

SOUTHEAST = (1, 1)
NORTHEAST = (1, -1)
SOUTHWEST = (-1, 1)
NORTHWEST = (-1, -1)

direction_change_from_base = {
    SOUTHEAST: NORTHEAST,
    SOUTHWEST: NORTHWEST,
    NORTHEAST: SOUTHEAST,
    NORTHWEST: SOUTHWEST,
}
direction_change_from_height = {
    SOUTHEAST: SOUTHWEST,
    SOUTHWEST: SOUTHEAST,
    NORTHEAST: NORTHWEST,
    NORTHWEST: NORTHEAST,
}


def generate_table(base, height):
    table = []
    top = ["╭"] + ["―"] * (base - 1) + ["╮"]
    table.append(top)
    for row in range(height - 1):
        table.append(["|"] + [" "] * (base - 1) + ["|"])
    bottom = ["╰"] + ["―"] * (base - 1) + ["╯"]
    table.append(bottom)
    return table


def simulation(table, base, height):
    CORNERS = ((base, 0), (0, height), (base, height))
    direction = SOUTHEAST
    x, y = (1, 1)
    rebounds = 0
    while True:
        if y == 0 or y == height:
            direction = direction_change_from_base[direction]
            rebounds += 1
        elif x == 0 or x == base:
            direction = direction_change_from_height[direction]
            rebounds += 1

        table[y][x] = "*"
        x, y = x + direction[0], y + direction[1]

        if (x, y) in CORNERS:
            table[y][x] = "0"
            break
        for row in table:
            print(*row)
        if max(base, height) > 10:
            time.sleep(0.001)
        else:
            time.sleep(0.15)
        os.system('cls' if os.name == 'nt' else 'clear')
    for row in table:
        print(*row)
    print(f"Number of rebounds: {rebounds}")


def count_rebounds(base, height):
    CORNERS = ((base, 0), (0, height), (base, height))
    direction = SOUTHEAST
    x, y = (1, 1)
    rebounds = 0
    while True:
        if y == 0 or y == height:
            direction = direction_change_from_base[direction]
            rebounds += 1
        elif x == 0 or x == base:
            direction = direction_change_from_height[direction]
            rebounds += 1
        x, y = x + direction[0], y + direction[1]
        if (x, y) in CORNERS:
            break
    return rebounds


if __name__ == "__main__":
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))
    table = generate_table(base, height)
    simulation(table, base, height)
