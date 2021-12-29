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


def values_for_reshape_sorted(array):

    array_length = len(array)


    nearest_perfect_square_of_array_length = round(math.sqrt(array_length))**2

    print("Nearest PS is :", nearest_perfect_square_of_array_length)

    if array_length >= nearest_perfect_square_of_array_length:

        nearest_perfect_square_of_array_length = (round(math.sqrt(array_length))+1)**2

    print("Nearest PS 2 is :", nearest_perfect_square_of_array_length)
    
    col = 5
    row = nearest_perfect_square_of_array_length//col

    if row > 1000000:
        col = col + 1
        row = 1000000

    print(row, col)

    return row, col



def values_for_reshape_unsorted(array):

    array_length = len(array)

    row = 1000000

    col = array_length//row

    if array_length > (row*col):
        col = col+1

    print(row, col)

    return row, col
