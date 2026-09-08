#!/bin/sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
python3 -m py_compile "$ROOT/scripts/heart_tool.py" "$ROOT/scripts/selftest.py"
exec python3 "$ROOT/scripts/selftest.py"
