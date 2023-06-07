import numpy as np
import math


def f(x):
    return 1 / (math.pow(2 * math.pi, -0.5)) * math.pow(math.e, -x * x / 2)


def polynomial_approximation(xx, coefficients_value):
    return np.sum([coefficients_value[i] * x ** i for i in range(len(coefficients_value))])


# Given [l, r], number of points
l = 0.0
r = 1.0
cnt = 40.0
h = float((r - l) / cnt)
# Degree of the polynomial
degree = 1
# init list x, fx
arr = []
arrFx = []

for i in range(40):
    arr = arr + [i * h + l]
    arrFx = arrFx + [f(i * h + l)]

print(arr)

x = np.array(arr)
y = np.array(arrFx)

# Create the Vandermonde matrix
V = np.vander(x, degree + 1, increasing=True)

# Solve the least squares problem
coefficients, residuals, rank, singular_values = np.linalg.lstsq(V, y, rcond=None)

x_value = 1
approximation_value = polynomial_approximation(x_value, coefficients)

# Print the coefficients
print("Coefficients:", coefficients)
print("Approximation_value", approximation_value)
