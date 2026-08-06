print("Name - Ekta Buneti")
print("Roll No - S078")
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

data = np.random.randn(100)
x
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")

plt.subplot(2, 2, 2)
plt.bar(x, y)
plt.title("Bar Chart")

plt.subplot(2, 2, 3)
plt.scatter(x, y)
plt.title("Scatter Plot")

plt.subplot(2, 2, 4)
plt.hist(data, bins=10)
plt.title("Histogram")

plt.tight_layout()

plt.show()
