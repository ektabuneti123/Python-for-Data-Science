# EktaS078
# Practical 5(c)
# Create pandas Series from the given dataset

import pandas as pd

# Read the Excel dataset
df = pd.read_excel("StressLevelDataset.xlsx")

# Create a Series from one column
series = pd.Series(df["stress_level"])

# Display the Series
print("Pandas Series:")
print(series)
