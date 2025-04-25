import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


omega = 2 * np.pi                     
t_vals = np.linspace(0, 1, 200)       


alpha0 = np.sqrt((2 + np.sqrt(2)) / 4)
beta0 = np.sqrt((2 - np.sqrt(2)) / 4)


alpha_t = alpha0 * np.exp(-1j * omega * t_vals / 2)
beta_t = beta0 * np.exp(1j * omega * t_vals / 2)


def bloch_coords(alpha, beta):
    x = 2 * np.real(np.conj(alpha) * beta)
    y = 2 * np.imag(np.conj(alpha) * beta)
    z = np.abs(alpha)**2 - np.abs(beta)**2
    return x, y, z


x_vals, y_vals, z_vals = [], [], []
for a, b in zip(alpha_t, beta_t):
    x, y, z = bloch_coords(a, b)
    x_vals.append(x)
    y_vals.append(y)
    z_vals.append(z)


u, v = np.mgrid[0:2*np.pi:60j, 0:np.pi:30j]
xs = np.cos(u) * np.sin(v)
ys = np.sin(u) * np.sin(v)
zs = np.cos(v)


fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')


ax.plot_surface(xs, ys, zs, color='lightblue', alpha=0.1, linewidth=0)


ax.plot(x_vals, y_vals, z_vals, color='purple', label='Qubit state trajectory')
ax.scatter(x_vals[0], y_vals[0], z_vals[0], color='green', s=50, label='Start (t=0)')
ax.scatter(x_vals[-1], y_vals[-1], z_vals[-1], color='blue', s=50, label='End (t=1)')


ax.set_title(r"$\alpha = \sqrt{\frac{2 + \sqrt{2}}{4}}, \quad \beta = \sqrt{\frac{2 - \sqrt{2}}{4}}$")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
ax.set_box_aspect([1, 1, 1])

plt.show()
