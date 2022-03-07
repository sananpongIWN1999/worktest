from ast import Global
import random
import sys
num = random.randint(1, 10)
guess = None

def gue():
    
    global num,guess
    
    while guess != num:
        guess = input("guess a number between 1 and 10: ")
        guess = int(guess)

        if guess == num:
            print("YOU WON!")
            again()
            break
        else:
            print("nope,try again!")
def again():
    
    againloop = input('''select 'yes' if you want to play again or 'no' stop program''')
    if againloop.lower() == 'yes':
        gue()
    elif againloop.lower() == 'no':
        sys.exit("Thank you")
    else :
        again()

gue()