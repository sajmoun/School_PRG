import re

def find_dates(text):
    """
    Tato funkce vyhledá a vrátí všechna data ve zadaném textu.
    :param text: str
    :return: list
    """
    # Regulární výraz pro shodu s daty ve formátu DD.MM.RRRR
    pattern = r'\b\d{1,2}\.\d{1,2}\.\d{4}\b'
    return re.findall(pattern, text)
