import numpy as np


def build_L_matrix(n_1=1, n1=2, n2=3, n3=4, n4=5):
    """
    Создает матрицу L с определенной блочной структурой
    
    Параметры:
        n_1, n1, n2, n3, n4 - параметры для построения матрицы
        
    Возвращает:
        L - построенная матрица
        block_coords - структура координат для визуализации блоков
    """
    
    # Создание блоков матрицы L в прямом виде
    # Блок z_1
    z1_blocks = [
        -np.kron(np.ones((n_1, n2)), np.eye(n3*n4)),            # Блок 1.1
        np.kron(np.ones((n_1, n1)), np.eye(n3*n4)),             # Блок 1.2
        np.zeros((n3*n4, n1*n2*n4 + n1*n2*n3))                 # Блок 1.3
    ]
    z_1 = np.hstack(z1_blocks)

    # Блок z_2
    z2_blocks = [
        -np.kron(np.kron(np.eye(n2), np.ones((n_1, n3))), np.eye(n4)), # Блок 2.1
        np.zeros((n2*n4, n1*n3*n4)),                           # Блок 2.2
        np.kron(np.ones((n_1, n1)), np.eye(n2*n4)),            # Блок 2.3
        np.zeros((n2*n4, n1*n2*n3))                           # Блок 2.4
    ]
    z_2 = np.hstack(z2_blocks)

    # Блок z_3
    z3_blocks = [
        np.zeros((n1*n4, n2*n3*n4)),                          # Блок 3.1
        -np.kron(np.kron(np.eye(n1), np.ones((n_1, n3))), np.eye(n4)), # Блок 3.2
        np.kron(np.kron(np.eye(n1), np.ones((n_1, n2))), np.eye(n4)), # Блок 3.3
        np.zeros((n1*n4, n1*n2*n3))                          # Блок 3.4
    ]
    z_3 = np.hstack(z3_blocks)

    # Блок z_4
    z4_blocks = [
        -np.kron(np.eye(n2*n3), np.ones((n_1, n4))),         # Блок 4.1
        np.zeros((n2*n3, n1*n3*n4 + n1*n2*n4)),              # Блок 4.2
        np.kron(np.ones((n_1, n1)), np.eye(n2*n3))           # Блок 4.3
    ]
    z_4 = np.hstack(z4_blocks)

    # Блок z_5
    z5_blocks = [
        np.zeros((n1*n3, n2*n3*n4)),                        # Блок 5.1
        -np.kron(np.eye(n1*n3), np.ones((n_1, n4))),         # Блок 5.2
        np.zeros((n1*n3, n1*n2*n4)),                        # Блок 5.3
        np.kron(np.kron(np.eye(n1), np.ones((n_1, n2))), np.eye(n3)) # Блок 5.4
    ]
    z_5 = np.hstack(z5_blocks)

    # Блок z_6
    z6_blocks = [
        np.zeros((n1*n2, n2*n3*n4 + n1*n3*n4)),              # Блок 6.1
        -np.kron(np.eye(n1*n2), np.ones((n_1, n4))),          # Блок 6.2
        np.kron(np.eye(n1*n2), np.ones((n_1, n3)))           # Блок 6.3
    ]
    z_6 = np.hstack(z6_blocks)

    # Создаем массив содержащий блоки матрицы L
    z_blocks = [z_1, z_2, z_3, z_4, z_5, z_6]
    all_sub_blocks = [z1_blocks, z2_blocks, z3_blocks, z4_blocks, z5_blocks, z6_blocks]

    # Объединение блоков в общую матрицу
    L = np.vstack(z_blocks)

    # Создание структуры координат для визуализации
    block_coords = compute_block_coordinates(z_blocks, all_sub_blocks, n1, n2, n3, n4)
    
    return L, block_coords


def compute_block_coordinates(z_blocks, all_sub_blocks, n1, n2, n3, n4):
    """
    Вычисляет координаты блоков для визуализации
    
    Параметры:
        z_blocks - список основных блоков матрицы
        all_sub_blocks - список всех подблоков
        n1, n2, n3, n4 - параметры размеров
        
    Возвращает:
        coords - словарь с координатами блоков
    """
    coords = {
        'main_blocks': [],
        'sub_blocks': []
    }

    # Вычисляем координаты для основных блоков
    row_start = 0
    for i, z_block in enumerate(z_blocks):
        rows, cols = z_block.shape
        
        # Добавляем координаты блока
        coords['main_blocks'].append({
            'rows': [row_start, row_start + rows - 1],
            'cols': [0, cols - 1]
        })
        
        row_start += rows

    # Вычисляем координаты для подблоков
    row_start = 0
    sub_block_idx = 0

    for i, z_block in enumerate(z_blocks):
        block_height = z_block.shape[0]

        # Если есть информация о подблоках для этого блока
        if i < len(all_sub_blocks):
            sub_blocks = all_sub_blocks[i]

            # Обрабатываем каждый подблок
            col_start = 0
            for j, sub_block in enumerate(sub_blocks):
                sub_width = sub_block.shape[1]

                # Добавляем координаты подблока
                coords['sub_blocks'].append({
                    'parent': i,
                    'rows': [row_start, row_start + block_height - 1],
                    'cols': [col_start, col_start + sub_width - 1]
                })

                col_start += sub_width
                sub_block_idx += 1

        row_start += block_height

    # Добавляем линии для совместимости с графическим отображением
    main_block_heights = [z_blocks[b].shape[0] for b in range(len(z_blocks)-1)]
    coords['hlines'] = np.cumsum(main_block_heights)
    coords['vlines'] = np.cumsum([n2*n3*n4, n1*n3*n4, n1*n2*n4, n1*n2*n3])
    
    return coords
