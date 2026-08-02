#!/bin/bash
# klyc-pmm update.sh — 一键更新全部 pmm_watch.sh 副本
# 从在线源下载 → SHA256 校验 → 发现全部本地副本 → 逐个覆盖 → 更新在线 sha256
set -euo pipefail

PMM_URL="https://kunlunyaochi.com/skills/klyc-pmm/pmm_watch.sh"
PMM_SHA256_URL="https://kunlunyaochi.com/skills/klyc-pmm/pmm_watch.sh.sha256"

RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[0;33m'; NC='\033[0m'
ok() { echo -e "  ${GREEN}✅${NC} $*"; }
warn() { echo -e "  ${YELLOW}⚠️${NC} $*"; }
err() { echo -e "  ${RED}❌${NC} $*"; }

echo "🔄 klyc-pmm 一键更新（全部副本）..."
echo "  源: ${PMM_URL}"
echo ""

# ── 1. 下载 + 校验 ──
TMP=$(mktemp)
if ! curl -fsSL "$PMM_URL" -o "$TMP"; then
    echo "❌ 下载失败"
    rm -f "$TMP"
    exit 1
fi

EXPECTED_SHA256=$(curl -fsSL "$PMM_SHA256_URL" 2>/dev/null | awk '{print $1}')
if [ -n "$EXPECTED_SHA256" ]; then
    ACTUAL_SHA256=$(sha256sum "$TMP" 2>/dev/null | awk '{print $1}')
    if [ "$EXPECTED_SHA256" != "$ACTUAL_SHA256" ]; then
        err "SHA256 校验失败！期望 ${EXPECTED_SHA256}，实际 ${ACTUAL_SHA256}"
        rm -f "$TMP"
        exit 1
    fi
    ok "SHA256 校验通过"
else
    warn "无法获取校验和，跳过完整性验证"
fi

REMOTE_VER=$(grep 'readonly VERSION' "$TMP" 2>/dev/null | grep -oP '"([^"]+)"' | tr -d '"')
echo "  在线版本: ${REMOTE_VER:-未知}"
echo ""

# ── 2. 发现全部本地副本 ──
echo "🔍 发现副本..."

declare -a PATHS
# 搜索策略：遍历已知位置 + 全局 find（去重）
KNOWN=(
    "/root/.openclaw/workspace/skills/klyc-pmm/scripts/pmm_watch.sh"
    "/root/.openclaw/workspace/skills/klyc-pmm/scripts/pmm_watch.sh"
    "/root/bin/pmm_watch.sh"
    "/www/wwwroot/kunlunyaochi/skills/pmm_watch.sh"
    "/www/wwwroot/kunlunyaochi/skills/klyc-pmm/scripts/pmm_watch.sh"
    "/www/wwwroot/kunlunyaochi/skills/klyc-pmm/pmm_watch.sh"
)
# 也搜其他位置（兼容非标准安装）
while IFS= read -r -d '' f; do
    KNOWN+=("$f")
done < <(find /root -name "pmm_watch.sh" -type f -not -path "*/backups/*" -print0 2>/dev/null || true)
while IFS= read -r -d '' f; do
    KNOWN+=("$f")
done < <(find /www/wwwroot -name "pmm_watch.sh" -type f -not -path "*/backups/*" -print0 2>/dev/null || true)

# 去重
declare -A seen
for f in "${KNOWN[@]}"; do
    rp=$(realpath "$f" 2>/dev/null || echo "$f")
    if [ -f "$f" ] && [ -z "${seen[$rp]:-}" ]; then
        seen["$rp"]=1
        PATHS+=("$f")
    fi
done

UPDATED=0; SKIPPED=0; FAILED=0

# ── 3. 逐个更新 ──
for f in "${PATHS[@]}"; do
    local_ver=$(grep 'readonly VERSION' "$f" 2>/dev/null | grep -oP '"([^"]+)"' | tr -d '"')
    local_md5=$(sha256sum "$f" 2>/dev/null | cut -d' ' -f1)

    # 已经是同一文件，跳过
    if [ "$local_md5" = "$EXPECTED_SHA256" ]; then
        echo "  ⏭️  $f → v${local_ver}（已最新）"
        SKIPPED=$((SKIPPED + 1))
        continue
    fi

    # 检查 chattr +i
    attr=$(lsattr "$f" 2>/dev/null | awk '{print $1}' | tr -d '-')
    if echo "$attr" | grep -q 'i'; then
        if ! chattr -i "$f" 2>/dev/null; then
            warn "$f → v${local_ver} → ❌ chattr -i 失败（需 root）"
            FAILED=$((FAILED + 1))
            continue
        fi
        was_immutable=1
    else
        was_immutable=0
    fi

    # 备份 + 覆盖
    cp "$f" "${f}.bak.$(date +%Y%m%d-%H%M%S)" 2>/dev/null || true
    if cat "$TMP" > "$f" 2>/dev/null; then
        chmod +x "$f"
        [ "$was_immutable" = "1" ] && chattr +i "$f" 2>/dev/null
        ok "$f → v${REMOTE_VER} （原 v${local_ver}）"
        UPDATED=$((UPDATED + 1))
    else
        err "$f → ❌ 写入失败"
        FAILED=$((FAILED + 1))
    fi
done

rm -f "$TMP"

# ── 4. 更新在线 sha256（如果当前机器是服务器）──
ONLINE_PUB="/www/wwwroot/kunlunyaochi/skills/klyc-pmm"
if [ -d "$ONLINE_PUB" ]; then
    echo ""
    echo "🌐 刷新在线源 ..."
    PUB_SH="${ONLINE_PUB}/pmm_watch.sh"
    if [ -f "$PUB_SH" ]; then
        sha256sum "$PUB_SH" | awk '{print $1}' > "${ONLINE_PUB}/pmm_watch.sh.sha256"
        ok "在线 sha256 已刷新"
    fi
fi

# ── 5. 总结 ──
echo ""
echo "════════════════════════════════════════"
echo "  ✅ 更新 $UPDATED  |  ⏭️ 跳过 $SKIPPED  |  ❌ 失败 $FAILED"
echo "  版本: v${REMOTE_VER}"
echo "════════════════════════════════════════"

# 如果有 watch 守护，提醒重启
if pgrep -f 'pmm_watch.sh watch' >/dev/null 2>&1; then
    echo ""
    echo "💡 检测到 watch 守护在运行，建议重启:"
    echo "   pkill -f 'pmm_watch.sh watch' && pmm_watch.sh watch MEMORY.md IDENTITY.md &"
fi

[ "$FAILED" -eq 0 ] && exit 0 || exit 1
