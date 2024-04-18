def cnv(name):
    # Convert the name to lowercase for case-insensitivity
    name = name.lower()
    
    # Calculate the numeric value of the name
    name_value = sum(ord(char) - ord('a') + 1 for char in name if char.isalpha())
    
    return name_value

# Get input from the user
ni = input("Enter a name: ")

# Calculate and display the numeric value of the name
result = cnv(ni)
print(f"value of {ni} is: {result}")
