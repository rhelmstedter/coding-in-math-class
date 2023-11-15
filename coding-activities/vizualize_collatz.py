import turtle


def hailstone(n: int) -> list[int]:
    """Return a list of the hailstone sequence for the number n."""
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def draw():
    """Visualize the collatz conjecture."""
    screen = turtle.Screen()
    screen.setup(1.0, 1.0)
    screen.tracer(0, 0)
    colors = [
        "#001219",
        "#005F73",
        "#0A9396",
        "#94D2BD",
        "#E9D8A6",
        "#EE9B00",
        "#CA6702",
        "#BB3E03",
        "#AE2012",
        "#9B2226",
    ]
    rotation = 4
    for n in range(5, 1000):
        collatz = turtle.Turtle()
        collatz.hideturtle()
        collatz.penup()
        collatz.setposition(-400, -400)
        collatz.setheading(90)
        collatz.speed(0)
        collatz.pendown()
        collatz.pensize(3)
        collatz.color(colors[n % len(colors)])
        for term in hailstone(n):
            if term % 2 == 0:
                collatz.right(rotation)
            else:
                collatz.left(rotation)
            collatz.forward(8)
        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    draw()
