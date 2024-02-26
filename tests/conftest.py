"""Test configuration file"""

# Built-in imports
import json
from os import environ

# PIP installed imports
from pytest import fixture
import toml
import yaml

# Second party imports
from secret_garden.utils import FILE_ENCODING, Path


DATA_DIR = Path(__file__).parent / "data"


DATA = {
    "INT_VAR": 1,
    "FLOAT_VAR": 1.0,
    "STRING_VAR": "hello",
    "BOOL_VAR": True,
    "LIST_INT_VAR": [1, 2, 3],
    "LIST_FLOAT_VAR": [1.0, 2.0, 3.0],
    "LIST_STRING_VAR": ["hello", "world"],
    "LIST_BOOL_VAR": [True, False],
    "DICT_VAR": {"name": "John", "age": 25},
}


@fixture
def excluded_vars():
    """Return the excluded variable"""

    excluded = ["INT_VAR"]
    environ["EXCLUDE"] = str(excluded)

    return excluded


@fixture
def data_dir():
    """Return the data directory"""
    return DATA_DIR


@fixture
def invalid_data_dir():
    """Return the invalid data directory"""
    return Path("/path/to/invalid/directory")


@fixture
def data():
    """Return the test data"""
    return DATA


@fixture
def final_data(excluded_vars):
    """Return the test data without the excluded variables"""

    data_ = DATA.copy()
    for excluded_var in excluded_vars:
        data_.pop(excluded_var)

    return data_


@fixture
def file_formats(excluded_vars):
    """Return the file formats"""

    contents = {
        "env": "\n".join([f"{var}={str(val)}" for var, val in DATA.items()]),
        "json": json.dumps(DATA),
        "toml": toml.dumps(DATA),
        "yaml": yaml.dump(DATA),
    }

    for format_, content in contents.items():
        with open(DATA_DIR / f"env.{format_}", "w", encoding=FILE_ENCODING) as file:
            file.write(content)

    return list(contents.keys())


@fixture
def file_paths(file_formats, excluded_vars):
    """Return the file paths"""

    return [DATA_DIR / f"env.{format_}" for format_ in file_formats]


@fixture
def environ_data():
    """Return the environment data"""
    return {var: str(val) for var, val in DATA.items()}


@fixture
def included_vars(data):
    """Return the included variable"""

    for var, val in data.items():
        environ[var] = str(val)

    return list(data.keys())
