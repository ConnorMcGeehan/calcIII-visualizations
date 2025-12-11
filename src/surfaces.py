import numpy as np
import matplotlib.pyplot as plt

# Define a grid
x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

a = np.linspace(-2,2, 50)
b = np.linspace(-2,2,50)
A, B = np.meshgrid(a,b)
C = A**2 - B**2

# Plot the surface
fig, axs = plt.subplots(1, 2, subplot_kw={"projection":"3d"})

axs[0].plot_surface(X, Y, Z, cmap="viridis")

axs[1].plot_surface(A, B, C, cmap="viridis")

plt.show()


