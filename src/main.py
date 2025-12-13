import numpy as np
import pandas as pd
from function_surface import FunctionSurface
from data_point import DataPoint


class Main:

    def run(self):
        """
        The function that runs the project
        """
        FunctionSurface().plot()


Main().run()