"""Pytest fixtures for atmospheric-correction tests."""
import importlib.util
import os
import sys

import pytest

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(SKILL_DIR, "geoskill-atmospheric-correction.py")


def load_module():
    """Load atmospheric-correction.py as a module."""
    spec = importlib.util.spec_from_file_location("atmospheric_correction", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["atmospheric_correction"] = module
    spec.loader.exec_module(module)
    return module


ac = load_module()


@pytest.fixture
def skill_dir():
    return SKILL_DIR


@pytest.fixture
def script_path():
    return SCRIPT


@pytest.fixture
def tmp_output(tmp_path):
    return str(tmp_path / "output")
