import hashlib
import random
import string
import time


def generate_id(name: str, length: int):
    input_string = name + str(time.time())
    hashed_string = hashlib.md5(input_string.encode())
    hash_prefix = hashed_string.hexdigest()[:length].upper()
    suffix = "".join(random.choices(string.ascii_uppercase + string.digits, k=2))
    user_id = hash_prefix + suffix
    return user_id
