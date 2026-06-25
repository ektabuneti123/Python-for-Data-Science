# Question 2b: Write a Python code to sort the nested tuple using sorted() function

subjects = (
    ("Python", 3),
    ("Operating System", 1),
    ("TOC", 2)
)

sorted_tuple = tuple(sorted(subjects, key=lambda x: x[1]))

print("Original Nested Tuple:")
print(subjects)

print("\nSorted Nested Tuple:")
print(sorted_tuple)
