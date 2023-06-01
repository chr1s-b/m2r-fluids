import numpy as np
import matplotlib.pyplot as plt
from difference_equations import backward_euler, lax_friedrichs, lax_wendroff, beam_warming

# controls
L = 4       # domain size
T = 0.2     # final time
h = 0.01    # mesh width
k = 0.5 * h # time step (wrt mesh ratio and h)
a = -L/2.   # lower bound
b = L/2.    # upper bound


def u_0(y: np.ndarray):
    """Define initial condition at t=0."""
    return np.where(y <= 0.2, 1.0, 0.0)


# choose difference method to numerically solve the problem
difference_method = lax_wendroff

# create space for numerical solution

x = np.arange(a, b, h)
t = np.arange(0, T, k)

u = np.zeros((len(t), len(x)))

# apply initial condition
u[0] = u_0(x)

# numerically solve
for n in range(len(t)-1):
    for j in range(1, len(x)-1):
        difference_method(u, n, j, h, k)

# apply analytic solution
exact_solution = np.zeros((len(t), len(x)))
for n in range(len(t)):
    exact_solution[n] = u_0(x - t[n])

# plot


def method_to_name(method: callable) -> str:
    """Convert function to a name."""
    return method.__name__.replace("_", "-").title()


plt.title(f"{method_to_name(difference_method)}")
plt.xlabel("x")
plt.ylabel("u")
plt.xlim([0, 1])
plt.ylim([-0.5, 1.5])
plt.plot(x, u[-1], '.')
plt.plot(x, exact_solution[-1])
plt.grid(True)
plt.show()
