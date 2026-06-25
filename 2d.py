# Question 2d: Write a Python code to check immutability property of Python tuples

student = ("Ekta", "S077", "BSc CS")

print("Original Tuple:", student)

try:
    student[0] = "Python"
except TypeError:
    print("Tuple is immutable. Elements cannot be changed.")
