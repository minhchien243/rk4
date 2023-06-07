import math


def three_point_midpoint(f, x0, h):
    d = (f(x0 + h) - f(x0 - h)) / (2.0 * h)
    return d


def three_point_endpoint(f, x0, h):
    d = (-3 * f(x0) + 4 * f(x0 + h) - f(x0 + 2 * h)) / (2.0 * h)
    return d


def five_point_midpoint(f, x0, h):
    d = (f(x0 - 2 * h) - 8 * f(x0 - h) + 8 * f(x0 + h) - f(x0 + 2 * h)) / (12 * h)
    return d


def five_point_endpoint(f, x0, h):
    d = (-25 * f(x0) + 48 * f(x0 + h) - 36 * f(x0 + 2 * h) + 16 * f(x0 + 3 * h) - 3 * f(x0 + 4 * h)) / (12.0 * h)
    return d


def second_derivative(f, x0, h):
    d = h ** (-2) * (f(x0 - h) - 2 * f(x0) + f(x0 + h))
    return d


def f(value):
    return 1 / (math.pow(2 * math.pi, -0.5)) * math.pow(math.e, -value * value / 2)


l = 0
r = 1
cnt = 50
h = (r - l) / 50

for i in range(50):
    x0 = l + i * h
    print("value x0: ", x0)
    print("3-point midpoint: ", three_point_midpoint(f, x0, h))
    print("3-point endpoint: ", three_point_endpoint(f, x0, h))
    print("5-point midpoint: ", five_point_midpoint(f, x0, h))
    print("5-point endpoint: ", five_point_endpoint(f, x0, h))
    print("Second derivative: ", second_derivative(f, x0, h))
