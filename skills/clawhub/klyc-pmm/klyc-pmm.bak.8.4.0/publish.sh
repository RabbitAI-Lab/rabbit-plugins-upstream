#!/bin/bash
# klyc-pmm 一键发布脚本 v3.7
# 用法: /root/bin/publish_klyc-pmm.sh [changelog描述]

set -euo pipefail
shopt -s nullglob 2>/dev/null || true

export PATH="$HOME/.local/bin:$PATH"

ROOT=/root/.openclaw/workspace/skills
PUB=/www/wwwroot/kunlunyaochi/skills/klyc-pmm
SITE=/www/wwwroot/kunlunyaochi
FAIL=0; ERRS=""

e() { echo "  ❌ $*" >&2; FAIL=1; ERRS="${ERRS}$*"$'\n'; }
o() { echo "  ✅ $*"; }
w() { echo "  ⚠️ $*" >&2; }

# ── 版本号 ──
V=$(grep '^readonly VERSION=' "$ROOT/klyc-pmm/scripts/pmm_watch.sh" | grep -oP '"[^"]+"' | tr -d '"')
[ -z "$V" ] && { echo "❌ 读不到版本号"; exit 1; }
MSG="${1:-v${V} 版本更新}"

echo "🏔️ 一键发布 klyc-pmm v${V}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# ═══════════════════════════════════════
# STEP 1: 前置检查
# ═══════════════════════════════════════
echo "🔍 检查..."

# 1a. 核心文件在不在
for f in "$ROOT/klyc-pmm/scripts/pmm_watch.sh" "$ROOT/klyc-pmm/SKILL.md" "$ROOT/klyc-pmm/skill.json" "$ROOT/klyc-pmm/scripts/pmm_distill.sh" "$ROOT/klyc-pmm/scripts/pmm_watch.sh"; do
    [ -f "$f" ] && o "$(basename "$f")" || e "缺失: $f"
done
[ "$FAIL" -ne 0 ] && { echo "❌ 核心文件缺失"; exit 1; }

# 1b. 全量版本号对齐
for f in "$ROOT/SKILL.md" "$ROOT/skill.json" \
         "$ROOT/klyc-pmm/scripts/pmm_watch.sh" "$ROOT/klyc-pmm/scripts/pmm_watch.sh" "$ROOT/klyc-pmm/scripts/pmm_distill.sh"; do
    grep -qE "v?${V}" "$f" && o "$(basename "$f")" || e "$(basename "$f"): 缺 v${V}"
done
[ "$FAIL" -ne 0 ] && { echo "❌ 版本未对齐"; exit 1; }

# 1c. 安全
grep -qP '(sk-[a-zA-Z0-9]{20,}|150\.158\.21\.6|10\.0\.0\.3)' "$ROOT/klyc-pmm/scripts/pmm_watch.sh" && { e "含硬编码密钥/IP"; exit 1; } || o "安全合规"
bash -n "$ROOT/klyc-pmm/scripts/pmm_watch.sh" && o "bash语法" || { e "语法错误"; exit 1; }

# 1d. 同步根 skill.json description
python3 -c "
import json
r=json.load(open('$ROOT/skill.json'))
s=json.load(open('$ROOT/klyc-pmm/skill.json'))
if r.get('description')!=s.get('description') or r.get('version')!=s.get('version'):
    r['version']=s['version']; r['description']=s['description']
    json.dump(r,open('$ROOT/skill.json','w'),ensure_ascii=False,indent=2)
    print('synced')
" 2>/dev/null

echo ""
echo "✅ 检查通过"
echo ""

# ═══════════════════════════════════════
# STEP 2: 网站发布（rsync — 零遗漏）
# ═══════════════════════════════════════

echo "📄 网站同步..."
mkdir -p "$PUB"
rsync -av --delete "$ROOT/klyc-pmm/" "$PUB/" | sed 's/^/  /'
# 在线更新源：update.sh 从 /skills/klyc-pmm/pmm_watch.sh 拉取
cp "$ROOT/klyc-pmm/scripts/pmm_watch.sh" "$PUB/pmm_watch.sh"
sha256sum "$PUB/pmm_watch.sh" | awk '{print $1}' > "$PUB/pmm_watch.sh.sha256"
chmod +x "$PUB/"*.sh "$PUB/scripts/"*.sh 2>/dev/null || true
o "网站目录: $(find "$PUB" -type f | wc -l) 文件"

