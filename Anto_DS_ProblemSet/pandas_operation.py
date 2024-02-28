import pandas as pd
# Load the Iris dataset
iris_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

# Display the first few rows of the dataset
print(iris_df.head())
import pandas as pd
# Load the Iris dataset into a DataFrame
iris_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

# Display the DataFrame
print(iris_df)
import pandas as pd
# Load the Iris dataset into a DataFrame
iris_df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
# Assign column names
iris_df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
# Filter records with species Iris-setosa
setosa_df = iris_df[iris_df['species'] == 'Iris-setosa']
# Display the filtered DataFrame
print(setosa_df)

