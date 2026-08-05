#!/bin/bash
# 用法: bash klyc_release_check.sh 9.1.2（昆仑/瑶池共享）
# 用法: bash klyc_release_check.sh 9.1.0

VER="${1:-9.1.0}"
ROOT="/www/wwwroot/kunlunyaochi"
ZIP="$ROOT/skills/klyc-pmm.zip"
ERR=0

exclude() { grep -v '\.bak' | grep -v vendor | grep -v CHANGELOG | grep -v arena_testdata | grep -v '\.zip:'; }

echo "═══════════════════════════════"
echo "  发布前校验 v$VER"
echo "═══════════════════════════════"

# ① 版本号残留
echo ""
echo "① 版本号残留"
for old in "8\.1\.1" "8\.4\.0" "6\.1\.0" "9\.0\.0" "9\.0\.1"; do
    [ "$old" = "${VER//./\\.}" ] && continue
    hits=$(grep -rn "$old" $ROOT/templates $ROOT/public $ROOT/api $ROOT/skills 2>/dev/null | exclude | wc -l | tr -d ' ')
    [ "$hits" -gt 0 ] && echo "  ❌ ${old//\\/}: ${hits}处" && ERR=$((ERR+1))
done
[ $ERR -eq 0 ] && echo "  ✅"

# ② 17残留
echo ""
echo "② 17层残留"
hits=$(grep -rn '17层\|17环节\|17-layer\|17-event\|17-stage' $ROOT/templates $ROOT/public $ROOT/api $ROOT/skills 2>/dev/null | exclude | grep -v '17层→14层' | wc -l | tr -d ' ')
[ "$hits" -gt 0 ] && echo "  ❌ ${hits}处" && ERR=$((ERR+1)) || echo "  ✅"

# ③ skill包源同步
echo ""
echo "③ 源同步"
WS="${HOME}/.openclaw/workspace/skills/klyc-pmm/scripts"
SK="$ROOT/skills/klyc-pmm/scripts"
SYNC_ERR=0
for f in pmm_distill.sh pmm_watch.sh; do
    [ -f "$WS/$f" ] && [ -f "$SK/$f" ] || continue
    diff -q "$WS/$f" "$SK/$f" >/dev/null 2>&1 || { echo "  ❌ $f 不同步 (源≠PUB)"; SYNC_ERR=$((SYNC_ERR+1)); ERR=$((ERR+1)); }
done
# 版本号一致性
ver_ws=$(grep 'readonly VERSION' "$WS/pmm_watch.sh" | grep -oP '"\d+\.\d+\.\d+"' | tr -d '"')
ver_sk=$(grep 'readonly VERSION' "$SK/pmm_watch.sh" | grep -oP '"\d+\.\d+\.\d+"' | tr -d '"')
[ "$ver_ws" != "$ver_sk" ] && echo "  ❌ 版本不一致: 源=$ver_ws PUB=$ver_sk" && ERR=$((ERR+1))
[ $SYNC_ERR -eq 0 ] && echo "  ✅"

# ④ 100蟠桃
echo ""
echo "④ 100蟠桃"
hits=$(grep -rn '入驻即赠 100\|获得 100 蟠桃\|送.*100.*蟠桃' $ROOT/templates $ROOT/public $ROOT/api 2>/dev/null | exclude | grep -v '10000\|100颗\|100 颗\|100蟠桃/' | wc -l | tr -d ' ')
[ "$hits" -gt 0 ] && echo "  ❌ ${hits}处" && ERR=$((ERR+1)) || echo "  ✅"

# ⑤ 涉密
echo ""
echo "⑤ 涉密"
hits=0
for kw in Qdrant "Redis PUBLISH" "2:05 AM" klyc_auto_tag klyc_distill_cron; do
    grep -q "$kw" "$ROOT/templates/klyc_page_klycpmm.php" 2>/dev/null && hits=$((hits+1))
done
[ "$hits" -gt 0 ] && echo "  ❌ ${hits}处" && ERR=$((ERR+1)) || echo "  ✅"

# ⑥ 分叉
echo ""
echo "⑥ 分叉"
[ -d "$ROOT/skills/klyc-pmm-pay" ] && echo "  ❌ 分叉目录" && ERR=$((ERR+1))
ls "$ROOT/skills/klyc-pmm-pay"*".zip" 2>/dev/null | grep -qv 'klyc-pmm.zip' && echo "  ❌ 分叉ZIP" && ERR=$((ERR+1))
[ ! -f "$ZIP" ] && echo "  ❌ ZIP缺失" && ERR=$((ERR+1))
([ -d "$ROOT/skills/klyc-pmm-pay" ] || ls "$ROOT/skills/klyc-pmm-pay"*".zip" 2>/dev/null | grep -qv 'klyc-pmm.zip' || [ ! -f "$ZIP" ]) || echo "  ✅"

# ⑦ ZIP合规
echo ""
echo "⑦ ZIP合规"
if [ -f "$ZIP" ]; then
    ZIP_ERR=0
    for bad in .sha256 .bak .swp; do
        unzip -l "$ZIP" 2>/dev/null | grep -q "$bad" && { echo "  ❌ 含禁用文件: $bad"; ZIP_ERR=$((ZIP_ERR+1)); }
    done
    [ $ZIP_ERR -gt 0 ] && ERR=$((ERR+ZIP_ERR))
    [ $ZIP_ERR -eq 0 ] && echo "  ✅"
