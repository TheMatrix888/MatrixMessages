from config import MAX_KEY
from decrypt import decrypt


def pick_key(string: str) -> list[str]:
    res = []
    for key in range(MAX_KEY+1):
        res.append(decrypt(string, key))
    return res
