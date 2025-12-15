import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from function_surface import FunctionSurface
from level_curves import LevelCurves
from base_plot import BasePlot

class UI:
    def __init__(self):
        self.base_plot = BasePlot()
        self.fig = plt.figure(figsize=(14, 7))
        plt.subplots_adjust(bottom=0.25)
        
        self.ax1 = self.fig.add_subplot(121, projection='3d')
        self.ax2 = self.fig.add_subplot(122)
        
        self.surface = FunctionSurface(self.base_plot)
        self.curves = LevelCurves(self.base_plot)
        
        self.initial_plot()
        self.setup_sliders()
        
    def initial_plot(self):
        """Draw the initial plots"""
        self.surface.plot(ax=self.ax1)
        self.curves.plot(ax=self.ax2)
        
    def setup_sliders(self):
        ax_w1 = plt.axes([0.2, 0.15, 0.6, 0.03])
        ax_w2 = plt.axes([0.2, 0.10, 0.6, 0.03])
        ax_alpha = plt.axes([0.2, 0.05, 0.6, 0.03])
        
        self.slider_w1 = Slider(ax_w1, 'w1', -3, 3, valinit=0)
        self.slider_w2 = Slider(ax_w2, 'w2', -3, 3, valinit=0)
        self.slider_alpha = Slider(ax_alpha, 'alpha', 0, 10, valinit=0)

        self.slider_w1.on_changed(lambda val: self.on_slider_change())
        self.slider_w2.on_changed(lambda val: self.on_slider_change())
        self.slider_alpha.on_changed(lambda val: self.on_slider_change())

    def on_slider_change(self):
        """
        Callback function when any slider changes.
        Updates the base plot and redraws both figures.
        """
        self.base_plot.w1 = self.slider_w1.val
        self.base_plot.w2 = self.slider_w2.val
        self.base_plot.alpha = self.slider_alpha.val
        
        self.base_plot.update_plot()
        
        self.ax1.clear()
        self.ax2.clear()
        
        self.surface.plot(ax=self.ax1)
        self.curves.plot(ax=self.ax2)
        
        self.fig.canvas.draw()
    
    def show(self):
        plt.show()