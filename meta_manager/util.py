import hashlib
from pathlib import Path


def hash_file(filename: Path):
    h = hashlib.md5()
    with filename.open("rb") as file:
        chunk = 0
        while chunk != b"":
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


def hash_data(data: bytes):
    h = hashlib.md5()
    h.update(data)
    return h.hexdigest()


def comma_list(value: str):
    return value.split(",")
