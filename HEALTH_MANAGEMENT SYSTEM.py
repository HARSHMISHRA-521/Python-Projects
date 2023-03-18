# Instructions: Create a food log file for each client Create an exercise log file for each client. Ask the user
# whether they want to log or retrieve client data. Write a function that takes the user input of the client's name.
# After the client's name is entered, A message should display "What you want to log. Diet or Exercise" Use function
# def getdate(): import datetime return datetime.datetime.now() The purpose of this function is to give time with
# every record of food or exercise added in the file. Write a function to retrieve exercise or food file records for
# any client.

import os
import datetime


def gettime():
    return datetime.datetime.now()


def log(name):
    c = int(input("Enter 1 for Excersise and 2 for Food\n"))
    if c == 1:
        content = input('type here : \n')
        filename = name + "-exercise" + ".txt"
        with open(filename, "a") as f:
            f.write(str([str(gettime())]) + ":" + content + "\n")
            print("Succesfully logged")
            f.close()

    elif c == 2:
        content = input('type here : \n')
        filename = name + "-food" + ".txt"
        with open(filename, "a") as f:
            f.write(str([str(gettime())]) + ":" + content + "\n")
            print("Succesfully logged")
            f.close()

    else:
        print("Enter the valid input")


def retrive(name):
    c = int(input("Enter 1 for Excersise and 2 for Food:\n"))
    if c == 1:
        filename = name + "-exercise" + ".txt"
        if os.path.exists(filename):
            with open(filename, "r") as op:
             d = op.read()
             print(d)
            op.close()
        else:
            print("FILE DOES NOT EXISTS !")

    elif c == 2:
        filename = name + "-food" + ".txt"
        if os.path.exists(filename):
            with open(filename, "r") as op:
             d = op.read()
             print(d)
            op.close()
        else:
            print("FILE DOES NOT EXISTS !")
    else:
            print("Enter the valid input")


while (True):
    print("---------- HEALTH MANAGEMENT SYSTEM ----------\n")
    a = int(input("ENTER 1 FOR LOGGING AND 2 FOR RETRIVING DATA AND 3 FOR EXIT\n"))
    if a == 1:
        n = str(input("ENTER THE NAME\n"))
        log(n)
    elif a == 2:
        n = str(input("ENTER THE NAME\n"))
        retrive(n)
    elif a == 3:
        print("++++++++++++++++++++++ THANKS ++++++++++++++++++++++++++")
        exit()
    else:
        print("ENTER THE VALID INPUT")

    print("********************************************************\n\n")
