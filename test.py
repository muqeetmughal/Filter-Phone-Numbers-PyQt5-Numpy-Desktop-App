import math
import numpy as np
import pandas as pd
alist = [9488468339,7858401770,3894795005,7932666855,5850219943,4719131691
,8069298444,9108144604,2705313840,5413949345,8438947804,1220069578
,4476846600,3046518657,7041184338,8593838142,5904314041,4357999134
,7555900607,4790296017,4609747049,5402353441,8235027874,4650525358
,2628162976,7059858785,2371458467,5178110972,6371929722,5128127583
,2983437332,4855759853,9244468370,7089879445,6762834913,4096939334
,4438799041,7731627352,7991124052,5564371093,9015769628,9725065640
,3721764209,6823200950,2376727013,6373642026,6953782151,8859076004
,1956526604,8730208797,7593452916,5608255305,9614656914,8027884189
,2267209566]
array = np.array(alist)

def return_tuple(array):

    print(f"Length of array is: {len(array)}")


    nearest_perfect_square_of_array_length = round(math.sqrt(len(array)))**2
    if nearest_perfect_square_of_array_length < len(array):

        nearest_perfect_square_of_array_length = (round(math.sqrt(len(array)))+1)**2
    # > 1000000000

    print(f"Nearest Perfect Square is: {nearest_perfect_square_of_array_length}")


    if nearest_perfect_square_of_array_length > 1000000:
        row = 1000000
        col = nearest_perfect_square_of_array_length//row+1
        print(row,"X",col)
        return row, col
        

    else:
        row = int(nearest_perfect_square_of_array_length ** 0.5)
        col = row
        print(row,"X",col)
        return row, col

array = np.array(alist)



out = np.full((return_tuple(array)), np.nan, dtype='object')

out.ravel()[:len(alist)] = array



# print(out)
pd.DataFrame(out).to_csv("output.csv", index=False, header=False)

