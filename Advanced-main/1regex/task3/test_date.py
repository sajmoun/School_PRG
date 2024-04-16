from date import find_dates


def test_find_dates():
    text = "Důležitý termín je 15.02.2023 a další je 20.6.2024."
    expected_dates = ["15.02.2023", "20.6.2024"]
    actual_dates = find_dates(text)

    assert actual_dates == expected_dates, "Chyba při vyhledávání dat."
