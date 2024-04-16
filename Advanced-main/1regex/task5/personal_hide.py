import re

def phone_hide(persons: list[str]) -> list[str]:
    result = []
    for person in persons:
        result.append(re.sub(r'\d{3}-\d{3}-', '***-***-', person))
    return result

def email_hide(persons: list[str]) -> list[str]:
    result = []
    for person in persons:
        parts = person.split('@')
        name = parts[0]
        domain = parts[1]
        name = name[0] + '*' * (len(name) - 2) + name[-1]
        domain_parts = domain.split('.')
        domain = domain_parts[0][0] + '*' * (len(domain_parts[0]) - 1) + '.' + domain_parts[1]
        result.append(name + '@' + domain)
    return result
