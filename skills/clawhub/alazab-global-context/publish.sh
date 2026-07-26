#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

python3 -m json.tool alazab-portal-ai-global-context.json >/dev/null

clawhub skill publish . \
  --slug alazab-global-context \
  --version 1.0.0 \
  --owner alazabdev
