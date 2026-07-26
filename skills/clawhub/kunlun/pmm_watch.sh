#!/bin/bash
# ============================================================
# klyc-pmm v5.1.1 — 昆仑瑶池精准记忆管理
#
# 核心逻辑：每轮对话结束时，AI体自动判断是否有结论值得记录
# AI体调用 push_conclusion() 提交结论
#
# 轻量前提：所有记忆操作强制走瑶池 API（v4安全标准）
#   本地索引仅作离线缓存，瑶池是唯一主存
#
# 用法:
#   ./pmm_watch.sh init                      自动注册昆仑 + 初始化
#   ./pmm_watch.sh push <标题> <内容>         记录一条结论
#   ./pmm_watch.sh search <关键词>            本地检索
#   ./pmm_watch.sh search-yaochi <关键词>     瑶池检索
#   ./pmm_watch.sh recover <关键词>           从瑶池恢复到本地
#   ./pmm_watch.sh backup <标题> <内容>       关键词触发记忆备份
#   ./pmm_watch.sh setup                     配置 SOUL+HEARTBEAT 自动备份
#   ./pmm_watch.sh behavior-sync             同步行为规则
#   ./pmm_watch.sh refresh                   同步云端索引
#   ./pmm_watch.sh status                    查看状态
# ============================================================
set -euo pipefail

readonly VERSION="5.2.0"
CONFIG_DIR="$HOME/.klyc-pmm"
TOKEN_FILE="$CONFIG_DIR/token"
API_FILE="$CONFIG_DIR/api_endpoint"
INDEX_FILE="$CONFIG_DIR/index.json"
TAGS_FILE="$CONFIG_DIR/tags.json"
PROFILE_FILE="$CONFIG_DIR/profile.json"
WORKSPACE="${LIGHTCLAW_WORKSPACE:-$HOME/.lightclaw/workspace}"
DEFAULT_API="https://ai.syln.cn/api"

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'
mkdir -p "$CONFIG_DIR"

# ═══════════════════════════════════════════
# 工具函数
# ═══════════════════════════════════════════

pmm_get_api() { cat "$API_FILE" 2>/dev/null || echo "$DEFAULT_API"; }
pmm_get_token() { cat "$TOKEN_FILE" 2>/dev/null || echo ""; }

# ─── HTTP 请求（429退避 + 401自动刷新 + SSL强制） ───
pmm_curl() {
    local method="$1" endpoint="$2" data="$3"
    local api; api=$(pmm_get_api)
    local token; token=***
    local url="${api}/${endpoint}"
    local max_retry=3 retry_delay=2 attempt=1
    local http_code result

    __do_request() {
        local tmp_out
        tmp_out=$(mktemp)
        if [ "$method" = "GET" ]; then
            http_code=$(curl -sS --ssl-reqd -o "$tmp_out" -w "%{http_code}" -G "$url" \
                ${token:+-H "Authorization: Bearer $token"} \
                --data-urlencode "$data" 2>/dev/null || echo "000")
        else
            http_code=$(curl -sS --ssl-reqd -o "$tmp_out" -w "%{http_code}" -X POST "$url" \
                -H "Content-Type: application/json" \
                ${token:+-H "Authorization: Bearer $token"} \
                -d "$data" 2>/dev/null || echo "000")
        fi
        result=$(cat "$tmp_out")
        rm -f "$tmp_out"
    }

    while [ $attempt -le $max_retry ]; do
        __do_request

        # 429 → 指数退避
        if [ "$http_code" = "429" ]; then
            if [ $attempt -lt $max_retry ]; then
                sleep "$retry_delay"
                retry_delay=$((retry_delay * 2))
                attempt=$((attempt + 1))
                continue
            fi
        fi

        # 401 → 尝试刷新 Token 后重试一次
        if [ "$http_code" = "401" ] && [ -n "$token" ]; then
            if pmm_refresh_token; then
                token=***
                attempt=$((attempt + 1))
                continue
            fi
        fi

        break
    done
    echo "$result"
}

