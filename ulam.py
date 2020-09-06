import turtle
import pyglet
from pyglet import shapes
import math
import colorsys


def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))


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
    coords = [(0, 0)]
    count = 0
    unit_vec = (1, 0)  # Starting direction facing left
    vec = (0, 0)       # Origin point
    n = 1
    prime_list = generate_primes(iterations * 2)
    print(len(prime_list))
    index = 0

    while count < iterations:
        # forward  * n > draw point > left > forward * n > draw point > left

        # go forward n times
        for i in range(n):
            vec = (vec[0] + unit_vec[0], vec[1] + unit_vec[1])
            if prime_list[index] == count:
                coords.append(vec)  # forward
                index += 1
            count += 1

        # turn left
        unit_vec = rotate(unit_vec, math.pi / 2)  # turn left

        # go forward n times
        for i in range(n):
            vec = (vec[0] + unit_vec[0], vec[1] + unit_vec[1])
            if prime_list[index] == count:
                coords.append(vec)  # forward
                index += 1
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
    window = pyglet.window.Window(800, 800)
    scale = 2
    batch = pyglet.graphics.Batch()

    origin = (window.width / 2, window.height / 2)
    color_step = 1 / len(coords)
    color_count = 1

    points = []
    for point in coords:
        color = hsv2rgb(color_step * color_count, 1.0, 1.0)
        new_point = shapes.Circle(origin[0] + (point[0] * scale), origin[1] + (point[1] * scale), 1, segments=3,
                                  color=color, batch=batch)
        points.append(new_point)
        color_count += 1

    @window.event()
    def on_draw():
        window.clear()
        batch.draw()

    pyglet.app.run()


# Returns list of primes below a given number using
# Sieve of Eratosthenes
def generate_primes(iterations):
    list = [True] * (iterations+1)

    for i in range(2, (int(iterations**(1/2))) + 1):    # Iterates over numbers, from 2 to the sqrt(iterations)
        if list[i]:                                     # If a number is marked as prime, it will continue from there
            for j in range(i**2, iterations+1, i):      # unmark multiple of that prime
                list[j] = False

    primes = []
    j = 2
    for x in list[2:iterations+1]:
        if x:
            primes.append(j)
        j += 1

    return primes


if __name__ == '__main__':
    spiral_points = generate_spiral(200000)

    render_spiral(spiral_points)





