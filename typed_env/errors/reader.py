"""Reader errors"""

# Second-party imports
from . import TypedEnvError
from ..utils import ALLOWED_FORMATS, get_extension, Path, Pathy


class ReaderError(TypedEnvError):
    """Error experienced during the reading process"""


class FormatLoaderMissingError(ReaderError):
    """Format loader missing error"""

    def __init__(self, format_: str, name_error: NameError = None):

        message = f"Format loader missing for {format_}."
        check_condition = format_ in ALLOWED_FORMATS

        super().__init__(message, check_condition, raised_from=name_error)


class UnexpectedFormatError(ReaderError):
    """Invalid file format error"""

    def __init__(self, path: Pathy, expected_format: str):

        self.path = Path(path)
        self.expected_format = expected_format

        message = f"Unexpected file format for {path}. Expected {expected_format}."
        check_condition = get_extension(self.path.name) == self.expected_format

        super().__init__(message, check_condition)


class FormatUndeclaredError(ReaderError):
    """Format undeclared error"""

    def __init__(self, format_: str | None):

        message = "Format undeclared."
        check_condition = format_ is not None

        super().__init__(message, check_condition)


class InvalidFormatError(ReaderError):
    """Invalid file format error"""

    def __init__(self, format_: str):

        message = f"""Invalid file format: {format_}.
            Only {ALLOWED_FORMATS} are allowed.
            """
        check_condition = format_ in ALLOWED_FORMATS

        super().__init__(message, check_condition)
