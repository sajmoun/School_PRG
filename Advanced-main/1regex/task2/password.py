import re

def validate_password(password: str) -> bool:
    return bool(re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_+=]).{8,}$', password))
