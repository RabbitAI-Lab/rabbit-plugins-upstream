"""core package for world-boundary-download skill.

Exposes the main helper functions and exception classes.
"""

from .exceptions import (
    WorldBoundryError,
    NetworkError,
    ResolutionError,
    DataSourceError,
    FormatError,
    LicenseError,
)

__all__ = [
    "WorldBoundryError",
    "NetworkError",
    "ResolutionError",
    "DataSourceError",
    "FormatError",
    "LicenseError",
]

__version__ = "0.1.0"
