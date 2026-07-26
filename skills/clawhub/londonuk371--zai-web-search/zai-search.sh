#!/bin/bash
# zAI Web Search — calls Z.AI Web Search API
# Usage: zai-search.sh "query" [count]

QUERY="$1"
COUNT="${2:-5}"

if [ -z "$QUERY" ]; then
  echo "Usage: zai-search.sh \"query\" [count]"
  exit 1
fi

API_KEY=""
if [ -f "$HOME/.openclaw/.zai-key" ]; then
  API_KEY=$(cat "$HOME/.openclaw/.zai-key" | tr -d '[:space:]')
elif [ -n "$ZAI_API_KEY" ]; then
  API_KEY="$ZAI_API_KEY"
else
  echo "Error: No ZAI_API_KEY found"
  exit 1
fi

BASE_URL="https://api.z.ai/api/coding/paas/v4"

curl -s -X POST "${BASE_URL}/web_search" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(jq -n --arg q "$QUERY" --argjson c "$COUNT" '{
    search_engine: "search-prime",
    search_query: $q,
    count: $c,
    search_recency_filter: "noLimit"
  }')" | jq -r '
    if .search_result then
      .search_result[] | "## \( .title // "Untitled" )\nURL: \( .link // "N/A" )\n\( .content // "No summary" )\n"
    else
      .error // "No results"
    end
  '