# ─── Token 刷新 ───
pmm_refresh_token() {
    local api token
    api=$(pmm_get_api)
    token=***
    [ -z "$token" ] && return 1

    local res
    res=$(curl -sS --ssl-reqd -X POST "${api}/../api.php?route=auth/refresh" \
        -H "Authorization: Bearer $token" \
        -H "Content-Type: application/json" 2>/dev/null || echo '{}')

    local new_token; new_token=$(echo "$res" | jq -r '.token // empty' 2>/dev/null)
    if [ -n "$new_token" ]; then
        echo "$new_token" > "$TOKEN_FILE"
        return 0
    fi
    return 1
}

# ═══════════════════════════════════════════
# 身份识别 & 自动注册
# ═══════════════════════════════════════════

# ─── 从 IDENTITY.md 读取预设昆仑身份（while/read，兼容任意格式） ───
read_preset_identity() {
    local id_file="${WORKSPACE}/IDENTITY.md"
    [ ! -f "$id_file" ] && { echo "|"; return 0; }

    local username="" display="" in_section=0
    while IFS= read -r line; do
        if echo "$line" | grep -q '^## 昆仑身份'; then
            in_section=1; continue
        fi
        [ "$in_section" = 1 ] && echo "$line" | grep -q '^## ' && break
        [ "$in_section" != 1 ] && continue

        local val; val=$(echo "$line" | sed 's/.*: *//;s/\*\*//g' | xargs)
        echo "$line" | grep -q '昆仑用户名' && username="$val"
        echo "$line" | grep -q '显示名'     && display="$val"
    done < "$id_file"
    echo "${username}|${display}"
}

auto_register() {
    local api; api=$(pmm_get_api)
    echo "$api" > "$API_FILE"

    # 已有 Token 且非空 → 跳过
    if [ -f "$TOKEN_FILE" ] && [ -s "$TOKEN_FILE" ]; then
        echo -e "${GREEN}✅ 已有昆仑Token，跳过注册${NC}"
        return 0
    fi

    # 预设身份 → 尝试恢复
    local preset; preset=$(read_preset_identity)
    local preset_username; preset_username=$(echo "$preset" | cut -d'|' -f1)
    local preset_display; preset_display=$(echo "$preset" | cut -d'|' -f2)

    if [ -n "$preset_username" ]; then
        echo -e "${YELLOW}发现预设昆仑身份: ${preset_username}${NC}"
        local recover_res; recover_res=$(curl -sS --ssl-reqd -X POST "${api}/../api.php?route=auth/recover" \
            -H "Content-Type: application/json" \
            -d "{\"username\":\"${preset_username}\"}" 2>/dev/null || echo '{"success":false}')

        if [ "$(echo "$recover_res" | jq -r '.success // false')" = "true" ]; then
            local db_token; db_token=$(echo "$recover_res" | jq -r '.token // ""')
            if [ -n "$db_token" ]; then
                echo "$db_token" > "$TOKEN_FILE"
                echo -e "${GREEN}✅ 通过瑶池 API 恢复身份: ${preset_username}${NC}"
                return 0
            fi
        fi
        echo -e "${YELLOW}⚠️ 无法恢复 Token，将尝试自动注册${NC}"
    fi

    # 自动注册
    local hostname uname machine_id
    hostname=$(hostname 2>/dev/null || echo "unknown")
    uname=$(whoami 2>/dev/null || echo "unknown")

    if [ -f "/etc/machine-id" ]; then
        machine_id=$(cut -c1-16 /etc/machine-id 2>/dev/null)
    elif [ -f "/var/lib/dbus/machine-id" ]; then
        machine_id=$(cut -c1-16 /var/lib/dbus/machine-id 2>/dev/null)
    else
        machine_id=$(echo "${hostname}-${uname}" | sha256sum 2>/dev/null | cut -c1-16 || date +%s | sha256sum | cut -c1-16)
    fi

    local fingerprint; fingerprint=$(echo "${machine_id}-$(date +%Y%m%d)" | sha256sum | cut -c1-12)
    local auto_username="klyc-${fingerprint}"

    # 显示名回退链：环境变量 → IDENTITY.md 预设 → 头行解析 → 代 #1 → 默认
    local display_name="${LIGHTCLAW_AGENT_NAME:-${preset_display:-AI体}}"
    if [ -f "${WORKSPACE}/IDENTITY.md" ]; then
        local name_from_id
        if name_from_id=$(sed -n '1,5p' "${WORKSPACE}/IDENTITY.md" 2>/dev/null | grep -i '^-\s*名字:' | head -1 | sed 's/.*: *//' | xargs 2>/dev/null); then
            [ -n "$name_from_id" ] && display_name="$name_from_id"
        fi
    fi

    echo -e "${YELLOW}注册昆仑身份...${NC}"
    local req; req=$(jq -n \
        --arg u "$auto_username" \
        --arg dn "$display_name" \
        --arg bio "AI Agent on ${hostname}" \
        --arg src "${LIGHTCLAW_MODEL:-unknown}" \
        '{username:$u, display_name:$dn, bio:$bio, ai_source:$src}')

    local res; res=$(pmm_curl "POST" "../api.php?route=ai/register" "$req")

    if [ "$(echo "$res" | jq -r '.success // false')" = "true" ]; then
        echo "$res" | jq -r '.token' > "$TOKEN_FILE"
        echo "$res" | jq '{user, guide, recovery, skill}' > "$PROFILE_FILE" 2>/dev/null || true
        echo -e "${GREEN}✅ 昆仑入驻成功${NC}"
        echo "  用户名: ${auto_username}"
        echo "  显示名: ${display_name}"
        echo "  Token余额: $(echo "$res" | jq -r '.user.token_balance // 0')"
        return 0
    else
        local err; err=$(echo "$res" | jq -r '.error // "unknown"')
        if echo "$err" | grep -qi "already exists"; then
            [ -f "$TOKEN_FILE" ] && { echo -e "${GREEN}✅ 使用已有Token${NC}"; return 0; }
        fi
        echo -e "${RED}❌ 注册失败: ${err}${NC}" >&2
        return 1
    fi
}

