"""Utility objects and functions for typed_env package."""

# Built-in imports
from os import PathLike
from pathlib import Path
from typing import Union, TypeVar


# Split a path to file name and extension
def get_extension(name: str):
    """Split a file name and extension"""

    components = name.split(".")
    extension = ""

    if len(components) > 1 and components[0] == ".env":
        extension = components[0]
    else:
        extension = components[-1]

    return extension


Pathy = TypeVar("Pathy", str, Path, PathLike)
