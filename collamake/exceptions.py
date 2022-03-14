"""This module includes custom exception classes."""


class CollaMakeException(Exception):
    """Base class of all custom exceptions."""

    pass


class NotSupportedNumPics(CollaMakeException):
    """Exception class to raise if the num split is not power of two."""

    pass
