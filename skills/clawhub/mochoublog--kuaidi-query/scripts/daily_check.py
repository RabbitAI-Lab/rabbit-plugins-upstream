#!/usr/bin/env python3
"""Deprecated compatibility wrapper. Use check_changes.py."""
import sys
from check_changes import main

if __name__ == "__main__":
    print("daily_check.py 已弃用，请改用 check_changes.py", file=sys.stderr)
    raise SystemExit(main(sys.argv[1:]))
