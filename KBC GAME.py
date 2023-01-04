# THIS PROGRAM IS ABOUT GAME KBC WHERE YOU WILL GET 17 QUESTIONS AND MULTIPLE CHOICES FOR WHICH EVRY  CORRECT ANSWER
# THERE IS A PRIZE MONEY
import random
print("💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰\n")
print("\t\t🎇 WELCOME TO 🙏🏻 \t=================================")
print("\t\t\t\t\t\t\t|||\t\t 🪔 K B C 🪔   \t  |||")
print("\t\t\t\t\t\t\t================================= \t WITH HARSH MISHRA 👨🏻")

NAME = input('\nPLEASE ENTER YOUR NAME SIR : ')
amount = 0
flag =0

def rules():
    ''' This function shows the rule of the game'''
    print("***** RULES ARE 📖 : \n"
          "-> YOU HAVE 20 PYTHON'S QUESTIONS WITH MULTIPLE CHOICES\n"
          "-> YOU HAVE TO GIVE CORRECT ANSWER FOR EACH \n"
          "-> EACH TIME U GIVE CORRECT ANSWER A AMOUNT OF PRIZE MONEY WILL BE INCREMENTED\n"
          "-> AND IF U GIVE WRONG ANSWER U WILL LOOSE THE AMOUNT\n"
          "-> U WILL HAVE THE OPTION OF QUITTING THE GAME \n"
          "-> YOU WILL RECIEVE THE AMOUNT U WIN ,THERE ARE THREE HOLD POINT OF AMOUNT \n"
          "-> THAT IS 12,800 ; 4,09,600 ; 6,55,3600 THIS ARE THE AMOUNTS IF YOU CROSSED THIS AMOUNT THEN FOR \n"
          "-> SURE AFTER QUITTING OR LOSSING YOU WILL RECIEVE THIS AMOUNTS\n"
          f'\nWISHING YOU BEST OF LUCK 👍🏻👍🏻👍🏻  {NAME} :::::::::::::::::::::\n')


def quiz():
    print("LET'S START THE GAME : ")
    print(f'{NAME} ,the question is on your screen ..........\n')
    questions = [{'question': 'What is the output of the following code? print(2 + 3 * 4)',
                  'choices': ['14', '20', '10', '22',"QUIT!"],
                  'answer': 2},
                 {'question': 'What is the correct way to import the ''math'' module in Python?',
                  'choices': ['import math', 'include math', 'using math', 'require math',"QUIT!"],
                  'answer': 0},
                 {'question': 'What is the correct way to create a new tuple in Python?',
                  'choices': ['tuple = (1, 2, 3)', 'tuple (1, 2, 3)', 'tuple {1, 2, 3}', 'tuple [1, 2, 3]',"QUIT!"],
                  'answer': 0},
                 {'question': 'What is the output of the following code?\n'
                              'x = [1, 2, 3]\n'
                              'y = x\n'
                              'y[1] = 5\n'
                              'print(x)\n',
                  'choices': ['[1, 2, 3]', '[1, 5, 3]', '[5, 2, 3]', '[1, 2, 5]',"QUIT!"],
                  'answer': 1},
                 {'question': 'What is the correct way to iterate through a dictionary in Python?',
                  'choices': ['for key in dict', 'for item in dict', 'for i in dict', 'for key, value in dict',"QUIT!"],
                  'answer': 3},
                 {'question': 'What is the output of the following code?\n'
                              'def greet(name):\n'
                              '    return "Hello " + name\n'
                              'print(greet("John"))\n',
                  'choices': ['Hello John', 'Hello', 'John', 'None',"QUIT!"],
                  'answer': 0},
                 {'question': 'What is the output of the following code?\n'
                              'x = "Hello"\n'
                              "y = 'world'\n"
                              "print(x == y)\n",
                  'choices': ['True', 'False', 'Hello', 'World',"QUIT!"],
                  'answer': 1},
                 {'question': 'What is the correct way to open a file in Python for reading?',
                  'choices': ['open("file.txt", "r")', 'read("file.txt")', 'file.open("r")', 'f = open('
                                                                                             '"file.txt")',"QUIT!"],
                  'answer': 0},
                 {'question': 'What is the output of the following code?\n'
                              'x = [1, 2, 3]\n'
                              'y = x[:]\n'
                              'y[1] = 5\n'
                              'print(x)\n',
                  'choices': ['[1, 2, 3]', '[1, 5, 3]', '[5, 2, 3]', '[1, 2, 5]',"QUIT!"],
                  'answer': 0},
                 {'question': 'What is the correct way to access the last element in a list in Python?',
                  'choices': ['list[-1]', 'list[len(list)]', 'list[end]', 'list.last()',"QUIT!"],
                  'answer': 0}]
    # question 1
    q1 = {'question': 'What is the output of the following code?\nprint(5 + "5")',
          'choices': ['10', '"55"', 'TypeError', '"5+5"',"QUIT!"],
          'answer': 2}
    questions.append(q1)
    # question 2
    q2 = {'question': 'What is the keyword used to define a function in Python?',
          'choices': ['define', 'function', 'def', 'func',"QUIT!"],
          'answer': 2}
    questions.append(q2)

    # question 3
    q3 = {'question': 'What is the output of the following code?\nfor i in range(5):\n print(i)',
          'choices': ['0 1 2 3 4', '5 4 3 2 1', '0', 'None',"QUIT!"],
          'answer': 0}
    questions.append(q3)

    # question 4
    q4 = {'question': 'What is the syntax for creating a tuple in Python?',
          'choices': ['( )', '{ }', '< >', '[ ]',"QUIT!"],
          'answer': 0}
    questions.append(q4)

    # question 5
    q5 = {'question': 'What is the output of the following code?\nx = [1, 2, 3]\ny = x\ny[1] = 5\nprint(x)',
          'choices': ['[1, 2, 3]', '[1, 5, 3]', '[1, 2, 3, 5]', 'Error',"QUIT!"],
          'answer': 1}
    questions.append(q5)

    # question 6
    q6 = {'question': 'What is the output of the following code?\nx = 5\nprint(type(x))',
          'choices': ['int', 'float', 'str', 'list',"QUIT!"],
          'answer': 0}
    questions.append(q6)

    # question 7
    q7 = {'question': 'What is the output of the following code?\nx = [1, 2, 3]\nfor i in x:\n print(i)',
          'choices': ['1 2 3', '3 2 1', '1', 'None',"QUIT!"],
          'answer': 0}
    questions.append(q7)

    # question 8
    q8 = {'question': 'Which of the following is NOT a built-in data type in Python?',
          'choices': ['list', 'tuple', 'dictionary', 'matrix',"QUIT!"],
          'answer': 3}
    questions.append(q8)

    # question 9
    q9 = {'question': 'What is the output of the following code?\nx = 5\nx += 3\nprint(x)',
          'choices': ['8', '5', '3', '11',"QUIT!"],
          'answer': 0}
    questions.append(q9)

    # question 10
    q10 = {'question': 'Which of the following is NOT a built-in function in Python?',
           'choices': ['print()', 'input()', 'exec()', 'eval()',"QUIT!"],
           'answer': 2}
    questions.append(q10)

    random.shuffle(questions)
    valid_answers = [1, 2, 3, 4, 5]

    for i, q in enumerate(questions, start=1):

        print(f'Question {i}: {q["question"]}')
        for j, c in enumerate(q['choices'], start=1):
            print(f"{j}: {c}")
        next_q = False
        while not next_q:
            user_answer = int(input('Enter your answer: '))
            if user_answer not in valid_answers:
                print("INVALID CHOICE !!!!")

            elif user_answer == q['answer'] + 1:
                print(f'Correct!Answer {NAME} 🏆\n')
                amt(i)
                next_q = True
            elif user_answer == 5:
                quit()
            else:
                print(f'☹ Sorry {NAME} you have given an Incorrect Answer! .\n The correct answer was '
                        f'{q["choices"][q["answer"]]}\n')
                loss()


