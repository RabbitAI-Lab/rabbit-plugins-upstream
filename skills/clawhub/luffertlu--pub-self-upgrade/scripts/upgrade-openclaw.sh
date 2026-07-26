#!/usr/bin/env bash
# ============================================================================
# OpenClaw 零停机升级脚本 v3
#
# 升级方式: npm install -g openclaw@latest
#
# 流程:
#   1. 查 release notes（备忘，不阻塞）
#   2. 旁路备份 openclaw → openclaw-fallback（安全锚点）
#   3. npm install -g openclaw@latest
#   4. 更新 systemd 单元版本号
#   5. 重启 + 健康检查
#   6. 失败回滚 / 成功清理
#
# 所有输出写入日志，控制台不输出。
# 如需用户操作（如输密码），通过 webchat 通知主公。
# ============================================================================

# ─── 日志 ───────────────────────────────────────────────────────────────
LOG_FILE="$HOME/.openclaw/workspace/logs/upgrade-$(date +%Y%m%d-%H%M%S).log"
mkdir -p "$(dirname "$LOG_FILE")"
exec >> "$LOG_FILE" 2>&1

set -euo pipefail

# ─── 工具 ───────────────────────────────────────────────────────────────
log()    { echo "[$(date +%H:%M:%S)] $*"; }
ok()     { echo "[$(date +%H:%M:%S)] ✅ $*"; }
warn()   { echo "[$(date +%H:%M:%S)] ⚠️  $*"; }
fail()   { echo "[$(date +%H:%M:%S)] ❌ $*"; }
step()   { echo ""; echo "===== $* ====="; }

# ─── 常量 ───────────────────────────────────────────────────────────────
BASE="$HOME/.npm-global/lib/node_modules"
CURDIR="$BASE/openclaw"
BAKDIR="$BASE/openclaw-fallback"
UNITFILE="$HOME/.config/systemd/user/openclaw-gateway.service"
SERVICE="openclaw-gateway"

# ────────────────────────────────────────────────────────────────────────
step "阶段 0: 前置检查"
# ────────────────────────────────────────────────────────────────────────

for cmd in node npm systemctl curl; do
    if ! command -v "$cmd" &>/dev/null; then
        fail "缺少命令: $cmd"
        log "升级中止：命令 $cmd 不存在"
        exit 1
    fi
done
ok "环境检查通过 (node $(node -v), npm $(npm -v))"

AVAIL=$(df -B1 "$HOME" | awk 'NR==2 {print $4}')
if [ "$AVAIL" -lt 2147483648 ]; then
    fail "磁盘空间不足: $(numfmt --to=iec $AVAIL) 可用，需要至少 2G"
    log "升级中止：磁盘空间不足"
    exit 1
fi
ok "磁盘空间: $(numfmt --to=iec $AVAIL)"

if [ "$(systemctl --user is-active "$SERVICE")" != "active" ]; then
    fail "openclaw-gateway 服务未运行"
    log "升级中止：服务未运行"
    exit 1
fi
CURRENT_VERSION_VAR=$(grep -oP 'OPENCLAW_SERVICE_VERSION=\K[^"]+' "$UNITFILE" 2>/dev/null || echo "unknown")
INSTALLED_VERSION=$(node -e "console.log(require('$CURDIR/package.json').version)" 2>/dev/null || echo "unknown")
ok "当前版本: $CURRENT_VERSION_VAR (安装: $INSTALLED_VERSION)"

# ─── 查 release notes（备忘，不阻塞） ──────────────────────────────
step "阶段 0b: 查 release notes"

