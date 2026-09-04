"""
Exercise for points given in a dart game.
"""
   
def score(x, y) -> int:
    """
    Determines the score given the position where the dart hits the target based on the below conditions
    1. outside the target, 0 points
    2. outer circle, 1 point
    3. midle circle, 5 points
    4. inner circle, 10 points

    Parameters:
    tuple(x,y): x and y co-ordinates of where the dart hit the target

    Returns:
    int : the score accordign to x, y
    """
    squared_coods = x**2 + y**2
    match squared_coods:
        case _ if squared_coods > 10**2:
            return 0
        case _ if squared_coods <= 1**2:
            return 10
        case _ if squared_coods <= 5**2:
            return 5
        case _ :
            return 1