"""Pytest fixtures for interactive-webgis tests."""
import importlib.util
import os
import sys
import pytest

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(SKILL_DIR, "geoskill-interactive-webgis.py")


def load_module():
    spec = importlib.util.spec_from_file_location("interactive_webgis", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["interactive_webgis"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


@pytest.fixture
def skill_dir():
    return SKILL_DIR


@pytest.fixture
def script_path():
    return SCRIPT
