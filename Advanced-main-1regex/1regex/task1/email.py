import re

def validate_email(email):
    """
    This function checks if the given email address is valid or not.
    :param email: str
    :return: bool
    """
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
