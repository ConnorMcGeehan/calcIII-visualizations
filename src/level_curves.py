from base_plot import BasePlot
import numpy as np
import matplotlib.pyplot as plt


class LevelCurves(BasePlot):

    def __init__(self):
        super().__init__()
        self.x = self.X
        self.y = self.Y
        self.z = self.Z

    def plot(self):
        """
        Draw level curves for the loss function/grid computed by `BasePlot`.
        :returns: The level curves plot for the function defined in `BasePlot`
        """
        fig, ax = plt.subplots()
        CS = ax.contour(self.x, self.y, self.z)
        ax.clabel(CS, fontsize=10)
        plt.show()

    def update_plot(self):
        """
        Convenience wrapper to redraw/update the level curves on when weights or
        alpha are updated.
        """
        pass
