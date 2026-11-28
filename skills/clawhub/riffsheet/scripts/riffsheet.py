#!/usr/bin/env python3
"""riffsheet: measure a short video and lay out the pictures a reading agent needs.

The entry script: the code is the package riffsheet_lib next to it; run with --help for the commands.
Runs as `python3 -I scripts/riffsheet.py ...`: -I leaves this script's folder off the module path, so
it is put back here. It writes no bytecode caches into the skill folder.
"""

import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from riffsheet_lib.cli import main  # noqa: E402  (needs the path above)

if __name__ == "__main__":
    main(entry=os.path.abspath(__file__))
