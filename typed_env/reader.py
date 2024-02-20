"""Read and load the environment variable strings"""

# Built-in imports
from os import environ
from configparser import ConfigParser
from json import loads as json_loads

# PIP imports
from dotenv import dotenv_values as dotenv_loads
from toml import loads as toml_loads
from xmltodict import parse as xml_loads
from yaml import safe_load as yaml_loads

# Second-party imports
from .errors.reader import InvalidFileFormatError
from .utils import Path, Pathy


class Reader:
    """
    Read environment variables from file.
    If file is not provided then read from environment variables.

    args:
        - path: Pathy
        - format_: str = "env" | "envs" | "ini" | "json" | "toml" | "xml" | "yaml"
        - included: list = None
    """

    def __init__(
        self,
        path: Pathy = ".env",
        format_=None,
        included: list = None,
    ):

        if format_ is None:
            format_ = "env"
        else:
            # Check if format is declared, path is also declared
            if not path:
                raise ValueError("Path not declared")

        path, format_ = Path(path), format_.lower()

        # Check if file exists
        if not path.exists():
            if not path.is_dir():
                raise FileNotFoundError(f"File not found: {path}")
            else:
                raise IsADirectoryError(f"Is a directory: {path}")

        # Check that declared format and file extension match
        InvalidFileFormatError(path, format_).check()

        self.format, self.path = format_, path

        if included is None:
            included = []

        self.included = included

    def read(self) -> dict:
        """Read and load the environment variable strings"""
        return getattr(self, f"__read_{self.format}")()

    def __read_env(self) -> dict:
        """Read and load the environment variable strings from .env file"""
        return dotenv_loads(self.path)

    def __read_ini(self) -> dict:
        """Read and load the environment variable strings from .ini file"""
        config = ConfigParser()
        config.read(self.path)
        return {section: dict(config[section]) for section in config.sections()}

    def __read_json(self) -> dict:
        """Read and load the environment variable strings from .json file"""
        with open(self.path, "r") as file:
            return json_loads(file.read())

    def __read_toml(self) -> dict:
        """Read and load the environment variable strings from .toml file"""
        with open(self.path, "r") as file:
            return toml_loads(file.read())

    def __read_xml(self) -> dict:
        """Read and load the environment variable strings from .xml file"""
        with open(self.path, "r") as file:
            return xml_loads(file.read())

    def __read_yaml(self) -> dict:
        """Read and load the environment variable strings from .yaml file"""
        with open(self.path, "r") as file:
            return yaml_loads(file.read())

    def __read_envs(self) -> dict:
        """Read and load the environment variable strings from environment variables"""

        vars_ = {}
        for var in self.included:
            if var not in environ:
                raise KeyError(f"Environment variable not found: {var}")

            vars_[var] = environ[var]

        return vars_
