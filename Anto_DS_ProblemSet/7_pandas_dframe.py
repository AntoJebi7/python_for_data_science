import pandas as pd

# List of dictionaries
data = [
    {'A': 1, 'B': 2, 'C': 3},
    {'A': 4, 'B': 5, 'C': 6},
    {'A': 7, 'B': 8, 'C': 9}
]

# Row and column indices
row_index = ['Row1', 'Row2', 'Row3']
column_index = ['A', 'B', 'C']

# Create DataFrame
df = pd.DataFrame(data, index=row_index, columns=column_index)

print(df)


'''
      A  B  C
Row1  1  2  3
Row2  4  5  6
Row3  7  8  9

'''