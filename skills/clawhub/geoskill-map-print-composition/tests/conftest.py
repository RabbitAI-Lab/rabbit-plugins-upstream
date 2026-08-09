"""Pytest fixtures for map-print-composition tests."""
import importlib.util
import os
import sys
import pytest

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(SKILL_DIR, "geoskill-map-print-composition.py")


def load_module():
    spec = importlib.util.spec_from_file_location("map_print_composition", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["map_print_composition"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


@pytest.fixture
def skill_dir():
    return SKILL_DIR


@pytest.fixture
def script_path():
    return SCRIPT
