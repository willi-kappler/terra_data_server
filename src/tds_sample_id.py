import random
import datetime
import string

# USED_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# def tds_gen_new_id2() -> str:
#     t1: bytes = int(time.time()).to_bytes(5, byteorder="big")
#     t2: str = base64.b32hexencode(t1).decode("utf-8")

#     b1: bytes = random.randbytes(40)
#     b2: str = base64.b32hexencode(b1).decode("utf-8")

#     return f"{t2}_{b2}"


def tds_gen_new_id() -> str:
    # 6 + 1 + 6 = 13 chars
    dt1: str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # 10 chars
    short: str = "schönb2345"
    # 27 chars unique random (22 ?)
    unique = "".join(random.choices(string.ascii_letters + string.digits, k=27))

    return f"TERRA_{dt1}_{short}_{unique}"
