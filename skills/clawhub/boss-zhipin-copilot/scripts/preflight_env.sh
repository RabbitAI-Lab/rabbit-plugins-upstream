#!/usr/bin/env bash
# preflight_env.sh - 环境预检/引导层（Axis B 执行环境就绪度）。
#
# 定位：本 skill 把「运行前提」拆成两层——
#   Axis A 任务成熟度（磁盘持久：profile / target_library / 已发记录 / 百+岗位）——持久可信；
#   Axis B 执行环境就绪度（会话级临时：python+yaml / cygpath / sleep / seq 等 coreutils）——会话级、易归零。
# 历史 Round 5 暴露：Axis A 再成熟也救不了 Axis B 归零——缺 cygpath→脚本路径静默回退 POSIX、
# 受管 base python 缺 PyYAML→所有解析脚本确定性失败，白白耗 70 分钟排查。
#
# 本层职责（第一性原理：只覆盖「缺了必然崩」的硬前置，不碰可恢复的运行时状态如登录态——R11 已失败驱动）：
#   1) 防御性确认 PYTHON 能 import yaml（resolve_python 已保证，此处兜底拦截）；
#   2) 缺失即安全自举的 coreutils 兜底（sleep/seq 注册会话级 shell 函数，零磁盘写入）；
#   3) 路径转换统一走 to_win_path（common.sh），不再维护 cygpath 兼容 shim（已删，死代码）。
set -euo pipefail

# ---- 1) PyYAML 可用（防御性二次确认）----
# resolve_python() 已保证返回的 PYTHON 能 import yaml（否则前者直接 FAIL_LOUD），
# 此处仅为防御性兜底；若未来 resolve_python 逻辑变化，这里能兜底拦截。
if ! "$PYTHON" -c 'import yaml' >/dev/null 2>&1; then
  echo "FAIL_LOUD: 当前 PYTHON=$PYTHON 无法 import yaml —— 所有解析/筛选脚本将确定性失败。" >&2
  echo "  请把 PYTHON 指向带 PyYAML 的解释器（推荐 WorkBuddy 受管 venv: $HOME/.workbuddy/binaries/python/envs/default）。" >&2
  exit 1
fi

# ---- 2) coreutils 兜底（仅当真实命令缺失时注册 shell 函数；零磁盘写入，会话级）----
# Git Bash 在某些 PATH 配置下会缺 sleep/seq（coreutils）。cooldown/bz_wait/rate_backoff 用 sleep，
# search_jobs.sh 的滚动循环用 seq；它们缺失会让计时器/循环静默失效。
if ! command -v sleep >/dev/null 2>&1; then
  sleep() { "$PYTHON" -c 'import time,sys; time.sleep(float(sys.argv[1]))' "${1:-0}" 2>/dev/null || true; }
  export -f sleep 2>/dev/null || true
fi
if ! command -v seq >/dev/null 2>&1; then
  seq() {
    local start=1 step=1 end
    case $# in
      1) end=$1 ;;
      2) start=$1; end=$2 ;;
      3) start=$1; step=$2; end=$3 ;;   # 标准 seq FIRST STEP LAST
      *) return 1 ;;
    esac
    local i=$start
    while [ "$i" -le "$end" ]; do printf '%s\n' "$i"; i=$((i+step)); done
  }
  export -f seq 2>/dev/null || true
fi

# ---- 3) cygpath 兜底：已移除 ----
# 本 skill 脚本已统一改用 to_win_path（common.sh），全库零裸 cygpath 调用；
# 该 shim 属死代码，删除以消除冗余（保留 to_win_path 为唯一路径转换入口）。
