from setuptools import setup, find_packages

setup(
    name="matrix_analysis",
    version="0.1.0",
    description="Инструменты для анализа матриц",
    author="Elena",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "matplotlib",
    ],
)
