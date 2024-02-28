import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the UCI Diabetes dataset
url = "C:\Users\antoa\Downloads\archive\diabetes_merged_date-time-sorted.csv"
diabetes_df = pd.read_csv(url)

# Univariate analysis
# Histogram for 'Age' column
plt.figure(figsize=(8, 6))
sns.histplot(diabetes_df['Age'], bins=20, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Bivariate analysis
# Scatter plot for 'Age' vs. 'Glucose'
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Age', y='Glucose', data=diabetes_df)
plt.title('Scatter plot of Age vs. Glucose')
plt.xlabel('Age')
plt.ylabel('Glucose')
plt.show()
