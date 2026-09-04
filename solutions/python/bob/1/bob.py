CALM = "Calm down, I know what I'm doing!"
SURE = "Sure."
CHILL = "Whoa, chill out!"
FINE = "Fine. Be that way!"
WHATEVER = "Whatever."

def response(hey_bob) -> str:
    """
    Determines what would be the response to input string based on the rules
    1. If it is a question
    2. If it is an angry statement
    3. If it is an angry question
    4. If there is no question or statement
    5. If it is none of the above

    Parameters: 
    hey_bob (str): The question or the statement

    Returns:
    str: The response based on the above rules.
    """
    hey_bob = hey_bob.rstrip()
    match hey_bob:
        case _ if hey_bob.endswith("?") and hey_bob.isupper():
            return CALM
        case _ if hey_bob.endswith("?"):
            return SURE
        case _ if hey_bob.isupper():
            return CHILL
        case _ if not hey_bob:
            return FINE
        case _ :
            return WHATEVER