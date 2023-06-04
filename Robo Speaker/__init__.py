# for mac:

# import os

# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker ::::::\n")
#     print("Created by Harsh Mishra `````\n")
#     x =input("Enter what you want me to speak : ")
#     command = f"say {x}"
#     os.system(command)

# for windows:


import pyttsx3

if __name__ == '__main__':  # is not necessary
    print("Welcome to RoboSpeaker ::::::\n")
    print("Created by Harsh Mishra ::::::\n")
    engine = pyttsx3.init()
    engine.say("Welcome to RoboSpeaker")
    engine.runAndWait()
    engine = pyttsx3.init()
    engine.say("Created by Harsh Mishra ")
    engine.runAndWait()

    x = input("Enter what you want me to speak: ")

    engine = pyttsx3.init()
    engine.say(x)
    engine.runAndWait()
