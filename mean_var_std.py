import numpy as np


def calculate(digits):
    try:
        matrix = np.array(digits).reshape(3, 3)
    except ValueError:
        raise ValueError("List must contain nine numbers.")

    calculations = {
        "mean": [list(matrix.mean(axis=0)), list(matrix.mean(axis=1)), matrix.mean()],
        "variance": [list(matrix.var(axis=0)), list(matrix.var(axis=1)), matrix.var()],
        "standard deviation": [list(matrix.std(axis=0)), list(matrix.std(axis=1)), matrix.std()],
        "min": [list(matrix.min(axis=0)), list(matrix.min(axis=1)), matrix.min()],
        "max": [list(matrix.max(axis=0)), list(matrix.max(axis=1)), matrix.max()],
        "sum": [list(matrix.sum(axis=0)), list(matrix.sum(axis=1)), matrix.sum()]
    }

    return calculations
