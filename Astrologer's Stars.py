# '''You have to follow certain instructions, which are as follows:
# You have to take an integer type variable, and the input of the variable will define the length of the triangle.
# You have to declare another Boolean variable.
# When the value of Boolean is 1 i.e. True, the pattern will be printed as shown above.
# But if the value of Boolean is 0 or false, then the triangle will be printed upside down.
from pickle import TRUE

print("********** ASTROLOGER'S STARS ***************")



def upstars(n):
    for i in range(0, n):
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")
        # ending line after each row
        print("\r")


def downstars(n):
    for i in reversed(range(0, n)):
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")
        # ending line after each row
        print("\r")


while TRUE:
    print("ENTER YOUR CHOICE FOR : \n 1>STRAIGHT PATTERN \n 2>UPSIDE DOWN PATTERN \n 3>EXIT ")
    z = int(input())
    y = bool(z)
    match z:
        case 1:
            print("ENTER THE NO OF STARS YOU WANT : ")
            h = int(input())
            print(f"YOU ENETERED {h}  STARS AND YOUR STAR CHOICE IS : {y}")
            upstars(h)
            print("\n")

        case 2:
            print("ENTER THE NO OF STARS YOU WANT : ")
            h = int(input())
            print(f"YOU ENETERED {h}  STARS AND YOUR STAR CHOICE IS : {y}")
            downstars(h)
            print("\n")

        case 3:
            print("<<<<<<<<<<<<<<< END >>>>>>>>>>>>>>")
            exit()

        case _:
            print("WRONG INPUT!")
