import pandas as pd

# Creating a sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data, index=['Row1', 'Row2', 'Row3'])

print("Original DataFrame:")
print(df)

# Dropping rows by index label
rows_to_drop = ['Row1', 'Row3']
df = df.drop(rows_to_drop)

print("\nDataFrame after dropping rows:")
print(df)


'''
Original DataFrame:
      A  B  C
Row1  1  4  7
Row2  2  5  8
Row3  3  6  9

DataFrame after dropping rows:
      A  B  C
Row2  2  5  8

'''