# Snake, Water and Gun is a variation of the children's game ' \
# '"rock-paper-scissors" where players use hand gestures to represent a ' \
#  'snake, water, or a gun. The gun beats the snake,' \
# ' the water beats the gun, and the snake beats the water. ' \
#   'Write a python program to create ' \  'a Snake Water Gun game' \
#   ' in Python using if-else statements. ' \
# 'Do not create any fancy GUI. Use proper functions to check for win.

import random

print("💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰\n")
print("\t\t🎇 WELCOME TO 🙏🏻 \t=================================")
print("\t\t\t\t\t\t\t|||\t\t Snake🐍  Water🥛   Gun🔫   \t  |||")
print("\t\t\t\t\t\t\t================================= \t WITH HARSH MISHRA 👨🏻")


def check(comp, user):
    if comp == user:
        return 0

    if (comp == 0 and user == 1):
        return -1

    if (comp == 1 and user == 2):
        return -1

    if (comp == 2 and user == 0):
        return -1

    return 1


computer = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(computer, user)

print("You: ", user)
print("Computer: ", computer)

if (score == 0):
    print("Its a draw")
elif (score == -1):
    print("You Lose")
else:
    print("You Won")
