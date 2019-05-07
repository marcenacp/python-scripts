import hashlib
import time


def compute_hash():
    sha1_hash = hashlib.sha1()
    sha1_hash.update(str(time.time()).encode('utf-8'))
    return sha1_hash.hexdigest()
