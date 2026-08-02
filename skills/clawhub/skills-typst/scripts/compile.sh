#!/usr/bin/env bash
#
# kirklin-typst · compile.sh
#   Compile a .typ file to PDF with the Typst compiler, then optionally render
#   PNG previews (one per page).
#
# Usage:
#   scripts/compile.sh FILE.typ [options]
#
# Options:
#   --preview         Render one PNG per page (written next to the PDF)
#   --preview-dir D   Directory for the PNGs (implies --preview)
#   --dpi N           Preview resolution in DPI                     (default: 150)
#   --root D          Project root Typst may read files from        (default: file's dir)
#   --font-path D     Add a directory of custom fonts (repeatable)
#   -h, --help        Show this help
#
# Typst compiles in a single pass — it resolves cross-references, citations and
# outlines automatically, and has one engine, so there is no engine flag and no
# multi-run build. Previews are rendered from the PDF with pdftoppm (poppler).
#
set -uo pipefail

die() { printf 'compile.sh: %s\n' "$1" >&2; exit 1; }

FILE="" PREVIEW=0 PREVIEW_DIR="" DPI=150 ROOT="" FONT_PATHS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --preview)     PREVIEW=1; shift ;;
    --preview-dir) PREVIEW=1; PREVIEW_DIR="${2:-}"; shift 2 ;;
    --dpi)         DPI="${2:-}"; shift 2 ;;
    --root)        ROOT="${2:-}"; shift 2 ;;
    --font-path)   FONT_PATHS+=("${2:-}"); shift 2 ;;
    -h|--help)     sed -n '2,19p' "$0"; exit 0 ;;
    -*)            die "unknown option: $1 (try --help)" ;;
    *)             FILE="$1"; shift ;;
  esac
done

[ -n "$FILE" ] || die "no .typ file given (try --help)"
[ -f "$FILE" ] || die "file not found: $FILE"
command -v typst >/dev/null 2>&1 || die "typst not found — install it (e.g. 'brew install typst')"

DIR="$(cd "$(dirname "$FILE")" && pwd)"
BASE="$(basename "$FILE")"
STEM="${BASE%.typ}"
PDF="$DIR/$STEM.pdf"

# --- assemble typst args ----------------------------------------------------
ARGS=(compile --root "${ROOT:-$DIR}")
for fp in "${FONT_PATHS[@]:-}"; do
  [ -n "$fp" ] && ARGS+=(--font-path "$fp")
done
ARGS+=("$DIR/$BASE" "$PDF")

# --- compile ----------------------------------------------------------------
echo "→ compiling $BASE  (typst)"
if ! typst "${ARGS[@]}"; then
  die "compilation failed — see the Typst diagnostics above"
fi
[ -f "$PDF" ] || die "no PDF produced"

PAGES="$(pdfinfo "$PDF" 2>/dev/null | awk '/^Pages/{print $2}')"
echo "✓ $PDF  (${PAGES:-?} pages)"

# --- previews ---------------------------------------------------------------
if [ "$PREVIEW" = 1 ]; then
  command -v pdftoppm >/dev/null 2>&1 || die "pdftoppm not found — install poppler-utils"
  OUT="${PREVIEW_DIR:-$DIR}"
  mkdir -p "$OUT"
  pdftoppm -png -r "$DPI" "$PDF" "$OUT/${STEM}-page"
  echo "✓ previews: $OUT/${STEM}-page-*.png"
fi