def amt(x):
    amount = 100
    flag=0
    for i in range(1, x+1 ):
        amount *= 2
        if x == 20:
            amount = 70000000
    if amount>=10000:
       print(f'🤑 CONGRATULATIONS , {NAME} YOU HAVE WON AMOUNT OF RS :'+f'{amount:,}')
    elif amount >=1638400 :
        print(f"🤑 CONGRATULATIONS , {NAME} YOU ARE NOW A MILLIONAIRE AND YOU WON AN AMOUNT OF RS :" + f'{amount:,}')
    elif amount ==70000000:
        print(f"🤑 CONGRATULATIONS , {NAME} YOU HAVE SUCCESSFULLY COMPLETED THE GAME 🎁🏆🏆 \n AND YOU ARE NOW A "
              "MILLIONAIRE AND YOU WON 🎯 \n"
              "AN AMOUNT OF RS :" + f'{amount:,} \n🥂🥂🥂')
    else:
        print(f"🤑 CONGRATULATIONS , {NAME} YOU HAVE WON AMOUNT OF RS :" + f'{amount}')
    if (x) == 8:
        flag += 1
        print("YOU HAVE CROSSED THE FIRST BARRIER ")
    elif (x)==13  :
        flag+=1
        print("YOU HAVE CROSSED THE SECOND BARRIER")
    elif (x)==17:
        flag+= 1
        print("YOU HAVE CROSSED THE THIRD BARRIER")


def loss():
    if flag==1 :
        amount = 12800
        print(f'{NAME} , you have won an amount of {amount:,} 👏🏻👏🏻👏🏻')

    elif flag==2 :
        amount= 409600
        print(f'{NAME} , you have won an amount of {amount:,} 👏🏻👏🏻👏🏻')

    elif flag==3 :
        amount= 6553600
        print(f'{NAME} , you have won an amount of {amount:,} 👏🏻👏🏻👏🏻')

    else:
        print(f'{NAME} , you have not won any amount  🤦🏻 🥴\n Better luck next time !')
    exit()


def quit():
    print(f'THANKS FOR PLAYING WITH US {NAME} 🤝🏻🤝🏻🤝🏻 ')
    loss()
    print("\n💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰💰")
    exit()


while True:
    print(f'CHOOSE AN OPTION FROM THE MENU SHOWN BELOW MR/MRS {NAME} 🎯:\n'
          f'1) FOR PLAYING THE GAME \n 2) FOR KNOWING THE RULES \n 3) QUIT THE GAME !')
    choice = int(input())
    if choice == 1:
        quiz()
    elif choice == 2:
        rules()
    elif choice == 3:
        quit()
    else:
        print ("YOU HAVE ENTERED A WRONG CHOICE !")
