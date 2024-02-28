import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Create example car dataset
car_data = {
    'Company': ['Toyota', 'Honda', 'Ford', 'Tesla', 'BMW'],
    'Model': ['Corolla', 'Civic', 'Fiesta', 'Model S', '3 Series'],
    'Volume': [1.8, 1.5, 1.2, 2.0, 2.0],  # in liters
    'Weight': [1200, 1100, 1000, 1800, 1500],  # in kg
    'CO2': [100, 90, 80, 120, 110]  # in g/km
}

df = pd.DataFrame(car_data)

# Define independent variables (features) and dependent variable (target)
X = df[['Volume', 'Weight']]
y = df['CO2']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perform multiple linear regression using scikit-learn
model = LinearRegression()
model.fit(X_train, y_train)

# Print the coefficients
print('Coefficients:', model.coef_)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print('R-squared:', model.score(X_test, y_test))

# Perform multiple linear regression using statsmodels (for more statistical analysis)
X_train_sm = sm.add_constant(X_train)  # adding a constant
sm_model = sm.OLS(y_train, X_train_sm).fit()
print(sm_model.summary())
