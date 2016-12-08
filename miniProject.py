import turtle

LENGTH = 200


def draw():
    window = turtle.Screen()
    window.bgcolor("white")

    brad = turtle.Turtle()
    brad.shape("turtle")
    color = "yellow"
    brad.color(color)
    brad.speed(100)

    n = 36
    for counter in range(1, n + 1):
        draw_triangle(brad)
        brad.left(130)
        brad.color(color)
        color = switch_color(color)


    window.exitonclick()


def switch_color(color):
    if color == "yellow":
        color = "green"
    elif color == "green":
        color = "yellow"
    return color


def draw_triangle(any_turtle):
    any_turtle.forward(LENGTH)
    any_turtle.right(-120)
    any_turtle.forward(LENGTH)
    any_turtle.left(120)
    any_turtle.forward(LENGTH)


draw()
