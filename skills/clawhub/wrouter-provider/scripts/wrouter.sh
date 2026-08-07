#!/usr/bin/env bash
# wrouter.sh — tiny helper for the WRouter OpenAI-compatible gateway.
# Usage:
#   wrouter.sh models
#   wrouter.sh chat <model> <prompt>
# Reads WROUTER_BASE_URL / WROUTER_API_KEY from the environment, falling back
# to ~/.config/wrouter/credentials.
set -euo pipefail

cred="${HOME}/.config/wrouter/credentials"
if [ -f "$cred" ]; then
  # shellcheck disable=SC1090
  . "$cred"
fi
BASE_URL="${WROUTER_BASE_URL:-https://wrouter.ai/v1}"
API_KEY="${WROUTER_API_KEY:-}"

if [ -z "$API_KEY" ]; then
  echo "error: WROUTER_API_KEY not set (env or ~/.config/wrouter/credentials)" >&2
  exit 1
fi

cmd="${1:-}"
case "$cmd" in
  models)
    curl -fsS "${BASE_URL%/}/models" -H "Authorization: Bearer ${API_KEY}"
    echo
    ;;
  chat)
    model="${2:?usage: wrouter.sh chat <model> <prompt>}"
    prompt="${3:?usage: wrouter.sh chat <model> <prompt>}"
    curl -fsS "${BASE_URL%/}/chat/completions" \
      -H "Authorization: Bearer ${API_KEY}" \
      -H "Content-Type: application/json" \
      -d "$(cat <<JSON
{"model": "${model}", "messages": [{"role": "user", "content": $(printf '%s' "$prompt" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))')}]}
JSON
)"
    echo
    ;;
  *)
    echo "usage: wrouter.sh {models | chat <model> <prompt>}" >&2
    exit 2
    ;;
esac
