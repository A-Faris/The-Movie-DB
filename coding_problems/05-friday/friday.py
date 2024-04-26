def is_valid_IP(strng: str) -> bool:
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


print(is_valid_IP('12.255.56.1'))  # True
print(is_valid_IP('12.34.56 .1'))  # False
print(is_valid_IP('123.045.067.089'))  # False
