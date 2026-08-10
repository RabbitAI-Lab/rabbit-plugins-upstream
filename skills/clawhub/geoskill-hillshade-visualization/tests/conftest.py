"""Pytest fixtures for hillshade-visualization tests."""
import importlib.util
import os
import sys
import pytest

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(SKILL_DIR, "geoskill-hillshade-visualization.py")


def load_module():
    spec = importlib.util.spec_from_file_location("hillshade_visualization", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["hillshade_visualization"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


@pytest.fixture
def skill_dir():
    return SKILL_DIR


@pytest.fixture
def script_path():
    return SCRIPT
