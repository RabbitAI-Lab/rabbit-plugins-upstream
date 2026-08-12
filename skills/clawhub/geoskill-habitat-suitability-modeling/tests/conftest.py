"""Pytest fixtures for habitat-suitability-modeling tests."""
import importlib.util
import os
import sys
import pytest

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(SKILL_DIR, "geoskill-habitat-suitability-modeling.py")


def load_module():
    spec = importlib.util.spec_from_file_location("habitat_suitability_modeling", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["habitat_suitability_modeling"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


@pytest.fixture
def skill_dir():
    return SKILL_DIR


@pytest.fixture
def script_path():
    return SCRIPT
