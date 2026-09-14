#!/bin/bash
# run_tests.sh — run the hPL docking stack test suite (pytest).
# Usage: bash run_tests.sh [--debug]
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
PY="${1:-}"
if [ -z "$PY" ] || [ ! -x "$PY" ]; then
  # prefer the conda env (has rdkit + pytest); fall back to system python
  if [ -x /home/user/out/plenv/bin/python ]; then
    PY=/home/user/out/plenv/bin/python
  elif command -v python3 >/dev/null; then
    PY=python3
  else
    echo "no python found"; exit 1
  fi
fi
echo "== running tests with: $PY =="
cd "$HERE"
"$PY" -m pytest tests/ -v --tb=short "$@" 2>&1 | tail -40
