#!/usr/bin/env bash
# process_job.sh - 单岗处理：书签 / 读JD / 发消息（可复用 lease，落实 R6/R8）
#
# 用法（自管模式，脚本自己开/关 tab）:
#   bash scripts/process_job.sh --url <url> [--bookmark] [--read-jd [--out f]] [--send --msg f] [--keep]
#
# 用法（复用模式，由调用方持有 lease/tab，批量连续不重开）:
#   bash scripts/process_job.sh --lease <id> --tab <id> --url <url> [--bookmark] [--read-jd ...] [--send ...]
#
# 后端：经 common.sh 选择 BrowserDriver（默认 brs，唯一 sanctioned）。hosted 短路（bz_emit_plan）仅历史 `_deprecated/codex` 会触发，已被 R12 在 common.sh 拒绝加载。
#       生成可粘贴进外部 Agent 的步骤提示词，不实际驱动浏览器。
#
# 红线:
#   - 发消息需 AUTHORIZED=1，否则拒绝 (exit 4)
#   - 撞墙 exit 3 停手
#   - 仅真实光标 (ui click/type)，绝不合成点击
#   - 选择器见 references/boss_selectors.md（待校准项首次须复核）
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# SCRIPT_DIR_W 改为在 source common.sh 后用 to_win_path 计算（见下方），统一去除对 cygpath 的散落依赖。

# ---- 统一授权门控（最早执行，必须在 source common.sh / 加载后端之前）----
# F9/F10: 书签与发送均属「改账号状态动作」，需 AUTHORIZED=1 才放行。提到最前可保证
# 本地 brs（后端加载即探测 brs.js）在未授权时 **exit 4**，
# 不会因后端缺失先报 exit 1 而掩盖授权语义。
SEND_RAW=0; BOOKMARK_RAW=0
for _a in "$@"; do
  [ "$_a" = "--send" ] && SEND_RAW=1
  [ "$_a" = "--bookmark" ] && BOOKMARK_RAW=1
done
AUTHORIZED="${AUTHORIZED:-0}"
if { [ "$SEND_RAW" -eq 1 ] || [ "$BOOKMARK_RAW" -eq 1 ]; } && [ "$AUTHORIZED" != "1" ]; then
  echo "FAIL_LOUD: 未授权，禁止生成/执行书签或发送计划 (R5 每岗授权)。设置 AUTHORIZED=1 后重试。" >&2
  exit 4
fi

source "$SCRIPT_DIR/common.sh"

# Windows Git Bash 下 win-native python 收不到 POSIX 路径（MSYS 把 C:/Users 错转成 C:\c\Users）。
# 改用 to_win_path（统一替代 cygpath -w，缺失 cygpath 也不再静默回退 POSIX 路径）。
SCRIPT_DIR_W="$(to_win_path "$SCRIPT_DIR")"

# hosted 模式：不实际驱动，生成外部 Agent 步骤提示词后退出
# （必须在参数解析前执行，以保留原始 argv 传给 bz_emit_plan）
if backend_is_hosted; then bz_emit_plan "$@"; exit 0; fi

BOOKMARK=0; READJD=0; SEND=0; KEEP=0
URL=""; LEASE=""; TAB=""; OUT_JSON="${WORK_DIR:-.work}/recruiter_jd.json"; MSG=""
SELF_MANAGED=1

while [ $# -gt 0 ]; do
  case "$1" in
    --url)   URL="$2"; shift 2;;
    --lease) LEASE="$2"; SELF_MANAGED=0; shift 2;;
    --tab)   TAB="$2"; SELF_MANAGED=0; shift 2;;
    --bookmark) BOOKMARK=1; shift;;
    --read-jd)  READJD=1; shift;;
    --out)   OUT_JSON="$2"; shift 2;;
    --send)  SEND=1; shift;;
    --msg)   MSG="$2"; shift 2;;
    --keep)  KEEP=1; shift;;
    *) echo "未知参数: $1" >&2; exit 1;;
  esac
done

[ -z "$URL" ] && { echo "用法: bash scripts/process_job.sh --url <url> [--bookmark] [--read-jd] [--send --msg f]" >&2; exit 1; }

fail_loud_if_down

# ---- 自管模式：开 lease + tab ----
if [ "$SELF_MANAGED" -eq 1 ]; then
  cooldown "${BOOKMARK_COOLDOWN:-${ACTION_INTERVAL_SECONDS:-5}}"
  bz_browse_start "$URL" enhanced || { echo "FAIL_LOUD: browse-start 失败" >&2; exit 1; }
  LEASE="$BZ_LEASE"; TAB="$BZ_TAB"
  cleanup(){ [ "$KEEP" -eq 0 ] && bz_browse_end "$LEASE" || true; }
  trap cleanup EXIT
