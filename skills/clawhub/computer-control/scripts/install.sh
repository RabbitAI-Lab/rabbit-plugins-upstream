#!/bin/bash
# Install tarsx (computer-control backend) for the computer-control skill.
set -e
SRC="$(cd "$(dirname "$0")/tarsx" && pwd)"
BIN_DIR="${HOME}/.local/bin"
mkdir -p "$BIN_DIR"
# node_modules for MCP server use is optional; the CLI itself is dependency-free.
mkdir -p "$HOME/.tarsx"
cp "$SRC/cli.mjs" "$HOME/.tarsx/cli.mjs"
cp "$SRC/core.mjs" "$HOME/.tarsx/core.mjs"
cat > "$BIN_DIR/tarsx" <<'WRAPPER'
#!/usr/bin/env node
import path from 'node:path';
const file = path.join(process.env.HOME, '.tarsx', 'cli.mjs');
await import(file);
WRAPPER
chmod +x "$BIN_DIR/tarsx"
echo "tarsx installed -> $BIN_DIR/tarsx"
tarsx info || true
