"""Conftest for rs-index-calc tests."""

import importlib.util
import os
import sys

def load_module():
    """Load rs-index-calc.py as a module."""
    module_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "rs-index-calc.py")
    spec = importlib.util.spec_from_file_location("rs_index_calc", module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["rs_index_calc"] = module
    spec.loader.exec_module(module)
    return module

rs_index_calc = load_module()
