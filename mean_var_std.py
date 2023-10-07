#Mean-Variance-StandardDeviation Calculator(FreeCodeCamp 1st Project)
#7th of October, 2023

#Import NumPy
import numpy as np

#Initialise the List to be analysed.
my_list = []

#The calculate() function...
def calculate(my_list):
    #Initialising the dictionary for output 
    my_result = {}

    #Control Input: Raise a ValueError if the number of List items is NOT 9.
    if len(my_list) != 9:
        raise ValueError("Number of items in list must be 9!")
    else:
        #Convert List into a flattened array and a 3x3 1-D array
        array_flat = np.asarray(my_list)
        array_matrix = np.reshape(array_flat,(3,3))

        #Calculation on flattened array
        mean_flat = array_flat.mean()
        var_flat = round((array_flat.var()),2)
        std_flat = round((array_flat.std()),2)
        max_flat = array_flat.max()
        min_flat = array_flat.min()
        sum_flat = array_flat.sum()

        #Calculation on 3x3 1-D array
        #Calcultion on first row 
        mean_row1 = array_matrix[0,:].mean()
        var_row1 = round((array_matrix[0, :].var()),2)
        std_row1 = round((array_matrix[0, :].std()),2)
        max_row1 = array_matrix[0, :].max()
        min_row1 = array_matrix[0, :].min()
        sum_row1 = array_matrix[0, :].sum()


        #Calculation on the second row
        mean_row2 = array_matrix[1, :].mean()
        var_row2 = round((array_matrix[1, :].var()),2)
        std_row2 = round((array_matrix[1, :].std()),2)
        max_row2 = array_matrix[1, :].max()
        min_row2 = array_matrix[1, :].min()
        sum_row2 = array_matrix[1, :].sum()

        #Calculation on the thrid row 
        mean_row3 = array_matrix[2, :].mean()
        var_row3 = round((array_matrix[2, :].var()),2)
        std_row3 = round((array_matrix[2, :].std()),2)
        max_row3 = array_matrix[2, :].max()
        min_row3 = array_matrix[2, :].min()
        sum_row3 = array_matrix[2, :].sum()

        #Calculation on the first column
        mean_col1 = array_matrix[: ,0].mean()
        var_col1 = round((array_matrix[: ,0].var()),2)
        std_col1 = round((array_matrix[: ,0].std()),2)
        max_col1 = array_matrix[: ,0].max()
        min_col1 = array_matrix[: ,0].min()
        sum_col1 = array_matrix[: ,0].sum()

        #Calculation on the second column
        mean_col2 = array_matrix[: ,1].mean()
        var_col2 = round((array_matrix[: ,1].var()),2)
        std_col2 = round((array_matrix[: ,1].std()),2)
        max_col2 = array_matrix[: ,1].max()
        min_col2 = array_matrix[: ,1].min()
        sum_col2 = array_matrix[: ,1].sum()

        #Calculation on the thrid column
        mean_col3 = array_matrix[: ,2].mean()
        var_col3 = round((array_matrix[: ,2].var()),2)
        std_col3 = round((array_matrix[: ,2].std()),2)
        max_col3 = array_matrix[: ,2].max()
        min_col3 = array_matrix[: ,2].min()
        sum_col3 = array_matrix[: ,2].sum()

        #My Result...
        my_result = {
            'Mean: ':[[mean_row1, mean_row2, mean_row3], [mean_col1, mean_col2, mean_col3], mean_flat],
            'Variance':[[var_row1, var_row2, var_row3], [var_col1, var_col2, var_col3], var_flat],
            'Standard Deviation': [[std_row1, std_row2, std_row3], [std_col1, std_col2, std_col3], std_flat],
            'Maximum': [[max_row1, max_row2, max_row3], [max_col1, max_col2, max_col3], max_flat],
            'Minimum': [[min_row1, min_row2, min_row3], [min_col1, min_col2, min_col3], min_flat],
            'Sum': [[sum_row1, sum_row2, sum_row3], [sum_col1, sum_col2, sum_col3], sum_flat]
        }

    return my_result
        
#The Main Function...
def main():
    for i in range(0,9):
        a = int(input("Enter item {}:".format(i+1)))
        my_list.append(a)

    #Using calculate() function..
    result = calculate(my_list)
    print(result)

if __name__ == '__main__':
     main()
