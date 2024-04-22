def wave(people: str) -> list[str]:
    return [people[:num] + person.upper() + people[num+1:] for num, person in enumerate(people) if person != " "]
    # return [people[:num] + people[num].upper() + people[num+1:] for num in range(len(people)) if people[num] != " "]