# 根级入口
echo "📄 根级入口..."
cp "$ROOT/skill.json"   "$SITE/skills/skill.json"
cp "$ROOT/SKILL.md"     "$SITE/skills/SKILL.md"
cp "$ROOT/CHANGELOG.md" "$SITE/skills/CHANGELOG.md"
cp "$ROOT/SKILL.md"     "$SITE/public/klyc-pmm.skill"
o "根级文件就位"

# ZIP
echo "📦 ZIP..."
cd "$SITE/skills"
rm -f klyc-pmm.zip
zip -qr klyc-pmm.zip klyc-pmm/ -x "*.bak*" "*.swp" "*~"
ZIP_N=$(unzip -l klyc-pmm.zip 2>/dev/null | grep -c '\.')
ZIP_S=$(stat -c%s klyc-pmm.zip)
o "klyc-pmm.zip: ${ZIP_S}B ${ZIP_N}文件"
o "SHA256: $(sha256sum klyc-pmm.zip | cut -d' ' -f1)"
unzip -p klyc-pmm.zip klyc-pmm/SKILL.md 2>/dev/null | grep -q "version: ${V}" && o "ZIP版本验证" || e "ZIP版本不对"

# ═══════════════════════════════════════
# STEP 3: 平台发布（失败不阻断）
# ═══════════════════════════════════════
echo "📡 ClawHub..."
cd "$ROOT/klyc-pmm"
clawhub skill publish . --slug klyc-pmm --version "$V" --changelog "$MSG" 2>&1 | tail -1 && o "ClawHub" || w "ClawHub 失败"

echo "📡 SkillHub.cn..."
skillhub publish "$ROOT/klyc-pmm" --changelog "$MSG" 2>&1 | tail -1 && o "SkillHub.cn" || w "SkillHub.cn 失败"

# agent-card
echo "📄 agent-card..."
python3 -c "
import json
with open('$SITE/public/.well-known/agent-card.json') as f: d=json.load(f)
for s in d.get('skills',[]):
    if 'klyc' in s.get('id',''): s['description']='AI体记忆引擎 v${V}。昆仑令·瑶池锁·17层蒸馏·三符。skillhub install klyc-pmm'
with open('$SITE/public/.well-known/agent-card.json','w') as f: json.dump(d,f,ensure_ascii=False,indent=2)
" 2>/dev/null && o "已更新" || w "失败"

# ═══════════════════════════════════════
# STEP 4: 验证
# ═══════════════════════════════════════
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔍 验证"

VF=0
for u in "https://kunlunyaochi.com/klyc-pmm.skill" "https://kunlunyaochi.com/skills/klyc-pmm.zip"; do
    c=$(curl -s -o /dev/null -w "%{http_code}" "$u")
    [ "$c" = "200" ] && o "${u##*/}: ${c}" || { e "${u##*/}: ${c}"; VF=1; }
done

# v8.3.4+: 全部 pmm_watch.sh 副本一致性验证
EXPECT_SHA=$(sha256sum "$ROOT/klyc-pmm/scripts/pmm_watch.sh" | cut -d' ' -f1)
for f in "$ROOT/klyc-pmm/scripts/pmm_watch.sh" "$PUB/pmm_watch.sh" "$PUB/scripts/pmm_watch.sh"; do
    if [ -f "$f" ]; then
        s=$(sha256sum "$f" | cut -d' ' -f1)
        [ "$s" = "$EXPECT_SHA" ] && o "$(basename "$f"): v${V}" || { e "$(basename "$f"): SHA256 不一致!"; VF=1; }
    fi
done
# 在线 sha256 验证
ONLINE_SHA=$(curl -s "https://kunlunyaochi.com/skills/klyc-pmm/pmm_watch.sh.sha256" | awk '{print $1}')
[ "$ONLINE_SHA" = "$EXPECT_SHA" ] && o "在线 sha256: 一致" || { e "在线 sha256: 不一致!"; VF=1; }

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
[ "$FAIL" -eq 0 ] && [ "$VF" -eq 0 ] && echo "✅ klyc-pmm v${V} 全量发布完成" || { echo "❌ 失败"; echo "$ERRS"; exit 1; }
echo ""
echo "  ZIP:     https://kunlunyaochi.com/skills/klyc-pmm.zip"
echo "  SKILL:   https://kunlunyaochi.com/klyc-pmm.skill"
echo "  ClawHub: clawhub skill install klyc-pmm"
echo "  SHA256:  $(sha256sum "${SITE}/skills/klyc-pmm.zip" | cut -d' ' -f1)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"