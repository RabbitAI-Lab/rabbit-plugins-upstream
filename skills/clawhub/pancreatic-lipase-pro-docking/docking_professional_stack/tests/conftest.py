"""pytest fixtures: point sys.path at the docking stack under test."""
import sys
from pathlib import Path

_here = Path(__file__).resolve().parent.parent
_cands = [
    _here,                                                     # tests/ inside the stack root (payload layout)
    _here / "stack" / "docking_professional_stack",            # dev layout
]
STACK = next((c for c in _cands if (c / "multi_site_docking.py").exists()), _cands[0])
sys.path.insert(0, str(STACK))

import pytest


@pytest.fixture(scope="session")
def stack_dir():
    return STACK


@pytest.fixture(scope="session")
def real_receptor():
    """1LPB receptor PDB if available (skipped otherwise)."""
    cands = [
        STACK / "receptor" / "1LPB.pdb",
        Path("/home/user/skillbuild_v300/receptor_1LPB.pdb"),
        Path("/home/user/skillbuild_v200/receptor_1LPB.pdb"),
    ]
    for c in cands:
        if c.exists():
            return c
    return None
