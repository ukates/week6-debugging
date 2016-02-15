def add( first, second):
    # TODO:
    # there's an error in this code, fix it
    return int(first) + int(second) # original code didn't convert first/ second into an integer so it could be used to add.  Also original code had 'plus' instead of using the correct opperator '+'  

def subtract( first, second):
    return int(first) - int(second) #turned first/second into integers used opperator '-' for subtraction this will return the answer for the user. 
    # TODO:
    # fill in code here that will return the difference between first and second

def multiply( first, second):
    return int(first) * int(second)
    # TODO:
    # fill in code here that will return the product of first and second

def divide( first, second):
    if second == int(0): #this is an if statement saying that if the user inputs an int equal to 0 then after the program errors, an exception will be raised telling the user why the program crashed, in this case (I'm sorry, I can't devide by zero) 
        raise Exception ("I'm sorry, I can't divide by zero") # I used double quotation marks so that the strings wouldnt end when i wrote the contractions i'm and can't for the exception to print. 
    return int(first) / int(second)
    # TODO:
    # fill in code here that:
    #   1. checks the second number to see if it is zero
    #   2. if the second number is zero, an exception is raised, the exception text must say exactly the following (make sure everything including casing and spaces match)
    #       I'm sorry, I can't divide by zero
    #   3. returns the quotient of first and second
