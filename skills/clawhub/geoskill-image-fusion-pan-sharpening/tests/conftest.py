"""Pytest fixtures for image-fusion-pan-sharpening tests."""
import importlib.util
import os
import sys
import pytest

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(SKILL_DIR, "geoskill-image-fusion-pan-sharpening.py")


def load_module():
    spec = importlib.util.spec_from_file_location("image_fusion_pan_sharpening", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules["image_fusion_pan_sharpening"] = module
    spec.loader.exec_module(module)
    return module


mod = load_module()


@pytest.fixture
def skill_dir():
    return SKILL_DIR


@pytest.fixture
def script_path():
    return SCRIPT
