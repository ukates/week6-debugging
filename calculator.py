def add( first, second):
    # TODO:
    # there's an error in this code, fix it
    return int(first) + int(second)

def subtract( first, second):
    return int(first) - int(second)
    # TODO:
    # fill in code here that will return the difference between first and second

def multiply( first, second):
    return int(first) * int(second)
    # TODO:
    # fill in code here that will return the product of first and second

def divide( first, second):
    if second == int(0):
        raise Exception ("I'm sorry, I can't divide by zero")
    return int(first) / int(second)


    
    # TODO:
    # fill in code here that:
    #   1. checks the second number to see if it is zero
    #   2. if the second number is zero, an exception is raised, the exception text must say exactly the following (make sure everything including casing and spaces match)
    #       I'm sorry, I can't divide by zero
    #   3. returns the quotient of first and second
