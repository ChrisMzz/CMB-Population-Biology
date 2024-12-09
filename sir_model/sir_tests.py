import numpy as np
import matplotlib.pyplot as plt
from sir_model import SIR, SIRConfig


config = SIRConfig(
    T=10,
    N=300
)


model = SIR(
    beta=1,
    gamma=0.5,
    y0=np.array([0.7, 0.3, 0.0]),
    config=config
)

fig, (ax1, ax2) = plt.subplots(1,2)
model.show_SvI(ax1)
model.display(ax2, showRinfty=True)
plt.show()


