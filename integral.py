import math


def f(value):
    return math.sqrt(2 * math.pi) * math.pow(math.e, -value ** 2 / 2)


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n  # Step size
    integral = 0  # The result

    integral += (f(a) + f(b)) / 2.0
    for i in range(1, n):
        x = a + i * h  # Calculate x coordinate
        integral += f(x)

    integral *= h

    return integral


def midpoint_rule(f, a, b, n):
    h = (b - a) / n  # Step size
    integral = 0

    for i in range(n - 1):
        x = a + (i + 0.5) * h
        integral += f(x)

    integral *= h

    return integral


def simpson_rule(f, a, b, n):
    h = (b - a) / n  # Step size
    integral = 0

    for i in range(n):
        x0 = a + i * h
        x1 = a + (i + 0.5) * h
        x2 = a + (i + 1) * h

        integral += f(x0) + 4 * f(x1) + f(x2)

    integral *= h / 6

    return integral


l = 0
r = 1
n = 50

trap = trapezoidal_rule(f, l, r, n)
mid = midpoint_rule(f, l, r, n)
simp = simpson_rule(f, l, r, n)

print("Trapezoidal_rule: ", trap)
print("Midpoint_rule: ", mid)
print("Simpson_rule: ", simp)
