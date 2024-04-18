from cgi import print_form
import sys
filename = input("Enter filename: ")
with open(filename, "r") as f:
    contents = f.read()
letter_counts = {}
for c in contents:
    if c.isalpha():
        letter = c.lower()
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
print("Letter Counts:")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")

