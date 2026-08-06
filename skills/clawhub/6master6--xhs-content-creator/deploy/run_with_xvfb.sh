#!/usr/bin/env bash
set -euo pipefail

# Self-contained: derive project root from this script's location (parent of deploy/).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="${PROJECT_ROOT:-$(cd "${SCRIPT_DIR}/.." && pwd)}"
PYTHON_BIN="${PYTHON_BIN:-${PROJECT_ROOT}/.venv/bin/python}"
CONTENT_PATH="${1:-${PROJECT_ROOT}/runtime/my_content.json}"
MODE="${MODE:-publish}"
LOGIN_TIMEOUT="${LOGIN_TIMEOUT:-300}"
DISPLAY_NUM="${DISPLAY_NUM:-99}"

# Optional .env at PROJECT_ROOT (still respected if present for back-compat,
# but the caller in generate_and_publish.py already passes MODE explicitly).
if [ -f "${PROJECT_ROOT}/.env" ]; then
  # shellcheck disable=SC1091
  set -a
  . "${PROJECT_ROOT}/.env"
  set +a
fi

echo "[run] project root: ${PROJECT_ROOT}"
echo "[run] content path: ${CONTENT_PATH}"
echo "[run] mode: ${MODE}"
echo "[run] login timeout: ${LOGIN_TIMEOUT}"

if [ ! -x "${PYTHON_BIN}" ]; then
  echo "[run] python environment not found: ${PYTHON_BIN}" >&2
  exit 1
fi

if [ ! -f "${CONTENT_PATH}" ]; then
  echo "[run] content file not found: ${CONTENT_PATH}" >&2
  exit 1
fi

cd "${PROJECT_ROOT}"

exec xvfb-run \
  --auto-servernum \
  --server-num="${DISPLAY_NUM}" \
  --server-args="-screen 0 1440x1000x24" \
  "${PYTHON_BIN}" \
  "${PROJECT_ROOT}/scripts/publish_xhs.py" \
  --content "${CONTENT_PATH}" \
  --mode "${MODE}" \
  --login-timeout "${LOGIN_TIMEOUT}"
