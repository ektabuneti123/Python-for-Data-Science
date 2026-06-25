# Question 1: Write a Python program to demonstrate tuple operations such as creating a tuple, indexing, slicing, concatenation, reversing, counting elements, finding index, membership testing, list-to-tuple conversion, sorting, repetition, and tuple immutability.

t1 = ("Ekta", "S077", "MVLU College", "Python", "Python")

print("Tuple:", t1)

# Indexing
print("First Element:", t1[0])

# Slicing
print("Sliced Tuple:", t1[1:4])

# Concatenation
t2 = ("BSc CS", "Sem 3")
concat_tuple = t1 + t2
print("Concatenated Tuple:", concat_tuple)

# Reversing
print("Reversed Tuple:", t1[::-1])

# Count
print("Count of Python:", t1.count("Python"))

# Index
print("Index of MVLU College:", t1.index("MVLU College"))

# Membership Testing
print("Ekta" in t1)

# List to Tuple Conversion
lst = ["OS", "TOC", "PDS"]
new_tuple = tuple(lst)
print("List to Tuple:", new_tuple)

# Sorting
num_tuple = (5, 2, 8, 1, 4)
sorted_tuple = tuple(sorted(num_tuple))
print("Sorted Tuple:", sorted_tuple)

# Repetition
print("Repeated Tuple:", ("Python",) * 3)

# Tuple Immutability
try:
    t1[0] = "Student"
except TypeError:
    print("Tuple is immutable.")
