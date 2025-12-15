from base_plot import BasePlot
import numpy as np
import matplotlib.pyplot as plt


class LevelCurves():

    def __init__(self, base_plot):
        self.bp = base_plot

    def plot(self, ax=None):
        """
        Draw level curves for the loss function/grid computed by `BasePlot`.
        :returns: The level curves plot for the function defined in `BasePlot`
        """
        if ax==None:
            fig, ax = plt.subplots()

        contour = ax.contour(self.bp.X, self.bp.Y, self.bp.Z)
        ax.clabel(contour, fontsize=10)
        ax.scatter([self.bp.w1], [self.bp.w2], c="red", s=100)
        ax.quiver(self.bp.w1, self.bp.w2, self.bp.grad_X, self.bp.grad_Y,
                   color='red', scale=15)

        ax.set_xlabel("Season Record Weight")
        ax.set_ylabel("Number of Races Run Weight")
        ax.set_title("Level Curves of Loss Function for Predicting Personal Record")