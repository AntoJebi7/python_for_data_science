import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Pima Indians Diabetes dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
diabetes_df = pd.read_csv(url, names=column_names)

# Bivariate analysis
# Scatter plot of Glucose vs. Insulin
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Glucose', y='Insulin', data=diabetes_df, hue='Outcome', palette='Set1')
plt.title('Scatter plot of Glucose vs. Insulin')
plt.xlabel('Glucose')
plt.ylabel('Insulin')
plt.show()

# Pairplot of selected variables
sns.pairplot(diabetes_df, vars=['Glucose', 'BMI', 'Age', 'BloodPressure'], hue='Outcome', palette='Set1')
plt.suptitle('Pairplot of Glucose, BMI, Age, and Blood Pressure', y=1.02)
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(diabetes_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Pima Indians Diabetes dataset')
plt.show()
