import hashlib
from pathlib import Path

import typer


def hash_file(file: Path, algorithm: str) -> str:
    with open(file, "rb", buffering=0) as f:
        hash = hashlib.file_digest(f, algorithm).hexdigest()
    return hash


def name_file(path: Path, hash: str) -> str:
    suffix = f".[{hash}]"
    extension = path.suffix
    new_name = f"{path.stem}{suffix}{extension}"
    return path.with_name(new_name)
