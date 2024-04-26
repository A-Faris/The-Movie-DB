"""Friday"""


def is_valid_ip(strng: str) -> bool:
    """is valid ip"""
    if len(strng.split(".")) != 4:
        return False

    for num in strng.split("."):
        if not num.isdigit():
            return False
        if not 0 <= int(num) <= 255:
            return False
        if int(num[0]) == 0 and len(num) > 1:
            return False

    return True
