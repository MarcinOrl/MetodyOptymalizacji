import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def lagrange_method(f, constraints, variables):
    # Mnożniki Lagrange'a
    lambdas = sp.symbols(f'lambda1:{len(constraints) + 1}')

    # Funkcja Lagrange'a
    L = f + sum(lambdas[i] * constraints[i] for i in range(len(constraints)))

    # Pochodne cząstkowe
    derivatives = [sp.diff(L, i) for i in variables] + constraints

    # Układ równań
    result = sp.solve(derivatives, variables + list(lambdas), dict=True)

    return result

def print_solution(solution):
    for sol in solution:
        for var, val in sol.items():
            print(f"{var} = {val.evalf(n=1)}")
        print()

# Przykład 1
x1, x2 = sp.symbols('x1 x2')
f1 = x1 ** 2 + x2 ** 2
constraint1 = [2 * x1 + x2 - 2]
variables1 = [x1, x2]

solution1 = lagrange_method(f1, constraint1, variables1)
print("Przykład 1:")
print_solution(solution1)

# Wartości rozwiązania
ext = {var: sol[var].evalf() for sol in solution1 for var in variables1}

# Wizualizacja
x_vals = np.linspace(-2, 2, 400)
y_vals = np.linspace(-2, 2, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = X**2 + Y**2

constraint_f = lambda x1, x2: 2 * x1 + x2 - 2

plt.figure(figsize=(6, 6))
plt.contour(X, Y, Z, levels=10)
plt.contour(X, Y, constraint_f(X, Y), levels=[0], colors='red')
plt.scatter([ext[x1]], [ext[x2]], color='red')

plt.title('Metoda Mnożników Lagrange\'a')
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.grid(True)
plt.show()

#Przykład 2
x, y, h = sp.symbols('x y h')
f2 = x * y * h
constraint2 = [6 - x - y - h]
variables2 = [x, y, h]

solution2 = lagrange_method(f2, constraint2, variables2)
print("Przykład 2:")
print_solution(solution2)