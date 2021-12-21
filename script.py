import pandas as pd
import numpy as np
import datetime


class Convertor:


    def read_csv_file(self, path, header=None):

        try:
            dataframe = pd.read_csv(path,header=header)

            np_array = dataframe.to_numpy().flatten()

            return np_array
        except FileNotFoundError as e:
            print(e)

    def filter_array(self, left_file_array, right_file_array):

        unique_array = np.setdiff1d(right_file_array, left_file_array).reshape(-1)

        return unique_array

    def array_to_csv(self, np_array, filename,header=None, index=None):

        try:
            dataframe = pd.DataFrame(np_array)
            dataframe.to_csv(f"{filename}.csv",header=header, index=index)

            return "File Saved!"

        except Exception as e:
            return str(e)
       