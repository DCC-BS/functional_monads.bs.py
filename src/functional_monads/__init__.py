from .either import Either, Left, Right, left, right
from .maybe import Maybe, Just, Nothing, nothing, just
from ._version import get_version_dict

__all__ = [
    "Either",
    "left",
    "right",
    "Maybe",
    "nothing",
    "just",
    "Just",
    "Nothing",
    "Left",
    "Right",
]

__version__ = get_version_dict()["version"]
