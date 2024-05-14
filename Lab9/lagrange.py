import sympy as sp


def lagrange_multiplier(f, constraints, variables):
    # Tworzenie mnożników Lagrange'a
    lambdas = sp.symbols('lambda1:%d' % (len(constraints) + 1))
    L = f  # Funkcja Lagrange'a zaczyna się od funkcji celu

    # Dodawanie ograniczeń z mnożnikami do funkcji Lagrange'a
    for lam, h in zip(lambdas, constraints):
        L += lam * h

    # Wyznaczanie pochodnych względem wszystkich zmiennych i mnożników
    grad = [sp.diff(L, var) for var in variables + list(lambdas)]

    # Rozwiązywanie równań: pochodne ustawione na 0
    solutions = sp.solve(grad, variables + list(lambdas), dict=True)

    return solutions


# Przykład: prostopadłościan o maksymalnej objętości
x, y, h = sp.symbols('x y h')
f = x * y * h  # funkcja celu: objętość prostopadłościanu
constraint = x + y + h - 6  # ograniczenie z drutu

# Rozwiązanie
results = lagrange_multiplier(f, [constraint], [x, y, h])

# Filtrowanie wyników dla dodatnich wartości x, y, h
valid_results = [res for res in results if all(res[var] > 0 for var in [x, y, h])]
print(valid_results)
