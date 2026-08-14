#!/usr/bin/env bash
# common.sh - 被其他脚本 source，提供跨平台通用能力 + 浏览器后端(BrowserDriver)分发。
# 设计原则（遵循 OpenClaw 脚本约定）：用环境变量而非硬编码路径；fail loud；幂等。
#
# 浏览器后端抽象：
#   本 skill 不直接调用某个具体浏览器工具，而是对 references/browser_backend.md 定义的
#   BrowserDriver 契约（bz_* 函数）编程。BZC_BACKEND 选择后端（默认 brs），
#   common.sh 负责探测/加载后端并实现 fail-loud；缺失任何仿真人浏览器即拒绝启动。
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$SCRIPT_DIR/backends"

# node / python 可执行解析（兼容 Windows Git Bash 的 win-native 路径坑）
# 优先级：环境变量 PYTHON > PATH python3(Windows 须 win-native) > WorkBuddy 受管 python > 回退 python3
# Windows Git Bash 下严禁混用 WSL/MSYS 的 python（路径/编码错乱）；受管路径用 /c/... 形式。
# 解析 + 强制校验 PyYAML：选第一个「能 import yaml」的解释器；找不到即 FAIL_LOUD（不再静默选到缺 yaml 的解释器导致解析脚本确定性失败）。
# - 显式 PYTHON：严格遵从（不自动改选），缺 yaml 直接 FAIL_LOUD + 指引。
# - 未设 PYTHON：按 PATH(win-native) > 受管 3.13.12 > 受管 venv(envs/default, 预装 yaml) > python3 顺序挑第一个带 yaml 的。
resolve_python() {
  local explicit="${PYTHON:-}"
  local candidates=()
  if [ -n "$explicit" ]; then
    candidates=("$explicit")
  else
    local p
    if p=$(command -v python3 2>/dev/null) && [ -n "$p" ]; then
      case "$(uname -s 2>/dev/null)" in
        MINGW*|MSYS*|CYGWIN*)
          if "$p" -c 'import sys; sys.exit(0 if sys.platform.startswith(("win","cygwin")) else 1)' 2>/dev/null; then
            candidates+=("$p")
          fi ;;
        *) candidates+=("$p") ;;
      esac
    fi
    candidates+=("$HOME/.workbuddy/binaries/python/versions/3.13.12/python.exe")
    candidates+=("$HOME/.workbuddy/binaries/python/envs/default/Scripts/python.exe")
    candidates+=("$HOME/.workbuddy/binaries/python/envs/default/bin/python")
    candidates+=("$HOME/.workbuddy/binaries/python/envs/default/python")
    # 注意：非 Windows 平台已由上方 `*) candidates+=("$p")` 覆盖 PATH 上的 python3；
    # 此处**不再**无条件追加裸 "python3"——Windows 下该候选会重中 WSL/MSYS 解释器
    # （带 yaml 即被选），重蹈旧代码规避的「混用 WSL python」坑。
  fi
  local c
  for c in "${candidates[@]}"; do
    [ -z "$c" ] && continue
    if [ -x "$c" ] || command -v "$c" >/dev/null 2>&1; then
      if "$c" -c 'import yaml' >/dev/null 2>&1; then
        printf '%s' "$c"; return 0
      fi
    fi
  done
  echo "FAIL_LOUD: 找不到可用的「带 PyYAML 的 python」解释器（所有解析/筛选脚本的前提）。" >&2
  echo "  已候选: ${candidates[*]}" >&2
  if [ -n "$explicit" ]; then
    echo "  你显式设了 PYTHON=$explicit，但它 import yaml 失败。" >&2
  fi
  echo "  解决二选一:" >&2
  echo "    1) 给选中的 python 装 PyYAML:  $candidates pip install pyyaml" >&2
  echo "    2) 或设 PYTHON 指向已含 yaml 的解释器（推荐 WorkBuddy 受管 venv: $HOME/.workbuddy/binaries/python/envs/default）" >&2
  exit 1
}
PYTHON="$(resolve_python)"
NODE="${NODE:-node}"

