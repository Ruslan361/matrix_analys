# Using this Package in Google Colab

This guide explains how to use the matrix_analysis package in Google Colab and take advantage of its collaborative features.

## Quick Start

1. Open one of our notebooks directly in Google Colab:
   - [Full Matrix Analysis Notebook](https://colab.research.google.com/github/your_username/matrix_analysis/blob/main/matrix_analysis_notebook.ipynb)
   - [Quick Demo](https://colab.research.google.com/github/your_username/matrix_analysis/blob/main/colab_demo.ipynb)

2. The notebook will automatically install the package from GitHub.

3. Run all cells or explore step by step.

## Manual Installation in Any Notebook

If you're using your own notebook, add this code to install the package:

```python
!pip install git+https://github.com/your_username/matrix_analysis.git
```

Then import the functions you need:

```python
# Import all main functions
from matrix_analysis import (build_L_matrix, visualize_matrix, 
                            visualize_eigenvalues, compute_matrix_rank)

# Or import everything
from matrix_analysis import *
```

## Saving Your Work

Since Google Colab is a temporary environment, make sure to:

1. Save generated visualizations by clicking the three dots in the output and selecting "Save image as..."
2. Download your modified notebook using File > Download > Download .ipynb
3. Save to Google Drive using File > Save a copy in Drive

## Example Workflow

```python
# Install the package
!pip install git+https://github.com/your_username/matrix_analysis.git

# Import what you need
from matrix_analysis import build_L_matrix, visualize_matrix, compute_matrix_rank
import numpy as np
import matplotlib.pyplot as plt

# Build a matrix
L, block_coords = build_L_matrix(1, 2, 3, 4, 5)

# Analyze it
rank = compute_matrix_rank(L)
print(f"Matrix rank: {rank}")

# Visualize
visualize_matrix(L, 'Matrix L')
plt.show()
```

## Sharing Your Results

One of the main advantages of Google Colab is easy sharing:

1. Click "Share" in the top right
2. Set access permissions (anyone with the link, specific people, etc.)  
3. Share the link with collaborators

Your collaborators will see exactly the same environment with all the outputs.
