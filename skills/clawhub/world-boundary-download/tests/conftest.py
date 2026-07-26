"""Pytest configuration for the world-boundary-download skill tests.

The test suite uses the layout::

    tests/
        conftest.py
        test_iso_resolver.py
        test_geoboundaries.py
        test_gadm.py
        test_format.py
        test_format_integration.py
        test_geometry.py
        test_cache.py
        test_sources.py

Tests that hit the network are marked with ``@pytest.mark.network``.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

# Make the scripts/ directory importable as `core` etc.
SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def pytest_configure(config: pytest.Config) -> None:
    """Register the custom `network` marker used by integration tests."""

    config.addinivalue_line(
        "markers",
        "network: tests that require live network access to public APIs",
    )

