import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def function(x, y):
    # return y * y * y + 3 * x * x - x * y - 2 * x + 5
    return 2.5 * (x**2 - y) ** 2 + (1 - x) ** 2


xb = xb0 = x0 = [-0.5, 1]
wo1 = np.array([1, 0])
wo2 = np.array([0, 1])
e = 0.5
beta = 0.5
n = 2
epsilon = 0.00001


def hooke_jeeves(x0, xb, e, wo1, wo2, n, epsilon, beta):
    iter = 0
    path = [x0.copy()]

    while True:
        j = 1
        f0 = function(x0[0], x0[1])
        fb = function(xb[0], xb[1])

        x_next = x0 + e * wo1
        f = function(x_next[0], x_next[1])

        if f < f0:
            f0 = f
        else:
            x_next = x_next - 2 * e * wo1
            f = function((x_next[0]), x_next[1])

            if f < f0:
                f0 = f
            else:
                x_next = x_next + e * wo1

        if j != n:
            j += 1

            x_next = x_next + e * wo2
            f = function((x_next[0]), x_next[1])

            if f < f0:
                f0 = f
            else:
                x_next = x_next - 2 * e * wo2
                f = function((x_next[0]), x_next[1])

                if f < f0:
                    f0 = f
                else:
                    x_next = x_next + e * wo2

            if fb > f0:
                xb0 = xb
                xb = x_next
                x0 = 2 * xb - xb0
                print(x0)
            elif e > epsilon:
                e = beta * e
                x0 = xb

        path.append(x_next.copy())
        iter += 1

        if e < epsilon:
            return x_next[0], x_next[1], iter, path


x, y, iterations, path = hooke_jeeves(x0, xb, e, wo1, wo2, n, epsilon, beta)
path = np.array(path)

print(f"Optymalny punkt:, [{x}, {y}], znaleziony w {iterations} iteracjach.")
print("Wartość funkcji w punkcie optymalnym:", function(x, y))

# Wizualizacja
plt.figure(figsize=(8, 6))

# Gradually change colors along the path
colors = cm.viridis(np.linspace(0, 1.5, len(path)))
for i in range(len(path) - 1):
    plt.plot(
        path[i : i + 2, 0],
        path[i : i + 2, 1],
        "o--",
        color=colors[i],
        label="Ścieżka optymalizacji" if i == 0 else "",
    )

plt.scatter(
    [x],
    [y],
    c="red",
    marker="o",
    label="Optymalny punkt",
    zorder=2,
)
plt.title("Metoda Hooke’a-Jeevesa")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
