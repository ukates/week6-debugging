#this is the runner file, it is responsible for running your code from calculator.py
import calculator   #this line imports your code

#let's greet the user and grab their input
print('Welcome to the calculator program!')

print('First, enter the first number you\'d like to use:')
first = int(input())

print('Great! Now enter the second number: ')
second = int(input())

choice = 0

#let's output a menu
while choice != 5:
    print('Choose what you\'d like to do with ' + str(first) + ' and ' + str(second) + ':')
    print('\t1: add')
    print('\t2: subtract')
    print('\t3: multiply')
    print('\t4: divide')
    print('\t5: exit')

    choice = int(input())

    # this series of if-statements call the proper functions from within the calculator program
    if choice == 1:
        print('The calculator returned: ' + str(calculator.add( first, second )))
    elif choice == 2:
        print('The calculator returned: ' + str(calculator.subtract( first, second )))
    elif choice == 3:
        print('The calculator returned: ' + str(calculator.multiply( first, second )))
    elif choice == 4:
        print('The calculator returned: ' + str(calculator.divide( first, second )))
    else:
        print('Sorry that\'s not a valid choice. Try again.')

print('Goodbye!')