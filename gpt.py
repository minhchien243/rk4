import math


def f(x):
    return math.sin(x)


def dfx(x, tol):
    return (f(x + tol) - f(x)) / tol


def bisection_method(f, a, b, tol):
    if f(a) * f(b) >= 0:
        print("Cannot apply bisection method on this interval.")
        return None

    while (b - a) >= tol:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


def fixed_point_iteration(f, x0, tol, max_iterations):
    x = x0

    for i in range(max_iterations):
        if abs(x - (x + f(x))) <= tol:
            return x
        x = x + f(x)
    return x


def falsepoint_method(f, a, b, tol, max_iterations):
    if f(a) * f(b) >= 0:
        print("Cannot apply chord method on this interval.")
        return None

    for i in range(max_iterations):
        p = (a * f(b) - b * f(a)) / (f(b) - f(a))
        fx = f(p)
        if abs(a - b) < tol:
            return p
        elif fx > 0:
            b = p
        else:
            a = p
    return a


def newton_method(f, dfx, x0, tol, max_iterations):
    x = x0

    for i in range(max_iterations):
        x1 = x - f(x) / dfx(x, tol)
        if abs(x1 - x) < tol:
            return x1
        x = x1

    return x


def secant_method(f, x0, x1, tol, max_iterations):
    x_prev = x0
    x = x1
    iteration = 0

    for i in range(max_iterations):
        x1 = x - f(x) * (x - x_prev) / (f(x) - f(x_prev))
        if abs(x1 - x) < tol:
            return x1
        x_prev = x
        x = x1

    return x


tol = 1e-6
max_iterations = 1000

a = 3
b = 4

print("Bisection method:")
result_bisection = bisection_method(f, a, b, tol)
print("Result:", result_bisection)

print("\nFixed-point iteration method:")
result_fixed_point = fixed_point_iteration(f, a, tol, max_iterations)
print("Result:", result_fixed_point)

print("\nFalse point method:")
result_falsepoint = falsepoint_method(f, a, b, tol, max_iterations)
print("Result:", result_falsepoint)

print("\nNewton method:")
result_newton = newton_method(f, dfx, a, tol, max_iterations)
print("Result:", result_newton)

print("\nSecant method:")
result_secant = secant_method(f, a, b, tol, max_iterations)
print("Result:", result_secant)
