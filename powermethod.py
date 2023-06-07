import numpy as np
import math


def morm(A: np.ndarray):
    sum = 0
    for x in A:
        sum += x**2
    return math.sqrt(sum)


def euclidean_scaling(A: np.ndarray, x: np.ndarray, iter):
    lamda = 0
    for i in range(iter):
        Ax = np.matmul(A, x)
        lamda = np.dot(Ax, x)
        x = Ax / morm(Ax)
        print("euclidean_scaling: ", Ax, x, lamda)
    return lamda, x


def maximum_entry_scaling(A: np.ndarray, x: np.ndarray, iter):
    lamda = 0
    for i in range(iter):
        Ax = np.matmul(A, x)
        lamda = np.dot(Ax, x) / np.dot(x, x)
        x = Ax / max(Ax)
        print("euclidean_scaling: ", lamda, x)
    return lamda, x

A = [[3, 2], [2, 3]]
x = [1, 0]


euclidean_scaling(np.array(A), np.array(x), 5)