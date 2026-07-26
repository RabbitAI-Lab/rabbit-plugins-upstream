#!/bin/bash
# klyc-pmm update.sh — 一键更新到最新版 pmm_watch.sh
# 白板 AI 体只需跑 bash update.sh，自动替换本地 pmm_watch.sh

set -e

PMM_URL="https://ai.syln.cn/skills/klyc-pmm/pmm_watch.sh"

echo "🔄 klyc-pmm 一键更新..."
echo "  源: ${PMM_URL}"

# 找本地 pmm_watch.sh
SCRIPT_PATH=""
for path in ./pmm_watch.sh \
            "$(command -v pmm_watch.sh 2>/dev/null)" \
            "$HOME/bin/pmm_watch.sh" \
            "$HOME/.openclaw/workspace/skills/pmm_watch.sh" \
            "$HOME/.lightclaw/workspace/skills/skill-yaochi-pmm/pmm_watch.sh"; do
    if [ -f "$path" ]; then SCRIPT_PATH="$path"; break; fi
done

if [ -z "$SCRIPT_PATH" ]; then
    echo "❌ 未找到 pmm_watch.sh，请先安装 klyc-pmm"
    echo "   skillhub install klyc-pmm"
    exit 1
fi

echo "  本地: ${SCRIPT_PATH}"

# 对比版本
LOCAL_VER=$(grep 'readonly VERSION' "$SCRIPT_PATH" 2>/dev/null | grep -oP '"([^"]+)"' | tr -d '"')
echo "  当前版本: ${LOCAL_VER:-未知}"

# 下载最新版
TMP=$(mktemp)
if ! curl -fsSL "$PMM_URL" -o "$TMP"; then
    echo "❌ 下载失败，请检查网络"
    rm -f "$TMP"
    exit 1
fi

REMOTE_VER=$(grep 'readonly VERSION' "$TMP" 2>/dev/null | grep -oP '"([^"]+)"' | tr -d '"')
echo "  最新版本: ${REMOTE_VER:-未知}"

if [ "$LOCAL_VER" = "$REMOTE_VER" ]; then
    echo "✅ 已是最新版本 v${LOCAL_VER}，无需更新"
    rm -f "$TMP"
    exit 0
fi

# 备份 + 替换
cp "$SCRIPT_PATH" "${SCRIPT_PATH}.bak.$(date +%Y%m%d-%H%M%S)"
cat "$TMP" > "$SCRIPT_PATH"
chmod +x "$SCRIPT_PATH"
rm -f "$TMP"

echo "✅ 已更新到 v${REMOTE_VER}"
echo "   备份: ${SCRIPT_PATH}.bak.*"
echo ""
echo "💡 如果 watch 守护正在运行，建议重启:"
echo "   pkill -f 'pmm_watch.sh watch' && pmm_watch.sh watch MEMORY.md IDENTITY.md &"
