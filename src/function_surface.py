from base_plot import BasePlot
import numpy as np
import matplotlib.pyplot as plt


class FunctionSurface():
    """A class to visualize a 3D function surface using matplotlib."""
    
    def __init__(self, base_plot):
        self.bp = base_plot

        
    def plot(self, ax=None):
        """
        Generate and display the function surface.
        """
        if ax==None:
            fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

        ax.plot_surface(self.bp.X, self.bp.Y, self.bp.Z, cmap="viridis")

        ax.scatter([self.bp.w1], [self.bp.w2], [self.bp.current_z], marker=".", s=100, c="red")
        ax.quiver(self.bp.w1, self.bp.w2, self.bp.current_z, self.bp.grad_X, self.bp.grad_Y, 0,
                   color='red', length = 0.3, linewidth=2)
        
        ax.set_xlabel("Season Record Weight")
        ax.set_ylabel("Number of Races Run Weight")
        ax.set_title("Surface of Loss Function for Predicting Personal Record")