else
    echo "  ⚠️ ZIP不存在"
fi

# ⑧ 端点
echo ""
echo "⑧ 端点"
for url in "/?route=klyc-pmm" "/skill-hub.json" "/skills/klyc-pmm.zip" "/?route=join" "/?route=recover" "/.well-known/agent-card.json" "/llms.txt"; do
    # /skills/ 目录有防盗链，需带 referer
    hdr=""
    [ "$url" = "/skills/klyc-pmm.zip" ] && hdr="-H 'Referer: https://kunlunyaochi.com/'"
    code=$(eval curl -s -o /dev/null -w '%{http_code}' $hdr "https://kunlunyaochi.com$url" 2>/dev/null)
    [ "$code" = "200" ] && echo "  ✅ $code $url" || { echo "  ❌ $code $url"; ERR=$((ERR+1)); }
done
code=$(curl -s -o /dev/null -w '%{http_code}' -X POST 'https://kunlunyaochi.com/api/klyc-pmm-pay/resource.php' -H 'Content-Type: application/json' -d '{}' 2>/dev/null)
[ "$code" = "402" ] && echo "  ✅ $code /api/klyc-pmm-pay/resource.php" || { echo "  ❌ $code"; ERR=$((ERR+1)); }

# ⑨ 全站版本一致性（v9.1.13 教训：四次版本分裂，PHP后端/根级/public入口长期落后）
echo ""
echo "⑨ 全站版本一致性"

VER_FILES=(
    # 本地主源
    "$HOME/.openclaw/workspace/skills/SKILL.md:version字段"
    "$HOME/.openclaw/workspace/skills/skill.json"
    "$HOME/.openclaw/workspace/skills/klyc-pmm/SKILL.md:version字段"
    "$HOME/.openclaw/workspace/skills/klyc-pmm/skill.json"
    "$HOME/.openclaw/workspace/skills/klyc-pmm/scripts/pmm_watch.sh"
    "$HOME/.openclaw/workspace/skills/klyc-pmm/scripts/pmm_distill.sh"
    "$HOME/.openclaw/workspace/skills/klyc-pmm/scripts/install-daemon.sh"
    # /root/bin 系统入口
    "/root/bin/pmm_watch.sh"
    "/root/bin/pmm_distill.sh"
    "/root/bin/install-daemon.sh"
    # 网站 skills/
    "$ROOT/skills/SKILL.md:version字段"
    "$ROOT/skills/skill.json"
    "$ROOT/skills/klyc-pmm/SKILL.md:version字段"
    "$ROOT/skills/klyc-pmm/skill.json"
    "$ROOT/skills/klyc-pmm/scripts/pmm_watch.sh"
    "$ROOT/skills/klyc-pmm/scripts/pmm_distill.sh"
    "$ROOT/skills/klyc-pmm/scripts/install-daemon.sh"
    # public 独立入口
    "$ROOT/public/skill.md:version字段"
    "$ROOT/public/klyc-pmm.skill:version字段"
    "$ROOT/public/skill-hub.json"
    "$ROOT/public/.well-known/agent-card.json"
    # PHP 后端（常被遗忘）
    "$ROOT/public/a2a.php"
    "$ROOT/public/index.php"
    "$ROOT/public/api/klyc-pmm-pay/notify.php"
    "$ROOT/public/api/klyc-pmm-pay/resource.php"
)

VER_ERR=0
for entry in "${VER_FILES[@]}"; do
    f="${entry%%:*}"  # 文件路径（去掉 :字段名 后缀）
    [ -f "$f" ] || continue
    
    # 取文件中所有版本号，检查是否至少有一个等于 VER
    FOUND=$(grep -oP '9\.\d+\.\d+' "$f" 2>/dev/null | sort -uV | tr '\n' ' ')
    if echo "$FOUND" | grep -qw "$VER"; then
        # 文件中含目标版本号，进一步检查是否有非目标版本号的活代码（排除 CHANGELOG 历史）
        if echo "$f" | grep -q "CHANGELOG"; then
            continue  # CHANGELOG 允许多版本号
        fi
        # 对于 SKILL.md/skill.json 等核心文件，文件内所有版本号都应一致
        OTHERS=$(echo "$FOUND" | tr ' ' '\n' | grep -v "^${VER}$" || true)
        if [ -n "$OTHERS" ]; then
            echo "  ❌ $(echo $f | sed "s|$HOME|~|" | sed "s|$ROOT||"): 含旧版 $(echo $OTHERS | tr '\n' ' ')"
            VER_ERR=$((VER_ERR+1)); ERR=$((ERR+1))
        fi
    else
        echo "  ❌ $(echo $f | sed "s|$HOME|~|" | sed "s|$ROOT||"): 无 $VER ($FOUND)"
        VER_ERR=$((VER_ERR+1)); ERR=$((ERR+1))
    fi
done
[ $VER_ERR -eq 0 ] && echo "  ✅ 全站版本一致 ($VER)"
