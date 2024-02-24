"""A better way to manage your dotenv variables"""

# Built-in imports
from os import PathLike

# Second-party imports
from .parsers import (
    EnvironParser,
    FileParser,
)
from .utils import Path, Pathy


__all__ = [
    "load",
    "load_space",
    "load_file",
]


def load_space(include: list[str], globals_: dict = None) -> dict | None:
    """Load the environment variables from the environment namespace

    Args:
        include (list[str]): The environment variables to include
        globals_ (dict, optional): The globals dictionary to use when loading

    Returns:
        dict: The environment variables
    """

    vars_ = EnvironParser(include).vars

    if globals_ is None:
        return vars_
    else:
        globals_.update(vars_)


def load_file(path: Pathy, format_: str, globals_: dict = None) -> dict | None:
    """Args:
        - format_ (str): The format of the file or string. It can be one of the following:

                - 'environ': Load the environment variables from a string
                - 'env': Load the environment variables from a dotenv file
                - 'json': Load the environment variables from a json file
                - 'toml': Load the environment variables from a toml file
                - 'yaml': Load the environment variables from a yaml file

        - path (Pathy): The path to the file or the string containing the environment variables
        - globals_ (dict, optional): The globals to use when loading

    Returns:
        dict: The environment variables
    """

    vars_ = FileParser(path, format_).vars

    if globals_ is None:
        return vars_
    else:
        globals_.update(vars_)


def load(
    path_or_include: Pathy | list[str],
    format_: str = "environ",
    globals_: dict = None,
) -> dict | None:
    """Load the environment variables from a file or a string.

    Args:
        - path_or_include (Pathy): The path to the file containing the environment variables
        or the environment variables to include
        - format_ (str): The format of the file or string. It can be one of the following:

                - 'environ': Load the environment variables from a string
                - 'env': Load the environment variables from a dotenv file
                - 'json': Load the environment variables from a json file
                - 'toml': Load the environment variables from a toml file
                - 'yaml': Load the environment variables from a yaml file

        - globals_ (dict, optional): The globals dictionary to use when loading

    Returns:
        dict: The environment variables
    """

    if isinstance(path_or_include, list):
        return load_space(path_or_include, globals_)
    elif isinstance(path_or_include, (Path, PathLike, str)):
        return load_file(path_or_include, format_, globals_)
    else:
        raise ValueError(
            f'Invalid type "{type(path_or_include)}"for argument "path_or_include"'
        )
