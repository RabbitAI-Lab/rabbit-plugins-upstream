#!/usr/bin/env bash
set -euo pipefail

# Self-contained: derive project root from this script's location (parent of deploy/).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${PROJECT_ROOT:-$(cd "${SCRIPT_DIR}/.." && pwd)}"
PYTHON_BIN="${PYTHON_BIN:-python3}"

echo "[project] project root: ${PROJECT_ROOT}"
echo "[project] preparing project directories"

# runtime/ subdirs are pre-created by the skill loader (.gitkeep placeholders).
# Ensure they exist in case someone cloned fresh without the placeholders.
mkdir -p "${PROJECT_ROOT}/runtime/browser-profile"
mkdir -p "${PROJECT_ROOT}/runtime/runs"
mkdir -p "${PROJECT_ROOT}/runtime/lobster-notify"
mkdir -p "${PROJECT_ROOT}/runtime/inbound"

if [ ! -d "${PROJECT_ROOT}/.venv" ]; then
  echo "[project] creating virtual environment"
  "${PYTHON_BIN}" -m venv "${PROJECT_ROOT}/.venv"
fi

echo "[project] installing python dependencies"
"${PROJECT_ROOT}/.venv/bin/pip" install --upgrade pip
"${PROJECT_ROOT}/.venv/bin/pip" install -r "${PROJECT_ROOT}/requirements.txt"

echo "[project] installing playwright chromium into this project environment"
"${PROJECT_ROOT}/.venv/bin/python" -m playwright install chromium

echo "[project] done"
echo "[project] root: ${PROJECT_ROOT}"