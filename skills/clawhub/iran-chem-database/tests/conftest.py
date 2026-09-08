"""Shared test fixtures."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Hermetic tests: never hit PubChem for CAS→structure resolution unless a test
# opts back in explicitly (config is a process-wide singleton, so this must be
# set before the first get_config() call).
os.environ.setdefault("IRANCHEM__PARSING__RESOLVE_CAS_STRUCTURES", "false")

FIXTURES = Path(__file__).parent / "fixtures"
