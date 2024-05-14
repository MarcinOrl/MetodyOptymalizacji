import numpy as np
import matplotlib.pyplot as plt

# Parametry początkowe z przykładu
x_B = np.array([-0.5, 1])  # Punkt bazowy
xi = np.array([[1, 0], [0, 1]])  # Baza wektorów ortogonalnych
e = 0.5  # Początkowa długość kroku
beta = 0.5  # Współczynnik zmniejszenia kroku
epsilon = 0.0001  # Dokładność obliczeń
n = 2  # Liczba zmiennych niezależnych

# Definicja funkcji celu z przykładu
def f(x):
    x1, x2 = x
    #return 2.5 * (x1**2 - x2)**2 + (1 - x1)**2
    return x2 * x2 * x2 + 3 * x1 * x1 - x1 * x2 - 2 * x1 + 5

# Implementacja metody Hooke’a-Jeevesa
def hooke_jeeves(x_B, e, beta, epsilon, f):
    def trial_step(x, e, xi):
        for j in range(n):
            f_x = f(x)
            x_trial = x + e * xi[j]
            f_trial = f(x_trial)
            if f_trial < f_x:
                x = x_trial
            else:
                x_trial = x - e * xi[j]
                f_trial = f(x_trial)
                if f_trial < f_x:
                    x = x_trial
        return x

    x_B0 = x_B.copy()  # Punkt bazowy z poprzedniej iteracji
    x = x_B.copy()  # Punkt startowy
    path = [x.copy()]  # Ścieżka do wizualizacji

    while e > epsilon:
        x_new = trial_step(x, e, xi)
        if f(x_new) < f(x):
            x_B0 = x_B.copy()
            x_B = x_new.copy()
            x = 2 * x_B - x_B0  # Krok roboczy
        else:
            e = beta * e
            x = x_B.copy()
        path.append(x.copy())
    return x, path

# Wywołanie metody Hooke’a-Jeevesa
ext, path = hooke_jeeves(x_B, e, beta, epsilon, f)
ext_rounded = np.round(ext, 8)

# Wizualizacja
path = np.array(path)
plt.figure(figsize=(8, 6))
x_range = np.linspace(-1, 2, 400)
y_range = np.linspace(-1, 2, 400)
X, Y = np.meshgrid(x_range, y_range)
Z = f([X, Y])
plt.contour(X, Y, Z, levels=50)
plt.plot(path[:, 0], path[:, 1], 'o-', color='blue', label='Ścieżka iteracji')
plt.plot(ext[0], ext[1], 'ro', label='Punkt ekstremum')
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Metoda Hooke’a-Jeevesa')
plt.legend()
plt.grid(True)
plt.show()

# Wyniki
print(f"Znalezione minimum: {ext_rounded}")
