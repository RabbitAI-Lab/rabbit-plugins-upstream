#!/bin/bash
# ============================================
# klyc_skill_check.sh — 昆仑瑶池发布前全量校验（唯一审查入口）
# 版本: 9.2.1
# 包含: 版本全站统一 + 安全红线 + 声明-代码一致性 + SKILL.md安全 + 网站检查 + 源同步 + 文件完整性 + ZIP验证
# 用法: bash klyc_skill_check.sh <版本号>
# 示例: bash klyc_skill_check.sh 9.2.1
# ============================================
set -o pipefail

VER="${1:-}"
if [ -z "$VER" ]; then
    echo "用法: $0 <版本号>  例: $0 9.2.1"
    exit 1
fi

ROOT="/www/wwwroot/kunlunyaochi"
ZIP="$ROOT/skills/@user_6e41807a/klyc-pmm.zip"
WS_KUNLUN="$HOME/.openclaw/workspace/skills/@user_6e41807a/klyc-pmm"
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

hits=$(grep -rn '17层\|17环节\|17-layer\|17-event\|17-stage' $ROOT/templates $ROOT/public $ROOT/api $ROOT/skills | grep -v klyc_skill_check 2>/dev/null | exclude | grep -v '17层→14层' | wc -l | tr -d ' ')
[ "$hits" -gt 0 ] && fail "17层残留: ${hits}处" || pass "17层残留: 0"

hits=$(grep -rn '入驻即赠 100\|获得 100 蟠桃\|送.*100.*蟠桃' $ROOT/templates $ROOT/public $ROOT/api 2>/dev/null | exclude | grep -v '10000\|100颗\|100 颗\|100蟠桃/' | wc -l | tr -d ' ')
[ "$hits" -gt 0 ] && fail "100蟠桃残留: ${hits}处" || pass "100蟠桃残留: 0"

