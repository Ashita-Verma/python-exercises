def equilateral(sides):
    """ 
    Determines if triangle is equlateral by evaluating if its valid trangle and if the list of sides when converted to set, since all duplicates are removed, the len of set would be 1.

    Parameters:
    sides (list) :  the list of len of all side of the triangle

    Returns:
    Boolean : True if the triangle is equilateral, False otherwise
    """
    return is_valid_triangle(sides) and (len(set(sides)) == 1)


def isosceles(sides):
    """ 
    Determines if triangle is isosceles by evaluating if its valid trangle and if the list of sides when converted to set, since all duplicates are removed, the len of set would be either 1 or 2.

    Parameters:
    sides (list) :  the list of len of all side of the triangle

    Returns:
    Boolean : True if the triangle is isosceles, False otherwise
    """
    return is_valid_triangle(sides) and (len(set(sides)) <= 2)

def is_valid_triangle(sides):
    """ 
    Determines if triangle is valid, by evaluating the conditions
    1. The number of sides should be exactly 3
    2. All the sides should be more than 0
    3. when lenght of sides is sorted, the addition of the first 2 sides should be greater or equal to the biggest side.

    Parameters:
    sides (list) :  the list of len of all side of the triangle

    Returns:
    Boolean : True if the triangle is valid, False otherwise
    """
    if len(sides) == 3:
        if all(everyside > 0 for everyside in sides):
            a,b,c = sorted(sides)
            if a + b >= c:
                return True

    return False

def scalene(sides):
    """ 
    Determines if triangle is scalene by evaluating if its valid trangle and if the list of sides when converted to set, since all duplicates are removed, the lenght of set should be 3 as all sides should be different lenght.

    Parameters:
    sides (list) :  the list of len of all side of the triangle

    Returns:
    Boolean : True if the triangle is scalene, False otherwise
    """
    return is_valid_triangle(sides) and (len(set(sides)) == 3)
