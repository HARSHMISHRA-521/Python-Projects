import time
print("********* THIS IS HOW YOU TEACH YOUR SYSTEM ,TO WISH YOU ACCORDING TO THE TIME *************")

st = (time.strftime('%H:%M:%S:%Y'))
t=int(time.strftime('%H'))
if t>=0 and t< 4:
    print("TIME IS : ",st)
    print("THOUGH ITS MORNING ,STILL GOOD NIGHT ! \n SWEET DREAMS!")
elif t >= 4 and t < 12:
        print("TIME IS : ", st)
        print("GOOD MORNING SIR, HAVE A NICE DAY!")
elif t>=12 and t< 18:
    print("TIME IS : ", st)
    print("GOOD AFTERNOON SIR, HAVE A NICE DAY!")
elif t>=18 and t< 22:
    print("TIME IS : ", st)
    print("GOOD EVENING SIR, HAVE A NICE DAY!")
else:
    print("TIME IS : ", st)
    print("GOOD NIGHT SIR, SWEET DREAMS !")
