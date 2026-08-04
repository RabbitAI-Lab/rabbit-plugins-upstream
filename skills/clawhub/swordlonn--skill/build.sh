#!/bin/bash
# Build the WatchItAI skill zip package from skill/ directory.
#
# Includes ALL 5 platform Go binaries so the same .zip works on:
#   macOS Intel (darwin/amd64)
#   macOS Apple Silicon (darwin/arm64)
#   Linux Intel (linux/amd64)
#   Linux ARM / Graviton / RPi 64-bit (linux/arm64)
#   Windows x64 (windows/amd64)
#
# If bin/ is missing a platform binary, it is fetched from ../watchitai-go/dist/.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
GO_DIST="${PROJECT_ROOT}/watchitai-go/dist"
OUTPUT_DIR="${PROJECT_ROOT}/public"
OUTPUT_FILE="${OUTPUT_DIR}/watchitai-skill.zip"
TMP_DIR=$(mktemp -d)
BIN_DIR="${SCRIPT_DIR}/bin"

REQUIRED_BINS=(
  "watchitai-darwin-amd64"
  "watchitai-darwin-arm64"
  "watchitai-linux-amd64"
  "watchitai-linux-arm64"
  "watchitai-windows-amd64.exe"
)

echo "📦 Building WatchItAI skill package..."

# ---- Validate / fetch binaries -------------------------------------------
mkdir -p "$BIN_DIR"
MISSING=()
for bin in "${REQUIRED_BINS[@]}"; do
  if [ ! -s "${BIN_DIR}/${bin}" ]; then
    if [ -s "${GO_DIST}/${bin}" ]; then
      echo "  ⤵  Copying ${bin} from watchitai-go/dist"
      cp "${GO_DIST}/${bin}" "${BIN_DIR}/${bin}"
      chmod +x "${BIN_DIR}/${bin}" 2>/dev/null || true
    else
      MISSING+=("${bin}")
    fi
  fi
done
if [ "${#MISSING[@]}" -gt 0 ]; then
  echo "❌ Missing binaries, run watchitai-go/build.sh first:" >&2
  for m in "${MISSING[@]}"; do echo "   - $m" >&2; done
  exit 1
fi
echo "  ✅ All 5 platform binaries present"

# ---- Assemble zip payload ------------------------------------------------
mkdir -p "${TMP_DIR}/watchitai/lib" "${TMP_DIR}/watchitai/scripts" "${TMP_DIR}/watchitai/bin"

cp "${SCRIPT_DIR}/SKILL.md"   "${TMP_DIR}/watchitai/"
cp "${SCRIPT_DIR}/README.md"  "${TMP_DIR}/watchitai/" 2>/dev/null || true
cp "${SCRIPT_DIR}/package.json" "${TMP_DIR}/watchitai/"
cp "${SCRIPT_DIR}/config.json"  "${TMP_DIR}/watchitai/"
cp "${SCRIPT_DIR}/run.sh"      "${TMP_DIR}/watchitai/"
cp "${SCRIPT_DIR}/run.cmd"     "${TMP_DIR}/watchitai/"
cp "${SCRIPT_DIR}/install.sh"  "${TMP_DIR}/watchitai/"
cp "${SCRIPT_DIR}/install.ps1" "${TMP_DIR}/watchitai/" 2>/dev/null || true
cp "${SCRIPT_DIR}/lib/"*.js     "${TMP_DIR}/watchitai/lib/" 2>/dev/null || true
cp "${SCRIPT_DIR}/lib/"*.html   "${TMP_DIR}/watchitai/lib/" 2>/dev/null || true
cp "${SCRIPT_DIR}/scripts/"*    "${TMP_DIR}/watchitai/scripts/" 2>/dev/null || true

# Copy all 5 binaries (keep cliclick for macOS)
cp "${BIN_DIR}"/watchitai-*  "${TMP_DIR}/watchitai/bin/"
[ -f "${BIN_DIR}/cliclick" ] && cp "${BIN_DIR}/cliclick" "${TMP_DIR}/watchitai/bin/" || true

chmod +x "${TMP_DIR}/watchitai/bin/"* 2>/dev/null || true

mkdir -p "$OUTPUT_DIR"
rm -f "$OUTPUT_FILE"

( cd "$TMP_DIR" && zip -r "$OUTPUT_FILE" watchitai/ >/dev/null )

rm -rf "$TMP_DIR"

SIZE=$(du -h "$OUTPUT_FILE" | awk '{print $1}')
FILES=$(unzip -l "$OUTPUT_FILE" 2>/dev/null | tail -1 | awk '{print $2}' || echo "?")
echo ""
echo "✅ Skill package built: ${OUTPUT_FILE}"
echo "   Size: ${SIZE}   Files: ${FILES}"
echo "   Platform binaries: darwin-amd64, darwin-arm64, linux-amd64, linux-arm64, windows-amd64.exe"
