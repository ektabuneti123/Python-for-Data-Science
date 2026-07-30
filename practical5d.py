# EktaS078
# Practical 5(d)
# Demonstrate filtering pandas Series with Boolean arrays

import pandas as pd

# Read the Excel dataset
df = pd.read_excel("StressLevelDataset.xlsx")

# Create a Series from the stress_level column
series = pd.Series(df["stress_level"])

# Filter the Series using a Boolean condition
filtered_series = series[series > 1]

# Display the filtered Series
print("Filtered Pandas Series:")
print(filtered_series)
