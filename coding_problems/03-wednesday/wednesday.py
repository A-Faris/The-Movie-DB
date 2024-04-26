"""Wednesday"""


def meeting(s: str) -> str:
    """Meeting"""
    return "".join(sorted([f"({", ".join(name.upper().split(":")[::-1])})"
                           for name in s.split(";")]))
