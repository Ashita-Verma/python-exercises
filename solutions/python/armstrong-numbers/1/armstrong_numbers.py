def is_armstrong_number(number):
    """
    Determines if the number is Armstrong number.
    A number can be Armstrong number if the sum of its own digits each raised to the power of the number of digits.

    Parameters:
    number (int): The number which needs to be evaluated as Armstrong number.

    Returns:
    Boolean : True if the number is Armstrong number, False otherwise.
    
    """

    str_of_number = str(number)
    power = len(str_of_number)
    return sum(int(every_chr)**power for every_chr in str_of_number ) == number
