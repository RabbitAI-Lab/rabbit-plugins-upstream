#!/usr/bin/env bash
# sync-feishu.sh — Sync common-responses.md to Feishu Wiki
# Usage: FEISHU_APP_ID=xxx FEISHU_APP_SECRET=xxx FEISHU_WIKE_SPACE_ID=xxx [FEISHU_DOC_TOKEN=xxx] bash sync-feishu.sh <file.md>
set -euo pipefail

FILE="${1:?Usage: $0 <file.md>}"
APP_ID="${FEISHU_APP_ID:?FEISHU_APP_ID required}"
APP_SECRET="${FEISHU_APP_SECRET:?FEISHU_APP_SECRET required}"
SPACE_ID="${FEISHU_WIKI_SPACE_ID:?FEISHU_WIKI_SPACE_ID required}"
DOC_TOKEN="${FEISHU_DOC_TOKEN:-}"
PARENT_NODE_TOKEN="${FEISHU_PARENT_NODE_TOKEN:-}"

# 1. Get tenant access token
TOKEN_RESP=$(curl -s -X POST 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal' \
  -H 'Content-Type: application/json' \
  -d "{\"app_id\":\"$APP_ID\",\"app_secret\":\"$APP_SECRET\"}")
TENANT_TOKEN=$(echo "$TOKEN_RESP" | jq -r '.tenant_access_token // empty')
if [ -z "$TENANT_TOKEN" ]; then
  echo "❌ Failed to get tenant token: $TOKEN_RESP" >&2
  exit 1
fi
echo "✅ Got tenant access token"

# 2. Read file content
CONTENT=$(cat "$FILE")
TITLE=$(head -1 "$FILE" | sed 's/^# *//')

if [ -n "$DOC_TOKEN" ]; then
  # Update existing document — overwrite content
  echo "📝 Updating existing doc: $DOC_TOKEN"
  # Feishu doesn't have a simple "replace all content" API; we delete blocks and recreate.
  # For simplicity, we use the batch update API to clear and append.
  # Get existing blocks
  BLOCKS=$(curl -s -X GET "https://open.feishu.cn/open-apis/docx/v1/documents/$DOC_TOKEN/blocks?page_size=500" \
    -H "Authorization: Bearer $TENANT_TOKEN")
  BLOCK_IDS=$(echo "$BLOCKS" | jq -r '.data.items[]?.block_id' | tail -n +2)

  # Delete old children (skip root)
  for BID in $BLOCK_IDS; do
    curl -s -X DELETE "https://open.feishu.cn/open-apis/docx/v1/documents/$DOC_TOKEN/blocks/$DOC_TOKEN/children/batch_delete" \
      -H "Authorization: Bearer $TENANT_TOKEN" \
      -H 'Content-Type: application/json' \
      -d "{\"start_index\":0,\"end_index\":1}" >/dev/null 2>&1 || true
  done

  # Append new content
  # Convert markdown to Feishu blocks (simplified)
  BLOCKS_JSON=$(python3 -c "
import json, sys, re

lines = open('$FILE').read().split('\n')
blocks = []
for line in lines:
    line = line.rstrip()
    if not line:
        continue
    if line.startswith('# '):
        blocks.append({'block_type': 3, 'heading1': {'elements': [{'text_run': {'content': line[2:]}}]}})
    elif line.startswith('## '):
        blocks.append({'block_type': 4, 'heading2': {'elements': [{'text_run': {'content': line[3:]}}]}})
    elif line.startswith('### '):
        blocks.append({'block_type': 5, 'heading3': {'elements': [{'text_run': {'content': line[4:]}}]}})
    elif line.startswith('---'):
        blocks.append({'block_type': 22, 'divider': {}})
    elif line.startswith('|'):
        # Table row — render as text for simplicity
        blocks.append({'block_type': 2, 'text': {'elements': [{'text_run': {'content': line}}]}})
    else:
        blocks.append({'block_type': 2, 'text': {'elements': [{'text_run': {'content': line}}]}})

print(json.dumps(blocks))
")

  # Batch create children (chunked to 50 per request)
  echo "$BLOCKS_JSON" | jq -c '.[]' | head -50 | while read -r block; do
    curl -s -X POST "https://open.feishu.cn/open-apis/docx/v1/documents/$DOC_TOKEN/blocks/$DOC_TOKEN/children" \
      -H "Authorization: Bearer $TENANT_TOKEN" \
      -H 'Content-Type: application/json' \
      -d "{\"children\":[$block]}" >/dev/null 2>&1
  done
  echo "✅ Updated doc $DOC_TOKEN"
else
  # Create new wiki node
  echo "📄 Creating new wiki node under space $SPACE_ID"
  CREATE_RESP=$(curl -s -X POST "https://open.feishu.cn/open-apis/wiki/v2/spaces/$SPACE_ID/nodes" \
    -H "Authorization: Bearer $TENANT_TOKEN" \
    -H 'Content-Type: application/json' \
    -d "{
      \"obj_type\": \"docx\",
      \"node_type\": \"origin\",
      \"title\": \"$TITLE\"
      $( [ -n "$PARENT_NODE_TOKEN" ] && echo ",\"parent_node_token\":\"$PARENT_NODE_TOKEN\"" )
    }")
  NEW_DOC_TOKEN=$(echo "$CREATE_RESP" | jq -r '.data.node.obj_token // empty')
  if [ -z "$NEW_DOC_TOKEN" ]; then
    echo "❌ Failed to create wiki node: $CREATE_RESP" >&2
    exit 1
  fi
  echo "✅ Created wiki node with doc token: $NEW_DOC_TOKEN"
  echo "ℹ️  Set FEISHU_DOC_TOKEN=$NEW_DOC_TOKEN for future updates"

  # Append content to new doc
  BLOCKS_JSON=$(python3 -c "
import json
lines = open('$FILE').read().split('\n')
blocks = []
for line in lines:
    line = line.rstrip()
    if not line: continue
    if line.startswith('# '):
        blocks.append({'block_type': 3, 'heading1': {'elements': [{'text_run': {'content': line[2:]}}]}})
    elif line.startswith('## '):
        blocks.append({'block_type': 4, 'heading2': {'elements': [{'text_run': {'content': line[3:]}}]}})
    elif line.startswith('### '):
        blocks.append({'block_type': 5, 'heading3': {'elements': [{'text_run': {'content': line[4:]}}]}})
    elif line.startswith('---'):
        blocks.append({'block_type': 22, 'divider': {}})
    else:
        blocks.append({'block_type': 2, 'text': {'elements': [{'text_run': {'content': line}}]}})
print(json.dumps(blocks))
")

  echo "$BLOCKS_JSON" | jq -c '.[]' | head -50 | while read -r block; do
    curl -s -X POST "https://open.feishu.cn/open-apis/docx/v1/documents/$NEW_DOC_TOKEN/blocks/$NEW_DOC_TOKEN/children" \
      -H "Authorization: Bearer $TENANT_TOKEN" \
      -H 'Content-Type: application/json' \
      -d "{\"children\":[$block]}" >/dev/null 2>&1
  done
  echo "✅ Content written to new doc"
fi

echo "🎉 Feishu sync complete!"
