import random
print("*************************************************************")
print("             NUMBER GUESSING GAME        ")
print("**************************************************************")


while True:
    print("-> ENTER YOUR CHOICE : \n 1) TO PLAY THE GAME \n 2) RULES OF THE GAME \n 3)EXIT THE GAME ")
    inp = int (input())
    rnum = random.randint(1,100)
    if inp ==1:
        print("LET'S START ->>>>>>>")
        print("YOU HAVE TEN CHANCES TO GUESS THE NUMBER ^_^")
        for i in range(0,10):
            print("ENTER THE NUMBER")
            unum=int(input())
            if unum<rnum:
                print("DUDE,GUESS MORE HIGHER NUMBER>>>>>> ")
                print("YOU HAVE MORE ",10-(i+1),"CHANCES LEFTOUT")
                while i + 1 == 10:
                    print("---------> GaMe @ OvEr!!!!!!!!")
                    break
                continue
            elif unum >rnum:
                print("DUDE,GUESS LESS LOWER NUMBER<<<<<<<<")
                print("YOU HAVE MORE ", 10 - (i+1), "CHANCES LEFTOUT")
                while i+1==10:
                    print("---------> GaMe @ OvEr!!!!!!!!")
                    break
                continue
            elif unum==rnum:
                print(" YEAH BOUYYYY ,YOU GUESSED THE RIGHT ANSWER \"",rnum,"\" ")
                print("YOU WON IN ",i+1," CHANCES *")
                break

    print("\n")
    if inp == 2:
        print("WELCOME TO HARSH MISHRA'S PROJECT :->>>")
        print("THIS IS NUMBER GUESSING GAME,YOU HAVE \nTO GUESS THE NUMBER WITHIN 10 CHANCES \nSELECTED BY THE COMPUTER  WITHIN RANGE 1 -100")
        print("IF YOU GET SUCCESS IN GUESSING THE RIGHT NUMBER WITHIN LIMITED CHANCES THEN YOU WIN !")
        print("\n")
        continue
    elif inp == 3:
        print("$$$$$$$$$$$ THAN YOU $$$$$$$$$$$$")
        print(exit())


