import numpy as np


def simplex(c, A, b, signs, maximize=True):
    n_vars = len(c)
    n_constraints = len(b)

    # Inicjalizacja tablicy
    tableau = np.zeros((n_constraints + 1, n_vars + n_constraints + 1))

    # Wypełnienie tablicy ograniczeniami
    for i in range(n_constraints):
        tableau[i, :n_vars] = A[i]
        if signs[i] == "<=":
            tableau[i, n_vars + i] = 1

        elif signs[i] == ">=":
            tableau[i, n_vars + i] = -1
        else:
            raise ValueError("Nieprawidłowy znak ograniczenia. Użyj '<=' lub '>='.")

    # Ustawienie wartości po prawej stronie (RHS)
    tableau[:-1, -1] = b

    # Ustawienie funkcji celu w tablicy
    if maximize:
        tableau[-1, :n_vars] = -c

    else:
        tableau[-1, :n_vars] = c

    # Główna pętla algorytmu simpleks
    while np.any(tableau[-1, :-1] < 0):
        pivot_col = np.argmin(tableau[-1, :-1])  # Znalezienie kolumny pivot
        if np.all(tableau[:-1, pivot_col] <= 0):

            raise Exception("Program liniowy jest nieograniczony.")

        # Obliczenie ilorazów do wyboru wiersza pivot
        ratios = np.divide(
            tableau[:-1, -1],
            tableau[:-1, pivot_col],
            out=np.full_like(tableau[:-1, -1], np.inf),
            where=tableau[:-1, pivot_col] > 0,
        )
        pivot_row = np.argmin(ratios)  # Znalezienie wiersza pivot

        # Wykonanie operacji pivot
        tableau[pivot_row, :] /= tableau[pivot_row, pivot_col]
        for row in range(len(tableau)):
            if row != pivot_row:
                tableau[row, :] -= tableau[row, pivot_col] * tableau[pivot_row, :]

    # Ekstrakcja rozwiązania
    solution = np.zeros(n_vars)
    for i in range(n_vars):
        if (
            np.sum(tableau[:, i] == 1) == 1
            and np.sum(tableau[:, i] == 0) == len(tableau) - 1
        ):
            row = np.where(tableau[:, i] == 1)[0][0]
            solution[i] = tableau[row, -1]

    # Pobranie wartości funkcji
    sol_value = tableau[-1, -1]
    if not maximize:
        sol_value = -sol_value

    return solution, sol_value


# Przykład 1: Rozwiązanie [2, 8], Wartość funkcji 18
c = np.array([1, 2])
A = np.array([[1, 1], [-2, 1]])
b = np.array([10, 4])
constraint_signs = ["<=", "<="]

# Odkomentuj, aby przetestować inne przykłady

# Przykład 2: Rozwiązanie [0, 2], Wartość funkcji 10
# c = np.array([2, 5])
# A = np.array([[2, 1], [1, 2]])
# b = np.array([5, 4])
# constraint_signs = ['<=', '<=']

# Przykład 3: Rozwiązanie [4, 8], Wartość funkcji 400
# c = np.array([40, 30])
# A = np.array([[1, 1], [2, 1]])
# b = np.array([12, 16])
# constraint_signs = ['<=', '<=']

solution, sol_value = simplex(c, A, b, constraint_signs, maximize=True)
print("Rozwiązanie:", solution)
print("Wartość funkcji w punkcie:", sol_value)
