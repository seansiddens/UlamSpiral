import turtle
import pyglet
import math


def turtle_spiral(iterations):
    # Setup
    WIDTH = 800
    HEIGHT = 800
    canvas_width = 1000
    canvas_height = 1000

    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT)
    screen.bgcolor("black")
    screen.setworldcoordinates(-canvas_width, -canvas_height, canvas_width, canvas_height)

    length = canvas_width / 100

    # Turtle setup
    t = turtle.Turtle()
    t.speed('fastest')
    t.color('white')
    t.penup()

    num = 1
    count = 0
    while count < iterations:
        for i in range(num):
            t.forward(length)
            count += 1
            if is_prime(count):
                print(count)
                t.dot(2)
        t.left(90)
        for i in range(num):
            t.forward(length)
            count += 1
            if is_prime(count):
                print(count)
                t.dot(2)
        t.left(90)

        num += 1

    screen.update()
    screen.mainloop()


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# f(n) = 4n^2 + bn + c
def draw_polynomial(b, c, iterations):

    poly_nums = []
    for n in range(iterations):
        poly_nums.append(4 * pow(n, 2) + b * n + c)

    print(poly_nums)


    length = 10

    p = turtle.Turtle()
    p.speed('fastest')
    p.color('red')
    p.penup()

    num = 1
    count = 0
    index = 0
    while count < iterations:
        for i in range(num):
            p.forward(length)
            count += 1
            if count == poly_nums[index]:
                index += 1
                p.dot(2)
        p.left(90)
        for i in range(num):
            p.forward(length)
            count += 1
            if count == poly_nums[index]:
                index += 1
                p.dot(2)
        p.left(90)

        num += 1


def generate_spiral(iterations):
    coords = [(0,0)]
    count = 0
    unit_vec = (1, 0)  # Starting direction facing left
    vec = (0, 0)       # Origin point
    n = 1
    while count < iterations:
        # forward  * n > draw point > left > forward * n > draw point > left

        # go forward n times
        for i in range(n):
            vec = (vec[0] + unit_vec[0], vec[1] + unit_vec[1])
            coords.append(vec)  # forward
            count += 1

        # turn left
        unit_vec = rotate(unit_vec, math.pi / 2)  # turn left

        # go forward n times
        for i in range(n):
            vec = (vec[0] + unit_vec[0], vec[1] + unit_vec[1])
            coords.append(vec)  # forward
            count += 1

        # turn left
        unit_vec = rotate(unit_vec, math.pi / 2)

        n += 1

    return coords


def rotate(point, angle):
    px, py = point

    qx = (px * math.cos(angle)) - (py * math.sin(angle))
    qy = (px * math.sin(angle)) + (py * math.cos(angle))

    return int(qx), int(qy)


def render_spiral(coords):
    window = pyglet.window.Window
    pass


if __name__ == '__main__':

    iterations = 10000
    turtle_spiral(iterations)

    points = generate_spiral(100000)




