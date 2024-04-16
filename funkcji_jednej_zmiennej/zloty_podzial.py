import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2 * (x ** 3) + 6.5 * (x ** 2) - 5 * x + 6


def zloty_podzial_maximum(a, b, epsilon):
    iter = 0
    xs_max = []
    k = (np.sqrt(5) - 1) / 2

    x1 = b - k * (b - a)
    x2 = a + k * (b - a)

    while abs(x2 - x1) >= epsilon:
        iter += 1
        if f(x1) > f(x2):
            b = x2
            x2 = x1
            x1 = b - k * (b - a)

        else:
            a = x1
            x1 = x2
            x2 = a + k * (b - a)

        xs_max.append((a + b) / 2)

    return (a + b) / 2, f((a + b) / 2), iter, xs_max


def zloty_podzial_minimum(a, b, epsilon):
    iter = 0
    xs_min = []
    k = (np.sqrt(5) - 1) / 2

    x1 = b - k * (b - a)
    x2 = a + k * (b - a)

    while abs(x2 - x1) >= epsilon:
        # if iter >= 20:
        #     break
        xs_min.append((a + b) / 2)
        iter += 1
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = b - k * (b - a)

        else:
            a = x1
            x1 = x2
            x2 = a + k * (b - a)

    return (a + b) / 2, f((a + b) / 2), iter, xs_min


a = 0.1
b = 4
e = 0.0001

minimum_x, minimum_y, iter_min, xs_min = zloty_podzial_minimum(a, b, e)
maximum_x, maximum_y, iter_max, xs_max = zloty_podzial_maximum(a, b, e)

print(f"Minimum: x = {minimum_x}, f(x) = {minimum_y}, {iter_min} iteracji")
print(f"Maksimum: x = {maximum_x}, f(x) = {maximum_y}, {iter_max} iteracji")

x = np.linspace(a, b, 100)
plt.plot(x, f(x), color='red')

for x_min in xs_min:
    plt.scatter([x_min], [f(x_min)], color='blue', s=20)

for x_max in xs_max:
    plt.scatter([x_max], [f(x_max)], color='green', s=20)

plt.scatter([minimum_x], [minimum_y], color='lightskyblue', label='Minimum', s=100)
plt.scatter([maximum_x], [maximum_y], color='lime', label='Maksimum', s=100)

plt.legend()
plt.grid(True)
plt.title("Metoda złotego podziału")
plt.show()