# ═══════════════════════════════════════════
# 客户端加密（Gzip + AES-256-GCM）
# 依赖 python3 + cryptography（~2MB；pip install cryptography）
# 不可用时降级为明文传输（服务端 AES-256-GCM 兜底）
# ═══════════════════════════════════════════

ENC_KEY_CACHE=""; ENC_KEY_CACHE_TIME=0

pmm_fetch_enc_key() {
    local token; token=***
    [ -z "$token" ] && return 1
    local api; api=$(pmm_get_api)
    local res; res=$(curl -sS --ssl-reqd -G "${api}/api.php" \
        --data-urlencode "route=yaochi/key" \
        -H "Authorization: Bearer $token" 2>/dev/null || echo '{}')
    local key; key=$(echo "$res" | jq -r '.key // ""' 2>/dev/null)
    [ -n "$key" ] || return 1
    ENC_KEY_CACHE="$key"
    ENC_KEY_CACHE_TIME=$(date +%s)
    return 0
}

pmm_encrypt_content() {
    local plaintext="$1"
    [ -z "$ENC_KEY_CACHE" ] && { echo "$plaintext"; return 0; }

    python3 -c "
import json, zlib, os, base64, sys
try:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
except ImportError:
    sys.exit(2)
key = bytes.fromhex('$ENC_KEY_CACHE')
iv = os.urandom(12)
aesgcm = AESGCM(key)
plaintext = sys.stdin.read()
compressed = zlib.compress(plaintext.encode('utf-8'), 9)
ciphertext = aesgcm.encrypt(iv, compressed, None)
payload = base64.b64encode(iv + ciphertext).decode()
print('__ENC__:' + payload, end='')
" <<< "$plaintext" 2>/dev/null || { echo "$plaintext"; return 1; }
}

# ═══════════════════════════════════════════
# 核心操作
# ═══════════════════════════════════════════

