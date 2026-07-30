#EktaS078
# Practical 5(b)
# Show statistical information on the given dataset

import pandas as pd

# Read the Excel dataset
df = pd.read_excel("StressLevelDataset.xlsx")

# Display statistical information
print("Statistical Information:")
print(df.describe())
