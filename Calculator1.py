""""""
#It is important to use functions when there are many tesks
#function to add
#function to subtact
#function to multiply
#function to divide

""""""

import sys
number1=0
number2=0

def again():
    againloop = input('''select (y) if you want to continue and (n) stop program''')
    if againloop.upper() == 'Y':
        validate_num1()
        validate_num2()
        validate_operator()
    else :
        sys.exit("Thank you")


def validate_num1():
    global number1
    try: 
        number1=float(input("insert the first value"))
    except:
        print("The first in put is not a number\n")
        validate_num1()
def validate_operator():
    operation=input('''please type in the math operation you would like to complate:
    + for addition 
    - for subtraction 
    * for multiplycation
    / for division
    ''')
    if(operation == '+' or operation == '-' or operation == '*' or operation == '/'):
        if operation == '+':
                addition()
        elif operation == '-':
                subtraction()
        elif operation == '*':
                multiply()
        elif operation == "/":
                divide()
        else:
                sys.exit("select on of the following: +, -, *, or /\n")
    else:
        print("Invalid operator\n")
        validate_operator()
    again()
def validate_num2():
    global number2 
    try:
        number2=float(input("Insert the second value"))
    except:
        print("The second input is not a number\n")
        validate_num2
validate_num1()
validate_num2()

def addition(): 
        result=number1+number2
        print(f"The sumation for the two values is equal to: {result}")
def subtraction():
        result=number1-number2
        print(f"The subtracton result of the two values is equal to: {result}")
def multiply():
        result=number1*number2
        print(f"The mulplication of the two values is equal to: {result}")
def divide():
        result=number1/number2
        print(f"The division for the two values is equal to: {result}")
validate_operator()

          
    
