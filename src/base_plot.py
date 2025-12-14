import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data_point import DataPoint

class BasePlot:
    def __init__(self) -> None:
        self.w1_range = np.linspace(-1, 3, 50)
        self.w2_range = np.linspace(-2, 2, 50)
        self.alpha = 0
        # w1 is season record
        self.w1= 0
        # w2 is number of races run
        # trying to predict personal record
        self.w2 = 0
        self.data_list = []
        self.get_data()

        self.X, self.Y, self.Z = self.compute_loss_grid()
        self.grad_X, self.grad_Y = self.compute_gradient()
        self.current_z = self.compute_loss_at_point(self.w1, self.w2)

    def get_data(self):
        """
        Parses nationals_data.csv and stores the relevant rows/columns
        as `DataPoint` objects.
        :post: self.data_list is populated with `DataPoint` objects
        """
        df = pd.read_csv("./data/nationals_data.csv")
        
        personal_records = df["personal_record"]
        season_records = df["season_record"]
        num_races = df["number_races_run"]

        season_records = (season_records - season_records.mean()) / season_records.std()
        num_races = (num_races - num_races.mean()) / num_races.std()
        personal_records = (personal_records - personal_records.mean()) / personal_records.std()


        for i in range(len(df)):
            data_point = DataPoint(season_records[i], num_races[i], personal_records[i])
            self.data_list.append(data_point)

    def compute_loss_grid(self):
        """
        Computes the loss value for each possible weight combination.
        """
        X, Y = np.meshgrid(self.w1_range, self.w2_range)

        inner_terms = []
        for dp in self.data_list:
            loss = ((X*dp.get_season_record()) 
                    + (Y*dp.get_num_races()) 
                    - (dp.get_personal_record()))
            
            inner_terms.append(loss**2)
        
        Z = (1/len(self.data_list)) * sum(inner_terms) + (self.alpha*((X**4 + Y**4)))

        return X, Y, Z

    
    def compute_gradient(self):
        """
        Computes the gradient at the current point (self.w1, self.w2)
        """
        w1_mse_grad = 0
        w2_mse_grad = 0
        
        for dp in self.data_list:
            residual = (
                (self.w1 * dp.get_season_record()) 
                + (self.w2 * dp.get_num_races()) 
                - dp.get_personal_record()
            )
            
            w1_mse_grad += residual * dp.get_season_record()
            w2_mse_grad += residual * dp.get_num_races()
        
        w1_mse_grad = (2 / len(self.data_list)) * w1_mse_grad
        w2_mse_grad = (2 / len(self.data_list)) * w2_mse_grad
        
        w1_partial = w1_mse_grad + (4 * self.alpha * (self.w1**3))
        w2_partial = w2_mse_grad + (4 * self.alpha * (self.w2**3))

        return w1_partial, w2_partial
    
    def compute_loss_at_point(self, w1, w2):
        """
        Computes the loss at a specific point
        
        :param w1: The x-value of the point (weight 1)
        :param w2: The y-value of the point (weight 2)
        :returns: The z-value for the function L(w1, w2)
        """
        sq_error = 0
        for dp in self.data_list:
            loss = (w1*dp.get_season_record()) + (w2*dp.get_num_races()) - dp.get_personal_record()
            sq_error += loss**2

        mse = sq_error/len(self.data_list)
        z = mse + (self.alpha*(self.w1**4 + self.w2**4))
        return z


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