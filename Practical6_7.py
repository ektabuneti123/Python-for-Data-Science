print("Name - Ekta Buneti")
print("Roll No - S078")
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(100)

plt.hist(data, bins=20)

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")

plt.grid(True)

plt.show()
