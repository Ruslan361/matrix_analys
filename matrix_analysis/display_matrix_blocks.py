import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def display_matrix_blocks(L, block_coords):
    """
    Отображает блоки матрицы L
    
    Параметры:
        L - матрица для отображения
        block_coords - словарь с координатами блоков
    """
    # Настройка цвета и типа линий для всех границ
    BORDER_COLOR = (0.5, 0.5, 0.5)  # Серый цвет
    BORDER_STYLE = '--'             # Пунктирная линия
    MAIN_WIDTH = 1.2                # Ширина линии основных блоков
    SUB_WIDTH = 0.8                 # Ширина линии подблоков
    
    # Рисуем основные блоки (z_1, z_2, ..., z_6)
    for block in block_coords['main_blocks']:
        rows = block['rows']
        cols = block['cols']
        
        # Позиция прямоугольника [x, y, width, height]
        x = cols[0] - 0.5
        y = rows[0] - 0.5
        width = cols[1] - cols[0] + 1
        height = rows[1] - rows[0] + 1
        
        # Рисуем прямоугольник для основного блока
        rect = Rectangle((x, y), width, height, 
                        fill=False, 
                        edgecolor=BORDER_COLOR, 
                        linewidth=MAIN_WIDTH, 
                        linestyle=BORDER_STYLE)
        plt.gca().add_patch(rect)
    
    # Рисуем подблоки (компоненты внутри z_1, z_2, ...)
    for block in block_coords['sub_blocks']:
        rows = block['rows']
        cols = block['cols']
        
        # Позиция прямоугольника
        x = cols[0] - 0.5
        y = rows[0] - 0.5
        width = cols[1] - cols[0] + 1
        height = rows[1] - rows[0] + 1
        
        # Рисуем прямоугольник для подблока
        rect = Rectangle((x, y), width, height, 
                        fill=False, 
                        edgecolor=BORDER_COLOR, 
                        linewidth=SUB_WIDTH, 
                        linestyle=BORDER_STYLE)
        plt.gca().add_patch(rect)
