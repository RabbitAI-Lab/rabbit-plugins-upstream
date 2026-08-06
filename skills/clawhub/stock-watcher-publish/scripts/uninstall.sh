#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
WATCHLIST_DIR="${STOCK_WATCHER_DATA_DIR:-$SKILL_DIR/data}"
WATCHLIST_DIR="${WATCHLIST_DIR/#\~/$HOME}"

if [ -d "$WATCHLIST_DIR" ]; then
    rm -rf "$WATCHLIST_DIR"
    echo "Removed watchlist directory: $WATCHLIST_DIR"
fi

echo "Stock watcher local data removed."
