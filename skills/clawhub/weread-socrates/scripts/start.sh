#!/bin/bash
# weread-socrates v1.3.1 · 一键诊断并启动
set -euo pipefail
SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PORT="${PORT:-3456}"
CHECK_ONLY=0
FORCE_DEMO=0
for arg in "$@"; do
  case "$arg" in
    --check|--doctor) CHECK_ONLY=1 ;;
    --demo) FORCE_DEMO=1 ;;
    -h|--help) echo "用法: bash scripts/start.sh [--check|--demo]"; exit 0 ;;
    *) echo "未知参数: $arg"; exit 2 ;;
  esac
done

load_key_file() {
  local file="$1" line value
  [ -f "$file" ] || return 0
  while IFS= read -r line || [ -n "$line" ]; do
    case "$line" in
      WEREAD_API_KEY=*|export\ WEREAD_API_KEY=*)
        value="${line#*WEREAD_API_KEY=}"
        value="${value#\"}"; value="${value%\"}"
        SQ="$(printf "\\047")"; value="${value#"$SQ"}"; value="${value%"$SQ"}"
        [ -n "$value" ] && export WEREAD_API_KEY="$value"
        ;;
    esac
  done < "$file"
}

if [ "$FORCE_DEMO" -eq 1 ]; then unset WEREAD_API_KEY || true; fi
if [ -z "${WEREAD_API_KEY:-}" ] && [ "$FORCE_DEMO" -eq 0 ]; then
  load_key_file "$SKILL_DIR/.env.local"
  load_key_file "${HOME}/.config/weread-socrates/config"
fi

export PORT
bash "$SKILL_DIR/scripts/doctor.sh"
[ "$CHECK_ONLY" -eq 1 ] && exit 0

PID_FILE="$SKILL_DIR/assets/.server.pid"
OLD_PID=""
if [ -f "$PID_FILE" ]; then
  IFS= read -r OLD_PID < "$PID_FILE" || true
  case "$OLD_PID" in ""|*[!0-9]*) OLD_PID="" ;; esac
  if [ -n "$OLD_PID" ] && ! kill -0 "$OLD_PID" 2>/dev/null; then rm -f "$PID_FILE"; OLD_PID=""; fi
fi
if [ -n "$OLD_PID" ]; then
  echo "检测到旧服务 PID $OLD_PID，正在安全停止…"
  kill "$OLD_PID" 2>/dev/null || true
  for _ in 1 2 3 4 5; do kill -0 "$OLD_PID" 2>/dev/null || break; sleep 0.5; done
fi
if command -v lsof >/dev/null 2>&1; then
  PIDS="$(lsof -tiTCP:"$PORT" -sTCP:LISTEN 2>/dev/null || true)"
  if [ -n "$PIDS" ]; then
    echo "错误：端口 $PORT 被其他程序占用，不会自动终止。"
    exit 1
  fi
fi

echo "启动 AI 伴读：http://localhost:${PORT}"
echo "停止服务：按 Ctrl+C，或运行 bash scripts/stop.sh"
exec node "$SKILL_DIR/assets/server.js"
