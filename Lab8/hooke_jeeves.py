import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

f = lambda x_1, x_2: x_2 * x_2 * x_2 + 3 * x_1 * x_1 - x_1 * x_2 - 2 * x_1 + 5
x0 = [1, 1]
e = 0.5
beta = 0.5
epsilon = 0.01
n = 2

def hooke_jeeves(x0, n, e, beta, epsilon, max_iter=100):
    x_base = np.array(x0)
    x_new = x_base.copy()
    xi = np.eye(n)
    path = [x_base.copy()]

    for _ in range(max_iter):
        x_before = x_new.copy()
        improved = False

        # Exploratory move
        for j in range(n):
            for sign in [1, -1]:
                x_trial = x_new + sign * e * xi[j]
                if f(*x_trial) < f(*x_new):
                    x_new = x_trial
                    improved = True
                    break
            if improved:
                break

        if improved:
            # Pattern move
            x_step = 2 * x_new - x_base
            if f(*x_step) < f(*x_base):
                x_base = x_new
                x_new = x_step
            else:
                x_base = x_new
        else:
            e *= beta

        path.append(x_new.copy())

        if e < epsilon:
            break

    return x_new, path

opt_point, path = hooke_jeeves(x0, n, e, beta, epsilon)
path = np.array(path)

print("Optymalny punkt:", opt_point)
print("Wartość funkcji w punkcie optymalnym:", f(*opt_point))

# Wizualizacja
x = np.linspace(0.2, 1.1, 400)
y = np.linspace(-0.2, 1.4, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

plt.figure(figsize=(8, 6))
plt.contour(X, Y, Z, levels=10)

# Gradually change colors along the path
colors = cm.viridis(np.linspace(0, 1.5, len(path)))
for i in range(len(path)-1):
    plt.plot(path[i:i+2, 0], path[i:i+2, 1], 'o--', color=colors[i], label='Ścieżka optymalizacji' if i == 0 else "")

plt.scatter([opt_point[0]], [opt_point[1]], c='red', marker='o', label='Optymalny punkt', zorder=2)
plt.title('Metoda Hooke’a-Jeevesa')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
