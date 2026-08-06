#!/usr/bin/env bash
# One-time Vedetta x402 client setup (Node 18+).
set -euo pipefail

TARGET="${1:-$HOME/.vedetta-client}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$TARGET"
cd "$TARGET"
if [[ ! -f package.json ]]; then
  npm init -y >/dev/null 2>&1
fi
npm pkg set type=module >/dev/null
npm i @x402/axios @x402/evm axios viem

cp -f "$SCRIPT_DIR/pay.mjs" "$TARGET/pay.mjs"
chmod +x "$TARGET/pay.mjs"

echo "Installed Vedetta client at: $TARGET"
echo "Set: export VEDETTA_X402_PRIVATE_KEY='0x...'  # dedicated low-balance wallet"
echo "Test: cd $TARGET && node pay.mjs '/v1/feed?limit=1'"
