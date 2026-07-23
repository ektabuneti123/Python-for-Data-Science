import numpy as np

arr = np.array([15, 40, 25, 60, 35, 60])

# Finding the maximum value
max_value = np.max(arr)

# Filtering the maximum value
filter_arr = arr == max_value

print("Original Array:")
print(arr)

print("Maximum Value:", max_value)

print("Filtered Array:")
print(arr[filter_arr])
