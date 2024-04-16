def complex_word_filter(words: list[str], min_length: int) -> list[str]:
    return list(
        map(
            lambda w: w.upper()
            + str(
                w.count("a") + w.count("e") + w.count("i") + w.count("o") + w.count("u")
            ),
            filter(lambda w: len(w) > min_length, words),
        )
    )
