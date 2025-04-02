
"""
pysimple: A package for creating legends for quiver plots
==================================================================

Features
--------
- Create compact, customizable legends for vector field visualizations
- Position legends in any corner of the plot
- Control the appearance and spacing of legend elements

Example
-------
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> from quiverlegend import create_compact_legend
>>> 
>>> fig, ax = plt.subplots(dpi=200)
>>> X, Y = np.meshgrid(np.arange(0, 2, 0.2), np.arange(0, 2, 0.2))
>>> U = np.cos(X) * Y
>>> V = np.sin(Y)
>>> Q = ax.quiver(X, Y, U, V)
>>> 
>>> # Add a compact legend
>>> create_compact_legend(ax, Q, reference_value=1, unit='m/s')
>>> plt.show()
"""

from Easyxp import simple_quiver_legend

__version__ = '0.1.0'