import numpy as np


def compute_matrix_rank(matrix, tolerance=1e-10):
    """
    Вычисляет ранг матрицы
    
    Параметры:
        matrix - матрица для анализа
        tolerance - порог для определения значимых собственных чисел
        
    Возвращает:
        matrix_rank - ранг матрицы
    """
    # Используем SVD для вычисления ранга
    s = np.linalg.svd(matrix, compute_uv=False)
    matrix_rank = np.sum(s > tolerance)
    return matrix_rank
