# Practical No. 3a

print("Ekta S078")
print("-------------------------------------------------------------------------")

# Step 1: Ask the user to enter the text
text_to_search = input("Enter the text: ")

# Step 2: Ask the user to enter the word to search
search_word = input("Enter the word to search for: ")

# Step 3: Search the word in the text
if search_word in text_to_search:
    print("The word", search_word, "was found in the text.")
else:
    print("The word", search_word, "was NOT found in the text.")
