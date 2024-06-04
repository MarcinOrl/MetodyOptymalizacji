import numpy as np
import matplotlib.pyplot as plt

x0 = 1
y0 = 1
epsilon = 0.00001
h = 0.00001

# Definicja funkcji
def f(x, y):
    # return 10 * x ** 2 + 12 * x * y + 10 * y ** 2
    return y * y * y + 3 * x * x - x * y - 2 * x + 5


# Numeryczne obliczanie pochodnych
def df_dx(x, y):
    return (f(x + h, y) - f(x, y)) / h


def df_dy(x, y):
    return (f(x, y + h) - f(x, y)) / h


def d2f_dx2(x, y):
    return (f(x + 2 * h, y) - 2 * f(x + h, y) + f(x, y)) / (h ** 2)


def d2f_dy2(x, y):
    return (f(x, y + 2 * h) - 2 * f(x, y + h) + f(x, y)) / (h ** 2)


def d2f_dxdy(x, y):
    return (f(x + h, y + h) - f(x + h, y) - f(x, y + h) + f(x, y)) / (h ** 2)


def gradient(x, y):
    return np.array([df_dx(x, y), df_dy(x, y)])


def hessian(x, y):
    return np.array([[d2f_dx2(x, y), d2f_dxdy(x, y)], [d2f_dxdy(x, y), d2f_dy2(x, y)]])


def inv_hessian(x, y):
    h = hessian(x, y)
    a, b = h[0, 0], h[0, 1]
    c, d = h[1, 0], h[1, 1]
    det = a * d - b * c
    inv_h = 1 / det * np.array([[d, -b], [-c, a]])
    return inv_h


# Implementacja metody Newtona
def newton_method(x0, y0, epsilon):
    iter = 0
    xyk = np.array([x0, y0])
    xs = [xyk[0]]
    ys = [xyk[1]]
    while True:
        iter += 1
        grad = gradient(xyk[0], xyk[1])
        h_inv = inv_hessian(xyk[0], xyk[1])
        xyk1 = xyk - np.array(
            [h_inv[0, 0] * grad[0] + h_inv[0, 1] * grad[1], h_inv[1, 0] * grad[0] + h_inv[1, 1] * grad[1]])

        # Zapisywanie punktów
        xs.append(xyk1[0])
        ys.append(xyk1[1])

        # Warunek stopu
        if abs(xyk1[0] - xyk[0]) <= epsilon and abs(xyk1[1] - xyk[1]) <= epsilon:
            xyk = xyk1
            break

        xyk = xyk1

    return xyk, iter, xs, ys


# Wywołanie metody Newtona
ext, iterations, xs, ys = newton_method(x0, y0, epsilon)

ext_rounded = np.round(ext, 8)

print(f"Ekstremum w punkcie: {ext_rounded}, znalezione w {iterations} iteracjach.")

# Wygenerowanie wykresu funkcji
x = np.linspace(0, 1.5, 400)
y = np.linspace(0, 1.5, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.figure(figsize=(8, 6))
plt.contour(X, Y, Z, levels=20)
plt.scatter(xs, ys, color='blue', s=20, label='Punkty z każdej iteracji')
plt.scatter(ext[0], ext[1], color='red', label='Ekstremum')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Metoda Newtona')
plt.legend()
plt.grid(True)
plt.show()
