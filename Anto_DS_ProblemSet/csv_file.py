import numpy as np

# Create a numpy array
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Save the numpy array to a CSV file
np.savetxt('my_array.csv', my_array, delimiter=',')

print("Array saved to my_array.csv")


'''
This code will save the my_array numpy array into a file named my_array.csv in the current
 working directory. Each element in the array will be separated by a comma in the CSV file. 
 You can specify different delimiters if needed.
'''