#!/usr/bin/env bash
set -euo pipefail
# Usage: run_pipeline.sh PDF WORKDIR PROVIDERS_JSON TITLE
PDF="${1:?PDF required}"; WORK="${2:?workdir required}"; PROVIDERS="${3:?providers JSON required}"; TITLE="${4:?title required}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; mkdir -p "$WORK"
python3 "$ROOT/scripts/preflight.py"
python3 "$ROOT/scripts/extract_dual_ocr.py" "$PDF" --out "$WORK/extraction"
python3 "$ROOT/scripts/reasoning_team_correct.py" "$WORK/extraction/evidence.json" --providers "$PROVIDERS" --out "$WORK/corrections"
python3 "$ROOT/scripts/detect_session_candidates.py" "$WORK/corrections/final.json" --out "$WORK/session_candidates.json"
cat <<EOF
PAUSE — human/agent review required.
Review $WORK/session_candidates.json against rendered pages and create:
  $WORK/sessions.json
using templates/sessions.example.json. Then continue with:

python3 "$ROOT/scripts/reasoning_team_enrich.py" "$WORK/corrections/final.json" "$WORK/sessions.json" --providers "$PROVIDERS" --out "$WORK/enrichment" --maximum
python3 "$ROOT/scripts/build_selfcontained_html.py" "$WORK/corrections/final.json" "$WORK/extraction" "$WORK/enrichment/all.json" --output "$WORK/studyguide.html" --title "$TITLE"
python3 "$ROOT/scripts/fidelity_audit.py" "$WORK/extraction/evidence.json" "$WORK/corrections/final.json" --out "$WORK/fidelity.json"
python3 "$ROOT/scripts/qa_gates.py" "$WORK/studyguide.html"
python3 "$ROOT/scripts/verify_zip.py" "$WORK" "$WORK/final-studyguide.zip"
EOF
