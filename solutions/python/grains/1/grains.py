def square(number):
    """
    Determines the number of grains at the square. 
    if the square number is 5 then the grains would be 2 raised to     4, which is 16.

    Parameters:
    number (int): the number of square for which the grains is to be found.

    Returns:
    (int) : the number of grains on the square.
    """
    
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")

    return 2**(number-1)
    
def total():
    """
    Determines the total number of grains on the chessboard if Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time.

    Returns:
    (int) : The total number of grains on the chess board
    """
    return (2 ** 64) - 1
