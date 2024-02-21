"""Read and load the environment variable strings"""

# Built-in imports
from os import environ
from configparser import ConfigParser
from json import loads as json_loads

# PIP imports
from dotenv import dotenv_values as env_loads
from toml import loads as toml_loads
from xmltodict import parse as xml_loads
from yaml import safe_load as yaml_loads

# Second-party imports
from .errors.reader import (
    FormatUndeclaredError,
    InvalidFormatError,
    UnexpectedFormatError,
)
from .utils import Path, Pathy


def ini_loads(path: Path) -> dict:
    """Load the environment variable strings from an INI file"""

    config = ConfigParser()
    config.read(path)
    return {section: dict(config[section]) for section in config.sections()}


def environ_loads(vars_to_get: list[str]) -> dict:
    """Load the environment variable strings from os environment namespace"""

    return {var: environ[var] for var in vars_to_get}


class Reader:
    """Read and load the environment variable strings"""

    def __init__(self, format_: str, format_input: Pathy | list[str]) -> None:

        # Check if format is declared and is valid
        FormatUndeclaredError(format_).check()
        InvalidFormatError(format_).check()

        # Get environment variables to exclude
        self.exclude = environ.get("EXCLUDE", "list: []").split(",")

        # Map format to loader function
        self.loaders = {
            "env": env_loads,
            "environ": environ_loads,
            "ini": ini_loads,
            "json": json_loads,
            "toml": toml_loads,
            "xml": xml_loads,
            "yaml": yaml_loads,
        }

        self.format = format_
        self.vars = self.loaders[self.format](format_input)


class FileReader(Reader):
    """Read and load the environment variable strings from a file"""

    def __init__(self, path: Pathy, format_=".env") -> None:

        path = Path(path)

        # Ensure file extension and declared format match
        UnexpectedFormatError(path, format_).check()
        super().__init__(format_, path)
        self.path = path

        # Read environment variables from file
        self.load = self.loaders[self.format](path)


class EnvironReader(Reader):
    """Read and load the environment variable strings from os environment namespace"""

    def __init__(self, include: list[str]) -> None:
        super().__init__("environ", include)
