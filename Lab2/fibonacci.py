import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2 * (x ** 3) + 6.5 * (x ** 2) - 5 * x + 6


def fibonacci(n):
    if n <= 1:
        return n
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


def fibonacci_minimum(a, b, epsilon):
    n = 0
    iter = 0
    xs_min = []

    while (b - a) / fibonacci(n + 2) >= 2 * epsilon:
        n += 1

    x1 = b - (fibonacci(n + 1) / fibonacci(n + 2)) * (b - a)
    x2 = a + (fibonacci(n + 1) / fibonacci(n + 2)) * (b - a)
    xs_min.append((x1 + x2) / 2)

    while abs(x2 - x1) >= epsilon and n > 1:
        # if iter >= 20:
        #     break
        iter += 1
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            n -= 1
            x1 = b - (fibonacci(n + 1) / fibonacci(n + 2)) * (b - a)
            xs_min.append((x1 + x2) / 2)
        else:
            a = x1
            x1 = x2
            n -= 1
            x2 = a + (fibonacci(n + 1) / fibonacci(n + 2)) * (b - a)
            xs_min.append((x1 + x2) / 2)

    return (a + b) / 2, f((a + b) / 2), iter, xs_min


def fibonacci_maximum(a, b, epsilon):
    n = 0
    iter = 0
    xs_max = []

    while (b - a) / fibonacci(n + 2) >= 2 * epsilon:
        n += 1

    x1 = b - (fibonacci(n + 1) / fibonacci(n + 2)) * (b - a)
    x2 = a + (fibonacci(n + 1) / fibonacci(n + 2)) * (b - a)
    xs_max.append((x1 + x2) / 2)

    while abs(x2 - x1) >= epsilon and n > 1:
        iter += 1
        if f(x1) > f(x2):
            b = x2
            x2 = x1
            n -= 1
            x1 = b - (fibonacci(n + 1) / fibonacci(n + 2)) * (b - a)
            xs_max.append((x1 + x2) / 2)
        else:
            a = x1
            x1 = x2
            n -= 1
            x2 = a + (fibonacci(n + 1) / fibonacci(n + 2)) * (b - a)
            xs_max.append((x1 + x2) / 2)

    return (a + b) / 2, f((a + b) / 2), iter, xs_max


a = 0.1
b = 4
e = 0.001

minimum_x, minimum_y, iter_min, xs_min = fibonacci_minimum(a, b, e)
maximum_x, maximum_y, iter_max, xs_max = fibonacci_maximum(a, b, e)

print(f"Minimum: x = {minimum_x}, f(x) = {minimum_y}, {iter_min} iteracji")
print(f"Maksimum: x = {maximum_x}, f(x) = {maximum_y}, {iter_max} iteracji")

x = np.linspace(a, b, 100)
plt.plot(x, f(x), color='red')
plt.scatter([minimum_x], [minimum_y], color='lightskyblue', label='Minimum', s=100)
plt.scatter([maximum_x], [maximum_y], color='lime', label='Maksimum', s=100)

for x_min in xs_min:
    plt.scatter([x_min], [f(x_min)], color='blue', s=20)

for x_max in xs_max:
    plt.scatter([x_max], [f(x_max)], color='green', s=20)

plt.legend()
plt.grid(True)
plt.title("Metoda Fibonacciego")
plt.show()
