from converter import to_hex


def encrypt(string: str, key: int) -> str:
    res = ""
    for character in string:
        res = res + to_hex(ord(character) ^ key)
    return res
