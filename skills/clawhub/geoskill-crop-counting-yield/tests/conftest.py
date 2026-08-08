"""Pytest fixtures for crop-counting-yield tests."""
import importlib.util
import os
import sys
import pytest

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(SKILL_DIR, "geoskill-crop-counting-yield.py")


def load_module():
    spec = importlib.util.spec_from_file_location("crop_counting_yield", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["crop_counting_yield"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


@pytest.fixture
def skill_dir():
    return SKILL_DIR


@pytest.fixture
def script_path():
    return SCRIPT
