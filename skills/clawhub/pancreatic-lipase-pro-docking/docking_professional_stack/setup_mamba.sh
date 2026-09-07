#!/usr/bin/env bash
set -euo pipefail

# Professional docking stack installer for a Linux workstation/cloud VM.
# Recommended: run inside a persistent machine, not a temporary sandbox.

ENV_NAME="pro-docking"

if ! command -v micromamba >/dev/null 2>&1 && ! command -v mamba >/dev/null 2>&1 && ! command -v conda >/dev/null 2>&1; then
  echo "No conda/mamba found. Installing micromamba locally into $HOME/micromamba ..."
  mkdir -p "$HOME/micromamba"
  curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj -C "$HOME/micromamba" bin/micromamba
  export PATH="$HOME/micromamba/bin:$PATH"
  eval "$(micromamba shell hook -s bash)"
  micromamba create -y -n base -c conda-forge
else
  echo "Found conda/mamba/micromamba."
fi

if command -v micromamba >/dev/null 2>&1; then
  MAMBA=micromamba
elif command -v mamba >/dev/null 2>&1; then
  MAMBA=mamba
else
  MAMBA=conda
fi

echo "Creating environment $ENV_NAME ..."
$MAMBA env create -f environment.yml || $MAMBA env update -n "$ENV_NAME" -f environment.yml

echo "\nInstallation complete. Activate with:"
echo "  $MAMBA activate $ENV_NAME"
echo "\nVerify with:"
echo "  python verify_stack.py"
