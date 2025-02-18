from typing import Callable, Generic, TypeVar, Union, cast
from abc import ABC, abstractmethod

T = TypeVar("T")
U = TypeVar("U")


def just(value: T) -> "Maybe[T]":
    """
    Create a Just instance with the given value.

    Args:
        value (T): The value to wrap in a Just.

    Returns:
        Maybe[T]: A Just instance containing the value.
    """
    return Just(value)


def nothing() -> "Maybe[T]":
    """
    Create a Nothing instance.

    Returns:
        Maybe[T]: A Nothing instance.
    """
    return Nothing()


class Maybe(ABC, Generic[T]):
    """
    Abstract base class representing an optional value.
    """

    def __init__(self, value: Union[T, None]):
        self._value = value

    @abstractmethod
    def is_nothing(self) -> bool:
        """
        Check if the instance is a Nothing.

        Returns:
            bool: True if the instance is a Nothing, False otherwise.
        """
        pass

    @abstractmethod
    def is_just(self) -> bool:
        """
        Check if the instance is a Just.

        Returns:
            bool: True if the instance is a Just, False otherwise.
        """
        pass

    @abstractmethod
    def map(self, func: Callable[[T], U]) -> "Maybe[U]":
        """
        Apply a function to the value if it is a Just.

        Args:
            func (Callable[[T], U]): The function to apply.

        Returns:
            Maybe[U]: A new Maybe instance with the result of the function.
        """
        pass

    @abstractmethod
    def bind(self, func: Callable[[T], "Maybe[U]"]) -> "Maybe[U]":
        """
        Apply a function that returns a Maybe to the value if it is a Just.

        Args:
            func (Callable[[T], Maybe[U]]): The function to apply.

        Returns:
            Maybe[U]: The result of the function.
        """
        pass

    def get_or_else(self, default: T) -> T:
        """
        Get the value if it is a Just, otherwise return the default value.

        Args:
            default (T): The default value to return if the instance is a Nothing.

        Returns:
            T: The value or the default value.
        """
        if isinstance(self, Nothing):
            return default

        return cast(Just[T], self).just_value

    def __irshift__(self, func: Callable[[T], "Maybe[U]"]) -> "Maybe[U]":
        """
        Apply a function that returns a Maybe to the value using the >> operator.

        Args:
            func (Callable[[T], Maybe[U]]): The function to apply.

        Returns:
            Maybe[U]: The result of the function.
        """
        return self.bind(func)

    def __repr__(self) -> str:
        """
        Get a string representation of the instance.

        Returns:
            str: The string representation.
        """
        if self.is_nothing():
            return "Nothing"
        return f"Just({self._value})"


class Just(Generic[T], Maybe[T]):
    """
    Class representing a value that is present.
    """

    def __init__(self, value: T):
        if value is None:
            raise ValueError("Some value cannot be None")
        self._value: T = value

    @property
    def just_value(self) -> T:
        """
        Get the value contained in the Just.

        Returns:
            T: The value.
        """
        return self._value

    def is_nothing(self) -> bool:
        """
        Check if the instance is a Nothing.

        Returns:
            bool: False, as this is a Just.
        """
        return False

    def is_just(self) -> bool:
        """
        Check if the instance is a Just.

        Returns:
            bool: True, as this is a Just.
        """
        return True

    def map(self, func: Callable[[T], U]) -> Maybe[U]:
        """
        Apply a function to the value.

        Args:
            func (Callable[[T], U]): The function to apply.

        Returns:
            Maybe[U]: A new Just instance with the result of the function.
        """
        return Just(func(self._value))

    def bind(self, func: Callable[[T], Maybe[U]]) -> Maybe[U]:
        """
        Apply a function that returns a Maybe to the value.

        Args:
            func (Callable[[T], Maybe[U]]): The function to apply.

        Returns:
            Maybe[U]: The result of the function.
        """
        return func(self._value)


class Nothing(Generic[T], Maybe[T]):
    """
    Class representing the absence of a value.
    """

    def __init__(self) -> None:
        self._value = None

    def is_nothing(self) -> bool:
        """
        Check if the instance is a Nothing.

        Returns:
            bool: True, as this is a Nothing.
        """
        return True

    def is_just(self) -> bool:
        """
        Check if the instance is a Just.

        Returns:
            bool: False, as this is a Nothing.
        """
        return False

    def map(self, func: Callable[[T], U]) -> Maybe[U]:
        """
        Apply a function to the value, which does nothing as this is a Nothing.

        Args:
            func (Callable[[T], U]): The function to apply.

        Returns:
            Maybe[U]: A Nothing instance.
        """
        return Nothing()

    def bind(self, func: Callable[[T], Maybe[U]]) -> Maybe[U]:
        """
        Apply a function that returns a Maybe to the value, which does nothing as this is a Nothing.

        Args:
            func (Callable[[T], Maybe[U]]): The function to apply.

        Returns:
            Maybe[U]: A Nothing instance.
        """
        return Nothing()
