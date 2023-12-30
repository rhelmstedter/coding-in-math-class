def exploding_dots(number, base):
    machine = []  # machine starts as emptylist
    print(f"The code for {number} in a 1 <- {base} machine is:\n")
    while number >= base:
        explosions = number // base
        leftoverDots = number % base
        machine.append(leftoverDots)
        number = explosions
    machine.append(number)
    for digit in reversed(
        machine
    ):  # the list starts with 1s digit so we have to reverse it
        print(f"| {digit}", end=" ")


# takes input from user and converts to integers
# base = int(input("Enter the machine do you want to work in? "))
# number = int(input(f"Enter a number into the 1 <- {base} machine: "))

exploding_dots(13, 2)
