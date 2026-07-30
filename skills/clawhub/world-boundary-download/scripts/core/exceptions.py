"""Custom exception hierarchy for the world-boundary-download skill.

All exceptions inherit from :class:`WorldBoundryError` so callers can catch
them generically and individual subclasses allow fine-grained error handling.
"""

from __future__ import annotations


class WorldBoundryError(Exception):
    """Base class for every error raised by this skill."""


class NetworkError(WorldBoundryError):
    """Raised on HTTP / socket failures after retries are exhausted."""


class ResolutionError(WorldBoundryError):
    """Raised when a country name cannot be resolved to an ISO code."""


class DataSourceError(WorldBoundryError):
    """Raised when a data source returns unexpected or missing data.

    Subclasses (or instances) should provide the source name and the
    offending ISO / level pair when known.
    """

    def __init__(self, message: str, *, source: str = "", iso: str = "", level: str = "") -> None:
        super().__init__(message)
        self.source = source
        self.iso = iso
        self.level = level


class FormatError(WorldBoundryError):
    """Raised when conversion between vector formats fails."""


class LicenseError(WorldBoundryError):
    """Raised when a data source's license forbids the requested use."""
