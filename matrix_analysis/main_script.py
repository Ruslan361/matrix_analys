import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Импорт собственных функций
from build_L_matrix import build_L_matrix
from visualize_matrix import visualize_matrix
from visualize_eigenvalues import visualize_eigenvalues
from display_matrix_blocks import display_matrix_blocks
from compute_matrix_rank import compute_matrix_rank
from create_custom_colormap import create_custom_colormap
from matrix_analysis_functions import save_characteristic_polynomial


def main():
    """
    Основной скрипт для построения и визуализации матрицы L
    """
    # Определение переменных
    n_1 = 1
    n1 = 2
    n2 = 3
    n3 = 4
    n4 = 5

    # Вызов функции построения матрицы L
    L, block_coords = build_L_matrix(n_1, n1, n2, n3, n4)

    # Настройка визуализации
    d_limits = {
        'x_top': L.shape[1],
        'x_bottom': 0,
        'y_top': L.shape[0],
        'y_bottom': 0
    }

    # Сохранение матрицы L в отдельный файл
    # Используем альтернативный метод из-за проблем с правами доступа
    try:
        # Сначала пробуем текстовый формат, который должен работать
        L_txt_filename = 'matrix_L.txt'
        with open(L_txt_filename, 'w') as f:
            f.write(f'# Матрица L размера {L.shape[0]}x{L.shape[1]}\n')
            for i in range(L.shape[0]):
                for j in range(L.shape[1]):
                    f.write(f'{L[i,j]:8.4f} ')
                f.write('\n')
        print(f'Матрица L сохранена в текстовый файл: {L_txt_filename}')
    except Exception as e:
        print(f'Ошибка при сохранении матрицы L: {str(e)}')

    # Визуализация матрицы L с выделенными блоками
    plt.figure(figsize=(10, 10))

    # Отрисовка матрицы
    plt.imshow(L)
    plt.colorbar(cmap=create_custom_colormap())

    # Устанавливаем равные пропорции осей
    plt.axis('equal')

    # Устанавливаем границы осей, чтобы каждый элемент занимал ровно 1 пиксель
    plt.xlim(0.5, L.shape[1] + 0.5)
    plt.ylim(0.5, L.shape[0] + 0.5)

    # Исправляем направление оси Y
    plt.gca().invert_yaxis()  # Переворачиваем ось Y, чтобы строки шли сверху вниз

    # Применение пользовательской цветовой схемы
    plt.imshow(L, cmap=create_custom_colormap())
    plt.colorbar()
    plt.clim(-1, 1)

    # Добавление прямоугольных областей для выделения блоков
    display_matrix_blocks(L, block_coords)

    # Настройка заголовка и меток осей
    plt.title('Матрица L с выделенными блоками', fontsize=14)
    plt.xlabel('Столбцы (j)', fontsize=12)
    plt.ylabel('Строки (i)', fontsize=12)

    # Настройка внешнего вида графика
    plt.grid(False)
    plt.box(True)

    # Сохранение изображения
    plt.savefig('heatmap.png', dpi=300)
    plt.close()

    # Вычисление и визуализация матрицы L*L^T
    Lt = L.T
    L_LT = L @ Lt

    # Сохранение матрицы L*L^T в текстовый файл
    try:
        L_LT_txt_filename = 'matrix_L_LT.txt'
        with open(L_LT_txt_filename, 'w') as f:
            f.write(f'# Матрица L*L^T размера {L_LT.shape[0]}x{L_LT.shape[1]}\n')
            for i in range(L_LT.shape[0]):
                for j in range(L_LT.shape[1]):
                    f.write(f'{L_LT[i,j]:12.6f} ')
                f.write('\n')
        print(f'Матрица L*L^T сохранена в текстовый файл: {L_LT_txt_filename}')
    except Exception as e:
        print(f'Ошибка при сохранении матрицы L*L^T: {str(e)}')

    # Визуализация матрицы L*L^T с отображением максимального значения
    visualize_matrix(L_LT, 'Матрица L * L^T', create_custom_colormap, 'L_LT_heatmap.png', True)

    # Анализ собственных чисел матрицы L*L^T
    # Вычисление собственных чисел
    eigenvalues_LLT, V_LLT = np.linalg.eig(L_LT)
    sorted_idx = np.argsort(eigenvalues_LLT)[::-1]
    sorted_eigenvalues = eigenvalues_LLT[sorted_idx]
    sorted_eigenvectors = V_LLT[:, sorted_idx]

    # Вычисление ранга матрицы
    matrix_rank = compute_matrix_rank(L_LT)
    matrix_rank_L = compute_matrix_rank(L)

    # Сохранение в текстовый файл
    try:
        eigen_filename = 'eigenvalues_L_LT.txt'
        with open(eigen_filename, 'w') as f:
            f.write('АНАЛИЗ СОБСТВЕННЫХ ЧИСЕЛ МАТРИЦЫ L*L^T\n')
            f.write('===========================================\n\n')
            f.write(f'Дата создания: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
            f.write(f'РАЗМЕР МАТРИЦЫ: {L_LT.shape[0]} x {L_LT.shape[1]}\n\n')
            f.write(f'РАНГ МАТРИЦЫ: {matrix_rank}\n\n')
            f.write('СОБСТВЕННЫЕ ЧИСЛА (отсортированы по убыванию):\n')
            f.write('========================================================\n\n')

            for i, val in enumerate(sorted_eigenvalues):
                f.write(f'  λ{i+1} = {val:.15g}\n')

        print(f'Анализ собственных чисел сохранен в файл: {eigen_filename}')
    except Exception as e:
        print(f'Ошибка при сохранении собственных чисел: {str(e)}')

    # Визуализация собственных чисел
    visualize_eigenvalues(sorted_eigenvalues, 'Собственные числа матрицы L*L^T', 'eigenvalues_L_LT.png')

    # Вычисление и сохранение характеристического многочлена
    try:
        # Вычисляем и сохраняем характеристический многочлен
        save_characteristic_polynomial(L_LT, 'L*L^T', 'characteristic_polynomial.txt')
    except Exception as e:
        print(f'Ошибка при вычислении характеристического многочлена: {str(e)}')
        # Альтернативный метод, если основной не сработал
        try:
            poly_coeffs = np.poly(eigenvalues_LLT)

            with open('characteristic_polynomial_simple.txt', 'w') as f:
                f.write('КОЭФФИЦИЕНТЫ ХАРАКТЕРИСТИЧЕСКОГО МНОГОЧЛЕНА МАТРИЦЫ L*L^T\n')
                f.write('========================================================\n\n')
                f.write('Коэффициенты в порядке убывания степеней:\n')

                for i, coef in enumerate(poly_coeffs):
                    f.write(f'a{len(poly_coeffs)-i-1} = {coef:.15g}\n')

            print('Упрощенный характеристический многочлен сохранен в файл: characteristic_polynomial_simple.txt')
        except Exception as e2:
            print(f'Не удалось сохранить даже упрощенную версию многочлена: {str(e2)}')

    # Сохранение ранга в отдельный файл
    try:
        rank_filename = 'matrix_rank.txt'
        with open(rank_filename, 'w') as f:
            f.write('АНАЛИЗ РАНГА МАТРИЦ\n')
            f.write('===========================================\n\n')
            f.write(f'Дата создания: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
            f.write(f'Размер матрицы L: {L.shape[0]} x {L.shape[1]}\n')
            f.write(f'Размер матрицы L*L^T: {L_LT.shape[0]} x {L_LT.shape[1]}\n\n')
            f.write(f'Ранг матрицы L*L^T: {matrix_rank}\n')
            f.write('\nПояснение: ранг матрицы - это количество линейно независимых строк или столбцов.\n')
            f.write('Для симметричной матрицы L*L^T ранг равен количеству ненулевых собственных чисел.\n')
            f.write('===========================================\n\n')
            f.write('Ранг L:\n')
            f.write(f'  {matrix_rank_L}\n\n')
        print(f'Информация о ранге сохранена в файл: {rank_filename}')
    except Exception as e:
        print(f'Ошибка при сохранении информации о ранге: {str(e)}')

    # Вывод информации о собственных числах и их значении
    print('\nПояснение к функции eig():\n')
    print('[eigenvalues, eigenvectors] = np.linalg.eig(A) возвращает два массива:')
    print('- eigenvalues - массив собственных чисел матрицы A')
    print('- eigenvectors - матрица, столбцы которой являются собственными векторами, соответствующими этим собственным числам\n')

    print('Собственные числа показывают, как матрица растягивает пространство вдоль различных направлений.')
    print('Собственные векторы показывают эти направления.\n')

    print('Для симметричной матрицы (такой как L*L^T):')
    print('- собственные числа всегда действительны (без мнимой части)')
    print('- собственные векторы ортогональны друг другу\n')

    print('Характеристический многочлен матрицы A - это det(λI - A), где:')
    print('- λ - переменная многочлена')
    print('- I - единичная матрица того же размера, что и A')
    print('- det - определитель матрицы\n')

    print('Корни характеристического многочлена - это собственные числа матрицы.\n')

    print('Всего создано файлов с результатами анализа:')
    print('  - matrix_L.txt - матрица L в текстовом формате')
    print('  - matrix_L_LT.txt - матрица L*L^T в текстовом формате')
    print('  - eigenvalues_L_LT.txt - собственные числа матрицы L*L^T')
    print('  - characteristic_polynomial.txt - характеристический многочлен')
    print('  - matrix_rank.txt - информация о ранге матрицы')
    print('  - heatmap.png - визуализация матрицы L')
    print('  - L_LT_heatmap.png - визуализация матрицы L*L^T')
    print('  - eigenvalues_L_LT.png - визуализация собственных чисел')


if __name__ == "__main__":
    main()
