import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Column names for the UCI Diabetes dataset
column_names = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]

# Load the UCI Diabetes dataset with the specified column names
diabetes_df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/00463/Dataset_diabetes.csv", names=column_names, skiprows=1)

# Display the first few rows of the dataset
print(diabetes_df.head())

# Univariate analysis
# Histogram for 'Glucose' column
plt.figure(figsize=(8, 6))
sns.histplot(diabetes_df['Glucose'], bins=20, kde=True)
plt.title('Distribution of Glucose Levels')
plt.xlabel('Glucose Level')
plt.ylabel('Frequency')
plt.show()

# Boxplot for 'BMI' column
plt.figure(figsize=(8, 6))
sns.boxplot(x=diabetes_df['BMI'])
plt.title('Boxplot of BMI')
plt.xlabel('BMI')
plt.show()

# Violin plot for 'Age' column
plt.figure(figsize=(8, 6))
sns.violinplot(x=diabetes_df['Age'])
plt.title('Violin plot of Age')
plt.xlabel('Age')
plt.show()