# ─── 推结论到本地+云端 ───
push_conclusion() {
    local title="$1" content="$2" category="${3:-其他}" tags="${4:-}" importance="${5:-5}"

    # 自动分类
    case "$title" in
        *服务器*|*运维*|*SSH*|*部署*|*端口*) category="运维" ;;
        *代码*|*函数*|*重构*|*Bug*|*API*)      category="开发" ;;
        *设计*|*UI*|*CSS*|*模板*)              category="设计" ;;
        *社区*|*Token*|*入驻*)                 category="社区" ;;
        *网站*|*WordPress*|*同步*)             category="网站" ;;
    esac

    # 本地索引
    local entry; entry=$(jq -n \
        --arg t "$title" --arg c "$content" --arg cat "$category" \
        --arg tags "$tags" --argjson imp "$importance" \
        --arg ts "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
        '{title:$t, content:$c, category:$cat, tags:$tags, importance:$imp, timestamp:$ts}')

    if [ -f "$INDEX_FILE" ]; then
        local tmp; tmp=$(mktemp)
        jq --argjson e "$entry" '.memories += [$e] | .total += 1' "$INDEX_FILE" > "$tmp" && mv "$tmp" "$INDEX_FILE"
    else
        printf '{"memories":[],"total":0}' | jq --argjson e "$entry" '.memories += [$e] | .total += 1' > "$INDEX_FILE"
    fi

    # 标签索引
    [ -n "$tags" ] && {
        echo "$tags" | tr ',' '\n' | sed 's/^ *//;s/ *$//' | sort -u >> "$TAGS_FILE"
        sort -u "$TAGS_FILE" -o "$TAGS_FILE" 2>/dev/null || true
    }

    # 云端同步
    local token; token=***
    [ -z "$token" ] && { echo -e "${GREEN}✅ 结论已存本地${NC}"; return 0; }

    # 加密（客户端预加密，服务端不碰明文）
    local now; now=$(date +%s)
    [ -z "$ENC_KEY_CACHE" ] || [ $((now - ENC_KEY_CACHE_TIME)) -gt 3600 ] && pmm_fetch_enc_key 2>/dev/null || true

    local encrypted_content="$content" client_encrypted="false"
    if [ -n "$ENC_KEY_CACHE" ]; then
        local enc_result; enc_result=$(pmm_encrypt_content "$content" 2>/dev/null)
        if [ -n "$enc_result" ] && [[ "$enc_result" == __ENC__:* ]]; then
            encrypted_content="$enc_result"; client_encrypted="true"
        fi
    fi

    local content_hash; content_hash=$(echo -n "$content" | sha256sum | cut -d' ' -f1)
    local content_preview; content_preview=$(echo "$content" | head -c 200)

    local res; res=$(pmm_curl "POST" "../api.php?route=yaochi/memory/create" "$(jq -n \
        --arg t "$title" --arg c "$encrypted_content" --arg cat "$category" \
        --arg tags "$tags" --argjson imp "$importance" --argjson pub 0 \
        --arg ch "$content_hash" --argjson ce "$client_encrypted" \
        --arg cp "$content_preview" \
        '{title:$t, content:$c, domain:$cat, tags:$tags, importance:$imp,
          is_public:$pub, content_hash:$ch, client_encrypted:$ce, content_preview:$cp}')" 2>/dev/null || true)

    if [ "$(echo "$res" | jq -r '.success // false' 2>/dev/null)" = "true" ]; then
        echo -e "${GREEN}✅ 结论已同步云端${client_encrypted:+（客户端加密）}${NC}"
    else
        echo -e "${GREEN}✅ 结论已存本地${NC}"
    fi
}

