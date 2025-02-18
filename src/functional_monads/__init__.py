from .either import Either, left, right
from .maybe import Maybe, nothing, just

__all__ = ["Either", "left", "right", "Maybe", "nothing", "just"]

# src/my_project/__init__.py
from ._version import get_version_dict

__version__ = get_version_dict()["version"]
