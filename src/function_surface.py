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
        
    def plot(self, ax=None):
        """
        Generate and display the function surface.
        """
        if ax==None:
            fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

        ax.plot_surface(self.x, self.y, self.z, cmap="viridis")
        ax.set_xlabel("Season Record Weight")
        ax.set_ylabel("Number of Races Run Weight")
        ax.set_title("Surface of Loss Function for Predicting Personal Record")

