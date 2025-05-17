import numpy as np
import os
import tempfile
import shutil


def save_matrix_to_file(matrix, filename):
    """
    Сохраняет матрицу в отдельный файл
    
    Параметры:
        matrix - матрица для сохранения
        filename - имя файла
    """
    
    # Используем временный файл, чтобы избежать проблем с правами доступа
    try:
        # Создаем временный файл
        with tempfile.NamedTemporaryFile(suffix='.npz', delete=False) as temp_file:
            temp_filename = temp_file.name
            np.savez(temp_filename, matrix=matrix)
        
        # Проверяем, что временный файл создан успешно
        if os.path.exists(temp_filename):
            try:
                # Копируем временный файл в целевой
                shutil.copyfile(temp_filename, filename)
                # Удаляем временный файл
                os.remove(temp_filename)
                print(f'Матрица успешно сохранена в файл: {filename}')
            except Exception as e:
                print(f'Не удалось сохранить матрицу в файл {filename}: {str(e)}')
                print('Попробуйте сохранить в другую директорию.')
        else:
            print('Не удалось создать временный файл.')
    except Exception as e:
        print(f'Ошибка при сохранении матрицы: {str(e)}')
        print('Пробуем альтернативный метод сохранения...')
        
        # Альтернативный метод: сохраняем в текстовый файл
        txt_filename = filename.replace('.npz', '.txt') if filename.endswith('.npz') else filename + '.txt'
        try:
            with open(txt_filename, 'w') as f:
                f.write(f'# Матрица размера {matrix.shape[0]}x{matrix.shape[1]}\n')
                for i in range(matrix.shape[0]):
                    for j in range(matrix.shape[1]):
                        f.write(f'{matrix[i,j]:15.8f} ')
                    f.write('\n')
                print(f'Матрица сохранена в текстовый файл: {txt_filename}')
        except Exception as e:
            print(f'Ошибка при сохранении в текстовый файл: {str(e)}')
