#!/usr/bin/env bash
# yuanlin_qty 跨平台 CLI 入口（macOS / Linux；Windows 用 scripts/yuanlin_qty.cmd 或 python scripts/yuanlin_qty.py）。
exec python3 "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/yuanlin_qty.py" "$@"
