import math


def _u1(t, w):
    return w[1]


def _u2(t, w):
    return -w[0] - 2 * pow(math.e, t) + 1


def _u3(t, w):
    return -w[0] - pow(math.e, t) + 1


def u1(t):
    return math.cos(t) + math.sin(t) - pow(math.e, t) + 1


def u2(t):
    return -math.sin(t) + math.cos(t) - pow(math.e, t) + 1


def u3(t):
    return -math.sin(t) + math.cos(t)


def calc(w, k, frag):
    res = [0, 0, 0]
    for i in range(3):
        if frag == 0:
            res[i] = w[i] + k[i] / 2
        else:
            res[i] = w[i] + k[i]
    return res


def error(w, x):
    return [abs(u1(x) - w[0]), abs(u2(x) - w[1]), abs(u3(x) - w[2])]


wi = [1, 0, 1]
T = 0
h = 0.5
f = open("answer.txt", "a")
for i in range(9):
    f.writelines(["Ti: ", str(T), '\n'])
    f.writelines(["Wi: ", str(wi), '\n'])
    f.writelines(["Ui: ", str(u1(i/2)), str(u2(i/2)), str(u3(i/2)), '\n'])
    f.writelines(["Err: ", str(error(wi, i/2)), '\n'])
    k1 = [_u1(T, wi) * h, _u2(T, wi) * h, _u3(T, wi) * h]
    tmp = calc(wi, k1, 0)
    k2 = [_u1(T + h/2, tmp) * h, _u2(T + h/2, tmp) * h, _u3(T + h/2, tmp) * h]
    tmp = calc(wi, k2, 0)
    k3 = [_u1(T + h/2, tmp) * h, _u2(T + h/2, tmp) * h, _u3(T + h/2, tmp) * h]
    tmp = calc(wi, k3, 1)
    k4 = [_u1(T + h, tmp) * h, _u2(T + h, tmp) * h, _u3(T + h, tmp) * h]
    for i in range(3):
        wi[i] = wi[i] + (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6
    T = T + h
f.close()