log "查询 GitHub API 获取 release notes..."
RN=$(curl -sL --connect-timeout 10 \
    "https://api.github.com/repos/openclaw/openclaw/releases/tags/v2026.6.5" 2>/dev/null \
    | python3 -c "
import sys, json
try:
    d = json.load(sys.stdin)
    body = d.get('body', '')
    name = d.get('name', '')
    html = d.get('html_url', '')
    lines = body.strip().split('\n')
    safe = [l for l in lines[:50] if l.strip()]
    print(f'--- {name} ---')
    for l in safe: print(l)
    if len(lines) > 50: print('...')
    print(f'--- Full: {html} ---')
except Exception as e:
    print(f'ParseError: {e}')
" 2>/dev/null || echo "API 请求失败")

log "=== Release Notes ==="
echo "$RN" | while IFS= read -r l; do log "$l"; done
log "=== End Release Notes ==="

# 如果 release notes 里有 breaking/密码相关的关键词，记一笔
BREAKING_HINT=$(echo "$RN" | grep -ci "breaking\|BREAKING\|重新.*密码\|密码.*变更\|credential\|re-auth\|reauthenticate\|password.*change\|migration" || true)
if [ "$BREAKING_HINT" -gt 0 ]; then
    log "⚠️  Release notes 中含疑似 breaking change 关键词，升级后留意"
fi

# ────────────────────────────────────────────────────────────────────────
step "阶段 1: 旁路备份"
# ────────────────────────────────────────────────────────────────────────

rm -rf "$BAKDIR"
log "备份当前代码到 openclaw-fallback..."
cp -r "$CURDIR" "$BAKDIR"
ok "备份完成 ($(du -sh "$BAKDIR" | awk '{print $1}'))"

# ────────────────────────────────────────────────────────────────────────
step "阶段 2: npm install -g openclaw@latest"
# ────────────────────────────────────────────────────────────────────────

log "安装 openclaw@latest..."
if ! npm install -g openclaw@latest 2>&1; then
    fail "npm install 失败"
    log "尝试官方 registry..."
    if ! npm install -g openclaw@latest --registry https://registry.npmjs.org 2>&1; then
        fail "npm install 官方 registry 也失败"
        log "回滚..."
        rm -rf "$CURDIR"
        cp -r "$BAKDIR" "$CURDIR"
        ok "已恢复旧代码"
        rm -rf "$BAKDIR"
        log "升级中止：npm install 失败"
        exit 1
    fi
fi

NEW_VERSION=$(node -e "console.log(require('$CURDIR/package.json').version)" 2>/dev/null || echo "unknown")
if [ "$NEW_VERSION" = "$INSTALLED_VERSION" ] || [ "$NEW_VERSION" = "unknown" ]; then
    fail "版本未更新 ($INSTALLED_VERSION → $NEW_VERSION)"
    log "回滚..."
    rm -rf "$CURDIR"
    cp -r "$BAKDIR" "$CURDIR"
    ok "已恢复旧代码"
    rm -rf "$BAKDIR"
    log "升级中止：版本未变更"
    exit 1
fi

if [ ! -f "$CURDIR/dist/index.js" ] && [ ! -f "$CURDIR/openclaw.mjs" ]; then
    fail "入口文件缺失"
    log "回滚..."
    rm -rf "$CURDIR"
    cp -r "$BAKDIR" "$CURDIR"
    ok "已恢复旧代码"
    rm -rf "$BAKDIR"
    log "升级中止：入口文件缺失"
    exit 1
fi
ok "安装完成: $INSTALLED_VERSION → $NEW_VERSION"

# ────────────────────────────────────────────────────────────────────────
step "阶段 3: 更新 systemd 版本号"
# ────────────────────────────────────────────────────────────────────────

if grep -q "OPENCLAW_SERVICE_VERSION=" "$UNITFILE"; then
    sed -i "s/OPENCLAW_SERVICE_VERSION=[^\"]*/OPENCLAW_SERVICE_VERSION=$NEW_VERSION/" "$UNITFILE"
    systemctl --user daemon-reload
    ok "systemd 版本号已更新: $NEW_VERSION"
else
    warn "单元文件中未找到 OPENCLAW_SERVICE_VERSION，跳过"
fi

# ────────────────────────────────────────────────────────────────────────
step "阶段 4: 重启 + 健康检查"
# ────────────────────────────────────────────────────────────────────────

log "重启 $SERVICE (闪断)..."
systemctl --user restart "$SERVICE"

WAITED=0
while [ $WAITED -lt 60 ]; do
    sleep 2
    WAITED=$((WAITED + 2))
    STATUS=$(systemctl --user is-active "$SERVICE" 2>/dev/null || echo "inactive")
    if [ "$STATUS" = "active" ]; then
        break
    fi
done

FINAL_STATUS=$(systemctl --user is-active "$SERVICE" 2>/dev/null || echo "inactive")
SERVICE_VERSION=$(systemctl --user show "$SERVICE" -p Environment 2>/dev/null \
    | grep -oP 'OPENCLAW_SERVICE_VERSION=\K[^"]+' || echo "unknown")

if [ "$FINAL_STATUS" = "active" ]; then
    ok "升级成功: $INSTALLED_VERSION → $SERVICE_VERSION (闪断 ${WAITED}s)"
    log "自动清理 fallback 备份..."
    rm -rf "$BAKDIR"
    ok "已清理"
else
    # ── 回滚 ──
    warn "新版本启动异常 (status=$FINAL_STATUS, waited ${WAITED}s)"
    journalctl --user -u "$SERVICE" -n 20 --no-pager || true

    log "从 openclaw-fallback 恢复旧代码..."
    rm -rf "$CURDIR"
    cp -r "$BAKDIR" "$CURDIR"

    if grep -q "OPENCLAW_SERVICE_VERSION=" "$UNITFILE"; then
        sed -i "s/OPENCLAW_SERVICE_VERSION=[^\"]*/OPENCLAW_SERVICE_VERSION=$CURRENT_VERSION_VAR/" "$UNITFILE"
        systemctl --user daemon-reload
    fi

    log "重启旧版本..."
    systemctl --user restart "$SERVICE"
    sleep 10

    ROLLBACK_STATUS=$(systemctl --user is-active "$SERVICE" 2>/dev/null || echo "inactive")
    if [ "$ROLLBACK_STATUS" = "active" ]; then
        ok "已回滚到旧版本 ($CURRENT_VERSION_VAR)，服务恢复正常"
    else
        fail "回滚后服务仍无法启动！"
        fail "请手动检查: systemctl --user status $SERVICE"
    fi

    rm -rf "$BAKDIR"
    log "升级中止：健康检查失败，已回滚"
    exit 1
fi

ok "升级流程完成，日志: $LOG_FILE"
