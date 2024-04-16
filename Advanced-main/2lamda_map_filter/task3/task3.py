def add_initials(people: list[dict]) -> list[dict]:
    def add_initials(p):
        p["initials"] = p["name"][0] + p["surname"][0]
        return p

    return list(
        map(lambda p: {**p, "initials": p["name"][0] + p["surname"][0]}, people)
    )
