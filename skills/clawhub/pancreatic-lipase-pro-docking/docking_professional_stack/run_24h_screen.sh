#!/usr/bin/env bash
set -euo pipefail

# Runs a docking/screening job continuously with checkpoint-friendly logging.
# Usage:
#   bash run_24h_screen.sh ligands.csv
# or:
#   TARGET_PDB=1LPB HOURS=24 EXHAUSTIVENESS=8 CPU=8 bash run_24h_screen.sh ligands.csv

INPUT=${1:-ligands.csv}
HOURS=${HOURS:-24}
EXHAUSTIVENESS=${EXHAUSTIVENESS:-8}
CPU=${CPU:-$(nproc 2>/dev/null || echo 4)}
TARGET_PDB=${TARGET_PDB:-1LPB}
RUN_ID=${RUN_ID:-run_$(date +%Y%m%d_%H%M%S)}
LOG_DIR="logs/$RUN_ID"
mkdir -p "$LOG_DIR"

SECONDS_LIMIT=$((HOURS*3600))

echo "Run ID: $RUN_ID" | tee "$LOG_DIR/summary.log"
echo "Input: $INPUT" | tee -a "$LOG_DIR/summary.log"
echo "Target PDB: $TARGET_PDB" | tee -a "$LOG_DIR/summary.log"
echo "Hours: $HOURS" | tee -a "$LOG_DIR/summary.log"
echo "CPU: $CPU" | tee -a "$LOG_DIR/summary.log"
echo "Exhaustiveness: $EXHAUSTIVENESS" | tee -a "$LOG_DIR/summary.log"

# GNU timeout stops the job after requested duration. The Python script should checkpoint outputs.
timeout "${SECONDS_LIMIT}s" python professional_docking_runner.py \
  --input "$INPUT" \
  --target-pdb "$TARGET_PDB" \
  --mode full \
  --exhaustiveness "$EXHAUSTIVENESS" \
  --cpu "$CPU" \
  --run-id "$RUN_ID" 2>&1 | tee "$LOG_DIR/live.log"

STATUS=${PIPESTATUS[0]}
echo "Exit status: $STATUS" | tee -a "$LOG_DIR/summary.log"
echo "Finished: $(date)" | tee -a "$LOG_DIR/summary.log"
