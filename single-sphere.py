import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plotting

# Define parameters
omega = 2 * np.pi                          # Angular frequency (1 full turn per unit time)
t_vals = np.linspace(0, 1, 200)            # Time values from 0 to 1

# Define initial amplitudes (example: equal superposition)
alpha0 = 1 / np.sqrt(2)
beta0 = 1 / np.sqrt(2)

# Time evolution of the amplitudes under Hamiltonian H = (hbar*omega/2) * sigma_z
alpha_t = alpha0 * np.exp(-1j * omega * t_vals / 2)
beta_t = beta0 * np.exp(1j * omega * t_vals / 2)

# Function to map qubit state to Bloch sphere coordinates
def bloch_coords(alpha, beta):
    x = 2 * np.real(np.conj(alpha) * beta)
    y = 2 * np.imag(np.conj(alpha) * beta)
    z = np.abs(alpha)**2 - np.abs(beta)**2
    return x, y, z

# Compute Bloch sphere coordinates for each time step
x_vals, y_vals, z_vals = [], [], []
for a, b in zip(alpha_t, beta_t):
    x, y, z = bloch_coords(a, b)
    x_vals.append(x)
    y_vals.append(y)
    z_vals.append(z)

# Prepare Bloch sphere surface
u, v = np.mgrid[0:2*np.pi:60j, 0:np.pi:30j]
xs = np.cos(u) * np.sin(v)
ys = np.sin(u) * np.sin(v)
zs = np.cos(v)

# Plotting
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Draw Bloch sphere
ax.plot_surface(xs, ys, zs, color='lightblue', alpha=0.1, linewidth=0)

# Draw trajectory of qubit state
ax.plot(x_vals, y_vals, z_vals, color='red', label='Qubit state trajectory')
ax.scatter(x_vals[0], y_vals[0], z_vals[0], color='green', s=50, label='Start (t=0)')
ax.scatter(x_vals[-1], y_vals[-1], z_vals[-1], color='blue', s=50, label='End (t=1)')

# Aesthetic tweaks
ax.set_title("Qubit Evolution on Bloch Sphere (Z-rotation)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_box_aspect([1,1,1])  # Keep sphere proportions equal

plt.show()
