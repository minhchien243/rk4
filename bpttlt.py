import numpy as np
from scipy.integrate import quad
from scipy.optimize import minimize


def f(x):
    return np.sin(x)


def polynomial_approximation(x, coefficients):
    return np.sum([coefficients[i] * x ** i for i in range(len(coefficients))])


def error_function(coefficients):
    segment_start = 0
    segment_end = np.pi / 2
    error, _ = quad(lambda x: (f(x) - polynomial_approximation(x, coefficients)) ** 2, segment_start, segment_end)
    return error


# Degree of the polynomial approximation
n = 2

# Initial guess for the coefficients
initial_guess = np.zeros(n + 1)

# Minimize the error function
result = minimize(error_function, initial_guess)

optimized_coefficients = result.x

# Evaluate the polynomial approximation at a given point
x_value = 1.0
approximation_value = polynomial_approximation(x_value, optimized_coefficients)

print("Coefficients:", optimized_coefficients)
print("Approximation_value", approximation_value)
