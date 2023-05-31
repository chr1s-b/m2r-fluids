import numpy as np
import matplotlib.pyplot as plt

# constants
h = 0.01    # mesh width
k = 0.1     # time step

x = np.arange(-100, 100, h)
print(x)


def u_0(x: np.ndarray):
    """Define initial condition at t=0."""
    return np.heaviside(-x, 0.5)


u = u_0(x)

# plot

plt.plot(x, u)
plt.show()
