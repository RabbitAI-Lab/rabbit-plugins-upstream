#!/usr/bin/env bash
#SBATCH --job-name=dock_chunks
#SBATCH --array=0-99
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --output=logs/chunk_%A_%a.out
#SBATCH --error=logs/chunk_%A_%a.err

set -euo pipefail
mkdir -p logs
# conda activate pro-docking
FILE=$(sed -n "$((SLURM_ARRAY_TASK_ID+1))p" subchunk_files.txt)
echo "Running subchunk: $FILE"
python ../docking_speed_pipeline.py \
  --input "$FILE" \
  --target-pdb 1LPB \
  --mode dock \
  --quality standard \
  --total-cpu ${SLURM_CPUS_PER_TASK:-4} \
  --cpu-per-dock 1 \
  --gi-mode intestinal \
  --quiet \
  --no-html \
  --run-id "$(basename "$FILE" .csv)"
