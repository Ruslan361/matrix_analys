"""
Matrix Analysis - A toolkit for building and analyzing matrices.

This package provides tools for:
- Building specialized matrices (L matrix)
- Visualizing matrices with custom colormaps
- Computing and visualizing eigenvalues
- Analyzing matrix rank
- Saving analysis results to files
"""

# Import all important functions
from .build_L_matrix import build_L_matrix
from .visualize_matrix import visualize_matrix
from .visualize_eigenvalues import visualize_eigenvalues
from .display_matrix_blocks import display_matrix_blocks
from .compute_matrix_rank import compute_matrix_rank
from .create_custom_colormap import create_custom_colormap
from .matrix_analysis_functions import save_characteristic_polynomial
from .save_matrix_to_file import save_matrix_to_file

# Define package metadata
__version__ = "0.1.0"
__author__ = "Elena"
__description__ = "Tools for analyzing matrices"

# Define what should be imported with "from matrix_analysis import *"
__all__ = [
    'build_L_matrix',
    'visualize_matrix',
    'visualize_eigenvalues',
    'display_matrix_blocks',
    'compute_matrix_rank',
    'create_custom_colormap',
    'save_characteristic_polynomial',
    'save_matrix_to_file'
]

# Welcome message that will display when the package is imported directly
print("Matrix Analysis Toolkit v{}".format(__version__))
print("Use help(matrix_analysis) for more information on available functions.")