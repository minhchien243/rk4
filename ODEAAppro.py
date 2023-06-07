import numpy as np


def dfx(x, y):
    return 2 * x * y


def taylor_series(y, x0: float, df, h: float, iter):
    print("taylor_series: ")
    for i in range(iter):
        print("# i = ", i, ":", sep="", end=" ")
        y = y + h * df(x0, y)
        print("y = ", y)
        x0 += h

    print()


def midpoint(y, x0: float, df, h: float, iter):
    print("midpoint: ")
    for i in range(iter):
        print("# i = ", i, ":", sep="", end=" ")
        x_mid = x0 + h * 0.5
        y_mid = y + h * 0.5 * df(x0, y)
        f_mid = df(x_mid, y_mid)
        y = y + h * f_mid
        print("y =", y)
        x0 += h


def heun(y, x0: float, df, h: float, iter):
    print("heun: ")
    for i in range(iter):
        print("# i = ", i, ":", sep="", end=" ")
        y_predict = y + h * df(x0, y)
        y = y + h * 0.5 * (df(x0, y) + df(x0 + h, y_predict))
        print("y =", y)
        x0 += h


def rk4(y, x0: float, df, h: float, iter):
    print("rk4: ")
    for i in range(iter):
        print("# i = ", i, ":", sep="", end=" ")
        k1 = df(x0, y)
        # print("k1 = ", k1)
        k2 = df(x0 + 0.5 * h, y + 0.5 * h * k1)
        # print("k2 = ", k2)
        k3 = df(x0 + 0.5 * h, y + 0.5 * h * k2)
        # print("k3 = ", k3)
        k4 = df(x0 + h, y + h * k3)
        # print("k4 = ", k4)

        y = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

        print("x = ", x0, ", y = ", y)
        x0 += h
    print()


taylor_series(1, 1, dfx, 0.01, 10)
midpoint(1, 1, dfx, 0.01, 10)
heun(1, 1, dfx, 0.01, 10)
rk4(1, 1, dfx, 0.01, 10)
