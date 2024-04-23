def diamond(n: int) -> str:
    if n % 2 == 0 or n < 1:
        return None

    # output = ""
    # for i in range(-n//2+1, n//2+1):
    #     output += abs(i)*" " + (n-abs(i)*2)*"*" + "\n"
    # return output

    return "\n".join([abs(i)*" " + (n-abs(i)*2)*"*" for i in range(-n//2+1, n//2+1)]) + "\n"
