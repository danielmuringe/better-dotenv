"""Reader errors"""

# Second-party imports
from . import TypedEnvError
from ..utils import get_extension, Path, Pathy


class InvalidFileFormatError(TypedEnvError):
    """Invalid file format error"""

    def __init__(self, path: Pathy, expected_format: str):

        self.path = Path(path)
        self.expected_format = expected_format

        message = f"Invalid file format for {path}. Expected {expected_format}."
        check_condition = get_extension(self.path.name) == self.expected_format

        super().__init__(message, check_condition, raised_from=None)
