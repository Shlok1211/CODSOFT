import random
import string

print("---------- PASSWORD GENERATOR ----------")
length = int(input('Enter the length of Password :- '))
print("----------------------------------------\n")

useUpper = input("Do you want to include Uppercase (y/n) ? ").lower()
useLower = input("Do you want to include Lowercase (y/n) ? ").lower()
useDigits = input("Do you want to include Digits (y/n) ? ").lower()
useSpecial = input("Do you want to include Special Characters (y/n) ? ").lower()

characters = ""

if useUpper == 'y':
    characters += string.ascii_uppercase
if useLower == 'y':
    characters += string.ascii_lowercase
if useDigits == 'y':
    characters += string.digits
if useSpecial == 'y':
    characters += string.punctuation

if characters == "":
    print("\nYou must select at least one character type !")
else:
    password = "".join(random.choice(characters)
    for i in range(length))
    print("\nYour password is :-",password)
