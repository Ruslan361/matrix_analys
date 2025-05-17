import numpy as np
import matplotlib.pyplot as plt


def create_custom_colormap():
    """
    Создает пользовательскую цветовую схему
    
    Возвращает:
        custom_colormap - цветовая карта для визуализации матриц
    """
    import matplotlib.colors as mcolors
    
    n = 128
    # Создаем переход от синего к белому
    blue_to_white = np.column_stack([
        np.linspace(0, 1, n),
        np.linspace(0, 1, n),
        np.ones(n)
    ])
    
    # Создаем переход от белого к красному
    white_to_red = np.column_stack([
        np.ones(n),
        np.linspace(1, 0, n),
        np.linspace(1, 0, n)
    ])
    
    # Объединяем оба перехода
    colors = np.vstack([blue_to_white, white_to_red])
    
    # Создаем и возвращаем цветовую карту
    custom_colormap = mcolors.ListedColormap(colors)
    return custom_colormap
