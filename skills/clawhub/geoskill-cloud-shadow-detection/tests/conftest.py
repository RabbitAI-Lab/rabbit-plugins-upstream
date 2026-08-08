"""Pytest fixtures for cloud-shadow-detection tests."""
import importlib.util
import os
import sys
import pytest

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(SKILL_DIR, "geoskill-cloud-shadow-detection.py")


def load_module():
    spec = importlib.util.spec_from_file_location("cloud_shadow_detection", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["cloud_shadow_detection"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


@pytest.fixture
def skill_dir():
    return SKILL_DIR


@pytest.fixture
def script_path():
    return SCRIPT
