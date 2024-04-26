"""Monday"""


def wave(people: str) -> list[str]:
    """Wave"""
    return [people[:num] + person.upper() + people[num+1:]
            for num, person in enumerate(people) if person != " "]
