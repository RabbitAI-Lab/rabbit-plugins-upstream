#!/bin/bash
# ═══════════════════════════════════════════════════════════
# klyc_release_check.sh — 昆仑瑶池发布前全量校验
# 合并: 昆仑9项发布检查 + 瑶池8大类50项安全合规检查
# 用法: bash klyc_release_check.sh <版本号>
# 示例: bash klyc_release_check.sh 9.1.14
# ═══════════════════════════════════════════════════════════
set -o pipefail

VER="${1:-}"
if [ -z "$VER" ]; then
    echo "用法: $0 <版本号>  例: $0 9.1.14"
    exit 1
fi

ROOT="/www/wwwroot/kunlunyaochi"
ZIP="$ROOT/skills/klyc-pmm.zip"
WS_KUNLUN="$HOME/.openclaw/workspace/skills/klyc-pmm"
WS_YAOCHI="/root/.lightclaw/workspace/skills/@user_6e41807a/klyc-pmm"
ERR=0; PASS=0; TOTAL=0
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'

pass() { echo -e "  ${GREEN}✅${NC} $1"; PASS=$((PASS+1)); TOTAL=$((TOTAL+1)); }
fail() { echo -e "  ${RED}❌${NC} $1"; ERR=$((ERR+1)); TOTAL=$((TOTAL+1)); }
warn() { echo -e "  ${YELLOW}⚠️${NC}  $1"; TOTAL=$((TOTAL+1)); }
exclude() { grep -v '\.bak' | grep -v vendor | grep -v CHANGELOG | grep -v arena_testdata | grep -v '\.zip:'; }

echo "═══════════════════════════════════════════════════════════"
echo "  昆仑瑶池 发布前全量校验 v$VER"
echo "═══════════════════════════════════════════════════════════"

# ═══════════════════════════ 一、版本号全站统一 ═══════════════════════════
echo ""; echo "━━━ 一、版本号全站统一 ━━━"

for old in "8\.1\.1" "8\.4\.0" "6\.1\.0" "9\.0\.0" "9\.0\.1"; do
    [ "$old" = "${VER//./\\.}" ] && continue
    hits=$(grep -rn "$old" $ROOT/templates $ROOT/public $ROOT/api $ROOT/skills 2>/dev/null | exclude | wc -l | tr -d ' ')
    [ "$hits" -gt 0 ] && fail "旧版残留 ${old//\\/}: ${hits}处" || pass "旧版残留 ${old//\\/}: 0"
done

hits=$(grep -rn '17层\|17环节\|17-layer\|17-event\|17-stage' $ROOT/templates $ROOT/public $ROOT/api $ROOT/skills 2>/dev/null | exclude | grep -v '17层→14层' | wc -l | tr -d ' ')
[ "$hits" -gt 0 ] && fail "17层残留: ${hits}处" || pass "17层残留: 0"

hits=$(grep -rn '入驻即赠 100\|获得 100 蟠桃\|送.*100.*蟠桃' $ROOT/templates $ROOT/public $ROOT/api 2>/dev/null | exclude | grep -v '10000\|100颗\|100 颗\|100蟠桃/' | wc -l | tr -d ' ')
[ "$hits" -gt 0 ] && fail "100蟠桃残留: ${hits}处" || pass "100蟠桃残留: 0"

# 全站版本一致性
VER_FILES=(
    "$WS_KUNLUN/scripts/pmm_watch.sh"
    "$WS_KUNLUN/scripts/pmm_distill.sh"
    "$WS_KUNLUN/scripts/install-daemon.sh"
    "$WS_KUNLUN/SKILL.md"
    "$WS_KUNLUN/skill.json"
    "$WS_YAOCHI/scripts/pmm_watch.sh"
    "$WS_YAOCHI/scripts/pmm_distill.sh"
    "$WS_YAOCHI/scripts/install-daemon.sh"
    "$WS_YAOCHI/SKILL.md"
    "$WS_YAOCHI/skill.json"
    "/root/bin/pmm_watch.sh"
    "/root/bin/pmm_distill.sh"
    "/root/bin/install-daemon.sh"
    "$ROOT/skills/klyc-pmm/SKILL.md"
    "$ROOT/skills/klyc-pmm/skill.json"
    "$ROOT/skills/klyc-pmm/scripts/pmm_watch.sh"
    "$ROOT/skills/klyc-pmm/scripts/pmm_distill.sh"
    "$ROOT/skills/klyc-pmm/scripts/install-daemon.sh"
    "$ROOT/public/skill.md"
    "$ROOT/public/klyc-pmm.skill"
    "$ROOT/public/skill-hub.json"
    "$ROOT/public/.well-known/agent-card.json"
    # 网站 skills/ 根级清单（昆仑⑨——常被遗漏的元文件）
    "$ROOT/skills/SKILL.md"
    "$ROOT/skills/skill.json"
    "$HOME/.openclaw/workspace/skills/SKILL.md"
    "$HOME/.openclaw/workspace/skills/skill.json"
)
VER_ERR=0
for f in "${VER_FILES[@]}"; do
    [ -f "$f" ] || { warn "文件不存在: $(echo "$f" | sed "s|$HOME|~|" | sed "s|$ROOT||")"; continue; }
    [[ "$f" == *CHANGELOG* ]] && continue
    FOUND=$(grep -oP '9\.\d+\.\d+' "$f" 2>/dev/null | sort -uV | tr '\n' ' ')
    if echo "$FOUND" | grep -qw "$VER"; then
        OTHERS=$(echo "$FOUND" | tr ' ' '\n' | grep -v "^${VER}$" || true)
        if [ -n "$OTHERS" ]; then
            fail "$(echo "$f" | sed "s|$HOME|~|" | sed "s|$ROOT||"): 含旧版 $(echo $OTHERS | tr '\n' ' ')"
            VER_ERR=$((VER_ERR+1))
        fi
    else
        if [ -n "$FOUND" ]; then
            fail "$(echo "$f" | sed "s|$HOME|~|" | sed "s|$ROOT||"): 无$VER (有$FOUND)"
        else
            warn "$(echo "$f" | sed "s|$HOME|~|" | sed "s|$ROOT||"): 无版本号"
        fi
        VER_ERR=$((VER_ERR+1))
    fi
