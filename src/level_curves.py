from base_plot import BasePlot
import numpy as np
import matplotlib.pyplot as plt


class LevelCurves(BasePlot):

    def __init__(self):
        super().__init__()
        self.x = self.X
        self.y = self.Y
        self.z = self.Z

    def plot(self, ax=None):
        """
        Draw level curves for the loss function/grid computed by `BasePlot`.
        :returns: The level curves plot for the function defined in `BasePlot`
        """
        if ax==None:
            fig, ax = plt.subplots()

        contour = ax.contour(self.x, self.y, self.z)
        ax.clabel(contour, fontsize=10)
        ax.scatter([self.w1], [self.w2], c="red", s=100)
        ax.quiver(self.w1, self.w2, self.grad_X, self.grad_Y,
                   color='red', scale=15)

        ax.set_xlabel("Season Record Weight")
        ax.set_ylabel("Number of Races Run Weight")
        ax.set_title("Level Curves of Loss Function for Predicting Personal Record")
