import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

# Constants
hbar = 1.0  # Reduced Planck's constant
m = 1.0     # Mass of the particle
L = 1.0     # Length of the potential well
N = 1000    # Number of points in the grid

# Discretize the space
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# Kinetic energy operator (second derivative using finite difference method)
T = - (hbar**2 / (2 * m * dx**2)) * (np.diag(np.ones(N-1), -1) - 2 * np.diag(np.ones(N), 0) + np.diag(np.ones(N-1), 1))

# Potential energy operator (zero inside the well)
V = np.zeros(N)

# Hamiltonian operator
H = T + np.diag(V)

# Solve the eigenvalue problem
eigenvalues, eigenvectors = eigh(H)

# Plot the first few eigenstates
plt.figure(figsize=(10, 6))
for i in range(4):
    plt.plot(x, eigenvectors[:, i], label=f'n={i+1}, E={eigenvalues[i]:.2f}')
plt.xlabel('x')
plt.ylabel('Wavefunction')
plt.title('Eigenstates of a Particle in an Infinite Potential Well')
plt.legend()
plt.show()