done
[ $VER_ERR -eq 0 ] && pass "全站版本一致 ($VER)"

# ═══════════════════════════ 二、安全红线扫描 ═══════════════════════════
echo ""; echo "━━━ 二、安全红线扫描 ━━━"

scan_dir() {
    local dir="$1" label="$2"
    [ ! -d "$dir" ] && return
    local hits

    hits=$(grep -rn --include="*.sh" 'curl.*|.*bash\|wget.*|.*bash' "$dir" 2>/dev/null | grep -v "klyc_release_check\|klyc_pre_release_check" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "curl|bash=0 ($label)" || fail "curl|bash: ${hits}处 ($label)"

    hits=$(grep -rn --include="*.sh" '\beval\b\|\bexec\b' "$dir" 2>/dev/null | grep -v "pmm_watch.*exec\|klyc_release_check\|#.*exec\|findMem" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "eval/exec=0 ($label)" || warn "eval/exec: ${hits}处 ($label)"

    hits=$(grep -rn --include="*.sh" 'base64.*-d.*|\s*sh\b' "$dir" 2>/dev/null | grep -v "klyc_release_check" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "base64|sh=0 ($label)" || fail "base64|sh: ${hits}处 ($label)"

    hits=$(grep -rn --include="*.sh" 'DEBUG.*token\|echo.*\$token\|echo.*\$api_key' "$dir" 2>/dev/null | grep -v "klyc_release_check\|#.*DEBUG" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "DEBUG凭证=0 ($label)" || fail "DEBUG凭证: ${hits}处 ($label)"

    hits=$(grep -rn --include="*.sh" '/etc/shadow\|/root/.ssh/id_rsa' "$dir" 2>/dev/null | grep -v "klyc_release_check\|klyc_pre_release_check" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "敏感路径=0 ($label)" || fail "敏感路径: ${hits}处 ($label)"

    hits=$(grep -rn --include="*.sh" 'rm\s\+-rf\s\+/' "$dir" 2>/dev/null | grep -v "klyc_release_check\|klyc_pre_release_check" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "rm -rf /=0 ($label)" || fail "rm -rf /: ${hits}处 ($label)"
}
scan_dir "$WS_YAOCHI/scripts" "瑶池"
scan_dir "$WS_KUNLUN/scripts" "昆仑"

# ═══════════════════════════ 三、SKILL.md 安全声明 ═══════════════════════════
echo ""; echo "━━━ 三、SKILL.md 安全声明 ━━━"

for md in "$WS_YAOCHI/SKILL.md" "$WS_KUNLUN/SKILL.md"; do
    [ ! -f "$md" ] && { warn "SKILL.md 不存在"; continue; }
    label=$(echo "$md" | grep -q "openclaw" && echo "昆仑" || echo "瑶池")

    grep -q 'local_only:\s*false' "$md" && pass "local_only:false ($label)" || fail "local_only 应为 false ($label)"
    grep -q 'data_flow:' "$md" && pass "data_flow ($label)" || fail "data_flow 缺失 ($label)"
    grep -q 'network:' "$md" && pass "network ($label)" || fail "network 缺失 ($label)"
    grep -q 'no_collect:' "$md" && pass "no_collect ($label)" || fail "no_collect 缺失 ($label)"

    if awk '/^---$/{c++} /security_model:/{if(c<2)print}' "$md" | grep -q .; then
        fail "security_model 越位 frontmatter ($label)"
    else
        pass "security_model 未越位 ($label)"
    fi

    if awk '/^---$/{c++} /¥[0-9]/{if(c>=2)print}' "$md" | grep -q .; then
        warn "正文含¥金额 ($label)"
    else
        pass "正文无¥ ($label)"
    fi
    grep -q '认证边界' "$md" && pass "认证边界 ($label)" || warn "缺认证边界说明 ($label)"
    grep -q 'hooks-pull.*安全\|hooks-pull.*认证' "$md" && pass "hooks-pull安全 ($label)" || warn "缺hooks-pull说明 ($label)"
done

# ═══════════════════════════ 四、网站发布检查 ═══════════════════════════
echo ""; echo "━━━ 四、网站发布检查 ━━━"

hits=0
for kw in Qdrant "Redis PUBLISH" "2:05 AM" klyc_auto_tag klyc_distill_cron; do
    grep -q "$kw" "$ROOT/templates/klyc_page_klycpmm.php" 2>/dev/null && hits=$((hits+1))
done
[ "$hits" -gt 0 ] && fail "涉密信息: ${hits}处" || pass "涉密: 0"

FORK_ERR=0
[ -d "$ROOT/skills/klyc-pmm-pay" ] && { fail "分叉目录"; FORK_ERR=1; }
ls "$ROOT/skills/klyc-pmm-pay"*".zip" 2>/dev/null | grep -qv 'klyc-pmm.zip' && { fail "分叉ZIP"; FORK_ERR=1; }
[ ! -f "$ZIP" ] && { warn "ZIP缺失"; FORK_ERR=1; }
[ $FORK_ERR -eq 0 ] && pass "分叉: 无"

if [ -f "$ZIP" ]; then
    ZIP_ERR=0
    for bad in .sha256 .bak .swp; do
        unzip -l "$ZIP" 2>/dev/null | grep -q "$bad" && { fail "ZIP含 $bad"; ZIP_ERR=$((ZIP_ERR+1)); }
    done
    [ $ZIP_ERR -eq 0 ] && pass "ZIP合规"
fi

echo ""; echo "━━━ 四-续、端点可达性 ━━━"
for url in "/?route=klyc-pmm" "/skill-hub.json" "/skills/klyc-pmm.zip" "/?route=join" "/?route=recover" "/.well-known/agent-card.json" "/llms.txt"; do
    hdr=""
    [ "$url" = "/skills/klyc-pmm.zip" ] && hdr="-H 'Referer: https://kunlunyaochi.com/'"
    code=$(eval curl -s -o /dev/null -w '%{http_code}' $hdr "https://kunlunyaochi.com$url" 2>/dev/null)
    [ "$code" = "200" ] && pass "$code $url" || fail "$code $url"
done

# ═══════════════════════════ 五、源同步 ═══════════════════════════
echo ""; echo "━━━ 五、源同步 ━━━"

SK_PUB="$ROOT/skills/klyc-pmm/scripts"
for ws_label in "昆仑:$WS_KUNLUN/scripts" "瑶池:$WS_YAOCHI/scripts"; do
    label="${ws_label%%:*}"; ws="${ws_label#*:}"
    [ ! -d "$ws" ] && { warn "$label workspace 不存在"; continue; }
    for f in pmm_distill.sh pmm_watch.sh; do
        [ -f "$ws/$f" ] && [ -f "$SK_PUB/$f" ] || continue
        diff -q "$ws/$f" "$SK_PUB/$f" >/dev/null 2>&1 && pass "$label/$f ≡ PUB" || fail "$label/$f ≠ PUB"
    done
done

# ═══════════════════════════ 六、文件完整性 ═══════════════════════════
echo ""; echo "━━━ 六、文件完整性 ━━━"

for ws_label in "昆仑:$WS_KUNLUN" "瑶池:$WS_YAOCHI"; do
    label="${ws_label%%:*}"; dir="${ws_label#*:}"
    [ ! -d "$dir" ] && { warn "$label workspace 不存在"; continue; }
    for f in "SKILL.md" "skill.json" "CHANGELOG.md" "scripts/pmm_watch.sh" "scripts/pmm_distill.sh" "scripts/install-daemon.sh" "scripts/klyc_pre_release_check.sh"; do
        [ -f "$dir/$f" ] && pass "$label/$f" || warn "$label/$f 缺失"
    done
done

# ═══════════════════════════ 七、铁律#53 ═══════════════════════════
echo ""; echo "━━━ 七、铁律#53 ━━━"
warn "代码搜索≠运行时验证。安全头(CSP/HSTS/CORS)需手动 curl 验证"
echo "  curl -sI https://kunlunyaochi.com | grep -i 'content-security-policy\|strict-transport'"

# ═══════════════════════════ 总结 ═══════════════════════════
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "  版本: $VER  检查项: $TOTAL  通过: $PASS  失败: $ERR"
echo "═══════════════════════════════════════════════════════════"
if [ "$ERR" -eq 0 ]; then
    echo -e "  ${GREEN}✅ 发布前检查全部通过${NC}"
    exit 0
else
    echo -e "  ${RED}❌ $ERR 项未通过，修复后再发布${NC}"
    exit 1
fi
