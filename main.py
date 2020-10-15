from iteratorandgenerator import generator
from iteratorandgenerator import Number_it
from functions import finding_is_perfect
def user_input(givenchoice):
    while True:
        try:
            if givenchoice == "arrayinput":
                given = [int(i) for i in input("Input array elements : ").split()]

            else:
                given = int(input('Input ' + givenchoice + ': '))

        except ValueError:
            print("please enter a valid number ")
        else:
            return given





while True:
    print('''welcome user !!!!
    Choose your option: 
    1.Iterator 
    2. Generator
    3. Exit''')
    userchoice = user_input("your choice")
    if userchoice == 1:
        n = int(input(print("enter n value")))
        values= Number_it(n)
        for i in values:
           finding_is_perfect(i)


    elif userchoice == 2:
        n = int(input(print("enter n value :")))
        values = generator(n)
        for i in values:
            finding_is_perfect(i)
    else:
        print("thank you for your time!!!!!")
        break