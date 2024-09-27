import random
import time
import base64


#USED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def tds_gen_new_id() -> str:
        t1: bytes = int(time.time()).to_bytes(5, byteorder="big")
        t2: str = str(base64.b32hexencode(t1))

        b1: bytes = random.randbytes(40)
        b2: str = str(base64.b32hexencode(b1))

        return f"{t2}_{b2}"

