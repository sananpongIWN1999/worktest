from ast import Global
import random
import sys

x = ""
y = ""
num = ""
guess = None

print("---welcome to Game guess the numbers---")
       
def Guefunc():
    global x,y
    global num
    global guess
    x = int(input("input numbers you want to guess in A : "))
    y = int(input("input numbers you want to guess in B : "))
    num = random.randint(x, y)
    while guess != num:
        guess = int(input("guess a number between variable A and B: "))
        guess = int(guess)

        if guess == num:
            print("              YOU WON!!!             ")
            RestartFunc ()
        else:
            print("nope,try again!")

def RestartFunc ():
    Re = input("play again 'yes' or stop program 'no' : ").lower()
    if Re == "yes":
        Guefunc ()
    elif Re == "no":
        sys.exit("THANK YOU")
    else:
        RestartFunc()

Guefunc()

###########################################################################


