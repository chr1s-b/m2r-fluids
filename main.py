import numpy as np
import matplotlib.pyplot as plt

# constants
h = 0.01    # mesh width
k = 0.1     # time step
a = -100    # lower bound
b = 100     # upper bound

x = np.arange(a, b, h)


def u_0(x: np.ndarray):
    """Define initial condition at t=0."""
    return np.heaviside(-x, 0.5)


u = u_0(x)

# plot

plt.plot(x, u)
plt.show()