# ---- POSIX -> Windows 原生路径（Git Bash 下给 win-native python 用）----
# 统一替代散落的 cygpath -w 调用：消除「cygpath 缺失 → 静默回退 POSIX 路径 → win-python 误读」的确定性失败（Axis B 根因）。
# 非 Windows 直接透传；已是 Windows 路径也透传。
to_win_path() {
  local p="$1"
  case "$(uname -s 2>/dev/null)" in
    MINGW*|MSYS*|CYGWIN*) ;;
    *) printf '%s\n' "$p"; return 0;;
  esac
  case "$p" in
    [A-Za-z]:[\\/]*) printf '%s\n' "$p" ;;
    /[A-Za-z]/*) printf '%s:/%s\n' "${p:1:1}" "${p:3}" ;;
    /*) printf 'C:%s\n' "$p" ;;
    *) printf '%s\n' "$p" ;;
  esac
}

# ---- 环境预检/引导层（Axis B 就绪度）：硬前置缺失即 FAIL_LOUD，可自举的给 shell 函数兜底 ----
# shellcheck source=/dev/null
source "$SCRIPT_DIR/preflight_env.sh"

# ---- 浏览器后端探测 + 加载 ----
BZC_BACKEND="${BZC_BACKEND:-brs}"
# ⛔ 反作弊红线（R12）：BOSS 直聘禁止任何 Agent 的浏览器扩展直控（含 Codex @Chrome / CloakBrowser）。
# 仅允许 agent-browser-runtime 类受控运行时（受控 Chromium + 自带 companion 模拟真实光标）。
# 统一 brs 单后端——此拦截让「禁止扩展直控」从文档约束升级为可执行的硬失败。
case "$BZC_BACKEND" in
  codex|cloak)
    echo "FAIL_LOUD: 后端 '$BZC_BACKEND' 因 BOSS 反作弊风险已禁用（R12）。" >&2
    echo "  Codex @Chrome / CloakBrowser 属浏览器扩展直控，会触发 BOSS 反作弊封号。" >&2
    echo "  请改用唯一 sanctioned 后端 brs（agent-browser-runtime）：" >&2
    echo "    https://github.com/energypantry/agent-browser-runtime" >&2
    exit 1 ;;
esac
if [ ! -f "$BACKEND_DIR/$BZC_BACKEND.sh" ]; then
  echo "FAIL_LOUD: 未检测到可用的「仿真人浏览器」后端 '$BZC_BACKEND'。" >&2
  echo "  本 skill 必须运行在仿真人浏览器之上（直接裸 CDP / 合成点击 / 扩展直控会触发 BOSS 反作弊，曾导致封号）。" >&2
  echo "  请安装 agent-browser-runtime 并设 BZC_BACKEND=brs（默认值）：" >&2
  echo "    https://github.com/energypantry/agent-browser-runtime" >&2
  echo "  可用后端: $(ls "$BACKEND_DIR" 2>/dev/null | sed 's/\.sh$//' | tr '\n' ' ')" >&2
  exit 1
fi
# 加载后端实现（bz_mode / bz_status / bz_browse_* / bz_ui / bz_extract / bz_emit_plan）
# shellcheck source=/dev/null
source "$BACKEND_DIR/$BZC_BACKEND.sh"

# ---- 后端模式助手 ----
backend_is_hosted() { [ "$(bz_mode 2>/dev/null || echo local)" = "hosted" ]; }

# ---- 运行时就绪闸门：委托给后端 bz_status（不就绪时后端内部 fail-loud）----
fail_loud_if_down() { bz_status; }

# ---- 撞墙检查：传入 HTML 文本，命中即停手 ----
# 2026-07-28 修正：裸 "verify" 必然误命中 BOSS 每页都带的全局 CSS 类名
# (.verify-box / geetest 样式)，曾把「登录态过期」误报为撞墙。
# 现改为：URL 级信号 verify.html / captcha + 中文强信号词（页面文案，CSS 不含）。
# ⚠️ 安全优先：只去掉必然误报的裸 verify，中文词全保留，不得再收紧。
verify_wall() {
  local html="$1"
  if echo "$html" | grep -qi "verify\.html\|captcha\|验证码\|安全验证\|请完成\|拖动滑块\|账号存在风险"; then
    echo "FAIL_LOUD: 撞验证墙, 立即停手交人工, 冷却>=24h" >&2
    exit 3
  fi
}

# ---- 登录态状态机（机器级 / 跨产品 / 失败驱动，非主动预飞）----
# 机制真相：浏览器 runtime 用持久化 profile（cookie 在挂载卷），BOSS 登录态跨容器重启都在，
# 仅 cookie 过期才失效（非每小时）。故：默认信任「已登录」，仅在真实操作卡住时质疑。
# 状态文件位置：跟随 skill 自身安装目录（产品无关，适配 WorkBuddy/Claude Code/Codex/OpenClaw/Solo…），
# 不依赖具体 Agent 产品的 config 路径；位于 skills 目录下（非 git 仓库），不进 GitHub。
skill_login_state_file() {
  local root; root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
  printf "%s/.state/login_state" "$root"
}
get_login_state() {
  local f; f="$(skill_login_state_file)"
  [ -f "$f" ] && cat "$f" 2>/dev/null | tr -d '\r' | head -1 || echo "unknown"
}
set_login_state() {
  local f v; f="$(skill_login_state_file)"; v="$1"
  mkdir -p "$(dirname "$f")" 2>/dev/null
  printf '%s\t%s\n' "$v" "$(date +%FT%T%z)" > "$f"   # 单字节 printf 写，避免 CRLF/LF 混行（R10 同源坑）
}

# 登录态失效检测（按需调用，仅失败分支）：命中登录页信号→置 logged_out + exit 8（区别于撞墙：无需冷却）。
# 信号：登录页标题 / 扫码登录 / 搜索页出现「登录/注册」按钮（已登录页无此按钮）。
check_logged_in() {
  local html="$1"
  if echo "$html" | grep -q "注册登录】\|扫码登录\|>登录/注册<"; then
    set_login_state logged_out
    echo "FAIL_LOUD: BOSS 登录态已失效, 请在 noVNC 重新登录后再继续 (exit 8)" >&2
    exit 8
  fi
}

# ---- 冷却 sleep（含人体化抖动）----
# 固定 sleep 易被反作弊识别为机器节奏；叠加 ±COOLDOWN_JITTER 抖动更接近真人。
cooldown() {
  local base="${1:-${ACTION_INTERVAL_SECONDS:-5}}"
  local jitter="${COOLDOWN_JITTER:-3}"
  local secs=$base
  if [ "$jitter" -gt 0 ]; then
    local delta=$(( (RANDOM % (jitter * 2 + 1)) - jitter ))
    secs=$((base + delta))
    [ "$secs" -lt 1 ] && secs=1
  fi
  sleep "$secs"
}

# ---- 软限流指数退避（rate_backoff）----
# 命中「操作频繁」提示或接近日上限时调用：间隔按 2^(n-1) 指数拉长，封顶 BACKOFF_MAX。
rate_backoff_seq=0
rate_backoff() {
  rate_backoff_seq=$((rate_backoff_seq + 1))
  local factor=$((1 << (rate_backoff_seq - 1)))
  local secs=$(( (${ACTION_INTERVAL_SECONDS:-5}) * factor ))
  local cap="${BACKOFF_MAX:-60}"
  [ "$secs" -gt "$cap" ] && secs=$cap
  echo "[backoff] 第 $rate_backoff_seq 次退避, 间隔 ${secs}s (封顶 $cap)" >&2
  sleep "$secs"
}

# ---- 等待元素就绪（Item1：根治「面板未渲染完提取空串」）----
# 用法：bz_wait <lease> <tab> <token> [timeout=20] [interval=1]
#   token = 期望出现的 class / tag 名（自动去前导点）；轮询 browse-html 直到命中即返回 0。
#   超时返回 1 + FAIL_LOUD。hosted 模式不本地驱动，直接 return 0。
bz_wait() {
  if backend_is_hosted; then echo "[hosted] 跳过本地等待" >&2; return 0; fi
  local lease="$1" tab="$2" token="${3#.}" timeout="${4:-20}" interval="${5:-1}"
  [ -z "$token" ] && { echo "FAIL_LOUD: bz_wait 缺 token" >&2; return 2; }
  local elapsed=0 html
  while [ "$elapsed" -lt "$timeout" ]; do
    html=$(bz_browse_html "$lease" "$tab" 2>/dev/null) || true
    if printf '%s' "$html" | grep -qE "class=\"[^\"]*\b$token\b" || printf '%s' "$html" | grep -qF ">$token<"; then
      echo "[ok] 元素就绪: $token (${elapsed}s)" >&2
      return 0
    fi
    sleep "$interval"
    elapsed=$((elapsed + interval))
  done
  echo "FAIL_LOUD: 等待元素超时(${timeout}s 未出现): $token" >&2
  return 1
}

# ---- 日限额计数器（R3，跨调用持久化）----
# 每个「改账号状态」动作（书签 / 发消息）执行前调用一次；超过 DAILY_CAP 即 fail-loud（exit 5）。
# 计数落盘到 ${WORK_DIR:-.work}/.daily_action_count_YYYYMMDD，按自然日隔离，跨进程/跨调用累计。
# 说明：这是软性节流，防止单日突发批量触发反作弊；不替代 R5 授权门控与 R4 撞墙停手。
# F11: 本计数器仅在「本地后端（brs）」链路生效——process_job.sh 在 hosted 短路（backend_is_hosted）
#      前已 exit 0，bump_daily_cap 不会被调用。hosted 模式动作发生在 Codex 端，R3 日限额**无代码级
#      保障**，仅依赖 emit_plan 文本提示 + 执行方（人/外部 Agent）自律。文档须明示此边界。
bump_daily_cap() {
  local cap="${DAILY_CAP:-100}"
  # cap<=0 视作不限（仍会记录，便于审计）
  local dir="${WORK_DIR:-.work}"
  mkdir -p "$dir"
  local f="$dir/.daily_action_count_$(date +%Y%m%d)"
  local n=0
  [ -f "$f" ] && n=$(cat "$f" 2>/dev/null | tr -dc '0-9'); [ -z "$n" ] && n=0
  n=$((n + 1))
  echo "$n" > "$f"
  if [ "$cap" -gt 0 ] && [ "$n" -gt "$cap" ]; then
    echo "FAIL_LOUD: 已达单日动作上限 DAILY_CAP=$cap（今日第 $n 次改状态动作），停手 (R3)。" >&2
    echo "  如需继续，请确认风险后手动调高 DAILY_CAP 或次日再跑；切勿突发批量。" >&2
    exit 5
  fi
  echo "[cap] 今日改状态动作计数: $n/$cap" >&2
}
