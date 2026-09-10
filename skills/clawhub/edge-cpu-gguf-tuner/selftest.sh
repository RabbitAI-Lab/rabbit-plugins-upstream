#!/bin/sh
# Safe local regression suite. It creates only a temporary directory via Python.
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
python3 -m py_compile "$ROOT/scripts/edge_cpu_tuner.py" "$ROOT/scripts/selftest.py"
exec python3 "$ROOT/scripts/selftest.py"
