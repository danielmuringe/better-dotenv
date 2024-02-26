"""Test main loading functions"""

# Second-party imports
from . import secret_garden


class TestLoadSpace:
    """Test the load_space function"""

    def test_return_value(self, final_data, included_vars, excluded_vars):
        """Test return value"""
        vars_ = secret_garden.load_space(included_vars)
        assert vars_ == final_data

        # Test excluded variables
        for excluded_var in excluded_vars:
            assert excluded_var not in vars_

    def test_global_variables(self, final_data, included_vars, excluded_vars):
        """Test global variables"""
        secret_garden.load_space(included_vars, globals())
        for var, val in final_data.items():
            assert globals()[var] == val

        # Test excluded variables
        for excluded_var in excluded_vars:
            assert excluded_var not in globals()


class TestLoadFile:
    """Test the load_file function"""

    def test_return_value(self, final_data, data_dir, file_formats, excluded_vars):
        """Test return value"""
        for file_format in file_formats:
            file_path = data_dir / f"env.{file_format}"
            vars_ = secret_garden.load_file(file_path, file_format)
            assert vars_ == final_data

            # Test excluded variables
            for excluded_var in excluded_vars:
                assert excluded_var not in vars_

    def test_global_variables(self, final_data, data_dir, file_formats, excluded_vars):
        """Test global variables"""
        for file_format in file_formats:
            file_path = data_dir / f"env.{file_format}"
            secret_garden.load_file(file_path, file_format, globals())
            for var, val in final_data.items():
                assert globals()[var] == val

            # Test excluded variables
            for excluded_var in excluded_vars:
                assert excluded_var not in globals()


class TestLoad:
    """Test the load function"""

    def test_file_arg_only(
        self,
        final_data,
        file_formats,
        data_dir,
        excluded_vars,
    ):
        """Test loading using file only"""
        for file_format in file_formats:
            file_path = data_dir / f"env.{file_format}"

            # Test return value
            vars_ = secret_garden.load(file_path, format_=file_format)
            assert vars_ == final_data

            # Test global variables
            secret_garden.load(file_path, format_=file_format, globals_=globals())
            for var, val in final_data.items():
                assert globals()[var] == val

            # Test excluded variables
            for excluded_var in excluded_vars:
                assert excluded_var not in vars_
                assert excluded_var not in globals()

    def test_include_arg_only(
        self,
        final_data,
        included_vars,
        excluded_vars,
    ):
        """Test loading using include only"""

        # Test return value
        vars_ = secret_garden.load(included_vars)
        assert vars_ == final_data

        # Test global variables
        secret_garden.load(included_vars, globals_=globals())
        for var, val in final_data.items():
            assert globals()[var] == val

        # Test excluded variables
        for excluded_var in excluded_vars:
            assert excluded_var not in vars_
            assert excluded_var not in globals()

    def test_valid_file_and_include_args(
        self,
        final_data,
        file_formats,
        data_dir,
        included_vars,
        excluded_vars,
    ):
        """Test loading using a valid file and include args"""

        for file_format in file_formats:
            file_path = data_dir / f"env.{file_format}"

            # Test return value
            vars_ = secret_garden.load(file_path, included_vars, format_=file_format)
            assert vars_ == final_data

            # Test global variables
            secret_garden.load(
                file_path,
                included_vars,
                format_=file_format,
                globals_=globals(),
            )
            for var, val in final_data.items():
                assert globals()[var] == val

            # Test excluded variables
            for excluded_var in excluded_vars:
                assert excluded_var not in vars_
                assert excluded_var not in globals()

    def test_invalid_file_and_include_args(
        self,
        final_data,
        file_formats,
        invalid_data_dir,
        included_vars,
        excluded_vars,
    ):
        """Using an invalid file and include args where loader defaults to environment namespace"""

        for file_format in file_formats:
            file_path = invalid_data_dir / f"env.{file_format}"

            # Test return value
            vars_ = secret_garden.load(file_path, included_vars, format_=file_format)
            assert vars_ == final_data

            # Test global variables
            secret_garden.load(
                file_path,
                included_vars,
                format_=file_format,
                globals_=globals(),
            )
            for var, val in final_data.items():
                assert globals()[var] == val

            # Test excluded variables
            for excluded_var in excluded_vars:
                assert excluded_var not in vars_
                assert excluded_var not in globals()
