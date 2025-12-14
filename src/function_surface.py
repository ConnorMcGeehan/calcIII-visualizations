from base_plot import BasePlot
import numpy as np
import matplotlib.pyplot as plt


class FunctionSurface(BasePlot):
    """A class to visualize a 3D function surface using matplotlib."""
    
    def __init__(self):
        super().__init__()
        self.x = self.X
        self.y = self.Y
        self.z = self.Z
        self.grad_x = self.grad_X
        self.grad_y = self.grad_Y
        self.curr_z = self.current_z

        
    def plot(self, ax=None):
        """
        Generate and display the function surface.
        """
        if ax==None:
            fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

        ax.plot_surface(self.x, self.y, self.z, cmap="viridis")

        ax.scatter([self.w1], [self.w2], [self.curr_z], marker=".", s=100, c="red")
        ax.quiver(self.w1, self.w2, self.curr_z, self.grad_x, self.grad_y, 0,
                   color='red', length = 0.3, linewidth=2)
        
        ax.set_xlabel("Season Record Weight")
        ax.set_ylabel("Number of Races Run Weight")
        ax.set_title("Surface of Loss Function for Predicting Personal Record")

