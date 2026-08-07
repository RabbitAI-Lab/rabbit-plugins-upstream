#!/usr/bin/env python3
"""Basic tests for skill debugging."""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

class TestSkillDebug(unittest.TestCase):
    def test_debugger_import(self):
        """Test that debugger can be imported."""
        try:
            import debugger
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Could not import debugger: {e}")
    
    def test_recovery_import(self):
        """Test that recovery can be imported."""
        try:
            import recovery
            self.assertTrue(True)
        except ImportError as e:
            self.fail(f"Could not import recovery: {e}")

if __name__ == "__main__":
    unittest.main()
