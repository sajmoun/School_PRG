import re

def validate_email(email:str) -> bool:
    """
    This function checks if the given email address is valid or not.

    :param email: email address
    :type email: str
    :return: boolean value of valitation
    :rtype: bool
    """
    return bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email))