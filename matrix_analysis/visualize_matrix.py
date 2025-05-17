import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from create_custom_colormap import create_custom_colormap


def visualize_matrix(matrix, title_text, colormap_func=create_custom_colormap, filename=None, show_max_value=False, ax=None):
    """
    Создает тепловую карту матрицы
    
    Параметры:
        matrix - матрица для визуализации
        title_text - заголовок графика
        colormap_func - функция для цветовой схемы
        filename - имя файла для сохранения
        show_max_value - флаг отображения максимального значения
        ax - объект осей matplotlib (опционально)
    """
    # Create a new figure if ax not provided
    if ax is None:
        fig = plt.figure(figsize=(9, 7))
        ax = plt.gca()  # Get current axes
    else:
        fig = ax.figure
      # Отрисовка матрицы
    im = ax.imshow(matrix, cmap=colormap_func())
    ax.axis('equal')
    ax.axis('tight')
    
    # Настройка цветовой шкалы
    # Note: we don't automatically add colorbar since it might be managed externally
    # The caller can add it with plt.colorbar(im) or fig.colorbar(im)
    max_abs_val = np.max(np.abs(matrix))
    im.set_clim(-max_abs_val, max_abs_val)
    
    # Заголовок и метки осей
    if show_max_value:        
        max_val = np.max(matrix)
        min_val = np.min(matrix)
        max_pos = np.unravel_index(np.argmax(matrix), matrix.shape)
        min_pos = np.unravel_index(np.argmin(matrix), matrix.shape)
        
        title_with_max = f'{title_text}\nМакс. значение: {max_val:.4f} в позиции {max_pos}, мин. значение: {min_val:.4f} в позиции {min_pos}'
        ax.set_title(title_with_max, fontsize=14)
        
        # Отмечаем точки максимального и минимального значения
        ax.plot(max_pos[1], max_pos[0], 'ro', markersize=10, linewidth=2)
        ax.plot(min_pos[1], min_pos[0], 'go', markersize=10, linewidth=2)
    else:
        ax.set_title(title_text, fontsize=14)
    
    ax.set_xlabel('Столбцы (j)', fontsize=12)
    ax.set_ylabel('Строки (i)', fontsize=12)
    
    # Настройка внешнего вида
    ax.grid(False)
    ax.set_frame_on(True)  # equivalent to plt.box(True)
    
    # Сохранение
    if filename:
        fig = ax.figure
        fig.savefig(filename, dpi=300)
        print(f'Изображение сохранено в файл: {filename}')
    
    # Apply tight_layout to the figure if we created it
    if ax is plt.gca():
        fig = ax.figure
        fig.tight_layout()
        plt.show()
    
    # Return the image for potential external colorbar
    return im
