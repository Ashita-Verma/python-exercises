def leap_year(year):
    """ determines if a year is leap year based on the condition
    1. It should be evenly divisble by 4
    2. if its evenly divisible by 100, then its only a leap year if its also evenly divisible by 400.

    Parameters:
    year (int): The year which needs to be evaluated as leep year

    Returns:
    Boolean: True, if the year is leap year, false otherwise
    """
    return ((((year % 4 ) == 0) and ((year % 100 ) != 0)) or (((year % 100 ) == 0) and ((year % 400 ) == 0)))