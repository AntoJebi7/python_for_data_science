import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame with information about hours spent studying and exam score
np.random.seed(0)
data = {
    'Hours_Studied': np.random.randint(1, 10, 20),
    'Exam_Score': np.random.randint(50, 100, 20)
}

df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())

# Scatter plot to visualize the relationship between hours studied and exam score
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Hours_Studied', y='Exam_Score', data=df)
plt.title('Scatter Plot of Hours Studied vs Exam Score')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()

# Correlation analysis
correlation = df.corr()
print("\nCorrelation Matrix:")
print(correlation)

# Pairplot for bivariate analysis
sns.pairplot(df)
plt.title('Pairplot of Hours Studied and Exam Score')
plt.show()
