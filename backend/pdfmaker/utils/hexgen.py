import secrets


def get_random_hex(length: int) -> str:
    if not isinstance(length, int):
        raise TypeError("length must be integer")
    return secrets.token_hex(length)
