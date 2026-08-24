def steps(number):
    """
    Dertermins the number of steps for the number to reach Collatz Conjecture.For this, the following rules to be followed
    1. If the number is even, divide it by 2
    2. If the umber is odd, multiply by 3 and then add 1
    3. Repeat this till the number you reach is 1

    Parameter:
    number(int) : The number for which the steps need to calculated

    Returns:
    int : The number of steps to reach Collatz Conjecture

    Raises:
    ValueError : If the input number is 0 or negative
    """
    if(number <= 0):
        raise ValueError("Only positive integers are allowed")
        
    steps = 0
    while(number != 1):
        if ((number & 1) == 0):
            number = number // 2
        else:
            number = (number * 3) + 1
        steps += 1
    
    return steps