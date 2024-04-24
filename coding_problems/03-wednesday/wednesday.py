def meeting(s: str) -> str:
    return "".join(sorted(["(" + ", ".join(name.split(":")[::-1]) + ")"
                   for name in s.upper().split(";")]))
