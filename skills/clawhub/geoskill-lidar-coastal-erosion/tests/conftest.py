"""Pytest fixtures for lidar-coastal-erosion tests."""
import importlib.util
import os
import sys
import pytest

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(SKILL_DIR, "geoskill-lidar-coastal-erosion.py")


def load_module():
    spec = importlib.util.spec_from_file_location("lidar_coastal_erosion", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["lidar_coastal_erosion"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


@pytest.fixture
def skill_dir():
    return SKILL_DIR


@pytest.fixture
def script_path():
    return SCRIPT
