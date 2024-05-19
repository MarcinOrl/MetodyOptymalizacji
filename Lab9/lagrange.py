import sympy as sp

def lagrange_method(f, constraints, variables):
    # Definiowanie mnożników Lagrange'a
    lambdas = sp.symbols(f'lambda1:{len(constraints)+1}')
    
    # Definiowanie funkcji Lagrange'a
    L = f + sum(lambdas[i] * constraints[i] for i in range(len(constraints)))

    # Obliczanie pochodnych cząstkowych
    derivatives = [sp.diff(L, var) for var in variables] + constraints

    # Rozwiązywanie układu równań
    solutions = sp.solve(derivatives, variables + list(lambdas), dict=True)
    
    return solutions

def print_solution(solution):
    for sol in solution:
        for var, val in sol.items():
            print(f"{var} = {val.evalf(n=1)}")
        print()

# Przykład 1
x1, x2 = sp.symbols('x1 x2')
f1 = x1**2 + x2**2
constraint1 = [2*x1 + x2 - 2]
variables1 = [x1, x2]

solution1 = lagrange_method(f1, constraint1, variables1)
print("Przykład 1:")
print_solution(solution1)

# Przykład 2
x, y, h = sp.symbols('x y h')
f2 = x * y * h
constraint2 = [6 - x - y - h]
variables2 = [x, y, h]

solution2 = lagrange_method(f2, constraint2, variables2)
print("Przykład 2:")
print_solution(solution2)
