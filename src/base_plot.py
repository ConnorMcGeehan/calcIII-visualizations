import numpy as np
import matplotlib.pyplot as plt

class BasePlot:
    def __init__(self) -> None:
        self.w1_range = np.linspace(0.5, 1.5, 50)
        self.w2_range = np.linspace(1, 2, 50)
        self.alpha = float
        # w1 is number of races run
        self.w1: float
        # w2 is season record
        # trying to predict personal record
        self.w2: float
        self.data_list = list
        X, Y = np.meshgrid(self.w1_range, self.w2_range)

    def compute_loss_grid(self):
        """
        Computes the loss value for each possible weight combination.
        TODO
        """
        pass
    
    def compute_gradient(self):
        """
        Computes the gradient component of the plot for the w1 and w2
        TODO
        """
        pass
    
    def update_w1(self, update)  -> None:
        """
        Updates the value of w1 when the slider is adjusted  

        :param update: The new value of w1
        """
        pass
    
    def update_w2(self, update) -> None:
        """
        Updates the value of w2 when the slider is adjusted
        
        :param update: New value of w2
        """
        pass
    
    def update_alpha(self, update) -> None:
        """
        Updates the value of alpha when the slider is adjusted
        
        :param update: New value of alpha
        """
        pass
    
    def update_plot(self) -> None:
        """
        Updates the plot whenever the value of the weights or alpha are changed
        """
        pass