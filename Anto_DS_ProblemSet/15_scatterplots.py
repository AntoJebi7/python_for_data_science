import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame with team name and rank
data = {
    'Team': ["Australia", "Bangladesh", "England", "India", "Srilanka"],
    'Points': [2500, 1000, 2000, 3000, 1500],
    'Rank': [1, 5, 3, 2, 4]
}

df = pd.DataFrame(data)

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Points'], df['Rank'])
plt.title('Scatter Plot of Points vs Rank')
plt.xlabel('Points')
plt.ylabel('Rank')
plt.grid(True)
plt.show()
