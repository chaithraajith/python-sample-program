char = input("Enter a character: ")
if char.isalpha():
    print("The character is an alphabet.")
elif char.isdigit():
    print("The character is a digit.")
else:
    print("The character is a special character.")