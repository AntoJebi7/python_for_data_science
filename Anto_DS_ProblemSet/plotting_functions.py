import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
iris_df = pd.read_csv(url, names=names)

# Display the first few rows of the dataset
print(iris_df.head())

# Pairplot
sns.pairplot(iris_df, hue='class', markers=["o", "s", "D"])
plt.title('Pairplot of Iris dataset')
plt.show()

# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris_df, orient='h')
plt.title('Boxplot of Iris dataset')
plt.show()

# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x='class', y='petal-length', data=iris_df)
plt.title('Violin plot of petal length by class')
plt.show()

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(iris_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Iris dataset')
plt.show()