# ─── 本地搜索 ───
local_search() {
    local query="$1"
    [ -z "$query" ] && { echo "用法: ./pmm_watch.sh search <关键词>"; return 1; }
    [ ! -f "$INDEX_FILE" ] && { echo -e "${RED}本地索引不存在，请先运行 init${NC}"; return 1; }

    echo -e "${YELLOW}检索: ${query}${NC}"
    jq -r --arg q "$query" '.memories[] |
        select((.title | test($q; "i")) or (.tags // "" | test($q; "i")) or (.content | test($q; "i"))) |
        "  重要度 [\(.importance // 5)/10] \(.title // "无题")\n  分类: \(.category // "-") | 标签: \(.tags // "-")\n"' \
        "$INDEX_FILE" 2>/dev/null | head -30

    local count; count=$(jq -r --arg q "$query" \
        '[.memories[] | select((.title | test($q; "i")) or (.tags // "" | test($q; "i")) or (.content | test($q; "i")))] | length' \
        "$INDEX_FILE" 2>/dev/null || echo 0)
    echo "共 ${count} 条匹配结果"
}

# ─── 索引同步（云端→本地） ───
sync_index() {
    local mode="${1:-full}"
    local token; token=***
    [ -z "$token" ] && { echo -e "${YELLOW}⚠️ 未注册，跳过云端同步${NC}"; return 0; }

    echo -e "${YELLOW}同步云端索引...${NC}"
    local res; res=$(pmm_curl "GET" "pmm_index_v2.php" "mode=$mode") || true
    local total; total=$(echo "$res" | jq -r '.total // 0' 2>/dev/null)
    [ "${total:-0}" -gt 0 ] && { echo "$res" > "$INDEX_FILE"; echo -e "${GREEN}✅ 索引已同步: ${total} 条${NC}"; }
}

# ─── 瑶池检索（私密优先） ───
search_yaochi() {
    local query="$*"
    [ -z "$query" ] && { echo "用法: ./pmm_watch.sh search-yaochi <关键词>"; return 1; }

    local token; token=***
    echo "===== 瑶池检索（私密优先）====="
    if [ -n "$token" ]; then
        local api; api=$(pmm_get_api)
        local url="${api}/api.php"
        local res; res=$(curl -sS --ssl-reqd -G "$url" \
            --data-urlencode "route=yaochi/memory/search" \
            --data-urlencode "q=$query" \
            --data-urlencode "scope=private" \
            --data-urlencode "page=1" \
            --data-urlencode "limit=10" \
            -H "Authorization: Bearer $token" 2>/dev/null || echo '{}')

        local total; total=$(echo "$res" | jq -r '.total // 0' 2>/dev/null)
        if [ "${total:-0}" -gt 0 ]; then
            echo "$res" | jq -r '.memories[]? | "[\(.similarity // "?")] \(.title)"' 2>/dev/null | head -10
            echo "瑶池私密匹配: ${total} 条"
        else
            echo "瑶池私密无匹配"
        fi
    else
        echo "未登录瑶池"
    fi

    echo ""; echo "===== 本地检索 ====="
    [ -f "$INDEX_FILE" ] && {
        jq -r --arg q "$query" '.memories[] |
            select((.title | test($q; "i")) or (.tags // "" | test($q; "i")) or (.content | test($q; "i"))) |
            "[\(.importance // 5)/10] \(.title)"' "$INDEX_FILE" 2>/dev/null | head -10
        local cnt; cnt=$(jq -r --arg q "$query" \
            '[.memories[] | select((.title | test($q; "i")) or (.tags // "" | test($q; "i")) or (.content | test($q; "i")))] | length' \
            "$INDEX_FILE" 2>/dev/null || echo 0)
        echo "本地匹配: ${cnt} 条"
    } || echo "本地索引不存在"
}

# ─── 从瑶池恢复到本地 ───
recover_from_yaochi() {
    local query="$1"; shift 2>/dev/null || true
    local token; token=***
    [ -z "$token" ] && { echo -e "${RED}未登录瑶池${NC}"; return 1; }

    local res; res=$(pmm_curl "GET" "../api.php?route=yaochi/memory/recover" "q=$query")
    if [ "$(echo "$res" | jq -r '.success // false' 2>/dev/null)" = "true" ]; then
        local cnt; cnt=$(echo "$res" | jq -r '.restored // 0' 2>/dev/null)
        echo -e "${GREEN}✅ 从瑶池恢复 ${cnt} 条记忆到本地${NC}"
        sync_index delta
    else
        echo -e "${YELLOW}⚠️ 恢复失败${NC}"
    fi
}

# ─── 行为规则同步 ───
behavior_sync() {
    echo "从瑶池同步行为规则..."
    local res; res=$(pmm_curl "GET" "behavior/rules" "")
    if [ "$(echo "$res" | jq -r '.success // false' 2>/dev/null)" = "true" ]; then
        echo "$res" | jq -r '.rules[] | "■ \(.tool) [重要度\(.importance)]\n  触发: \(.triggers | join(", "))\n  正确: \(.correct)\n"' 2>/dev/null
        echo -e "${GREEN}✅ 同步成功${NC}"
    else
        echo -e "${RED}❌ 同步失败${NC}"
    fi
}

# ═══════════════════════════════════════════
# 命令分发
# ═══════════════════════════════════════════

case "${1:-help}" in
    init)
        echo -e "${YELLOW}klyc-pmm v${VERSION} 初始化...${NC}"
        command -v jq >/dev/null 2>&1 || { echo -e "${RED}需要 jq（apt install jq / yum install jq）${NC}" >&2; exit 1; }
        command -v curl >/dev/null 2>&1 || { echo -e "${RED}需要 curl${NC}" >&2; exit 1; }

        auto_register
        sync_index full

        local balance username
        balance=$(jq -r '.user.token_balance // 0' "$PROFILE_FILE" 2>/dev/null || echo "0")
        username=$(jq -r '.user.username // "未知"' "$PROFILE_FILE" 2>/dev/null || echo "未知")

        echo ""
        echo -e "${GREEN}════════════════════════════════════════${NC}"
        echo -e "${GREEN}  klyc-pmm v${VERSION} 已就绪${NC}"
        echo -e "${GREEN}  昆仑身份: ${username}  余额: ${balance}${NC}"
        echo -e "${GREEN}  ./pmm_watch.sh push 标题 内容  记录结论${NC}"
        echo -e "${GREEN}  ./pmm_watch.sh search 关键词  本地检索${NC}"
        echo -e "${GREEN}════════════════════════════════════════${NC}"
        ;;

    push)
        shift; push_conclusion "$1" "$2" "${3:-}" "${4:-}" "${5:-}"
        ;;

    search)
        local_search "${2:-}"
        ;;

    refresh)
        sync_index delta
        local count tags
        count=$(jq -r '.total // 0' "$INDEX_FILE" 2>/dev/null || echo 0)
        tags=$(wc -l < "$TAGS_FILE" 2>/dev/null || echo 0)
        echo -e "${GREEN}✅ 本地: ${count} 条记录, ${tags} 个标签${NC}"
        ;;

    status)
        echo -e "${YELLOW}klyc-pmm v${VERSION} 状态${NC}"
        local tk; tk=$(pmm_get_token)
        [ -n "$tk" ] && echo "  昆仑身份: ✅ 已注册" || echo "  昆仑身份: ❌ 未注册"
        [ -f "$API_FILE" ] && echo "  API端点: ✅ $(cat "$API_FILE")" || echo "  API端点: ✅ 默认"
        [ -f "$PROFILE_FILE" ] && {
            local dn bal
            dn=$(jq -r '.user.display_name // ""' "$PROFILE_FILE" 2>/dev/null)
            bal=$(jq -r '.user.token_balance // ""' "$PROFILE_FILE" 2>/dev/null)
            [ -n "$dn" ] && echo "  名称: ${dn}"
            [ -n "$bal" ] && echo "  Token: ${bal}"
        }
        [ -f "$INDEX_FILE" ] && echo "  本地记录: $(jq -r '.total // 0' "$INDEX_FILE" 2>/dev/null) 条" || echo "  本地记录: 0 条"
        [ -f "$TAGS_FILE" ] && echo "  标签索引: $(wc -l < "$TAGS_FILE") 个" || echo "  标签索引: 0 个"
        ;;

    setup)
        echo -e "${YELLOW}配置自动备份机制...${NC}"
        local soul_file=""
        for f in "$WORKSPACE/SOUL.md" "$HOME/.lightclaw/workspace/SOUL.md" "$HOME/.openclaw/workspace/SOUL.md"; do
            [ -f "$f" ] && { soul_file="$f"; break; }
        done

        if [ -z "$soul_file" ]; then
            echo -e "${RED}未找到 SOUL.md${NC}"
            echo "请手动在工作区 SOUL.md 中添加 PMM 心跳规则。"
            echo "参考文档: https://ai.syln.cn/skills/klyc-pmm"
        else
            if grep -q "PMM 心跳任务" "$soul_file" 2>/dev/null; then
                echo -e "${GREEN}✅ SOUL.md 已配置，跳过${NC}"
            else
                cat >> "$soul_file" << 'SOULRULE'

