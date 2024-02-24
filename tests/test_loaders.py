"""Test main loading functions"""

# Second-party imports
from secret_garden import load, load_file, load_space


def test_load_space(final_data, included_vars, excluded_vars):
    """Test the load_space function"""

    # Test return value
    vars_ = load_space(included_vars)
    assert vars_ == final_data

    for excluded_var in excluded_vars:
        assert excluded_var not in vars_

    # Test global variables
    load_space(included_vars, globals())
    for var, val in final_data.items():
        assert globals()[var] == val

    for excluded_var in excluded_vars:
        assert excluded_var not in vars_


def test_load_file(final_data, data_dir, file_formats):
    """Test the load_file function"""

    for file_format in file_formats:
        file_path = data_dir / f"env.{file_format}"

        # Test return value
        vars_ = load_file(file_path, file_format)
        assert vars_ == final_data

        # Test global variables
        load_file(file_path, file_format, globals())
        for var, val in final_data.items():
            assert globals()[var] == val


def test_load(final_data, file_formats, data_dir, included_vars, excluded_vars):
    """Test the load function"""

    # TEST FILE VARS
    for file_format in file_formats:
        file_path = data_dir / f"env.{file_format}"

        # Test return value
        vars_ = load(file_path, file_format)
        assert vars_ == final_data

        # Test global variables
        load(file_path, file_format, globals())
        for var, val in final_data.items():
            assert globals()[var] == val

    # TEST SPACE VARS
    # Test return value
    vars_ = load(included_vars)
    assert vars_ == final_data

    for excluded_var in excluded_vars:
        assert excluded_var not in vars_

    # Test global variables
    load(included_vars, globals())
    for var, val in final_data.items():
        assert globals()[var] == val

    for excluded_var in excluded_vars:
        assert excluded_var not in vars_
