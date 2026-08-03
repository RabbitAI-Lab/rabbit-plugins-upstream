#!/bin/bash
# ============================================================
# PMM 身份文件备份 — 备份 AI 体所有身份文件到瑶池容灾域
# 配合 pmm_recover.sh 使用：备份 → finalize → 昆仑令 → 恢复
#
# 用法: ./pmm_backup_files.sh [工作区] [API Key]
#
# 典型流程:
#   ./pmm_watch.sh push "结论" "内容"   （逐条推记忆）
#   ./pmm_backup_files.sh               （备份身份文件）
#   → 调用 yaochi/backup/finalize        （归档生成昆仑令）
#   → 复制昆仑令告诉人类
# ============================================================
set -euo pipefail

WS="${1:-/root/.lightclaw/workspace}"
API="${KLYC_API_ENDPOINT:-https://kunlunyaochi.com/api}/api.php?route=yaochi/backup"
KEY_FILE="${WS}/.klyc-pmm/key"

# 优先用参数2，其次读 key 文件
if [ -n "${2:-}" ]; then
    KEY="$2"
elif [ -f "$KEY_FILE" ]; then
    KEY=$(cat "$KEY_FILE")
else
    echo "未找到 API Key (${KEY_FILE})。"
    echo "用法: $0 [工作区] [API Key]"
    exit 1
fi

FILES=("IDENTITY.md" "SOUL.md" "AGENTS.md" "USER.md" "TOOLS.md")
COUNT=0
TOTAL=${#FILES[@]}

echo "===== PMM 身份文件备份 ====="
echo "工作区: ${WS}"
echo ""

for f in "${FILES[@]}"; do
    FP="${WS}/${f}"
    if [ ! -f "$FP" ]; then
        echo "  ⚠️ $f 不存在，跳过"
        continue
    fi

    # 读取文件并 JSON 转义
    CONTENT=$(jq -Rs '.' "$FP" 2>/dev/null || python3 -c "import sys,json; print(json.dumps(open('$FP').read()))")
    RESP=$(curl -sS --ssl-reqd -X POST "$API" \
        -H "Content-Type: application/json" \
        -H "X-Kunlun-Key: $KEY" \
        -d "{\"title\":\"$f\",\"content\":${CONTENT},\"file\":\"$f\"}" 2>/dev/null || echo '{"success":false}')

    if echo "$RESP" | jq -e '.success == true' >/dev/null 2>&1; then
        echo -e "  ✅ $f"
        COUNT=$((COUNT + 1))
    else
        msg=$(echo "$RESP" | jq -r '.message // .error // "?"' 2>/dev/null)
        echo "  ⚠️ $f: $msg"
    fi
done

echo ""
echo "已备份 ${COUNT}/${TOTAL} 个文件"
echo ""
echo "下一步：调用 finalize 生成昆仑令 → 交给人类保存"
echo "  curl -sS --ssl-reqd -X POST \${KLYC_API_ENDPOINT:-https://kunlunyaochi.com/api}/api.php?route=yaochi/backup/finalize \\"
echo "    -H 'Content-Type: application/json' -H 'X-Kunlun-Key: $KEY'"
