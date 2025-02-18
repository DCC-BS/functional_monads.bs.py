from abc import ABC, abstractmethod
from typing import Any, Callable, Generic, TypeVar

L = TypeVar("L")  # Left type
R = TypeVar("R")  # Right type
T = TypeVar("T")  # Target type for transformations


def left(value: L) -> "Either[L, Any]":
    """Create a Left value."""
    return Left(value)


def right(value: R) -> "Either[Any, R]":
    """Create a Right value."""
    return Right(value)


class Either(ABC, Generic[L, R]):
    def is_right(self) -> bool:
        """Check if this is a Right (success) value."""
        return isinstance(self, Right)

    def is_left(self) -> bool:
        """Check if this is a Left (failure) value."""
        return isinstance(self, Left)

    @abstractmethod
    def map_right(self, f: Callable[[R], T]) -> "Either[L, T]":
        """
        Apply a function to the Right value, leaving Left values unchanged.

        Args:
            f: Function to apply to the Right value

        Returns:
            New Either with the transformed Right value, or the original Left
        """
        pass

    @abstractmethod
    def map_left(self, f: Callable[[L], T]) -> "Either[T, R]":
        """
        Apply a function to the Left value, leaving Right values unchanged.

        Args:
            f: Function to apply to the Left value

        Returns:
            New Either with the transformed Left value, or the original Right
        """
        pass

    @abstractmethod
    def bind_right(self, f: Callable[[R], "Either[L, T]"]) -> "Either[L, T]":
        """
        Chain computations that may succeed.

        Args:
            f: Function that returns a new Either

        Returns:
            Result of applying f to the Right value, or the original Left
        """
        pass

    @abstractmethod
    def bind_left(self, f: Callable[[L], "Either[T, R]"]) -> "Either[T, R]":
        """
        Chain computations that may fail.

        Args:
            f: Function that returns a new Either

        Returns:
            Result of applying f to the Left value, or the original Right
        """
        pass

    @abstractmethod
    def get_or_else_right(self, default: R) -> R:
        """
        Get the Right value or a default if this is a Left.

        Args:
            default: Value to return if this is a Left

        Returns:
            The Right value or the default
        """
        pass

    @abstractmethod
    def get_or_else_left(self, default: L) -> L:
        """
        Get the Left value or a default if this is a Right.

        Args:
            default: Value to return if this is a Right

        Returns:
            The Left value or the default
        """
        pass

    @abstractmethod
    def fold(self, left_f: Callable[[L], T], right_f: Callable[[R], T]) -> T:
        """
        Apply one of two functions depending on whether this is a Left or Right.

        Args:
            left_f: Function to apply to Left value
            right_f: Function to apply to Right value

        Returns:
            Result of applying the appropriate function
        """
        pass

    def __str__(self) -> str:
        match self:
            case Left(value):
                return f"Left({value})"
            case Right(value):
                return f"Right({value})"
            case _:
                raise ValueError("Invalid Either type")

    def __repr__(self) -> str:
        return self.__str__()


class Left(Either[L, R]):
    __match_args__ = ("value",)

    def __init__(self, value: L):
        self.value: L = value

    def map_right(self, f: Callable[[R], T]) -> "Either[L, T]":
        return Left(self.value)

    def map_left(self, f: Callable[[L], T]) -> "Either[T, R]":
        return Left(f(self.value))

    def bind_right(self, f: Callable[[R], "Either[L, T]"]) -> "Either[L, T]":
        return Left(self.value)

    def bind_left(self, f: Callable[[L], "Either[T, R]"]) -> "Either[T, R]":
        return f(self.value)

    def get_or_else_right(self, default: R) -> R:
        return default

    def get_or_else_left(self, default: L) -> L:
        return self.value

    def fold(self, left_f: Callable[[L], T], right_f: Callable[[R], T]) -> T:
        return left_f(self.value)

    def __str__(self) -> str:
        return f"Left({self.value})"

    def __repr__(self) -> str:
        return self.__str__()


class Right(Either[L, R]):
    __match_args__ = ("value",)

    def __init__(self, value: R):
        self.value: R = value

    def map_right(self, f: Callable[[R], T]) -> "Either[L, T]":
        return Right(f(self.value))

    def map_left(self, f: Callable[[L], T]) -> "Either[T, R]":
        return Right(self.value)

    def bind_right(self, f: Callable[[R], "Either[L, T]"]) -> "Either[L, T]":
        return f(self.value)

    def bind_left(self, f: Callable[[L], "Either[T, R]"]) -> "Either[T, R]":
        return Right(self.value)

    def get_or_else_right(self, default: R) -> R:
        return self.value

    def get_or_else_left(self, default: L) -> L:
        return default

    def fold(self, left_f: Callable[[L], T], right_f: Callable[[R], T]) -> T:
        return right_f(self.value)

    def __str__(self) -> str:
        return f"Right({self.value})"

    def __repr__(self) -> str:
        return self.__str__()
