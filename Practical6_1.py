print("Name - Ekta Buneti")
print("Roll No - S078")
'''1. Line Plot Basics
o Plot the following data using a line chart:
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
o Add a title "Simple Line Plot".
o Label the X-axis as "Numbers" and Y-axis as "Doubles".'''



import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o')

# Add title and axis labels
plt.title("Simple Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")

# Display the plot
plt.show()


