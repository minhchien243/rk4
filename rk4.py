import math

import numpy as np


def f(t, w: np.ndarray):
    result = np.ndarray(3)
    result[0] = w[2]
    if w[1] >= 0:
        result[1] = math.pow(w[1], 1/3) - t * w[2]
    else:
        result[1] = - math.pow(abs(w[1]), 1 / 3) - t * w[2]
    result[2] = math.pow(math.e, -w[2]) + w[0] - math.cos(t)
    return result


"""
def u1(t):
    return math.cos(t) + math.sin(t) - pow(math.e, t) + 1


def u2(t):
    return -math.sin(t) + math.cos(t) - pow(math.e, t) + 1


def u3(t):
    return -math.sin(t) + math.cos(t)


def error(w, x):
    return [abs(u1(x) - w[0]), abs(u2(x) - w[1]), abs(u3(x) - w[2])]
"""


wi = np.array([-2, 8, 0])
T = 0.0
h = 0.01
for i in range(100):
    k1 = f(T, wi)
    k2 = f(T + 0.5 * h, wi + 0.5 * h * k1)
    k3 = f(T + 0.5 * h, wi + 0.5 * h * k2)
    k4 = f(T + h, wi + h * k3)
    print("k1 = ", k1)
    print("k2 = ", k2)
    print("k3 = ", k3)
    print("k4 = ", k4)
    print("Ti: ", T)
    print("Wi: ", wi)
    wi = wi + (k1 + 1/2 * k2 + 1/2 * k3 + k4) * h / 6
    T = T + h
