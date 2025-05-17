import numpy as np
import os
from datetime import datetime
import matplotlib.pyplot as plt
from .compute_matrix_rank import compute_matrix_rank
from .visualize_matrix import visualize_matrix
from .visualize_eigenvalues import visualize_eigenvalues
from .create_custom_colormap import create_custom_colormap
from .display_matrix_blocks import display_matrix_blocks
from .save_matrix_to_file import save_matrix_to_file


def save_vector_to_file(vector, description, filename):
    """
    Сохраняет вектор (например, собственные числа) в текстовый файл
    
    Параметры:
        vector - вектор для сохранения
        description - описание вектора
        filename - имя файла
    """
    with open(filename, 'w') as f:
        f.write(f'{description}\n')
        f.write('===========================================\n\n')
        
        for i, val in enumerate(vector):
            f.write(f'Значение {i+1}: {val:.10f}\n')
    
    print(f'Вектор сохранен в файл: {filename}')


def analyze_and_save_eigenvalues(matrix, matrix_name, output_file):
    """
    Анализирует собственные числа матрицы
    
    Параметры:
        matrix - анализируемая матрица
        matrix_name - имя матрицы для отчета
        output_file - имя файла для сохранения результатов
        
    Возвращает:
        result - словарь с результатами анализа
    """
    # Вычисление собственных чисел и векторов
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    # Сортировка собственных чисел по убыванию
    idx = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[idx]
    sorted_eigenvectors = eigenvectors[:, idx]
    
    # Вычисление ранга матрицы
    matrix_rank = compute_matrix_rank(matrix)
    
    # Сохранение в файл
    with open(output_file, 'w') as f:
        f.write(f'АНАЛИЗ СОБСТВЕННЫХ ЧИСЕЛ МАТРИЦЫ {matrix_name}\n')
        f.write('===========================================\n\n')
        f.write(f'Дата создания: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        
        f.write(f'РАЗМЕР МАТРИЦЫ: {matrix.shape[0]} x {matrix.shape[1]}\n\n')
        f.write(f'РАНГ МАТРИЦЫ: {matrix_rank}\n\n')
        
        f.write('СОБСТВЕННЫЕ ЧИСЛА (отсортированы по убыванию):\n')
        for i, val in enumerate(sorted_eigenvalues):
            f.write(f'  λ{i+1} = {val:.10f}\n')
    
    print(f'Анализ собственных чисел сохранен в файл: {output_file}')
    
    # Возвращаем собственные числа, векторы и ранг
    result = {
        'eigenvalues': sorted_eigenvalues,
        'eigenvectors': sorted_eigenvectors,
        'rank': matrix_rank
    }
    
    # Сохраняем также в NPZ файл
    npz_file = output_file.replace('.txt', '.npz')
    np.savez(npz_file, **result)
    
    return result


def compute_characteristic_polynomial(matrix):
    """
    Вычисляет характеристический многочлен матрицы
    
    Параметры:
        matrix - квадратная матрица для анализа
        
    Возвращает:
        poly_coeffs - коэффициенты характеристического многочлена
    """
    # Проверяем, является ли матрица квадратной
    m, n = matrix.shape
    if m != n:
        raise ValueError('Матрица должна быть квадратной для вычисления характеристического многочлена')
    
    # Вычисляем собственные числа
    eigenvalues = np.linalg.eigvals(matrix)
    
    # Вычисляем коэффициенты характеристического многочлена
    # Используем np.poly для вычисления через собственные числа
    poly_coeffs = np.poly(eigenvalues)
    
    return poly_coeffs


def save_characteristic_polynomial(matrix, matrix_name, filename):
    """
    Вычисляет и сохраняет характеристический многочлен
    
    Параметры:
        matrix - квадратная матрица
        matrix_name - имя матрицы для отчета
        filename - имя файла для сохранения результатов
    """
    # Проверяем, является ли матрица квадратной
    m, n = matrix.shape
    if m != n:
        raise ValueError('Матрица должна быть квадратной для вычисления характеристического многочлена')
    
    # Вычисляем характеристический многочлен
    poly_coeffs = compute_characteristic_polynomial(matrix)
    
    # Получаем степень многочлена (размер матрицы)
    n = len(poly_coeffs) - 1
    
    # Сохраняем в файл
    try:
        with open(filename, 'w') as f:
            f.write(f'ХАРАКТЕРИСТИЧЕСКИЙ МНОГОЧЛЕН МАТРИЦЫ {matrix_name}\n')
            f.write('===========================================\n\n')
            f.write(f'Дата создания: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
            f.write(f'Размер матрицы: {m} x {n}\n\n')
            
            # Выводим многочлен в читаемом виде
            f.write('Характеристический многочлен det(λI - A):\n')
            
            # Формируем строку многочлена для отображения
            poly_str = ''
            for i in range(n+1):
                coef = poly_coeffs[i]
                power = n - i
                
                # Пропускаем нулевые коэффициенты, кроме свободного члена, если он - единственный
                if abs(coef) < 1e-10 and (power > 0 or i < n):
                    continue
                
                # Определяем знак для отображения
                if i == 0:
                    sign_str = ''  # Первый коэффициент без знака
                elif coef > 0:
                    sign_str = ' + '
                else:
                    sign_str = ' - '
                    coef = abs(coef)  # Используем модуль, так как знак уже в строке
                
                # Формируем член многочлена
                if power == 0:
                    term = f'{coef:.10g}'  # Свободный член
                elif power == 1:
                    if abs(coef - 1) < 1e-10:
                        term = 'λ'  # Коэффициент 1 при λ не пишем
                    else:
                        term = f'{coef:.10g}*λ'
                else:
                    if abs(coef - 1) < 1e-10:
                        term = f'λ^{power}'  # Коэффициент 1 не пишем
                    else:
                        term = f'{coef:.10g}*λ^{power}'
                
                poly_str += sign_str + term
            
            f.write(f'{poly_str}\n\n')
            
            # Выводим коэффициенты в виде массива для удобства использования
            f.write('Коэффициенты многочлена (в порядке убывания степеней):\n[')
            coef_strings = [f'{c:.15g}' for c in poly_coeffs]
            f.write(', '.join(coef_strings))
            f.write(']\n')
        
        print(f'Характеристический многочлен сохранен в файл: {filename}')
        
        # Также сохраняем коэффициенты в NPZ-файл
        npz_filename = filename.replace('.txt', '.npz')
        try:
            np.savez(npz_filename, poly_coeffs=poly_coeffs)
            print(f'Коэффициенты многочлена сохранены в файл: {npz_filename}')
        except Exception as e:
            print(f'Не удалось сохранить коэффициенты в NPZ-файл: {str(e)}')
    except Exception as e:
        print(f'Ошибка при сохранении характеристического многочлена: {str(e)}')
