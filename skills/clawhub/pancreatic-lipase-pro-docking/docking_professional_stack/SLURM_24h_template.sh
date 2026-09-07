#!/usr/bin/env bash
#SBATCH --job-name=dock10x
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=16
#SBATCH --mem=32G
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err

set -euo pipefail
mkdir -p logs
# module load mamba  # uncomment on clusters if needed
# conda activate pro-docking
python docking_10x_pipeline.py --target-pdb 1LPB --input ligands.csv --mode dock --exhaustiveness 8 --cpu ${SLURM_CPUS_PER_TASK:-16}
