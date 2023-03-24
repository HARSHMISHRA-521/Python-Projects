# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
#this program take a file name as parameter so,make sure that file exists
# This  program generates a new file for encrypted data and decrypted data as you exit the code

import os
import random
import string

def encrypt(name):
    input_filename = name + ".txt"
    output_filename = name + "_encrypted.txt"
    with open(input_filename, "r") as input_file:
        msg = input_file.read().strip()

    words = msg.split(" ")
    nword = []

    for word in words:
        if (len(word) >= 3):
            if word.isalpha():
                r1 = ''.join(random.choices(string.ascii_letters, k=3))
                r2 = ''.join(random.choices(string.ascii_letters, k=3))
                n = r1 + word[1:] + word[0] + r2
                nword.append(n)
            elif word.isdigit():
                d1 = ''.join(random.choices(string.digits, k=3))
                d2 = ''.join(random.choices(string.digits, k=3))
                g = d1 + word[1:] + word[0] + d2
                nword.append(g)
        else:
            nword.append(word[::-1])

    nnword = " ".join(nword)

    with open(output_filename, "w") as output_file:
        output_file.write(nnword + "\n")

    print("SUCCESSFULLY ENCRYPTED ^^^")
    print("THE ENCRYPTED MSG IS :")
    print(nnword)




def decrypt(name):
    filename = name + "_encrypted.txt"
    if os.path.exists(filename):
        with open(filename, "r") as f:
            msg = f.read().strip()
    else:
        print("FILE DOES NOT EXISTS !")

    words = msg.split()
    nword = []

    for word in words:
        if (len(word) >= 3):
            if word.isalpha():
                n = word[3:-3]
                n = n[-1] + n[:-1]
                nword.append(n)
            elif word.isdigit():
                m = word[3:-3]
                m = m[-1] + m[:-1]
                nword.append(m)
        else:
            nword.append(word[::-1])

    nnword = " ".join(nword)

    with open("decrypted_" + name+".txt", "w") as f:
        f.write(nnword + "\n")

    print("SUCCESSFULLY DECRYPTED vvv")
    with open("decrypted_" + name+".txt", "r") as f:
        rd = f.read()
        print("THE DECRYPTED MSG IS :")
        print(rd)



while True:
    print("!!!!!!!!!! Secret Code !!!!!!!!!!!!!!")
    ch=int(input("1.Encryption\n2.Decryption\n3.Exit\n"))
    if ch == 1:
        file=input("Enter the file name : \n")
        encrypt(file)
    elif ch == 2:
        file=input("Enter the file name: \n")
        decrypt(file)
    elif ch==3:
        print("------------------------  THANKS ---------------------------------")
        print("*************************  H M C  ********************************")
        exit()
    else:
        print("PLS ENTER A VALID INPUT !")
