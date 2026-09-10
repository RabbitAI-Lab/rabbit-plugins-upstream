#!/bin/bash
# run_pipeline.sh — end-to-end hPL docking pipeline (v100.2.0)
#
#   resolve names -> multi-site dock (5 positions) -> re-dock top-N at high
#   exhaustiveness -> comparison report
#
# Usage:
#   bash run_pipeline.sh <molecule_names.txt | ligands.csv> [options...]
#
# Options (passed through):
#   --exhaustiveness N   screen level (default 4)
#   --redock N           re-dock top-N at exhaustiveness 16 (default 10)
#   --workers N          parallel vina workers (default 2)
#   --max-mw / --max-rotb  memory guards (default 700 / 20)
#
# Outputs (in the current directory):
#   molecules_resolved.csv  dock_results/results_all_sites.csv
#   dock_results_ex16/…     REPORT.md
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
SRC="${1:?usage: run_pipeline.sh <names.txt|ligands.csv> [options...]}"
shift

EX=4; REDOCK=10; WORKERS=2
EXTRA=()
while [ $# -gt 0 ]; do
  case "$1" in
    --exhaustiveness) EX="${2}"; shift 2 ;;
    --redock) REDOCK="${2}"; shift 2 ;;
    --workers) WORKERS="${2}"; shift 2 ;;
    *) EXTRA+=("$1") ;;
  esac
done

# 1) resolve names -> SMILES (skip if already a ligands CSV with smiles column)
if grep -qi "smiles" <(head -1 "$SRC") 2>/dev/null; then
  cp "$SRC" molecules_resolved.csv
  echo "[1/4] ligands CSV provided: $(wc -l < molecules_resolved.csv) rows"
else
  echo "[1/4] resolving names via PubChem..."
  python3 "$HERE/resolve_names.py" "$SRC" molecules_resolved.csv molecules_missing.txt
fi

# 2) multi-site docking (checkpointed; re-run resumes)
echo "[2/4] multi-site docking (5 positions, ex=$EX, workers=$WORKERS)..."
python3 "$HERE/multi_site_docking.py" --ligands molecules_resolved.csv \
  --exhaustiveness "$EX" --workers "$WORKERS" "${EXTRA[@]}"

# 3) high-exhaustiveness re-dock of top-N
echo "[3/4] re-docking top-$REDOCK at exhaustiveness 16..."
python3 "$HERE/redock_high.py" --results dock_results/results_all_sites.csv \
  --top "$REDOCK" --exhaustiveness 16 --workers "$WORKERS" "${EXTRA[@]}"

# 4) report
echo "[4/4] building report..."
python3 "$HERE/build_report.py" --results dock_results/results_all_sites.csv \
  --results-ex16 dock_results_ex16/results_ex16.csv \
  --sites-file dock_results/sites.json -o REPORT.md

echo "✅ DONE — see REPORT.md (plus results CSVs + poses in dock_results*/)"
