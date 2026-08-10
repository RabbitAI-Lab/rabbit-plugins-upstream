"""Pytest configuration for sentinel-downloader tests.

Loads the hyphenated module sentinel-download.py and registers it as
`sentinel_downloader` in sys.modules.
"""
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, ".."))
SCRIPT_PATH = os.path.join(PROJECT_ROOT, "sentinel-download.py")

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

_spec = importlib.util.spec_from_file_location("sentinel_downloader", SCRIPT_PATH)
_module = importlib.util.module_from_spec(_spec)
sys.modules["sentinel_downloader"] = _module
_spec.loader.exec_module(_module)
