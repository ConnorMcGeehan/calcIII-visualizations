import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from function_surface import FunctionSurface
from level_curves import LevelCurves

class UI:
    def __init__(self):
        self.fig = plt.figure(figsize=(14, 7))
        plt.subplots_adjust(bottom=0.25)
        
        self.ax1 = self.fig.add_subplot(121, projection='3d')
        self.ax2 = self.fig.add_subplot(122)
        
        self.surface = FunctionSurface()
        self.curves = LevelCurves()
        
        self.setup_sliders()
        
    def setup_sliders(self):
        ax_w1 = plt.axes([0.2, 0.15, 0.6, 0.03])
        ax_w2 = plt.axes([0.2, 0.10, 0.6, 0.03])
        ax_alpha = plt.axes([0.2, 0.05, 0.6, 0.03])
        
        self.slider_w1 = Slider(ax_w1, 'w1', -3, 3, valinit=0)
        self.slider_w2 = Slider(ax_w2, 'w2', -3, 3, valinit=0)
        self.slider_alpha = Slider(ax_alpha, 'alpha', 0, 10, valinit=0)

    
    def show(self):
        self.surface.plot(ax=self.ax1)
        self.curves.plot(ax=self.ax2)
        plt.show()