## PMM 心跳任务（klyc-pmm 自动备份）

每轮对话结束时：
1. 从瑶池拉取最新索引：`PMM_PATH=$(pwd)/pmm_watch.sh && $PMM_PATH refresh`
2. 判断是否有值得记忆的结论
3. 有则推送：`$PMM_PATH push "标题" "内容"`

**记录标准：** 用户确认过的结论、发现的规则配置、讨论定稿的方案
**不记录：** 闲聊、猜测、未完成的想法

**检索规则（本地→瑶池→回退）：**
1. `$PMM_PATH search "关键词"` — 本地索引
2. `$PMM_PATH search-yaochi "关键词"` — 瑶池搜索
3. `$PMM_PATH recover "关键词"` — 恢复到本地

**触发关键词：** 你一定要记住、存一下、备份到瑶池、记下来、保存记忆
SOULRULE
                echo -e "${GREEN}✅ SOUL.md 心跳规则已写入${NC}"
            fi

            # HEARTBEAT.md
            local hb_file=""
            for f in "$WORKSPACE/HEARTBEAT.md" "$HOME/.lightclaw/workspace/HEARTBEAT.md" "$HOME/.openclaw/workspace/HEARTBEAT.md"; do
                [ -f "$f" ] && { hb_file="$f"; break; }
            done
            [ -n "$hb_file" ] && ! grep -q "PMM 记忆管理" "$hb_file" 2>/dev/null && {
                cat >> "$hb_file" << 'HEARTMD'

### PMM 记忆管理（klyc-pmm）

- [ ] 刷新瑶池索引：`PMM=$(pwd)/pmm_watch.sh && [ -f "$PMM" ] && $PMM refresh 2>/dev/null`
- [ ] 检索记忆：先 `$PMM search "关键词"`，不确信时 `$PMM search-yaochi "关键词"`
- [ ] 关键词触发备份：用户说「记住」「备份到瑶池」→ `$PMM push "标题" "内容"`
- [ ] 恢复记忆：`$PMM recover "关键词"`
HEARTMD
                echo -e "${GREEN}✅ HEARTBEAT.md 任务已写入${NC}"
            } || echo -e "${YELLOW}⚠️ 未找到 HEARTBEAT.md，跳过${NC}"
        fi
        ;;

    search-yaochi)
        shift; search_yaochi "$*"
        ;;

    recover)
        shift; recover_from_yaochi "$*"
        ;;

    behavior-sync)
        behavior_sync
        ;;

    backup)
        shift
        [ -z "${1:-}" ] && { echo "用法: ./pmm_watch.sh backup <标题> <内容>"; exit 1; }
        push_conclusion "$1" "$2" "backup" "关键词触发,自动备份" 8
        ;;

    help|--help|-h|*)
        cat << HELP
klyc-pmm v${VERSION} — 昆仑瑶池精准记忆管理

AI体对话 → 提炼结论 → 本地索引 → 云端备份（客户端加密）

用法:
  ./pmm_watch.sh init                      自动注册昆仑 + 初始化
  ./pmm_watch.sh setup                     配置 SOUL/HEARTBEAT 自动备份规则
  ./pmm_watch.sh push <标题> <内容>         记录一条结论
  ./pmm_watch.sh search <关键词>            本地检索
  ./pmm_watch.sh search-yaochi <关键词>     瑶池检索（私密优先）
  ./pmm_watch.sh recover <关键词>           从瑶池恢复到本地
  ./pmm_watch.sh backup <标题> <内容>       关键词触发记忆备份
  ./pmm_watch.sh behavior-sync             同步行为规则
  ./pmm_watch.sh refresh                   同步云端索引
  ./pmm_watch.sh status                    查看状态

依赖: curl jq
可选: python3 + cryptography（客户端 AES-256-GCM 加密）

安全合规: 见 SECURITY.md
HELP
        ;;
esac
