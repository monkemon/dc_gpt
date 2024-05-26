import random
from typing import Tuple


def get_random_hex_color() -> Tuple[int,int,int]:
    """BGR format"""
    b = random.randrange(0, 255)
    g = random.randrange(0, 255)
    r = random.randrange(0, 255)

    res = 0
    res |= r
    res = res << 8
    res |= g
    res = res << 8
    res |= b
    return res