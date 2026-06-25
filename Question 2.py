# Question 2: Write a Python program to perform various list operations such as finding the largest number, removing duplicates, counting even numbers, storing and displaying 5 numbers in a list, calculating the average of list elements using a function, converting a string into a list of characters, and joining list elements into a single string.

numbers = [10, 20, 30, 20, 40, 50, 10]

# Largest Number
print("Largest Number:", max(numbers))

# Remove Duplicates
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)

# Count Even Numbers
even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print("Count of Even Numbers:", even_count)

# Store and Display 5 Numbers
list5 = [1, 2, 3, 4, 5]
print("List of 5 Numbers:", list5)

# Average using Function
def average(lst):
    return sum(lst) / len(lst)

print("Average:", average(list5))

# Convert String into List of Characters
text = "Ekta"
char_list = list(text)
print("List of Characters:", char_list)

# Join List Elements into a String
words = ["MVLU", "College"]
joined_string = " ".join(words)
print("Joined String:", joined_string)