fi

# ---- 复用模式：同 tab 导航到目标岗（自管模式 browse-start 已带 URL）----
if [ "$SELF_MANAGED" -eq 0 ]; then
  cooldown "${ACTION_INTERVAL_SECONDS:-5}"
  bz_browse_nav "$LEASE" "$TAB" "$URL" >/dev/null || { echo "FAIL_LOUD: browse-nav 失败" >&2; exit 1; }
  sleep 3
fi

# ---- 读取页面，撞墙检查 ----
HTML=$(bz_browse_html "$LEASE" "$TAB" 2>&1)
verify_wall "$HTML"

# ---- 书签（点「感兴趣」）----
if [ "$BOOKMARK" -eq 1 ]; then
  bump_daily_cap   # R3 日限额（改状态动作）
  [ "$SELF_MANAGED" -eq 0 ] && cooldown "${BOOKMARK_COOLDOWN:-${ACTION_INTERVAL_SECONDS:-5}}"
  WF=$(bz_ui "$TAB" wait-for --selector ".btn-interest" 2>&1) || true
  echo "$WF" | grep -qi "verify\|验证码" && { echo "FAIL_LOUD: 撞验证墙"; exit 3; }
  bz_ui "$TAB" click --selector ".btn-interest" 2>&1 || { echo "[warn] 选择器未命中(.btn-interest)，请人工核对" >&2; }
  HTML2=$(bz_browse_html "$LEASE" "$TAB" 2>&1)
  if echo "$HTML2" | grep -q "取消感兴趣"; then
    echo "[ok] 书签成功 (按钮已变 取消感兴趣)"
    set_login_state logged_in
  else
    echo "[warn] 未确认书签成功, 请人工核对截图"
  fi
fi

# ---- 读 JD / 招聘方（真实招聘方来自 .job-boss-info .name，非 user-nav）----
if [ "$READJD" -eq 1 ]; then
  mkdir -p "$(dirname "$OUT_JSON")"
  # 防空串（Item1 / V5 已治）：等 JD 正文「job-sec-text」渲染就绪再抓取，
  # 避免面板未渲染完就提取到空串（bz_wait 此前定义却未接线，属回归风险，现落实）。
  bz_wait "$LEASE" "$TAB" "job-sec-text" || true
  HTML=$(bz_browse_html "$LEASE" "$TAB" 2>&1)
  verify_wall "$HTML"
  PARSED="${WORK_DIR:-.work}/.parse_job.tmp"; mkdir -p "$(dirname "$PARSED")"
  # 用稳健的 DOM 解析（parse_job.py）替换脆弱正则；HTML 经 stdin 传入
  "$PYTHON" "$SCRIPT_DIR_W/parse_job.py" --url "$URL" >"$PARSED" <<<"$HTML" \
    || { echo "FAIL_LOUD: parse_job.py 解析 JD 失败" >&2; rm -f "$PARSED"; exit 1; }
  # 单 dict 包成单元素列表写入（满足 audit_icebreaker.py 的「列表」契约，见 C1）
  "$PYTHON" - "$OUT_JSON" "$PARSED" <<'PY'
import sys, json
out, src = sys.argv[1], sys.argv[2]
d = json.load(open(src, encoding="utf-8"))
if isinstance(d, dict):
    d = [d]
