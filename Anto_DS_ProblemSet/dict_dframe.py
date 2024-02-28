import pandas as pd

# Dictionary with arrays as values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}

# Create DataFrame from the dictionary
df = pd.DataFrame.from_dict(data)

# Print the DataFrame
print("DataFrame:")
print(df)

'''
DataFrame:
      Name  Age         City
0    Alice   25     New York
1      Bob   30  Los Angeles
2  Charlie   35      Chicago
3    David   40      Houston

'''