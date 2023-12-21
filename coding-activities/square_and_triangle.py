
def square_number(n):
    """Return the nth square number."""
    return n ** 2


def triangle_number(n):
    """Return the nth triangle number."""
    return n * (n + 1) // 2


squares = []
both = []
n = 1

while len(both) < 3:
    nth_square = square_number(n)
    nth_triangle = triangle_number(n)

    squares.append(nth_square)

    # triangle numbers grow more slowly than squares
    if nth_triangle in squares:
        both.append(nth_triangle)
    n += 1

print(both)
