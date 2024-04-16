import re

def pick_numbers(text: str) -> list[int]:
    numbers = []
    matches = re.findall(r'\b\d+\b', text)
    for match in matches:
        numbers.append(int(match))

    return numbers
