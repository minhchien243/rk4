import numpy as np


def cholesky(A, b):
    n = len(A)
    L = np.zeros((n, n))
    y = np.zeros(n)

    for i in range(n):
        for j in range(i + 1):
            temp_sum = np.dot(L[i, :j], L[j, :j])
            if i == j:
                L[i, j] = np.sqrt(A[i, i] - temp_sum)
            else:
                L[i, j] = (A[i, j] - temp_sum) / L[j, j]

    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(L[i + 1:, i], x[i + 1:])) / L[i, i]

    return x


def doolittle(A, b):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i, i] = 1.0

        for j in range(i, n):
            U[i, j] = A[i, j] - np.dot(L[i, :i], U[:i, j])

        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x


def jacobi(A, b, x0, epsilon, max_iterations):
    n = len(A)
    x = np.copy(x0)
    iteration = 0

    while iteration < max_iterations:
        x_new = np.zeros(n)

        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

        if np.linalg.norm(x_new - x) < epsilon:
            break

        x = x_new
        iteration += 1

    return x


def gauss_seidel(A, b, x0, epsilon, max_iterations):
    n = len(A)
    x = np.copy(x0)
    iteration = 0

    while iteration < max_iterations:
        for i in range(n):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

        if np.linalg.norm(A @ x - b) < epsilon:
            break

        iteration += 1

    return x


if __name__ == "__main__":
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 4]])
    b = np.array([1, 2, 0, 1])
    x0 = np.zeros(len(A))
    epsilon = 1e-6
    max_iterations = 1000

    print("Cholesky method:")
    result_cholesky = cholesky(A, b)
    print("Result:", result_cholesky)

    print("\nDoolittle method:")
    result_doolittle = doolittle(A, b)
    print("Result:", result_doolittle)

    print("\nJacobi method:")
    result_jacobi = jacobi(A, b, x0, epsilon, max_iterations)
    print("Result:", result_jacobi)

    print("\nGauss-Seidel method:")
    result_gauss_seidel = gauss_seidel(A, b, x0, epsilon, max_iterations)
    print("Result:", result_gauss_seidel)
