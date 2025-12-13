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
        self.w1= 0.5
        # w2 is number of races run
        # trying to predict personal record
        self.w2 = 2
        self.data_list = []
        self.get_data()

        self.X, self.Y, self.Z = self.compute_loss_grid()

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