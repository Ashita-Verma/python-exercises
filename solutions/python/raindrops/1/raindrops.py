"""
This module is an exercise for using modulo
"""
def convert(number) -> str:
    """
    Gives a raindrops sound string given a number according to rules as below.
    1. If number is divisible by 3, return "Pling"
    2. If number is divisible by 5, return "Plang"
    1. If number is divisible by 7, return "Plong"
    1. If number is not divisible by 3,5,7, return the number as string

    Parameters:
    number (int): The input number to be converted to raindrop sounds

    Returns:
    str: The sound as a string or the number itself
    """

    sound_maps = [(3,"Pling"),(5,"Plang"),(7,"Plong")]
    sounds = "".join(sound for digit,sound in sound_maps if number % digit == 0)

    return sounds if sounds else str(number) 

    
