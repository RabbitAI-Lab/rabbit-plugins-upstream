#!/bin/bash
# ============================================================
# WatchItAI Skill - Install to Trae global skills directory
#
# The skill uses a self-contained Go binary — no npm install needed.
#
# Usage:
#   bash skill/install.sh
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_DIR="$HOME/.trae-cn/skills/watchitai"

echo "📦 Installing WatchItAI skill to Trae..."
echo "   Source: $SCRIPT_DIR"
echo "   Target: $TARGET_DIR"
echo ""

# Remove existing installation if present
if [ -d "$TARGET_DIR" ] || [ -L "$TARGET_DIR" ]; then
    echo "🗑️  Removing existing installation..."
    rm -rf "$TARGET_DIR"
fi

# Create target directory
mkdir -p "$TARGET_DIR"

# Copy skill files (excluding node_modules, install scripts, and test files)
echo "📋 Copying skill files..."
cp -R "$SCRIPT_DIR"/. "$TARGET_DIR"/
rm -rf "$TARGET_DIR/node_modules"
rm -f "$TARGET_DIR/install.sh"
rm -f "$TARGET_DIR/install.ps1"
rm -f "$TARGET_DIR/test_capture.cjs" "$TARGET_DIR/test_control.cjs" "$TARGET_DIR/test-ws.js"
rm -f "$TARGET_DIR/index.js"  # Legacy Node.js wrapper (removed, now using run.sh)

# Ensure binaries are executable
chmod +x "$TARGET_DIR/bin/"* 2>/dev/null || true

# Verify the Go binary exists for this platform
PLATFORM=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)
if [ "$ARCH" = "x86_64" ]; then
    ARCH="amd64"
elif [ "$ARCH" = "arm64" ] || [ "$ARCH" = "aarch64" ]; then
    ARCH="arm64"
fi
BINARY_NAME="watchitai-${PLATFORM}-${ARCH}"
BINARY_PATH="$TARGET_DIR/bin/$BINARY_NAME"

if [ -f "$BINARY_PATH" ]; then
    chmod +x "$BINARY_PATH"
    echo "✅ Binary found: $BINARY_NAME"
    "$BINARY_PATH" version
else
    echo "⚠️  Binary not found for platform: $PLATFORM/$ARCH"
    echo "   Expected: $BINARY_PATH"
    echo "   Please download the correct binary from https://watchitai.net"
fi

echo ""
echo "✅ Installation complete! No Node.js, no npm install needed."
echo ""
echo "📁 Installed files:"
ls -la "$TARGET_DIR" | head -15
echo ""
echo "📄 SKILL.md frontmatter:"
head -4 "$TARGET_DIR/SKILL.md"
echo ""
echo "🎉 WatchItAI skill installed successfully!"
echo "   The skill uses a self-contained Go binary."
echo "   Usage: bash ~/.trae-cn/skills/watchitai/run.sh share"
