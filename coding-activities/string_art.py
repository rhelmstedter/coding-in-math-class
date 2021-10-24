import turtle

def string_art(x, y, size, quad, color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.color(color)
    width = 10
    height = size
    lines = height//10

    if quad == 2:
        width = -width

    elif quad == 3:
        width = -width
        height = -height

    elif quad == 4:
        height = -height

    for _ in range(lines):
        turtle.penup()
        turtle.goto(x ,height + y)
        turtle.pendown()
        turtle.goto(width + x, y)
        turtle.goto(x ,height + y)

        if quad == 2:
            width -= 10
            height -= 10

        elif quad == 3:
            width -= 10
            height += 10

        elif quad == 4:
            width += 10
            height += 10

        else:
            width += 10
            height -= 10

turtle.speed(0)

for x in range (-200, 300, 100):
    for y in range (-200, 300, 100):
        for quad in range(1, 5):
            color = "#A5ACAF"
            if not x %200:
                color = '#3385ff'
            string_art(x, y, 100, quad, color)

turtle.ht()
turtle.exitonclick()

