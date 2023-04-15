import random
import string

print("\n********** Welcome To The Password Generator ***********\n")

length = int(input("Enter the password length: "))

# Define a set of characters to choose from
chars = string.ascii_letters + string.digits + string.punctuation

# Generate a random password
password = ''.join(random.choice(chars) for i in range(length))

print("The generated password is:", password)
#
# There are a few ways to make this password generator stronger:
#
# Increase the complexity of the character set: Consider adding more
# characters to the set of characters to choose from. This will increase the number
# of possible combinations and make it harder for someone to guess the password.
#
# Make the password longer: A longer password is generally more secure.
# Consider increasing the minimum length of the password.
#
# Use a mix of character types: Consider including a mix of upper and lower case letters,
# numbers, and special characters. This will make the password more complex and harder to guess.
#
# Avoid predictable patterns: Avoid using predictable patterns like consecutive letters
# or numbers. These patterns can make the password easier to guess.
#
# Avoid common phrases or words: Avoid using common phrases or words as passwords, as
# these can be easily guessed by attackers.

# or simply
# import random
# print("\n********** Welcome To The Password Generator ***********\n")
# chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*1234567890"
# length = int(input("Enter the password length.........\n"))
# password = ""
#
# for a in range(length):
#     password+=random.choice(chars)
#
# print("The passwod generated is : ",password)
