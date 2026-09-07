#!/usr/bin/env bash
set -euo pipefail

# End-to-end high-throughput workflow for 10k-like libraries.
# Usage:
#   bash run_10k_end_to_end.sh ligands.csv

INPUT=${1:-ligands.csv}
# Convert input to an absolute path before changing directories.
if command -v realpath >/dev/null 2>&1; then
  INPUT=$(realpath "$INPUT")
else
  INPUT=$(python -c 'import os,sys; print(os.path.abspath(sys.argv[1]))' "$INPUT")
fi
OUT=${OUT:-chunks_10k}
JOBS=${JOBS:-8}
TOPN=${TOPN:-200}
PER_CLUSTER=${PER_CLUSTER:-5}
TARGET=${TARGET:-1LPB}
SCREEN_QUALITY=${SCREEN_QUALITY:-screen}
REDOCK_QUALITY=${REDOCK_QUALITY:-high}
CPU_PER_DOCK=${CPU_PER_DOCK:-1}
TOTAL_CPU_PER_SUBJOB=${TOTAL_CPU_PER_SUBJOB:-1}

cd "$(dirname "$0")"

python library_chunker.py \
  --input "$INPUT" \
  --out "$OUT" \
  --target-pdb "$TARGET" \
  --quality "$SCREEN_QUALITY" \
  --target-chunk-size 500 \
  --subchunk-size 100 \
  --total-cpu "$TOTAL_CPU_PER_SUBJOB" \
  --cpu-per-dock "$CPU_PER_DOCK" \
  --gi-mode intestinal

cd "$OUT"
if command -v parallel >/dev/null 2>&1; then
  JOBS="$JOBS" bash run_parallel_subchunks.sh
else
  echo "GNU parallel not found; falling back to sequential subchunk runner."
  bash run_all_subchunks.sh
fi
cd ..

python merge_screen_results.py --root "$OUT" --out "$OUT/merged_results.csv"
python select_top_diverse_hits.py --input "$OUT/merged_results.csv" --out "$OUT/top_diverse_hits.csv" --top-n "$TOPN" --per-cluster "$PER_CLUSTER"

python docking_speed_pipeline.py \
  --input "$OUT/top_diverse_hits.csv" \
  --target-pdb "$TARGET" \
  --mode dock \
  --quality "$REDOCK_QUALITY" \
  --total-cpu "$(nproc 2>/dev/null || echo 8)" \
  --cpu-per-dock 2 \
  --gi-mode strict \
  --run-id "${OUT}_redock_top"

echo "DONE. Final redock results: speed_runs/${OUT}_redock_top/final_ranked_results.csv"
