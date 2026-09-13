#!/bin/sh
set -eu

bin="${TOKEN_STATS_BIN:-${AI_TOKEN_STATS_BIN:-token-stats}}"
agent="${AI_TOKEN_AGENT:-all}"
day="${AI_TOKEN_DAY:-$(date +%F)}"

if ! command -v "$bin" >/dev/null 2>&1; then
  echo "token-stats not found; set TOKEN_STATS_BIN or add token-stats to PATH" >&2
  exit 127
fi

set -- usage --agent "$agent" --day "$day" --refresh --output json

if [ -n "${AI_TOKEN_DATA_DIR:-}" ]; then
  set -- "$@" --data-dir "$AI_TOKEN_DATA_DIR"
fi
if [ -n "${AI_TOKEN_CODEX_HOME:-}" ]; then
  set -- "$@" --codex-home "$AI_TOKEN_CODEX_HOME"
fi
if [ -n "${AI_TOKEN_CLAUDE_HOME:-}" ]; then
  set -- "$@" --claude-home "$AI_TOKEN_CLAUDE_HOME"
fi
if [ -n "${AI_TOKEN_OPENCLAW_HOME:-}" ]; then
  set -- "$@" --openclaw-home "$AI_TOKEN_OPENCLAW_HOME"
fi
if [ -n "${AI_TOKEN_HERMES_HOME:-}" ]; then
  set -- "$@" --hermes-home "$AI_TOKEN_HERMES_HOME"
fi
if [ -n "${AI_TOKEN_OPENCODE_HOME:-}" ]; then
  set -- "$@" --opencode-home "$AI_TOKEN_OPENCODE_HOME"
fi
if [ -n "${AI_TOKEN_DEEPSEEK_HOME:-}" ]; then
  set -- "$@" --deepseek-home "$AI_TOKEN_DEEPSEEK_HOME"
fi
if [ -n "${AI_TOKEN_WORKBUDDY_HOME:-}" ]; then
  set -- "$@" --workbuddy-home "$AI_TOKEN_WORKBUDDY_HOME"
fi
if [ -n "${AI_TOKEN_WORKBUDDY_AI_HOME:-}" ]; then
  set -- "$@" --workbuddy-ai-home "$AI_TOKEN_WORKBUDDY_AI_HOME"
fi

if [ -n "${AI_TOKEN_RUN_DIR:-}" ]; then
  mkdir -p "$AI_TOKEN_RUN_DIR"
  stamp="$(date +%Y%m%dT%H%M%S%z)"
  output_file="$AI_TOKEN_RUN_DIR/${agent}-${day}-${stamp}.json"
  "$bin" "$@" > "$output_file"
  cat "$output_file"
else
  "$bin" "$@"
fi
