sample_array = [3,45,34,234,234,63,234,64,23,543,234,756,345,5612,235,456,34,43,24,3452,43]


# print(len(sample_array))
#21
import math
def values_for_reshape(array):

    print(f"Length of array is: {len(array)}")


    nearest_perfect_square_of_array_length = round(math.sqrt(len(array)))**2
    if nearest_perfect_square_of_array_length < len(array):

        nearest_perfect_square_of_array_length = (round(math.sqrt(len(array)))+1)**2

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

