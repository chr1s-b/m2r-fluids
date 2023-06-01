"""Define difference equations."""


def backward_euler(u, n, j, h, k):
    u[n+1, j] = u[n, j] - (k / (2*h)) * (u[n, j+1] - u[n, j-1])


def lax_friedrichs(u, n, j, h, k):
    u[n+1, j] = (1/2) * (u[n, j-1] - u[n, j+1]) - (k / (2*h)) * (u[n, j+1] - u[n, j-1])


def lax_wendroff(u, n, j, h, k):
    u[n+1, j] = u[n, j] - (k / (2*h)) * (u[n, j+1] - u[n, j-1]) + (k**2 / (2*h**2)) * (u[n, j+1] - 2*u[n, j] + u[n, j-1])


def beam_warming(u, n, j, h, k):
    u[n+1, j] = u[n, j] - (k / (2*h)) * (3*u[n, j] - 4*u[n, j-1] + u[n, j-2]) + (k**2 / (2*h**2)) * (u[n, j] - 2*u[n, j-1] + u[n, j-2])
