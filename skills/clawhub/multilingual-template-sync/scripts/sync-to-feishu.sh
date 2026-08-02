#!/usr/bin/env bash
# sync-to-feishu.sh — Sync a markdown template file to Feishu Wiki
# Usage: ./sync-to-feishu.sh <file-path> <wiki-space-id> <parent-node-token>
#
# Requires: curl, jq
# Env vars:
#   FEISHU_APP_ID      — Feishu app ID
#   FEISHU_APP_SECRET  — Feishu app secret
#
# The script converts markdown to Feishu doc blocks via the open API
# and creates/updates a wiki node under the given parent.

set -euo pipefail

FILE="${1:?Usage: $0 <file-path> <wiki-space-id> <parent-node-token>}"
SPACE_ID="${2:?Missing wiki space ID}"
PARENT_TOKEN="${3:?Missing parent node token}"

APP_ID="${FEISHU_APP_ID:?Set FEISHU_APP_ID}"
APP_SECRET="${FEISHU_APP_SECRET:?Set FEISHU_APP_SECRET}"

# 1. Get tenant access token
TOKEN=$(curl -s -X POST 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal' \
  -H 'Content-Type: application/json' \
  -d "{\"app_id\":\"$APP_ID\",\"app_secret\":\"$APP_SECRET\"}" | jq -r '.tenant_access_token')

if [ "$TOKEN" = "null" ] || [ -z "$TOKEN" ]; then
  echo "ERROR: Failed to get Feishu access token" >&2; exit 1
fi

# 2. Read file content
TITLE=$(grep -m1 '^# ' "$FILE" | sed 's/^# //')
CONTENT=$(cat "$FILE")

# 3. Create wiki node (doc type)
RESP=$(curl -s -X POST "https://open.feishu.cn/open-apis/wiki/v2/spaces/${SPACE_ID}/nodes" \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d "{
    \"obj_type\": \"docx\",
    \"parent_node_token\": \"${PARENT_TOKEN}\",
    \"node_type\": \"origin\",
    \"title\": \"${TITLE}\"
  }")

NODE_TOKEN=$(echo "$RESP" | jq -r '.data.node.node_token // empty')
OBJ_TOKEN=$(echo "$RESP" | jq -r '.data.node.obj_token // empty')

if [ -z "$NODE_TOKEN" ]; then
  echo "ERROR: Failed to create wiki node: $RESP" >&2; exit 1
fi

echo "Created wiki node: $NODE_TOKEN (obj: $OBJ_TOKEN)"

# 4. Insert content as raw text blocks (simplified — markdown→blocks conversion
#    can be enhanced with a proper parser in production)
#    For now, create a single text block with the markdown content.
#    Production use should parse markdown into Feishu block structures.
ESCAPED_CONTENT=$(echo "$CONTENT" | jq -Rs .)

curl -s -X POST "https://open.feishu.cn/open-apis/docx/v1/documents/${OBJ_TOKEN}/blocks/${OBJ_TOKEN}/children" \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  -d "{
    \"children\": [
      {
        \"block_type\": 2,
        \"text\": {
          \"elements\": [{\"text_run\": {\"content\": ${ESCAPED_CONTENT}}}],
          \"style\": {}
        }
      }
    ]
  }"

echo "Synced '$FILE' to Feishu Wiki node: $NODE_TOKEN"
