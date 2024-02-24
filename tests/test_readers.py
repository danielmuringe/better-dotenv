"""Test reader classes"""

# PIP installed imports

# Second-party imports
from typed_env.parsers import EnvironParser, FileParser, environ
from . import DATA_DIR


DATA_TESTS = {
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


def test_readers_correlation():
    """Ensure all file types return the same result"""

    # Add variables to the environment exclude
    environ["EXCLUDE"] = "['INT_VAR']"

    # TEST FILE READERS
    formats = ["json", "toml", "yaml", "env"]

    prev_test_data = None

    for format_ in formats:
        cur_test_data = FileParser(DATA_DIR / f"env.{format_}", format_).vars

        if prev_test_data is None:
            prev_test_data = cur_test_data

        assert cur_test_data == prev_test_data

    # TEST ENVIRON READER
    # Load test variables in to the environment namespace

    for var, val in prev_test_data.items():
        environ[var] = str(val)

    # Assert that the environ reader returns the same variables
    assert EnvironParser(prev_test_data.keys()).vars == prev_test_data

    # Assert that the excluded variable is not in the environ reader
    assert "INT_VAR" not in prev_test_data

    print(prev_test_data)