json.dump(d, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("OK ->", out)
PY
  rm -f "$PARSED" || true
fi

# ---- 发消息（授权门控，真实光标）----
if [ "$SEND" -eq 1 ]; then
  [ "${AUTHORIZED:-0}" = "1" ] || { echo "FAIL_LOUD: 未授权, 禁止发送 (需 AUTHORIZED=1)" >&2; exit 4; }
  [ -z "$MSG" ] && { echo "FAIL_LOUD: 缺少 --msg 消息文件" >&2; exit 1; }
  [ -f "$MSG" ] || { echo "FAIL_LOUD: 消息文件不存在: $MSG" >&2; exit 1; }
  TEXT=$(cat "$MSG")
  # 防御性拦截：若消息文件首行为「公司名 招聘方名[女士/先生/老师]」标题行
  # （非正文，通常是拆分话术时误写入的对端标识），剥离首行只发正文。
  # 2026-07-24 事故根因：--msg 文件被原样键入，标题行随之发出。
  TEXT=$("$PYTHON" "$SCRIPT_DIR_W/strip_title.py" <<<"$TEXT")
  bump_daily_cap   # R3 日限额（改状态动作）
  cooldown "${SEND_COOLDOWN:-${ACTION_INTERVAL_SECONDS:-20}}"
  # 选择器为 2026-07-20 实战校准值（见 boss_selectors.md 三）
  # 岗位关闭（无 .btn-startchat 且页面含「职位已关闭」）→ 跳过不算撞墙
  if echo "$HTML" | grep -q "职位已关闭"; then
    echo "[skip] 该岗位已关闭，跳过发送（请在岗位库标记「岗位关闭」）"; exit 6
  fi
  WF=$(bz_ui "$TAB" wait-for --selector ".btn-startchat" 2>&1) || true
  echo "$WF" | grep -qi "verify\|验证码" && { echo "FAIL_LOUD: 撞验证墙"; exit 3; }
  bz_ui "$TAB" click --selector ".btn-startchat" 2>&1 || { echo "[warn] 选择器未命中(.btn-startchat)，请人工核对" >&2; }
  sleep 3
  # 输入框：聊天弹窗为 #chat-input(contenteditable)，旧版为 textarea.input-area，依次尝试
  if ! bz_ui "$TAB" click --selector "#chat-input" >/dev/null 2>&1; then
    bz_ui "$TAB" click --selector "textarea.input-area" 2>&1 || { echo "[warn] 输入框未命中(#chat-input / textarea.input-area)" >&2; }
  fi
  bz_ui "$TAB" type --text "$TEXT" 2>&1
  sleep 1
  if ! bz_ui "$TAB" click --selector ".btn-send" >/dev/null 2>&1; then
    bz_ui "$TAB" click --selector ".send-message" 2>&1 || { echo "[warn] 发送按钮未命中(.btn-send / .send-message)" >&2; }
  fi
  sleep 3
  HTML3=$(bz_browse_html "$LEASE" "$TAB" 2>&1)
  # 软限流（操作频繁提示）：命中即指数退避拉长间隔（rate_backoff 此前定义却未接线，现落实；R11 软限流行）
  echo "$HTML3" | grep -q "操作频繁" && { rate_backoff; echo "[warn] 检测到「操作频繁」, 已指数退避拉长间隔" >&2; }
  SNIPPET=$("$PYTHON" -c "import sys,re;d=sys.stdin.buffer.read().decode('utf-8','ignore');print(re.sub(r'\s+','',d)[:20])" <<<"$TEXT")   # 去所有空白取前20字符做校验（避免换行/空格致匹配失败，见 R3076 误判 UNKNOWN）
  # 严格送达判定：编辑框已清空(草稿不残留) 且 页面消息区含话术前缀（含 [送达] 更佳）
  # 注意：不能「管道 + heredoc」同喂 stdin（heredoc 抢占 stdin 致 SIGPIPE/141），改走临时文件
  HTML_TMP="${WORK_DIR:-.work}/.verify_html3.tmp"; mkdir -p "$(dirname "$HTML_TMP")"; printf '%s' "$HTML3" > "$HTML_TMP"
  VERDICT=$("$PYTHON" - "$HTML_TMP" "$SNIPPET" <<'PY'
import sys, re
html = open(sys.argv[1], encoding="utf-8", errors="ignore").read(); snip = sys.argv[2]
html_nows = re.sub(r'\s+', '', html)          # 去所有空白后比对，规避换行/空格差异
m = re.search(r'id="chat-input"[^>]*>(.*?)</div>', html, re.S)
editor = re.sub(r'\s+', '', m.group(1)) if m else ""
in_editor = snip in editor
in_page = snip in html_nows
delivered = 'status-delivery' in html
if in_page and not in_editor: print("SENT" + ("_DELIVERED" if delivered else ""))
elif in_editor: print("DRAFT_ONLY")
else: print("UNKNOWN")
PY
)
  rm -f "$HTML_TMP" || true
  case "$VERDICT" in
    SENT_DELIVERED)
      echo "[ok] 消息已发送并送达 ([送达] 标记确认)"
      set_login_state logged_in;;
    SENT)
      echo "[ok] 消息已发送 (编辑框已清空, 消息区含话术)"
      set_login_state logged_in;;
    DRAFT_ONLY)
      echo "FAIL_LOUD: 话术仍在输入框草稿态，未发送成功，请人工核对" >&2; exit 7;;
    *)
      # 失败驱动：发送未确认时按需核验是否登录态失效（命中登录页→置 logged_out+exit 8）
      check_logged_in "$HTML3"
      echo "[warn] 未确认发送, 请人工核对截图";;
  esac
fi
