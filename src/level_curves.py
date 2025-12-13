from base_plot import BasePlot
import numpy as np
import matplotlib.pyplot as plt
from typing import Optional


class LevelCurves(BasePlot):
    """Level curves plotter.

    Inherits from `BasePlot`
    """

    def plot(self):
        """
        Draw level curves for the loss function/grid computed by `BasePlot`.
        :returns: The level curves plot for the function defined in `BasePlot`
        """
        pass

    def update_plot(self, ax: Optional[plt.Axes] = None, **kw):
        """
        Convenience wrapper to redraw/update the level curves on when weights or
        alpha are updated.
        """
        pass