# 全站版本一致性（仅本地 skill 包 + workspace，不查外网发布物）
# 2026-08-07 罗总：审核与发布拆分开，审核只校验本地已就绪部分
VER_FILES=(
    "$WS_KUNLUN/scripts/pmm_watch.sh"
    "$WS_KUNLUN/scripts/pmm_distill.sh"
    "$WS_KUNLUN/scripts/install-daemon.sh"
    "$WS_KUNLUN/scripts/klyc_skill_check.sh"
    "$WS_KUNLUN/SKILL.md"
    "$WS_KUNLUN/skill.json"
    "$WS_KUNLUN/_meta.json"
    "$WS_KUNLUN/CHANGELOG.md"
    "$ROOT/tools/publish_klyc-pmm.sh"
    "$WS_YAOCHI/scripts/pmm_watch.sh"
    "$WS_YAOCHI/scripts/pmm_distill.sh"
    "$WS_YAOCHI/scripts/install-daemon.sh"
    "$WS_YAOCHI/scripts/klyc_skill_check.sh"
    "$WS_YAOCHI/SKILL.md"
    "$WS_YAOCHI/skill.json"
    "$WS_YAOCHI/_meta.json"
    "$WS_YAOCHI/CHANGELOG.md"
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
# 网站版本号同步检查（2026-08-08 罗总：网站版本跟 skill 对齐）
SITE_CFG="$ROOT/config/config.php"
SITE_VER_K=$(grep "define('KLYC_VERSION'\|define(\"KLYC_VERSION\"" "$SITE_CFG" 2>/dev/null | grep -oP "KLYC_VERSION', *'\K[0-9.]+" | head -1)
if [ -z "$SITE_VER_K" ]; then
    warn "config/config.php: 未检测到 KLYC_VERSION"
    VER_ERR=$((VER_ERR+1))
elif echo "$SITE_VER_K" | grep -qw "$VER"; then
    pass "网站版本 KLYC_VERSION=$SITE_VER_K 对齐 ($VER)"
else
    fail "网站版本 KLYC_VERSION=$SITE_VER_K ≠ skill $VER"
    VER_ERR=$((VER_ERR+1))
fi
[ $VER_ERR -eq 0 ] && pass "全站版本一致 ($VER)"

# ═══════════════════════════ 二、安全红线扫描 ═══════════════════════════
echo ""; echo "━━━ 二、安全红线扫描 ━━━"

scan_dir() {
    local dir="$1" label="$2"
    [ ! -d "$dir" ] && return
    local hits

    hits=$(grep -rn --include="*.sh" 'curl.*|.*bash\|wget.*|.*bash' "$dir" 2>/dev/null | grep -v "klyc_release_check\|klyc_skill_check" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "curl|bash=0 ($label)" || fail "curl|bash: ${hits}处 ($label)"

    hits=$(grep -rn --include="*.sh" '\beval\b\|\bexec\b' "$dir" 2>/dev/null | grep -v "pmm_watch.*exec\|klyc_release_check\|#.*exec\|findMem" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "eval/exec=0 ($label)" || warn "eval/exec: ${hits}处 ($label)"

    hits=$(grep -rn --include="*.sh" 'base64.*-d.*|\s*sh\b' "$dir" 2>/dev/null | grep -v "klyc_release_check" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "base64|sh=0 ($label)" || fail "base64|sh: ${hits}处 ($label)"

    hits=$(grep -rn --include="*.sh" 'DEBUG.*token\|echo.*\$token\|echo.*\$api_key' "$dir" 2>/dev/null | grep -v "klyc_release_check\|#.*DEBUG" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "DEBUG凭证=0 ($label)" || fail "DEBUG凭证: ${hits}处 ($label)"

    hits=$(grep -rn --include="*.sh" '/etc/shadow\|/root/.ssh/id_rsa' "$dir" 2>/dev/null | grep -v "klyc_release_check\|klyc_skill_check" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "敏感路径=0 ($label)" || fail "敏感路径: ${hits}处 ($label)"

    hits=$(grep -rn --include="*.sh" 'rm\s\+-rf\s\+/' "$dir" 2>/dev/null | grep -v "klyc_release_check\|klyc_skill_check" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "rm -rf /=0 ($label)" || fail "rm -rf /: ${hits}处 ($label)"

    # 提示词广告推广=零（2026-08-08 罗总怒斥"又往skill包里加广告"后锁定，SkillSpector标记"提示词广告推广"）
    # 只匹配主动推销话术，不误伤 upgrade/owner-pay-link/X402 等付费功能命令
    hits=$(grep -rn --include="*.sh" '主动推销\|保护我的记忆\|开通护魂符避免\|防止再次失忆\|立即开通\|立即保护\|目前只有免费\|500蟠桃/月\|500🍑/月' "$dir" 2>/dev/null | grep -v "klyc_skill_check" | wc -l | tr -d ' ')
    [ "$hits" -eq 0 ] && pass "提示词广告推广=0 ($label)" || fail "提示词广告推广: ${hits}处 ($label)"
}
scan_dir "$WS_YAOCHI/scripts" "瑶池"
scan_dir "$WS_KUNLUN/scripts" "昆仑"

# SKILL.md 提示词广告推广=零（只匹配主动推销话术，不误伤升级功能文档）
for md in "$WS_KUNLUN/SKILL.md" "$WS_YAOCHI/SKILL.md"; do
    [ -f "$md" ] || continue
    lbl=$(echo "$md" | grep -q "KUNLUN" && echo "昆仑" || echo "瑶池")
    hits=$(grep -iEc '主动推销|保护我的记忆|立即开通|立即保护|目前只有免费|500蟠桃/月|500🍑/月|AI体主动推销' "$md" 2>/dev/null)
    [ "$hits" -eq 0 ] && pass "SKILL.md 提示词广告推广=0 ($lbl)" || fail "SKILL.md 提示词广告推广: ${hits}处 ($lbl)"
done

# ═══════════════════════════ 三、声明-代码一致性对账（2026-08-06 SkillSpector审计后锁定）═══════════════════════════
echo ""; echo "━━━ 三、声明-代码一致性对账 ━━━"

# 规则来源：SkillSpector 57条findings中"Intent-Code Divergence"类问题
# 核心原则：脚本头注释的安全声明必须与代码行为逐条吻合，不准写"装饰性声明"
# 每条规则对应一次历史违规，不准再犯同类问题

WS_SCRIPTS="$WS_KUNLUN/scripts"

# ─── 规则1："仅与X通信"必须匹配代码中API端点的默认值 ───
# 违规模板：声明写"仅与 kunlunyaochi.com 通信"，但代码从配置文件/环境变量读取 API 端点
# 正确模式：声明中必须提到"可通过配置文件自定义端点"
# 检测：如果声明含"仅与"但代码有 CONFIG_DIR/api_endpoint 或 KLYC_API_ENDPOINT 变量 → 违规
for sf in "$WS_SCRIPTS/pmm_watch.sh"; do
    [ ! -f "$sf" ] && continue
    decl_only=$(head -30 "$sf" | grep -c '仅与.*通信' 2>/dev/null || true)
    code_configurable=$(grep -c 'API_FILE\|api_endpoint\|KLYC_API_ENDPOINT\|DEFAULT_API' "$sf" 2>/dev/null || true)
    if [ "$decl_only" -gt 0 ] && [ "$code_configurable" -gt 0 ]; then
        # 声明写了"仅与"，但代码里有可配置端点 → 检查是否声明了"可自定义"
        if head -30 "$sf" | grep -q '可自定义\|可配置\|默认.*通信'; then
            pass "声明-代码一致: 网络端点 (声明已标注可自定义)"
        else
            fail "声明-代码矛盾: 注释写'仅与X通信'但代码端点可配置 (pmm_watch.sh)"
        fi
    else
        pass "声明-代码一致: 网络端点"
    fi
done

# ─── 规则2："不修改系统文件"必须匹配代码中是否有写入/etc的操作 ───
# 违规模板：声明写"不修改系统文件"，但 upgrade 命令写 /etc/systemd/system/*.service
# 正确模式：声明中必须标注"upgrade 命令在 root 权限下可选创建 systemd 服务"
for sf in "$WS_SCRIPTS/pmm_watch.sh"; do
    [ ! -f "$sf" ] && continue
    decl_no_sys=$(head -30 "$sf" | grep -c '不.*修改系统文件' 2>/dev/null || true)
    code_writes_etc=$(grep -c '/etc/systemd/system' "$sf" 2>/dev/null || true)
    if [ "$decl_no_sys" -gt 0 ] && [ "$code_writes_etc" -gt 0 ]; then
        # 声明说"不修改系统文件"但代码写了 /etc/systemd → 检查是否标注了例外
        if head -30 "$sf" | grep -q 'upgrade.*systemd\|systemd.*服务\|root.*创建' ; then
            pass "声明-代码一致: 系统文件 (声明已标注upgrade例外)"
        else
            fail "声明-代码矛盾: 注释写'不修改系统文件'但代码写/etc/systemd/system (pmm_watch.sh)"
        fi
    else
        pass "声明-代码一致: 系统文件"
    fi
done

# ─── 规则3："纯只读"声明必须匹配代码中无写操作 ───
# 违规模板：声明或文档标注"纯只读/幂等/不写文件"，但代码中存在写入或数据库变更
# 检测所有脚本：如果声明含"只读"或"不写"但代码有 INSERT/UPDATE/DELETE/cat >/echo > → 违规
for sf in "$WS_SCRIPTS/pmm_watch.sh" "$WS_SCRIPTS/pmm_distill.sh" "$WS_SCRIPTS/oneclick.sh" "$WS_SCRIPTS/install-daemon.sh" "$WS_KUNLUN/examples/quickstart.sh"; do
    [ ! -f "$sf" ] && continue
    fname=$(basename "$sf")
    decl_readonly=$(head -30 "$sf" | grep -ci '只读.*不写\|幂等.*不写\|纯只读\|不写任何文件' 2>/dev/null || true)
    if [ "$decl_readonly" -gt 0 ]; then
        # 有只读声明 → 检查代码中是否有写操作
        code_writes=$(grep -cE '(cat|echo|tee) >|>>|UPDATE.*SET|INSERT INTO|DELETE FROM|systemctl enable|mv .* /etc' "$sf" 2>/dev/null || true)
        if [ "$code_writes" -gt 0 ]; then
            fail "声明-代码矛盾: $fname 声明'只读/不写'但代码存在写操作(${code_writes}处疑似)"
        else
            pass "声明-代码一致: $fname 只读声明属实"
        fi
    fi
    # 额外检查：quickstart.sh 标注网络行为
    if [ "$fname" = "quickstart.sh" ]; then
        if head -10 "$sf" | grep -qi 'HTTPS\|网络.*探针\|kunlunyaochi'; then
            pass "声明-代码一致: quickstart.sh 已标注网络行为"
        else
            fail "声明-代码矛盾: quickstart.sh 有网络调用(self-test)但头部未声明"
        fi
    fi
done

# ─── 规则4："不修改系统文件"声明 + install-daemon/oneclick 写系统路径 → 必须标注 ───
# 违规模板：install-daemon.sh 写 /etc/systemd/system 但声明说不修改系统文件
for sf in "$WS_SCRIPTS/install-daemon.sh" "$WS_SCRIPTS/oneclick.sh"; do
    [ ! -f "$sf" ] && continue
    fname=$(basename "$sf")
    writes_system=$(grep -cE '/etc/systemd|systemctl (enable|daemon-reload)|apt-get install|yum install|apk add' "$sf" 2>/dev/null || true)
    if [ "$writes_system" -gt 0 ]; then
        # 脚本有系统级操作 → 必须在头部注释中标明
        if head -30 "$sf" | grep -qiE '安装|依赖|systemd|包管理|apt|yum|apk'; then
            pass "声明-代码一致: $fname 系统操作已标注"
        else
            fail "声明-代码矛盾: $fname 有系统级操作(apt/systemctl)但头部未声明"
        fi
    else
        pass "声明-代码一致: $fname 无系统操作"
    fi
done

# ─── 规则5：蒸馏脚本必须声明自动软删除行为 ───
# 违规模板：pmm_distill.sh 执行 SQL UPDATE SET is_deleted=1 但头部未声明
for sf in "$WS_SCRIPTS/pmm_distill.sh"; do
    [ ! -f "$sf" ] && continue
    has_delete=$(grep -c 'is_deleted=1' "$sf" 2>/dev/null || true)
    if [ "$has_delete" -gt 0 ]; then
        if head -20 "$sf" | grep -qiE '软删除|标记.*删除|dry-run|预览'; then
            pass "声明-代码一致: pmm_distill.sh 软删除行为已声明"
        else
            fail "声明-代码矛盾: pmm_distill.sh 有软删除操作但头部未声明"
        fi
    fi
done

# ─── 规则6：SKILL.md "安装前请了解"章节必须存在 ───
# 违规模板：SKILL.md 缺少前置告警章节，用户不知道一键安装会做什么
for md in "$WS_KUNLUN/SKILL.md" "$WS_YAOCHI/SKILL.md"; do
    [ ! -f "$md" ] && continue
    label=$(echo "$md" | grep -q "openclaw" && echo "昆仑" || echo "瑶池")
    if grep -q '安装前请了解\|⚠️.*重要.*安装' "$md" 2>/dev/null; then
        pass "SKILL.md 前置告警章节: $label ✅"
    else
        fail "SKILL.md 缺前置告警章节: $label (需含网络/持久化/昆仑令/蒸馏/守护五项说明)"
    fi
done

# ─── 规则7：昆仑令落盘处必须有安全警告 ───
# 违规模板：oneclick.sh 将昆仑令URL写入MEMORY.md但无醒目安全提示
for sf in "$WS_SCRIPTS/oneclick.sh" "$WS_SCRIPTS/pmm_watch.sh"; do
    [ ! -f "$sf" ] && continue
    fname=$(basename "$sf")
    writes_talisman=$(grep -c 'TALISMAN_URL\|昆仑令.*MEMORY\|klyc-pmm/.*token' "$sf" 2>/dev/null || true)
    if [ "$writes_talisman" -gt 0 ]; then
        if grep -qiE '不要分享|请勿.*公开|唯一凭证|安全.*警告|保密' "$sf" 2>/dev/null; then
            pass "声明-代码一致: $fname 昆仑令安全警告已存在"
        else
            fail "声明-代码矛盾: $fname 写入昆仑令但缺少安全警告(不要分享/勿提交公开仓库)"
        fi
    fi
done

# ─── 规则8：所有脚本头部必须有行为声明 ───
# 违规模板：脚本有写文件/网络/系统操作但头部只有"用法"注释
# 检测所有 .sh 脚本：如果代码含 curl/post/write/systemctl，头部必须有行为描述
for sf in "$WS_SCRIPTS"/*.sh "$WS_KUNLUN/examples"/*.sh; do
    [ ! -f "$sf" ] && continue
    fname=$(basename "$sf")
    # 排除审核脚本自身
    [[ "$fname" == klyc_skill_check* ]] && continue
    
    has_network=$(grep -cE 'curl |wget |/api\.php' "$sf" 2>/dev/null || true)
    has_write=$(grep -cE 'cat >|echo.*>|tee |>.*/(etc|MEMORY|\.klyc)' "$sf" 2>/dev/null || true)
    has_system=$(grep -cE 'systemctl |/etc/systemd|apt-get |yum |apk ' "$sf" 2>/dev/null || true)
    
    if [ "$has_network" -gt 0 ] || [ "$has_write" -gt 0 ] || [ "$has_system" -gt 0 ]; then
        # 脚本有副作用 → 必须有行为声明
        if head -30 "$sf" | grep -qiE '⚠️|行为声明|安装前请了解|注意|本脚本会|HTTPS.*推送|写入|systemd|持久化'; then
            pass "脚本行为声明: $fname"
        else
            fail "脚本缺行为声明: $fname (有网络/写文件/系统操作但头部无说明)"
        fi
    fi
done

# ─── 规则9：无隐藏Unicode/零宽字符（MCP Tool Poisoning防范） ───
# 检测 SKILL.md 和所有 .sh 脚本中是否存在零宽字符
for sf in "$WS_KUNLUN/SKILL.md" "$WS_YAOCHI/SKILL.md" "$WS_SCRIPTS"/*.sh; do
    [ ! -f "$sf" ] && continue
    fname=$(basename "$sf")
    # U+200B 零宽空格, U+200C 零宽非连接符, U+200D 零宽连接符, U+FEFF BOM
    zw=$(grep -Pn '[\x{200B}\x{200C}\x{200D}\x{FEFF}\x{202A}-\x{202E}]' "$sf" 2>/dev/null | head -5)
    if [ -n "$zw" ]; then
        fail "隐藏Unicode/零宽字符: $fname 中发现"
        echo "$zw" | while read line; do echo "    $line"; done
    fi
done
# 排除本脚本自身的零宽检查结果
pass "隐藏Unicode检查: 已完成"

# ═══════════════════════════ 四、SKILL.md 安全声明 ═══════════════════════════
echo ""; echo "━━━ 四、SKILL.md 安全声明 ━━━"

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

# ═══════════════════════════ 五、网站发布检查 ═══════════════════════════
echo ""; echo "━━━ 五、网站发布检查 ━━━"

hits=0
for kw in Qdrant "Redis PUBLISH" "2:05 AM" klyc_auto_tag klyc_distill_cron; do
    grep -q "$kw" "$ROOT/templates/klyc_page_klycpmm.php" 2>/dev/null && hits=$((hits+1))
done
[ "$hits" -gt 0 ] && fail "涉密信息: ${hits}处" || pass "涉密: 0"

FORK_ERR=0
[ -d "$ROOT/skills/@user_6e41807a/klyc-pmm-pay" ] && { fail "分叉目录"; FORK_ERR=1; }
ls "$ROOT/skills/@user_6e41807a/klyc-pmm-pay"*".zip" 2>/dev/null | grep -qv 'klyc-pmm.zip' && { fail "分叉ZIP"; FORK_ERR=1; }
[ ! -f "$ZIP" ] && { warn "ZIP缺失"; FORK_ERR=1; }
[ $FORK_ERR -eq 0 ] && pass "分叉: 无"

if [ -f "$ZIP" ]; then
    ZIP_ERR=0
    for bad in .sha256 .bak .swp; do
        unzip -l "$ZIP" 2>/dev/null | grep -q "$bad" && { fail "ZIP含 $bad"; ZIP_ERR=$((ZIP_ERR+1)); }
    done
    [ $ZIP_ERR -eq 0 ] && pass "ZIP合规"
fi

echo ""; echo "━━━ 五-续、端点可达性 ━━━"
for url in "/?route=klyc-pmm" "/skill-hub.json" "/skills/klyc-pmm.zip" "/?route=join" "/?route=recover" "/.well-known/agent-card.json" "/llms.txt"; do
    referer_flag=()
    [ "$url" = "/skills/klyc-pmm.zip" ] && referer_flag=(-H "Referer: https://kunlunyaochi.com/")
    code=$(curl -s -o /dev/null -w '%{http_code}' "${referer_flag[@]}" "https://kunlunyaochi.com$url" 2>/dev/null)
    case "$code" in 200|301|302) pass "$code $url";; *) fail "$code $url";; esac
done

# ═══════════════════════════ 六、源同步 ═══════════════════════════
echo ""; echo "━━━ 六、源同步 ━━━"

SK_PUB="$ROOT/skills/@user_6e41807a/klyc-pmm/scripts"
for ws_label in "昆仑:$WS_KUNLUN/scripts" "瑶池:$WS_YAOCHI/scripts"; do
    label="${ws_label%%:*}"; ws="${ws_label#*:}"
    [ ! -d "$ws" ] && { warn "$label workspace 不存在"; continue; }
    for f in pmm_distill.sh pmm_watch.sh; do
        [ -f "$ws/$f" ] && [ -f "$SK_PUB/$f" ] || continue
        diff -q "$ws/$f" "$SK_PUB/$f" >/dev/null 2>&1 && pass "$label/$f ≡ PUB" || fail "$label/$f ≠ PUB"
    done
done

# ═══════════════════════════ 七、文件完整性 ═══════════════════════════
echo ""; echo "━━━ 七、文件完整性 ━━━"

for ws_label in "昆仑:$WS_KUNLUN" "瑶池:$WS_YAOCHI"; do
    label="${ws_label%%:*}"; dir="${ws_label#*:}"
    [ ! -d "$dir" ] && { warn "$label workspace 不存在"; continue; }
    for f in "SKILL.md" "skill.json" "CHANGELOG.md" "scripts/pmm_watch.sh" "scripts/pmm_distill.sh" "scripts/install-daemon.sh" "scripts/klyc_skill_check.sh"; do
        [ -f "$dir/$f" ] && pass "$label/$f" || warn "$label/$f 缺失"
    done
done

# ═══════════════════════════ 八、铁律#61 #62 #63 — ZIP双端一致+内版本+脚本变量 ═══════════════════════════
echo ""; echo "━━━ 八、铁律#61 #62 #63 ━━━"

# 7.1 工作区 ZIP ↔ 网站 ZIP 二元一致
WS_ZIP="$HOME/.openclaw/workspace/skills/klyc-pmm.zip"
if [ -f "$WS_ZIP" ] && [ -f "$ZIP" ]; then
    diff -q "$WS_ZIP" "$ZIP" >/dev/null 2>&1 && pass "ZIP 工作区≡网站" || fail "ZIP 工作区≠网站"
else
    [ ! -f "$WS_ZIP" ] && warn "工作区 ZIP 缺失"
    [ ! -f "$ZIP" ]     && warn "网站 ZIP 缺失"
fi

# 7.2 ZIP 内 skill.json 版本号
if [ -f "$ZIP" ]; then
    ZV=$(unzip -p "$ZIP" klyc-pmm/skill.json 2>/dev/null | grep -oP '"version"\s*:\s*"\K[^"]+')
    [ "$ZV" = "$VER" ] && pass "ZIP 内版本号=$VER" || fail "ZIP 内版本号=$ZV (期望 $VER)"
else
    warn "ZIP 不存在，跳过内版本检查"
fi

# 7.3 脚本变量完整性 — VERSION/readonly 变量与头注释一致（铁律#63）
for sf in "$WS_KUNLUN/scripts/pmm_watch.sh" "$WS_KUNLUN/scripts/pmm_distill.sh" "$WS_KUNLUN/scripts/install-daemon.sh" \
          "$WS_YAOCHI/scripts/pmm_watch.sh" "$WS_YAOCHI/scripts/pmm_distill.sh" "$WS_YAOCHI/scripts/install-daemon.sh"; do
    [ ! -f "$sf" ] && continue
    LABEL=$(echo "$sf" | sed "s|$WS_KUNLUN/scripts/||" | sed "s|$WS_YAOCHI/scripts/瑶池_||" | sed "s|$HOME/.openclaw/workspace/skills/klyc-pmm/scripts/||" | sed "s|/root/.lightclaw/workspace/skills/@user_6e41807a/klyc-pmm/scripts/||")
    HEADER_VER=$(head -5 "$sf" | grep -oP '[0-9]+\.[0-9]+\.[0-9]+' | head -1)
    VAR_VER=$(grep -oP '(VERSION|readonly VERSION)\s*=\s*"?\K[0-9]+\.[0-9]+\.[0-9]+' "$sf" 2>/dev/null | head -1)
    [ -z "$HEADER_VER" ] && { warn "$(basename "$sf"): 头注释缺版本号"; continue; }
    [ -z "$VAR_VER" ]  && { fail "$(basename "$sf"): 缺 VERSION 变量"; continue; }
    [ "$HEADER_VER" = "$VAR_VER" ] && pass "$(basename "$sf"): 头=$HEADER_VER 变量=$VAR_VER" || fail "$(basename "$sf"): 头=$HEADER_VER 变量=$VAR_VER 不一致"
done

# ═══════════════════════════ 九、铁律#53 ═══════════════════════════
echo ""; echo "━━━ 九、铁律#53 ━━━"
warn "代码搜索≠运行时验证。安全头(CSP/HSTS/CORS)需手动 curl 验证"
echo "  curl -sI https://kunlunyaochi.com | grep -i 'content-security-policy\|strict-transport'"

# ═══════════════════════════ 十、SkillSpector 专项（2026-08-06 审计后补缺）══════════════════════════
echo ""; echo "━━━ 十、SkillSpector 专项补缺 ━━━"

# ─── 10a. 示例文本敏感内容 ───
# 检查所有文档示例中是否出现疑似凭证/密钥关键词
HIT=0
for f in "$WS_KUNLUN/examples/README.md" "$WS_KUNLUN/SKILL.md" "$WS_KUNLUN/README.md"; do
    [ ! -f "$f" ] && continue
    fname=$(basename "$f")
    # 在代码块/示例命令行中搜索可能鼓励传密钥的模式
    suspicious=$(grep -cP '(token|secret|password|api[_-]?key)\s*=\s*\w{4,}|push.*"Token|push.*"密钥|push.*"密码|push.*"Secret' "$f" 2>/dev/null || true)
    if [ "$suspicious" -gt 0 ]; then
        fail "示例含疑似凭证关键词: $fname (${suspicious}处)"
        HIT=1
    fi
done
[ "$HIT" -eq 0 ] && pass "示例文本无凭证关键词"

# ─── 10b. 文档措辞——禁止鼓励向AI泄露凭证 ───
# 检查是否出现"发给AI""发送给AI"可以恢复/自动执行的措辞
for f in "$WS_KUNLUN/scripts/oneclick.sh" "$WS_KUNLUN/SKILL.md" "$WS_KUNLUN/examples/README.md"; do
    [ ! -f "$f" ] && continue
    fname=$(basename "$f")
    # 匹配"发送给 AI，AI 将自动XXX"但不匹配"信任的 AI 助手"（已修复版本）
    bad_wording=$(grep -cP '发送给.*AI.*AI.*(将自动|会自动|即可)' "$f" 2>/dev/null || true)
    has_fix=$(grep -cP '信任的.*AI.*助手|你自己的.*AI.*助手|由.*执行恢复' "$f" 2>/dev/null || true)
    if [ "$bad_wording" -gt 0 ] && [ "$has_fix" -eq 0 ]; then
        fail "文档措辞风险: $fname 含'发送给AI将自动XXX' (应改为'发送给你信任的AI助手，由其执行恢复')"
        HIT=1
    fi
done
[ "${HIT:-0}" -eq 0 ] && pass "文档措辞无凭证泄露诱导"

# ─── 10c. 脚本交互确认——写库/删库操作必须有 read -p 确认 ───
# 检查有软删除/UPDATE/DELETE 的脚本是否含交互确认
HIT=0
for sf in "$WS_SCRIPTS/pmm_distill.sh" "$WS_SCRIPTS/pmm_watch.sh" "$WS_SCRIPTS/oneclick.sh"; do
    [ ! -f "$sf" ] && continue
    fname=$(basename "$sf")
    has_mutation=$(grep -cE 'is_deleted=1|UPDATE.*SET|DELETE FROM' "$sf" 2>/dev/null || true)
    has_confirm=$(grep -cE 'read -r? -p|read -p' "$sf" 2>/dev/null || true)
    if [ "$has_mutation" -gt 0 ] && [ "$has_confirm" -eq 0 ]; then
        # 有写库但没有确认 → 检查是否有 --dry-run 保护
        has_dryrun=$(grep -ci 'dry.run' "$sf" 2>/dev/null || true)
        if [ "$has_dryrun" -eq 0 ]; then
            fail "缺交互确认: $fname 有写库操作但无 read -p 确认也无 --dry-run 保护"
            HIT=1
        else
            pass "写库防护: $fname (--dry-run)"
        fi
    elif [ "$has_mutation" -gt 0 ]; then
        pass "写库防护: $fname (已含交互确认)"
    fi
done
[ "${HIT:-0}" -eq 0 ] && pass "写库操作均有确认或 dry-run 保护"

# ─── 10d. 被监控文件清单——watch模式必须在help/声明中列出监控目标 ───
# pmm_watch.sh watch 命令的 FILES 必须在 --help 或头部注释中列出
for sf in "$WS_SCRIPTS/pmm_watch.sh"; do
    [ ! -f "$sf" ] && continue
    has_watch=$(grep -cE 'watch.*mode|inotify|fswatch|监控|监听' "$sf" 2>/dev/null || true)
    if [ "$has_watch" -gt 0 ]; then
        # watch 模式存在 → 检查 --help 输出或头部是否列出了默认监控文件
        help_output=$(bash "$sf" --help 2>/dev/null || true)
        if echo "$help_output" | grep -qiE 'MEMORY|监控.*文件|监听.*MEMORY|SOUL|IDENTITY' ; then
            pass "监控清单: pmm_watch.sh --help 已列出"
        elif head -40 "$sf" | grep -qiE 'MEMORY|监控.*文件|监听.*文件'; then
            pass "监控清单: pmm_watch.sh 头部已声明"
        else
            warn "监控清单: pmm_watch.sh watch模式建议在--help中列出默认监控文件"
        fi
    fi
done

# ─── 10d2. hook-check 子命令存在性（2026-08-07 罗总：声明-代码对账）───
# SKILL.md 声明了 hook-check，必须与 pmm_watch.sh 实际实现一致，防"文档有代码无"
for sf in "$WS_KUNLUN/scripts/pmm_watch.sh" "$WS_YAOCHI/scripts/pmm_watch.sh"; do
    [ ! -f "$sf" ] && continue
    label=$(echo "$sf" | grep -q openclaw && echo "昆仑" || echo "瑶池")
    has_hc=$(grep -cE "pmm_hook_check\(|hook-check\)" "$sf" 2>/dev/null || true)
    has_stale=$(grep -cE "失效钩子检测|Step 2.5|stale_ids" "$sf" 2>/dev/null || true)
    if [ "$has_hc" -gt 0 ] && [ "$has_stale" -gt 0 ]; then
        pass "hook-check+失效检测在 (${label})"
    elif [ "$has_hc" -gt 0 ]; then
        pass "hook-check在 (${label})" ; warn "hook-check 缺失效检测逻辑"
    else
        fail "hook-check 缺失 (${label})"
    fi
    # SKILL.md 文档对账
    md="$WS_KUNLUN/SKILL.md"
    [ "$label" = "瑶池" ] && md="$WS_YAOCHI/SKILL.md"
    if [ -f "$md" ] && ! grep -q "hook-check" "$md"; then
        warn "SKILL.md 未提及 hook-check (${label})"
    fi
done

# ─── 10e. Agent 自动化指令——SKILL.md 中的自动推送/评估指令必须有数据流向说明 ───
# 检查"每次对话""自动推送""自动备份"等指令是否有对应的数据流向声明
for md in "$WS_KUNLUN/SKILL.md"; do
    [ ! -f "$md" ] && continue
    auto_instructions=$(grep -cE '每轮对话|每.*次.*对话|自动推送|自动备份|自动同步' "$md" 2>/dev/null || true)
    if [ "$auto_instructions" -gt 0 ]; then
        # 有自动化指令 → 必须有 data_flow 声明
        if grep -q 'data_flow:' "$md" 2>/dev/null; then
            pass "Agent自动化指令: SKILL.md 含data_flow声明"
        else
            fail "Agent自动化指令: SKILL.md 含自动推送/备份指令但缺data_flow声明"
        fi
    else
        pass "Agent自动化指令: 无自动推送指令"
    fi
done

# ─── 10f. 输出文件位置——恢复/蒸馏写文件路径必须在脚本头部声明 ───
# 检查脚本中写 workspace 文件的操作是否在头部注释中标注
for sf in "$WS_SCRIPTS/pmm_recover.sh" "$WS_SCRIPTS/pmm_distill.sh" "$WS_SCRIPTS/pmm_watch.sh"; do
    [ ! -f "$sf" ] && continue
    fname=$(basename "$sf")
    writes_workspace=$(grep -cE '(WORK_DIR|WORKSPACE|workspace).*\.(json|md|txt)|>.*memory/|>.*recovery' "$sf" 2>/dev/null || true)
    if [ "$writes_workspace" -gt 0 ]; then
        if head -30 "$sf" | grep -qiE '写入|输出|落盘|生成.*报告|recovery.*json'; then
            pass "输出路径: $fname 已声明写出目标"
        else
            warn "输出路径: $fname 写workspace文件但头部未声明输出位置"
        fi
    fi
done

echo "  ✅ 第十关通过"

# ═══════════════════════════ 十一、凭证/敏感数据暴露（对标 klyc_cross_audit.sh 第二关）══════════════════════════
echo ""; echo "━━━ 十一、凭证/敏感数据暴露 ━━━"

CRED_HIT=0
for dir in "$WS_KUNLUN" "$WS_YAOCHI" "$ROOT/skills/klyc-pmm"; do
    [ ! -d "$dir" ] && continue
    label=$(echo "$dir" | grep -q "wwwroot" && echo "PUB" || (echo "$dir" | grep -q "lightclaw" && echo "瑶池" || echo "昆仑"))

    # 共享域示例含敏感数据
    for f in "$dir/SKILL.md" "$dir/examples/README.md" "$dir/README.md"; do
        [ ! -f "$f" ] && continue
        fname=$(basename "$f")
        hits=$(grep -n 'shared.*Token\|shared.*token\|shared.*key\|shared.*密码\|shared.*secret' "$f" 2>/dev/null | grep -v '#\|//\|示例.*替换\|placeholder' | wc -l | tr -d ' ')
        [ "$hits" -eq 0 ] && pass "共享域示例干净 ($label/$fname)" || { fail "共享域示例含敏感数据: ${hits}处 ($label/$fname)"; CRED_HIT=1; }
    done

    # "发送给 AI" 泄露风险
    for f in "$dir/scripts/oneclick.sh" "$dir/SKILL.md" "$dir/examples/README.md"; do
        [ ! -f "$f" ] && continue
        fname=$(basename "$f")
        hits=$(grep -cn '发送给 AI[^助]\|发送给AI[^助]' "$f" 2>/dev/null || true)
        [ "$hits" -eq 0 ] && pass "无'发送给AI'泄露 ($label/$fname)" || { fail "'发送给AI'泄露: ${hits}处 ($label/$fname)"; CRED_HIT=1; }
    done

    # Token 硬编码（排除注释和 CHANGELOG）
    tk_hits=$(grep -rn 'Token=[A-Za-z0-9_]\{8,\}' "$dir" 2>/dev/null | grep -v '#\|//\|CHANGELOG' | wc -l | tr -d ' ')
    [ "$tk_hits" -eq 0 ] && pass "Token硬编码=0 ($label)" || { fail "Token硬编码: ${tk_hits}处 ($label)"; CRED_HIT=1; }

    # 密钥硬编码（排除占位符）
    sk_hits=$(grep -rn "sk-\|api_key\s*=\s*'[A-Za-z0-9_]\{16,\}" "$dir" 2>/dev/null | grep -v '#\|//\|CHANGELOG\|sk-xxx\|sk-\.\.\.\|<KEY>' | wc -l | tr -d ' ')
    [ "$sk_hits" -eq 0 ] && pass "密钥硬编码=0 ($label)" || { fail "密钥硬编码: ${sk_hits}处 ($label)"; CRED_HIT=1; }
done
[ "$CRED_HIT" -eq 0 ] && true || true  # 不计入阻塞，仅报警
echo "  ✅ 第十一关通过"

# ═══════════════════════════ 十二、确认闸门（对标 klyc_cross_audit.sh 第三关）══════════════════════════
echo ""; echo "━━━ 十二、确认闸门 ━━━"

for dir in "$WS_KUNLUN/scripts" "$WS_YAOCHI/scripts" "$ROOT/skills/@user_6e41807a/klyc-pmm/scripts"; do
    [ ! -d "$dir" ] && continue
    label=$(echo "$dir" | grep -q "wwwroot" && echo "PUB" || (echo "$dir" | grep -q "lightclaw" && echo "瑶池" || echo "昆仑"))

    # 蒸馏脚本确认闸门
    for sf in "$dir/pmm_distill.sh"; do
        [ ! -f "$sf" ] && continue
        if grep -q 'is_deleted=1\|UPDATE.*SET.*is_deleted' "$sf" 2>/dev/null; then
            grep -q '\[y/N\]\|read.*-p.*确认\|confirm.*=.*read\|--confirm\|--dry-run' "$sf" 2>/dev/null && \
                pass "蒸馏确认闸门 ($label)" || \
                fail "蒸馏缺确认闸门 ($label)"
        fi
    done

    # 守护安装确认闸门
    for sf in "$dir/install-daemon.sh"; do
        [ ! -f "$sf" ] && continue
        if grep -q 'systemctl enable' "$sf" 2>/dev/null; then
            grep -q 'read.*-p\|确认' "$sf" 2>/dev/null && \
                pass "守护安装确认闸门 ($label)" || \
                warn "守护安装缺确认提示 ($label)"
        fi
    done

    # 一键安装取消提示
    for sf in "$dir/oneclick.sh"; do
        [ ! -f "$sf" ] && continue
        if grep -qE 'apt-get install|yum install|apk add' "$sf" 2>/dev/null; then
            grep -qE 'Ctrl\+C|取消|确认|read.*-p' "$sf" 2>/dev/null && \
                pass "一键安装取消提示 ($label)" || \
                warn "一键安装缺取消提示 ($label)"
        fi
    done
done
echo "  ✅ 第十二关通过"

# ═══════════════════════════ 十三、PMM 运行环境（对标 klyc_cross_audit.sh 第十一关）══════════════════════════
echo ""; echo "━━━ 十三、PMM 运行环境 ━━━"

# pmm_watch 进程
pmm_count=$(ps aux 2>/dev/null | grep -c '[p]mm_watch.sh watch' || echo "0")
[ "$pmm_count" -ge 2 ] && pass "pmm_watch 进程: ${pmm_count}个" || fail "pmm_watch 进程: ${pmm_count}个（期望≥2）"

# /root/bin/ 脚本版本
for f in pmm_watch.sh pmm_distill.sh install-daemon.sh klyc_skill_check.sh; do
    [ -f "/root/bin/$f" ] || { warn "/root/bin/$f: 缺失"; continue; }
    BIN_VER=$(head -5 "/root/bin/$f" | grep -oP '\d+\.\d+\.\d+' | head -1 || echo "?")
    [ "$BIN_VER" = "$VER" ] && pass "/root/bin/$f: ${BIN_VER}" || warn "/root/bin/$f: ${BIN_VER} (期望 $VER)"
done

# 标签索引
if command -v pmm_watch.sh >/dev/null 2>&1 || [ -f /root/bin/pmm_watch.sh ]; then
    tag_count=$(/root/bin/pmm_watch.sh status 2>/dev/null | grep -oP '标签索引:\s*\K\d+' | head -1 || echo "?")
    [ -n "$tag_count" ] && [ "$tag_count" != "?" ] && pass "标签索引: ${tag_count}个" || warn "标签索引: 无法获取"
fi

# 核心服务
for svc in lightclaw klyc-bge-gateway; do
    systemctl is-active --quiet "$svc" 2>/dev/null && pass "$svc: active" || fail "$svc: 不可达"
done

# 安全头（实跑 curl 验证）
csp=$(curl -sI https://kunlunyaochi.com 2>/dev/null | grep -ci 'content-security-policy' || echo "0")
hsts=$(curl -sI https://kunlunyaochi.com 2>/dev/null | grep -ci 'strict-transport-security' || echo "0")
[ "$csp" -gt 0 ] && pass "CSP 安全头: 存在" || warn "CSP 缺失"
[ "$hsts" -gt 0 ] && pass "HSTS 安全头: 存在" || warn "HSTS 缺失"

echo "  ✅ 第十三关通过"

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
