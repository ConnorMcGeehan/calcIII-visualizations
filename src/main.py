import numpy as np
import pandas as pd
from base_plot import BasePlot
from data_point import DataPoint


class Main:
    def __init__(self):
        self.data_list = []

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

        for i in range(len(df)):
            data_point = DataPoint(season_records[i], num_races[i], personal_records[i])
            self.data_list.append(data_point)

    def run(self):
        """
        The function that runs the project
        """
        self.get_data()


m = Main()
m.run()