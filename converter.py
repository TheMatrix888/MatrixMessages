ALPHABET = "0123456789ABCDEF"
HEX_TO_DECIMAL = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                  'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def to_hex(decimal_number: int) -> str:
    result = ""
    while decimal_number:
        result = ALPHABET[decimal_number % 16] + result
        decimal_number //= 16
    if len(result) < 4:
        result = '0' * (4 - len(result)) + result
    return result


def to_decimal(hex_number: str) -> int:
    result = 0
    power = 0
    for decimal in hex_number[::-1]:
        result += HEX_TO_DECIMAL[decimal] * 16 ** power
        power += 1
    return result
