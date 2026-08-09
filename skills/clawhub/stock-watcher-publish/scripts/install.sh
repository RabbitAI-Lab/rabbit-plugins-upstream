#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"
WATCHLIST_DIR="${STOCK_WATCHER_DATA_DIR:-$SKILL_DIR/data}"
WATCHLIST_DIR="${WATCHLIST_DIR/#\~/$HOME}"
WATCHLIST_FILE="$WATCHLIST_DIR/watchlist.txt"

mkdir -p "$WATCHLIST_DIR"
if [ ! -f "$WATCHLIST_FILE" ]; then
    touch "$WATCHLIST_FILE"
    echo "Created empty watchlist file: $WATCHLIST_FILE"
fi

echo "Stock watcher local data initialized."
echo "Watchlist file: $WATCHLIST_FILE"
