#!/usr/bin/env bash
# restore_and_run.sh — one-shot helper for pancreatic-lipase-pro-docking skill
# Usage:
#   bash restore_and_run.sh /path/to/ligands.csv [extra flags passed to arena_auto_run.py]
#
# Outputs (speed_runs/<run-id>/) are written to the CURRENT WORKING DIRECTORY so
# users calling the skill from their project folder get results next to their data.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
PAYLOAD="$HERE/payload_universal_upload.txt"
TARGET_DIR="$HERE/docking_professional_stack"
INVOKE_DIR="$(pwd)"
if [ ! -f "$PAYLOAD" ]; then
  echo "[!] payload_universal_upload.txt not found next to this script: $PAYLOAD" >&2
  exit 1
fi
if [ ! -d "$TARGET_DIR" ]; then
  echo "[*] Extracting docking stack from universal payload into $HERE ..."
  # Extract INSIDE $HERE (not user's cwd) so $TARGET_DIR is always populated.
  (cd "$HERE" && python3 - "$PAYLOAD" <<'PY'
import sys, base64, re, zipfile, hashlib, io
from pathlib import Path
payload_path = Path(sys.argv[1])
payload = payload_path.read_text(encoding="utf-8", errors="ignore")
m = re.search(r'-----BEGIN BASE64_ZIP_PAYLOAD-----\n(.*?)\n-----END BASE64_ZIP_PAYLOAD-----', payload, re.S)
if not m:
    raise SystemExit('ERROR: payload block not found in ' + str(payload_path))
data = base64.b64decode(''.join(m.group(1).split()))
print(f"    sha256 = {hashlib.sha256(data).hexdigest()}")
print(f"    size   = {len(data)} bytes")
zipfile.ZipFile(io.BytesIO(data)).extractall('.')
print("    extracted -> docking_professional_stack/")
PY
)
fi
if [ ! -d "$TARGET_DIR" ] || [ ! -f "$TARGET_DIR/arena_auto_run.py" ]; then
  echo "[!] Extraction did not produce $TARGET_DIR/arena_auto_run.py — payload may be corrupt." >&2
  exit 1
fi
if [ $# -eq 0 ]; then
  echo "No ligand CSV provided. Showing help:"
  echo "Usage:"
  echo "  bash restore_and_run.sh /path/to/ligands.csv [extra flags]"
  echo "Examples:"
  echo "  bash restore_and_run.sh ligands.csv"
  echo "  bash restore_and_run.sh ligands.csv --exhaustiveness 32 --n-poses 10"
  echo "  bash restore_and_run.sh ligands.csv --quality high --cpu 8"
  echo "  bash restore_and_run.sh ligands.csv --allow-dry     # preview / CI"
  echo
  echo "Outputs (speed_runs/<run-id>/) are written to the current working directory."
  exit 0
fi
INPUT="$1"; shift
# Make INPUT an absolute path before we cd, so arena_auto_run.py finds it regardless
# of where it's invoked from.
if command -v realpath >/dev/null 2>&1; then
  INPUT="$(realpath "$INPUT")"
else
  INPUT="$(python3 -c 'import os,sys; print(os.path.abspath(sys.argv[1]))' "$INPUT")"
fi
# Run arena_auto_run.py from the STACK directory (so relative imports resolve)
# but with user's cwd preserved as the output-writing directory. We do this by
# invoking python with the script's absolute path and not cd'ing permanently.
# However, docking_speed_pipeline uses relative "speed_runs/" and "receptor/"
# paths, so those will be created under INVOKE_DIR (desired).
cd "$INVOKE_DIR"
exec python3 "$TARGET_DIR/arena_auto_run.py" --input "$INPUT" "$@"
