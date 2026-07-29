#!/bin/bash
# KLYC-PMM 昆仑令记忆恢复 v4
# 支持 URL: https://kunlunyaochi.com/klyc-pmm/TOKEN
# 支持 Code: KLYC-PMM-TOKEN
set -euo pipefail
CODE="${1:-}"; CODE=$(echo "$CODE" | tr -d '[:space:]')
[ -z "$CODE" ] && { echo "用法: $0 <昆仑令URL或code> [工作区]"; exit 1; }

# URL → extract token
if echo "$CODE" | grep -qi 'klyc-pmm/'; then
    TOK=$(echo "$CODE" | grep -oP 'klyc-pmm/\K[0-9a-f]+' | head -1)
    [ -n "$TOK" ] && CODE="KLYC-PMM-${TOK}"
fi

API="${KLYC_API_ENDPOINT:-https://kunlunyaochi.com/api}/api.php?route=yaochi/recover"
WORKSPACE="${2:-/root/.lightclaw/workspace}"
TMPFILE=$(mktemp)

echo "===== KLYC-PMM 昆仑令恢复 v4 ====="
echo "昆仑令: ${CODE:0:40}..."
echo "工作区: ${WORKSPACE}"

HTTP_CODE=$(curl -sS -o "$TMPFILE" -w "%{http_code}" -X POST "$API" \
    -H "Content-Type: application/json" -d "{\"token\":\"$CODE\"}" 2>/dev/null || echo "000")

if [ "$HTTP_CODE" != "200" ]; then
    if [ "$HTTP_CODE" = "402" ]; then
        jq -r '"🍑 蟠桃不足！需要\(.required)颗，当前余额\(.balance)颗\n👉 充值: \(.recharge_url)"' "$TMPFILE" 2>/dev/null
    else
        echo "恢复失败 (HTTP $HTTP_CODE)"
        jq -r '.error // "未知错误"' "$TMPFILE" 2>/dev/null || cat "$TMPFILE"
    fi; rm -f "$TMPFILE"; exit 1
fi

CNT=$(jq -r '.total // 0' "$TMPFILE" 2>/dev/null)
NAME=$(jq -r '.display_name // .agent // "AI体"' "$TMPFILE" 2>/dev/null)
echo "✅ 恢复成功！${NAME} 找回 ${CNT} 条记忆"
echo "恢复数据: ${WORKSPACE}/recovery_result.json"
jq '.' "$TMPFILE" > "${WORKSPACE}/recovery_result.json" 2>/dev/null || true
rm -f "$TMPFILE"
