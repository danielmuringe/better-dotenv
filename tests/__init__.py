"""Main test module"""

from os import environ
from sys import path
from pathlib import Path

SECRET_GARDEN_LOCAL = environ.get("SECRET_GARDEN_LOCAL", "true").lower()

if SECRET_GARDEN_LOCAL == "true":
    pass
elif SECRET_GARDEN_LOCAL == "false":
    path.remove(Path(__file__).parent.parent.as_posix())
else:
    raise ValueError('SECRET_GARDEN_LOCAL must be "true" or "false"')


import secret_garden
