import re

def find_dates(text: str) -> list[str]:
    # Nalezne všechna data ve formátu dd.mm.rrrr a uloží je do seznamu
    dates = re.findall(r'\b\d{1,2}\.\d{1,2}\.\d{4}\b', text)
    return dates
