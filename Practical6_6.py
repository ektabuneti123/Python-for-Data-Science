print("Name - Ekta Buneti")
print("Roll No - S078")
import matplotlib.pyplot as plt

x = [5, 7, 8, 7, 6, 9, 5]
y = [99, 86, 87, 88, 100, 86, 103]

plt.scatter(x, y, color="green", s=100)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot")

plt.show()
