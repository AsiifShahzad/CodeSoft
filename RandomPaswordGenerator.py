import random
import string

def generatePassword(length):
    letters = string.ascii_letters
    digits = string.digits
    characters = letters + digits

     Use random.choices to allow repeating characters
    passwordCharacters = random.choices(characters,k=length)

     Convert the list of characters to a string
    password = ''.join(passwordCharacters)

    return password

 Get the desired password length from the user
password_length = int(input("Enter the desired password length: "))

 Generate and print the password
password = generatePassword(password_length)
print("Generated Password:", password)