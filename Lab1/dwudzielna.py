import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2 * (x ** 3) + 6.5 * (x ** 2) - 5 * x + 6


def minimum(a, b, fx, e):
    xsr = (a + b) / 2
    L = b - a
    i = 0
    xsrs_min = []

    while L > e:
        # if i >= 20:
        #     break
        i += 1
        x1 = a + L / 4
        x2 = b - L / 4

        f_x1 = f(x1)
        f_x2 = f(x2)
        f_xsr = f(xsr)
        xsrs_min.append(xsr)

        if f_x1 < f_xsr:
            b = xsr
            xsr = x1
        elif f_x2 < f_xsr:
            a = xsr
            xsr = x2
        else:
            a = x1
            b = x2

        L = b - a

    return xsr, f(xsr), i, xsrs_min


def maksimum(a, b, fx, e):
    xsr = (a + b) / 2
    L = b - a
    i = 0
    xsrs_max = []

    while L > e:
        i += 1
        x1 = a + L / 4
        x2 = b - L / 4

        f_x1 = f(x1)
        f_x2 = f(x2)
        f_xsr = f(xsr)
        xsrs_max.append(xsr)

        if f_x2 > f_xsr:
            a = xsr
            xsr = x2
        elif f_x2 > f_xsr:
            a = xsr
            xsr = x2
        else:
            a = x1
            b = x2

        L = b - a

    return xsr, f(xsr), i, xsrs_max


a = 0.1
b = 4
e = 0.001

minimum_x, minimum_y, i_min, xsrs_min = minimum(a, b, f, e)
maksimum_x, maksimum_y, i_max, xsrs_max = maksimum(a, b, f, e)

print(f"Minimum: x = {minimum_x}, f(x) = {minimum_y}, {i_min} iteracji, {xsrs_min}")
print(f"Maksimum: x = {maksimum_x}, f(x) = {maksimum_y}, {i_max} iteracji, {xsrs_max}")

x = np.linspace(a, b, 100)
plt.plot(x, f(x), color='red')
plt.scatter([minimum_x], [minimum_y], color='lightskyblue', label='Minimum', s=100)
plt.scatter([maksimum_x], [maksimum_y], color='lime', label='Maksimum', s=100)

for xsr_min in xsrs_min:
    plt.scatter([xsr_min], [f(xsr_min)], color='blue', s=20)

for xsr_max in xsrs_max:
    plt.scatter([xsr_max], [f(xsr_max)], color='green', s=20)

plt.legend()
plt.grid(True)
plt.title("Metoda dwudzielna")
plt.show()
