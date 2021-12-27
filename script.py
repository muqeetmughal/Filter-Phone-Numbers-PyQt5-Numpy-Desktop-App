from numpy.lib.arraysetops import unique
import pandas as pd
import numpy as np
import datetime
from utils import values_for_reshape

class Convertor:


    def read_csv_file(self, path, header=None):

        try:
            dataframe = pd.read_csv(path,header=header)



            np_array = dataframe.to_numpy().flatten()

            print("Current Read Array is: ",np_array)

            return np_array


        except FileNotFoundError as e:
            print(e)

    def filter_array(self, left_file_array, right_file_array):

        array_difference = np.setdiff1d(right_file_array, left_file_array).reshape(-1)

        print("Array Difference is: ",array_difference)

        unique_array = np.array([el for el in array_difference.astype(str) if len(el) == 10])

        print("Unique Array is: ",unique_array)

        return np.unique(unique_array)

    def array_to_csv(self, np_array, filename,header=None, index=None):

                
        out = np.full((values_for_reshape(np_array)), np.nan, dtype='object')

        out.ravel()[:len(np_array)] = np_array


        try:
            dataframe = pd.DataFrame(out)
            dataframe.to_csv(f"{filename}",header=header, index=index)

            return "File Saved!"

        except Exception as e:
            return str(e)

    def reshape_array(self, array):

        array = np.sort(array)

        if len(array) < 1000000:

            target = array.reshape(len(array)//10,-1)

        elif len(array) > 1000000:
            # target = array.reshape()
            pass
        else:

            target = array

        return target


# import pandas as pd
# import numpy as np
# import datetime

# instance = Convertor()


# array = np.random.randint(1111111111,9999999999, size=(1000), dtype=np.int64)

# # print(x)
# unique_array = instance.reshape_array(array)

# new_df = pd.DataFrame(unique_array)


# new_df.to_csv("unique_file.csv",header=None, index=None)


