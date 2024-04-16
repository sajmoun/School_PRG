def transform_words(words: list) -> list:
    return [word.upper() + str(len(word)) for word in words]
