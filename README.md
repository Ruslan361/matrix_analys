# Matrix Analysis Toolkit

Комплексный инструментарий для построения и анализа специальной матрицы L с блочной структурой. Пакет предоставляет расширенные возможности для:

- 🏗️ **Построение матрицы L**: Два метода построения с блочной структурой (6 блоков строк × 4 блока столбцов)
  - `build_L_matrix` — стандартный метод
  - `generate_base` — метод с использованием `Ew1r` для автоматического обнуления линейно зависимых строк
- 📊 **Визуализация**: Тепловые карты с границами блоков, кастомные colormaps
- 🔢 **Анализ собственных значений**: Вычисление и визуализация спектра L·L^T
- 📐 **Ранг и базис**: Определение ранга матрицы и базисных строк методом RREF и через `generate_base`
- 🧮 **Линейная зависимость**: Автоматическое выявление и обнуление линейно зависимых строк
- 💾 **Экспорт результатов**: Сохранение матриц и отчётов в файлы

[English](#matrix-analysis-toolkit-en) | [Русский](#matrix-analysis-toolkit-ru)

---

<a name="matrix-analysis-toolkit-ru"></a>
# 🇷🇺 Matrix Analysis Toolkit (Русский)

## 🎯 Особенности

### Главный ноутбук: `analysis_master.ipynb`
Комплексный ноутбук с полным анализом матрицы L, включающий:

1. **Построение матрицы L** — использование пакета `matrix_analysis` для создания блочной матрицы
2. **Визуализация структуры** — тепловые карты с выделением блоков
3. **Анализ собственных значений** — вычисление для L·L^T с графиками распределения
4. **Вычисление ранга** — методом RREF с HTML-отчётами
5. **Базисные строки** — визуализация линейно независимых строк
6. **Метод generate_base** — альтернативное построение с `Ew1r` для обнуления линейно зависимых строк
7. **Сравнение методов** — визуальное сравнение L из кода и L_base
8. **Анализ линейно зависимых строк** — распределение по блокам с графиками

### Готово для Google Colab

Пакет разработан для бесшовной работы с Google Colab:

[![Открыть в Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ruslan361/matrix_analys/blob/main/analysis_master.ipynb)

## 📦 Установка

### Локальная установка

```bash
# Клонировать репозиторий
git clone https://github.com/Ruslan361/matrix_analys.git
cd matrix_analys

# Создать виртуальное окружение (рекомендуется)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# или
.venv\Scripts\activate  # Windows

# Установить зависимости
pip install -e .
# или использовать uv для более быстрой установки
uv pip install -e .
```

### Установка в Google Colab

В ноутбуке Google Colab выполните:

```python
# Установка напрямую из GitHub
!pip install git+https://github.com/Ruslan361/matrix_analys.git
```

Файл `analysis_master.ipynb` уже содержит код установки и автоматически выполнит его при запуске в Colab.

## 🚀 Использование

### Базовый пример

```python
import numpy as np
from matrix_analysis.build_L_matrix import build_L_matrix
from matrix_analysis.visualize_matrix import visualize_matrix
from matrix_analysis.create_custom_colormap import create_custom_colormap

# Параметры матрицы
PARAMS = {'n_1': 1, 'n1': 2, 'n2': 3, 'n3': 5, 'n4': 7}

# Построение матрицы L
L = build_L_matrix(**PARAMS)
print(f"Размер L: {L.shape}")  # (101, 247)

# Вычисление L·L^T
Lt = L.T
L_LT = L @ Lt

# Визуализация
cmap = create_custom_colormap()
visualize_matrix(L_LT, 'Матрица L·L^T', cmap)
```

### Альтернативный метод: generate_base

```python
from functools import reduce

def generate_base(n1, n2, n3, n4):
    """Построение базисной матрицы L с Ew1r"""
    # Функция Ew1r - единичная матрица с обнулённой последней строкой
    def Ew1r(n):
        result = np.eye(n)
        if n > 0:
            result[n-1, :] = 0
        return result
    
    # ... (полный код в analysis_master.ipynb)
    return np.vstack([row1, row2, row3, row4, row5, row6])

# Использование
L_base = generate_base(n1=2, n2=3, n3=5, n4=7)

# L_base содержит только базисные строки (85 из 101)
# Линейно зависимые строки автоматически обнулены
```

### 📓 Jupyter Notebooks

Проект включает несколько ноутбуков:

#### 1. **`analysis_master.ipynb`** — Главный комплексный анализ ⭐
   - Полный анализ матрицы L с всеми возможностями
   - Сравнение методов построения (build_L_matrix vs generate_base)
   - Визуализация базисных строк и линейно зависимых
   - HTML-отчёты с детальной статистикой
   - **Рекомендуется для полного анализа**

#### 2. **`matrix_analysis_notebook.ipynb`** — Базовый анализ
   - Простой пример использования пакета
   - Построение L и вычисление собственных значений
   - Подходит для быстрого старта

#### 3. **`colab_demo.ipynb`** — Демо для Colab
   - Упрощённая версия для Google Colab
   - Быстрая демонстрация основных возможностей

#### 4. **`eigenvectors.ipynb`** — Анализ собственных векторов
   - Расширенный анализ собственных векторов L·L^T

### Запуск локально

```bash
# Активировать виртуальное окружение
source .venv/bin/activate

# Запустить Jupyter
jupyter notebook analysis_master.ipynb

# Или использовать VS Code с расширением Jupyter
code analysis_master.ipynb
```

### Запуск в Google Colab

1. Нажмите кнопку "Открыть в Colab" выше
2. Ноутбук автоматически установит пакет
3. Запустите все ячейки для выполнения анализа

## 🔧 Устранение неполадок

### Ошибки импорта

Если возникает `ModuleNotFoundError` при запуске ноутбуков локально:

1. Убедитесь, что пакет установлен:
   ```bash
   # Из корневой директории репозитория
   pip install -e .
   ```

2. Или установите Python path вручную:
   ```bash
   # Для Windows PowerShell
   $env:PYTHONPATH = ".;./matrix_analysis"
   
   # Для Linux/macOS
   export PYTHONPATH=.:./matrix_analysis
   ```

3. В VS Code перезапустите ядро после установки: `Kernel > Restart Kernel`

### Проблемы с зависимостями

```bash
# Переустановить все зависимости
pip install --force-reinstall -e .

# Или использовать requirements из pyproject.toml
pip install numpy matplotlib seaborn sympy jupyter ipywidgets
```

### Ошибки в Colab

Если ноутбук не находит модули в Colab:
- Убедитесь, что ячейка установки (`!pip install git+...`) выполнена успешно
- Перезапустите runtime: `Runtime > Restart runtime`

## 📁 Структура проекта

```
matrix_analys/
├── matrix_analysis/          # 📦 Основной пакет
│   ├── __init__.py          # Объявления импортов
│   ├── build_L_matrix.py    # Построение матрицы L (стандартный метод)
│   ├── compute_matrix_rank.py    # Вычисление ранга методом RREF
│   ├── create_custom_colormap.py  # Кастомные цветовые схемы
│   ├── display_matrix_blocks.py   # Визуализация блочной структуры
│   ├── matrix_analysis_functions.py  # Вспомогательные функции
│   ├── save_matrix_to_file.py     # Экспорт результатов
│   ├── visualize_eigenvalues.py   # Визуализация спектра
│   └── visualize_matrix.py        # Визуализация матриц
│
├── analysis_master.ipynb    # ⭐ Главный комплексный ноутбук
├── matrix_analysis_notebook.ipynb  # Базовый анализ
├── colab_demo.ipynb        # Демо для Google Colab
├── eigenvectors.ipynb      # Анализ собственных векторов
├── manalis.ipynb           # Дополнительный анализ
│
├── main.py                 # CLI-скрипт для запуска анализа
├── setup.py                # Установка пакета (pip)
├── pyproject.toml          # Конфигурация проекта (современный формат)
├── uv.lock                 # Зависимости (uv package manager)
├── COLAB_USAGE.md          # Инструкции для Google Colab
└── README.md               # Этот файл
```

### Выходные файлы (генерируются при выполнении)

- `matrix_L_*.txt` — Матрица L (различные запуски)
- `matrix_LLT_*.txt` — Матрица L·L^T
- `eigenvalues_*.txt` — Собственные значения
- `analysis_report_*.md` — HTML/Markdown отчёты с результатами анализа
- `matrix_rank.txt` — Ранг матрицы

## 📋 Требования

### Основные зависимости
- **Python** >= 3.8
- **NumPy** >= 1.20.0 — работа с матрицами
- **Matplotlib** >= 3.4.0 — визуализация
- **Seaborn** — улучшенные графики
- **SymPy** — символьные вычисления
- **Jupyter** >= 1.0.0 — ноутбуки
- **ipywidgets** — интерактивные виджеты

### Опциональные
- **uv** — быстрый менеджер пакетов Python (рекомендуется)

Все зависимости указаны в `pyproject.toml` и устанавливаются автоматически при `pip install -e .`

## 🎓 Математическая справка

### Структура матрицы L

Матрица L имеет блочную структуру **6 блоков строк × 4 блока столбцов**:

**Размеры блоков строк** (параметры n₁=2, n₂=3, n₃=5, n₄=7):
1. Блок 1: n₃×n₄ = 5×7 = **35 строк**
2. Блок 2: n₂×n₄ = 3×7 = **21 строка**
3. Блок 3: n₁×n₄ = 2×7 = **14 строк** (с Ew1r → 7 базисных)
4. Блок 4: n₂×n₃ = 3×5 = **15 строк**
5. Блок 5: n₁×n₃ = 2×5 = **10 строк** (с Ew1r → 5 базисных)
6. Блок 6: n₁×n₂ = 2×3 = **6 строк** (с Ew1r → 2 базисных)

**Итого**: 101 строка, из которых **85 базисных** (линейно независимых)

### Функция Ew1r

`Ew1r(n)` — единичная матрица n×n с обнулённой последней строкой:
```
Ew1r(3) = [1 0 0]
          [0 1 0]
          [0 0 0]  ← последняя строка обнулена
```

Используется в блоках 3, 5, 6 для автоматического обнуления линейно зависимых строк.

## 🤝 Вклад в проект

Вклады приветствуются! Процесс:

1. Fork репозитория
2. Создайте ветку: `git checkout -b feature/amazing-feature`
3. Commit изменений: `git commit -m 'Add amazing feature'`
4. Push в ветку: `git push origin feature/amazing-feature`
5. Откройте Pull Request

## 📄 Лицензия

MIT License — см. файл `LICENSE`

## 👤 Автор

**Ruslan361**
- GitHub: [@Ruslan361](https://github.com/Ruslan361)
- Repository: [matrix_analys](https://github.com/Ruslan361/matrix_analys)

---

<a name="matrix-analysis-toolkit-en"></a>
# 🇬🇧 Matrix Analysis Toolkit (English)

## 🎯 Features

A comprehensive toolkit for building and analyzing the special L matrix with block structure:

- 🏗️ **L Matrix Construction**: Two methods with block structure (6 row blocks × 4 column blocks)
  - `build_L_matrix` — standard method
  - `generate_base` — method using `Ew1r` for automatic nullification of linearly dependent rows
- 📊 **Visualization**: Heatmaps with block boundaries, custom colormaps
- 🔢 **Eigenvalue Analysis**: Computing and visualizing the spectrum of L·L^T
- 📐 **Rank and Basis**: Determining matrix rank and basis rows via RREF and `generate_base`
- 🧮 **Linear Dependence**: Automatic detection and nullification of linearly dependent rows
- 💾 **Results Export**: Saving matrices and reports to files

### Ready for Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Ruslan361/matrix_analys/blob/main/analysis_master.ipynb)

## 📦 Installation

### Local Installation

```bash
# Clone the repository
git clone https://github.com/Ruslan361/matrix_analys.git
cd matrix_analys

# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate  # Windows

# Install dependencies
pip install -e .
# or use uv for faster installation
uv pip install -e .
```

### Installation in Google Colab

```python
# Install directly from GitHub
!pip install git+https://github.com/Ruslan361/matrix_analys.git
```

## 🚀 Usage

### Basic Example

```python
import numpy as np
from matrix_analysis.build_L_matrix import build_L_matrix
from matrix_analysis.create_custom_colormap import create_custom_colormap

# Matrix parameters
PARAMS = {'n_1': 1, 'n1': 2, 'n2': 3, 'n3': 5, 'n4': 7}

# Build L matrix
L = build_L_matrix(**PARAMS)
print(f"L size: {L.shape}")  # (101, 247)

# Compute L·L^T
L_LT = L @ L.T
```

### 📓 Jupyter Notebooks

#### 1. **`analysis_master.ipynb`** — Main Comprehensive Analysis ⭐
   - Complete L matrix analysis with all features
   - Comparison of construction methods (build_L_matrix vs generate_base)
   - Visualization of basis rows and linearly dependent rows
   - HTML reports with detailed statistics
   - **Recommended for full analysis**

#### 2. **`matrix_analysis_notebook.ipynb`** — Basic Analysis
   - Simple package usage example
   - L construction and eigenvalue computation

#### 3. **`colab_demo.ipynb`** — Colab Demo
   - Simplified version for Google Colab
   - Quick demonstration of key features

### Running Locally

```bash
# Activate virtual environment
source .venv/bin/activate

# Start Jupyter
jupyter notebook analysis_master.ipynb
```

## 📋 Requirements

- **Python** >= 3.8
- **NumPy** >= 1.20.0
- **Matplotlib** >= 3.4.0
- **Seaborn**, **SymPy**, **Jupyter**, **ipywidgets**

See `pyproject.toml` for complete list.

## 🤝 Contributing

Contributions welcome! Please submit a Pull Request.

## 📄 License

MIT License

## 👤 Author

**Ruslan361** — [@Ruslan361](https://github.com/Ruslan361)
