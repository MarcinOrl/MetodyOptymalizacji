import numpy as np
import matplotlib.pyplot as plt

# Parametry początkowe
x0 = 1.0059
y0 = 1.78978
epsilon = 0.00001
h = 0.00001


# Definicja funkcji i pochodnych
def f(x, y):
    return y * y * y + 3 * x * x - x * y - 2 * x + 5


def df_dx(x, y):
    return (f(x + h, y) - f(x, y)) / h


def df_dy(x, y):
    return (f(x, y + h) - f(x, y)) / h


def gradient(x, y):
    return np.array([df_dx(x, y), df_dy(x, y)])


# Metoda stycznych Newtona do znajdowania miejsca zerowego pochodnych
def stycznych_zero(df, start):
    x = start
    while True:
        dfd = df(x)
        d2fd = (df(x + h) - df(x)) / h
        x_new = x - dfd / d2fd
        if abs(df(x_new)) <= epsilon or abs(x_new - x) <= epsilon:
            #print('x_new: ', x_new, 'x: ', x, 'abs: ', abs(x_new - x), 'abs df: ', abs(df(x_new)))
            x = x_new
            break
        x = x_new
    return x


# Implementacja metody Gaussa-Seidla
def gauss_seidel_method(x0, y0, epsilon):
    iter = 0
    x, y = x0, y0
    xs = [x]
    ys = [y]
    while True:
        iter += 1
        x_new = stycznych_zero(lambda xi: df_dx(xi, y), x)
        y_new = stycznych_zero(lambda yi: df_dy(x_new, yi), y)
        xs.append(x_new)
        ys.append(y_new)
        if abs(x_new - x) <= epsilon and abs(y_new - y) <= epsilon:
            x, y = x_new, y_new
            break
        x, y = x_new, y_new
    return (x, y), xs, ys, iter


# Wywołanie metody Gaussa-Seidla
ext, xs, ys, iterations = gauss_seidel_method(x0, y0, epsilon)

ext_rounded = np.round(ext, 8)

print(f"Ekstremum w punkcie: {ext_rounded}, znalezione w {iterations} iteracjach.")

# Wizualizacja
x = np.linspace(0, 2, 400)
y = np.linspace(0, 2, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.figure(figsize=(8, 6))
plt.contour(X, Y, Z, levels=20)
plt.plot(xs, ys, color='blue', label='Ścieżka iteracji', marker='o')
plt.scatter(ext[0], ext[1], color='red', s=60, label='Punkt ekstremum', zorder=2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Metoda Gaussa-Seidla')
plt.legend()
plt.grid(True)
plt.show()
