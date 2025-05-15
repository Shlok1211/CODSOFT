def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

while True:
    num1 = int(input("Enter the first number :- "))
    num2 = int(input("Enter the second number :- "))

    choice = input('Enter the Operator( + , - , * , / ) :- ')

    if choice == '+':
        r = num1+num2
        print(r)
        break
    elif choice == '-':
        r = num1-num2
        print(r)
        break
    elif choice == '*':
        r = num1*num2
        print(r)
        break
    elif choice == '/':
        r = num1/num2
        print(r)
        break
    else:
        print("Enter a valid Operator! , Please Try Again")