"""Parent error module for typed_env"""


class TypedEnvError(Exception):
    """Base error class for typed_env"""

    def __init__(
        self,
        message: str = "",
        check_condition: bool = True,
        raised_from=None,
    ):
        self.check_condition = check_condition
        self.message = message
        self.raised_from = raised_from

    def check(self):
        """Check the condition and raise the error if it is met"""

        if self.check_condition:
            super().__init__(f"{self.message}")

            if self.raised_from is not None:
                raise self from self.raised_from
            else:
                raise self
        else:
            return False
