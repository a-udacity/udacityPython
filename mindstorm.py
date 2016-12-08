import turtle


def draw():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("green")

    n = 36
    for counter in range(1, n + 1):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()


def draw_square(any_turtle):
    n = 4
    for counter in range(1, n + 1):
        any_turtle.forward(100)
        any_turtle.right(90)



draw()
