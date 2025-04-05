
## example:




```python
import matplotlib.pyplot as plt
import numpy as np
from easyxp import simple_quiver_legend


x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)
u = np.cos(x)
v = np.sin(x)


fig, ax = plt.subplots(dpi=200)
q = ax.quiver(x, y, u, v)


simple_quiver_legend(
    ax=ax,
    quiver=q,
    reference_value=1.0,
    unit='m/s',
    legend_location='upper right',
    box_facecolor='lightgray'
)

plt.show()
```

![](./quiver.png)

---
