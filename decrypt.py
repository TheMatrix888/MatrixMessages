from converter import to_decimal


def decrypt(string: str, key: int) -> str:
    res = ""
    for i in range(len(string)//4):
        res += chr(to_decimal(string[4*i:4*(i+1)]) ^ key)
    return res
