"""Pytest fixtures for text-to-map-nlp tests."""
import importlib.util
import os
import sys
import pytest

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(SKILL_DIR, "geoskill-text-to-map-nlp.py")


def load_module():
    spec = importlib.util.spec_from_file_location("text_to_map_nlp", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["text_to_map_nlp"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


@pytest.fixture
def skill_dir():
    return SKILL_DIR


@pytest.fixture
def script_path():
    return SCRIPT
