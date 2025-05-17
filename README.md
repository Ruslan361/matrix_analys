# Matrix Analysis Toolkit

This package provides a set of tools for building and analyzing the special L matrix and performing various operations with it:

- Building the L matrix with a specified structure
- Visualizing the matrix as a heatmap
- Computing eigenvalues and eigenvectors
- Analyzing matrix rank
- Calculating the characteristic polynomial

[English | [Русский](#matrix-analysis-toolkit-ru)]

## Ready for Google Colab

This package is designed to work seamlessly with Google Colab. Just click the button below to open the notebook:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your_username/matrix_analysis/blob/main/matrix_analysis_notebook.ipynb)

## Installation

### Local Installation

```bash
# Clone the repository
git clone https://github.com/your_username/matrix_analysis.git
cd matrix_analysis

# Install in development mode
pip install -e .
```

### Installation in Google Colab

In your Google Colab notebook, simply run:

```python
# Install directly from GitHub
!pip install git+https://github.com/your_username/matrix_analysis.git
```

The `matrix_analysis_notebook.ipynb` file already includes this installation code and will handle it automatically when run in Colab.

## Usage

### Basic Usage

```python
import numpy as np
from matrix_analysis.build_L_matrix import build_L_matrix
from matrix_analysis.visualize_matrix import visualize_matrix
from matrix_analysis.create_custom_colormap import create_custom_colormap

# Build the matrix
L, block_coords = build_L_matrix(1, 2, 3, 4, 5)

# Calculate L*L^T
Lt = L.T
L_LT = L @ Lt

# Visualization
visualize_matrix(L_LT, 'L*L^T Matrix', create_custom_colormap)
```

### Jupyter Notebook

The project includes a Jupyter Notebook (`matrix_analysis_notebook.ipynb`) that demonstrates the main capabilities of the package and can be run locally or in Google Colab. The notebook provides an interactive interface for:

1. Building the L matrix with customizable parameters
2. Visualizing the matrix structure
3. Computing and visualizing eigenvalues
4. Analyzing matrix rank
5. Saving results to files

### Running in Google Colab

To run the notebook in Google Colab:
1. Open the notebook using the "Open in Colab" button at the top of this README
2. The notebook will automatically detect that it's running in Colab and install the package
3. Run all cells to perform the analysis

### Running Locally

To run the notebook locally:
1. Clone the repository as described in the Installation section
2. Open the notebook in Jupyter: `jupyter notebook matrix_analysis_notebook.ipynb`
3. Run the cells to perform the analysis

## Troubleshooting

### Import Errors

If you encounter `ModuleNotFoundError` when running the notebooks locally:

1. Make sure you've installed the package:
   ```bash
   # From the repository root directory
   pip install -e .
   ```

2. Or set the Python path manually:
   ```bash
   # For Windows PowerShell
   $env:PYTHONPATH = ".;./matrix_analysis"
   
   # For Linux/macOS
   export PYTHONPATH=.:./matrix_analysis
   ```

3. If using VS Code, try restarting the kernel after installation.

The notebooks have been updated with improved import handling that should automatically find the modules in most environments.

## Project Structure

- `matrix_analysis/` - main package directory
  - `__init__.py` - import declarations
  - `build_L_matrix.py` - function for building the L matrix
  - `compute_matrix_rank.py` - function for calculating matrix rank
  - `create_custom_colormap.py` - function for creating a custom color scheme
  - `display_matrix_blocks.py` - function for visualizing matrix blocks
  - `matrix_analysis_functions.py` - auxiliary functions
  - `save_matrix_to_file.py` - function for saving the matrix to a file
  - `visualize_eigenvalues.py` - function for visualizing eigenvalues
  - `visualize_matrix.py` - function for visualizing the matrix
- `matrix_analysis_notebook.ipynb` - interactive notebook with examples
- `colab_demo.ipynb` - simplified notebook for quick demonstration in Colab
- `setup.py` - file for package installation
- `requirements.txt` - package dependencies

## Requirements

- NumPy (>=1.20.0)
- Matplotlib (>=3.4.0)
- Jupyter (>=1.0.0)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT

---

<a name="matrix-analysis-toolkit-ru"></a>
# Matrix Analysis Toolkit (Русский)

Этот пакет предоставляет набор инструментов для построения и анализа специальной матрицы L и выполнения различных операций с ней:

- Построение матрицы L с заданной структурой
- Визуализация матрицы в виде тепловой карты
- Вычисление собственных чисел и векторов
- Анализ ранга матрицы
- Расчет характеристического многочлена

## Готово для Google Colab

Этот пакет разработан для бесшовной работы с Google Colab. Просто нажмите кнопку ниже, чтобы открыть ноутбук:

[![Открыть в Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your_username/matrix_analysis/blob/main/matrix_analysis_notebook.ipynb)

## Установка

### Локальная установка

```bash
# Клонировать репозиторий
git clone https://github.com/your_username/matrix_analysis.git
cd matrix_analysis

# Установить в режиме разработки
pip install -e .
```

### Установка в Google Colab

В вашем ноутбуке Google Colab просто выполните:

```python
# Установка напрямую из GitHub
!pip install git+https://github.com/your_username/matrix_analysis.git
```

Файл `matrix_analysis_notebook.ipynb` уже содержит этот код установки и автоматически выполнит его при запуске в Colab.

## Использование

### Базовое использование

```python
import numpy as np
from matrix_analysis.build_L_matrix import build_L_matrix
from matrix_analysis.visualize_matrix import visualize_matrix
from matrix_analysis.create_custom_colormap import create_custom_colormap

# Построение матрицы
L, block_coords = build_L_matrix(1, 2, 3, 4, 5)

# Вычисление L*L^T
Lt = L.T
L_LT = L @ Lt

# Визуализация
visualize_matrix(L_LT, 'Матрица L*L^T', create_custom_colormap)
```

### Jupyter Notebook

Проект включает Jupyter Notebook (`matrix_analysis_notebook.ipynb`), который демонстрирует основные возможности пакета и может быть запущен локально или в Google Colab. Ноутбук предоставляет интерактивный интерфейс для:

1. Построения матрицы L с настраиваемыми параметрами
2. Визуализации структуры матрицы
3. Вычисления и визуализации собственных чисел
4. Анализа ранга матрицы
5. Сохранения результатов в файлы

### Запуск в Google Colab

Для запуска ноутбука в Google Colab:
1. Откройте ноутбук, используя кнопку "Открыть в Colab" в начале этого README
2. Ноутбук автоматически определит, что он запущен в Colab, и установит пакет
3. Запустите все ячейки для выполнения анализа

### Запуск локально

Для запуска ноутбука локально:
1. Клонируйте репозиторий, как описано в разделе Установка
2. Откройте ноутбук в Jupyter: `jupyter notebook matrix_analysis_notebook.ipynb` 
3. Запустите ячейки для выполнения анализа

## Структура проекта

- `matrix_analysis/` - основная директория пакета
  - `__init__.py` - объявления импортов
  - `build_L_matrix.py` - функция построения матрицы L
  - `compute_matrix_rank.py` - функция расчета ранга матрицы
  - `create_custom_colormap.py` - функция создания цветовой схемы
  - `display_matrix_blocks.py` - функция визуализации блоков матрицы
  - `matrix_analysis_functions.py` - вспомогательные функции
  - `save_matrix_to_file.py` - функция сохранения матрицы в файл
  - `visualize_eigenvalues.py` - функция визуализации собственных чисел
  - `visualize_matrix.py` - функция визуализации матрицы
- `matrix_analysis_notebook.ipynb` - интерактивный ноутбук с примерами
- `colab_demo.ipynb` - упрощенный ноутбук для быстрой демонстрации в Colab
- `setup.py` - файл для установки пакета
- `requirements.txt` - зависимости пакета

## Требования

- NumPy (>=1.20.0)
- Matplotlib (>=3.4.0)
- Jupyter (>=1.0.0)

## Вклад в проект

Вклады приветствуются! Пожалуйста, не стесняйтесь отправлять Pull Request.

## Лицензия

MIT
