#!/usr/bin/env bash
# demo-scene-reel.sh — 官网「你说出场合，工作台改画面」短视频口令序列
# 给人（或 Screen Studio 录制）按节拍执行。默认每步停 2.2s。
#
# 用法：
#   ./scripts/demo-scene-reel.sh           # 完整五场景
#   ./scripts/demo-scene-reel.sh --fast    # 每步 1.4s
#   PAUSE=3 ./scripts/demo-scene-reel.sh  # 自定义停顿
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

PAUSE="${PAUSE:-2.2}"
if [[ "${1:-}" == "--fast" ]]; then PAUSE=1.4; fi

say() { printf '\n\033[38;5;208m▸ %s\033[0m\n' "$*"; }
run() {
  say "$*"
  # shellcheck disable=SC2086
  eval "$@"
  sleep "$PAUSE"
}

clear 2>/dev/null || true
printf '\n  会勇禾口王 · 场景美学引擎\n  你说出场合 · 工作台改画面\n\n'
sleep 1.2

run ./scripts/scene.sh apply daily
printf '  daily   · 米黑默认 · 轻毛玻璃\n'
sleep "$PAUSE"

run ./scripts/scene.sh apply focus
printf '  focus   · 不透明 · 少干扰\n'
sleep "$PAUSE"

run ./scripts/scene.sh apply present
printf '  present · 投屏 · 更大字号 · 藏路径\n'
sleep "$PAUSE"

run ./scripts/scene.sh apply record
printf '  record  · 录屏 · 纯色底 · 不闪光标\n'
sleep 2.8

run ./scripts/scene.sh apply remote
printf '  remote  · SSH · 身份更醒目\n'
sleep "$PAUSE"

run ./scripts/scene.sh apply daily
printf '\n  ✓ 回到 daily\n\n'
sleep 1.0
