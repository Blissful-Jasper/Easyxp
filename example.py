# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s

@email : xianpuji@hhu.edu.cn
"""


import matplotlib.pyplot as plt
import numpy as np
from Easyxp import simple_quiver_legend

# 创建示例数据
x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)
u = np.cos(x)
v = np.sin(x)

# 创建图形
fig, ax = plt.subplots(dpi=200)
q = ax.quiver(x, y, u, v)

# 添加图例
simple_quiver_legend(
    ax=ax,
    quiver=q,
    reference_value=1.0,
    unit='m/s',
    legend_location='upper right',
    box_facecolor='lightgray'
)

plt.show()