import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2 * (x ** 3) + 6.5 * (x ** 2) - 5 * x + 6


def f_derivative(x):
    return 6 * (x ** 2) + 13 * x - 5


def f_second_derivative(x):
    return 12 * x + 13


def f_third_derivative(x):
    return 12


def newton_method(a, b, e):
    if f_derivative(a) * f_derivative(b) >= 0:
        return "Warunek konieczny nie jest spełniony."

    if f_second_derivative(a) * f_second_derivative(b) < 0 or f_third_derivative(a) * f_third_derivative(b) < 0:
        print("Warunki zbieżności nie są spełnione.")

    if f_third_derivative(a) * f_derivative(a) > 0:
        x0 = a
    else:
        x0 = b

    iter = 0
    xsrs = []

    while True:
        # if iter >= 20:
        #     break
        iter += 1

        x1 = x0 - f_derivative(x0) / f_second_derivative(x0)

        if abs(f_derivative(x1)) < e or abs(x1 - x0) < e:
            return x1, f(x1), iter, xsrs

        x0 = x1
        xsrs.append(x0)

    return x1, f(x1), iter, xsrs


a = 0.1
b = 4
e = 0.001

result = newton_method(a, b, e)

if isinstance(result, str):
    print(result)
else:
    x_result, y_result, iter, xsrs = result

    print(f"Ekstremum: x = {x_result}, f(x) = {y_result}, {iter} iteracji")

    x = np.linspace(a, b, 100)
    plt.plot(x, f(x), color='red')

    for xsr in xsrs:
        plt.scatter([xsr], [f(xsr)], color='blue', s=20)

    plt.scatter([x_result], [y_result], color='red', label='Ekstremum', s=100)
    plt.legend()
    plt.grid(True)
    plt.title("Metoda stycznych (Newtona)")
    plt.show()
