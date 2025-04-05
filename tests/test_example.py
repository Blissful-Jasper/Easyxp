# tests/test_example.py
import matplotlib.pyplot as plt
import numpy as np
from easyxp import simple_quiver_legend

def test_simple_quiver_legend_runs():
    x = np.linspace(0, 2*np.pi, 10)
    y = np.sin(x)
    u = np.cos(x)
    v = np.sin(x)

    fig, ax = plt.subplots(dpi=200)
    q = ax.quiver(x, y, u, v)

    # 这里不做显示，也不保存图像，只是测试函数是否能正常调用
    simple_quiver_legend(
        ax=ax,
        quiver=q,
        reference_value=1.0,
        unit='m/s',
        legend_location='upper right',
        box_facecolor='lightgray'
    )

    plt.close(fig)  # 关闭图像，避免资源泄露
