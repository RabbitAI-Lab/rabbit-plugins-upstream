#!/usr/bin/env bash
# 9router-web-search: safe search wrapper (read-only GET/POST, never logs secret).
#
# Reads configuration ONLY from the environment:
#   NINEROUTER_URL   - base URL of the 9Router instance (required)
#   NINEROUTER_KEY   - bearer token (optional; only sent if server needs auth)
#
# The token is read from the environment and is NEVER printed, echoed, or logged.
# Usage:
#   search_wrapper.sh "my query" [provider] [max_results]
#
# Examples:
#   export NINEROUTER_URL="https://my.router.example.com"
#   export NINEROUTER_KEY="..."      # optional; never echoed by this script
#   ./search_wrapper.sh "latest LLM benchmarks" "tavily" 5
#   ./search_wrapper.sh "gold price" "search-combo" 10
set -euo pipefail

query="${1:-}"
provider="${2:-tavily}"
max_results="${3:-5}"

if [ -z "$query" ]; then
  echo "usage: $0 <query> [provider] [max_results]" >&2
  exit 2
fi

if [ -z "${NINEROUTER_URL:-}" ]; then
  echo "ERROR: NINEROUTER_URL is not set in the environment." >&2
  exit 3
fi

# Build the JSON body without ever expanding the secret into logs.
body=$(printf '{"model":"%s","query":%s,"max_results":%s}' \
  "$provider" "$(printf '%s' "$query" | python3 -c 'import sys,json;print(json.dumps(sys.stdin.read()))')" \
  "$max_results")

# Decide headers: only attach Authorization if a token is present.
headers=(-H "Content-Type: application/json")
if [ -n "${NINEROUTER_KEY:-}" ]; then
  headers+=(-H "Authorization: Bearer ${NINEROUTER_KEY}")
fi

# Use --fail so HTTP errors don't dump partial bodies; --silent avoids progress.
curl --fail --silent --show-error \
  --request POST \
  "${NINEROUTER_URL%/}/v1/search" \
  "${headers[@]}" \
  --data "$body"
echo
