import pandas as pd
import matplotlib.pyplot as plt

# Read from text file
iris_text_df = pd.read_csv('iris.txt', header=None, names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'])

# Read from Excel file
iris_excel_df = pd.read_excel('iris.xlsx', sheet_name='Sheet1')

# Read from the web
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_web_df = pd.read_csv(url, header=None, names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'])

# Explore commands for descriptive analytics

# Summary statistics
print("Summary Statistics:")
print(iris_text_df.describe())
print()

# Data types and missing values
print("Data Types and Missing Values:")
print(iris_text_df.info())
print()

# Count of unique values in categorical columns
print("Count of Unique Values in Categorical Columns:")
print(iris_text_df['Species'].value_counts())
print()

# Histograms
print("Histograms:")
iris_text_df.hist(figsize=(10, 8))
plt.show()
print()

# Boxplots
print("Boxplots:")
iris_text_df.boxplot(figsize=(10, 8))
plt.show()
