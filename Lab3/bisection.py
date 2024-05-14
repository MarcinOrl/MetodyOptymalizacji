import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2 * (x ** 3) + 6.5 * (x ** 2) - 5 * x + 6


def f_derivative(x):
    return 6 * (x ** 2) + 13 * x - 5


def bisection(a, b, e):
    if f_derivative(a) * f_derivative(b) >= 0:
        return "Warunek konieczny nie jest spełniony."

    iter = 0
    xsrs = []

    while True:
        # if iter >= 20:
        #     break
        iter += 1
        xsr = (a + b) / 2
        xsrs.append(xsr)

        if abs(f_derivative(xsr)) < e:
            return xsr, f(xsr), iter, xsrs

        if f_derivative(xsr) * f_derivative(a) < 0:
            b = xsr
        else:
            a = xsr

    return xsr, f(xsr), iter, xsrs


a = 0.1
b = 4
e = 0.001

result = bisection(a, b, e)

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
    plt.title("Metoda bisekcji (połowienia przedziałów)")
    plt.show()
