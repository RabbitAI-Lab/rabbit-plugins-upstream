#!/usr/bin/env bash
set -euo pipefail

# Full professional docking/simulation stack installer.
# Recommended for a persistent Linux workstation/cloud VM/HPC login node.
# Usage:
#   bash setup_full_stack.sh
#   micromamba activate pro-docking-full
#   python verify_full_stack.py

ENV_NAME=${ENV_NAME:-pro-docking-full}
ENV_FILE=${ENV_FILE:-environment_full.yml}

if ! command -v micromamba >/dev/null 2>&1 && ! command -v mamba >/dev/null 2>&1 && ! command -v conda >/dev/null 2>&1; then
  echo "No conda/mamba found. Installing micromamba locally into $HOME/micromamba ..."
  mkdir -p "$HOME/micromamba"
  curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj -C "$HOME/micromamba" bin/micromamba
  export PATH="$HOME/micromamba/bin:$PATH"
  eval "$(micromamba shell hook -s bash)"
fi

if command -v micromamba >/dev/null 2>&1; then
  MAMBA=micromamba
elif command -v mamba >/dev/null 2>&1; then
  MAMBA=mamba
else
  MAMBA=conda
fi

echo "Using installer: $MAMBA"
echo "Creating/updating environment: $ENV_NAME from $ENV_FILE"
$MAMBA env create -f "$ENV_FILE" || $MAMBA env update -n "$ENV_NAME" -f "$ENV_FILE"

echo "\nActivate with:"
echo "  $MAMBA activate $ENV_NAME"
echo "Verify with:"
echo "  python verify_full_stack.py"
