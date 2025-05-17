import numpy as np
import matplotlib.pyplot as plt


def visualize_eigenvalues(eigenvalues, title_text, filename=None, ax=None):
    """
    Визуализирует собственные числа
    
    Параметры:
        eigenvalues - вектор собственных чисел
        title_text - заголовок графика
        filename - имя файла для сохранения
        ax - объект осей matplotlib (опционально)
    """
    # Create a new figure if ax not provided
    if ax is None:
        fig = plt.figure(figsize=(8, 4))
        ax = plt.gca()  # Get current axes
    else:
        fig = ax.figure
    
    # Сортировка собственных чисел по убыванию
    sorted_eigenvalues = np.sort(eigenvalues)[::-1]
    
    # Визуализация собственных чисел
    markerline, stemlines, baseline = ax.stem(sorted_eigenvalues, linefmt='b-', markerfmt='bo', basefmt='r-')
    ax.grid(True)
    ax.set_title(title_text, fontsize=14)
    ax.set_xlabel('Индекс', fontsize=12)
    ax.set_ylabel('Значение', fontsize=12)
    
    # Сохранение
    if filename:
        fig.savefig(filename, dpi=300)
        print(f'Изображение сохранено в файл: {filename}')
    
    # Apply tight_layout to the figure if we created it
    if ax is plt.gca():
        fig.tight_layout()
        plt.show()
    
    return markerline
    plt.show()
