#!/usr/bin/env bash
# run_py.sh - 便携式 python 运行器（Agent 面向文档的统一入口）。
#
# 为什么需要它：受管环境（如 WorkBuddy 的 Git Bash）PATH 上常无 `python3`，
# 文档若写 `python3 scripts/xxx.py` 会让 Agent 直跑即失败（确定性崩溃）。
# 本包装统一经 common.sh 的 resolve_python() 取「带 PyYAML 的解释器」+ to_win_path 做路径转换，
# 与 skill 内部脚本完全一致——无论哪个 Agent / 哪个平台都能跑。
#
# 用法：bash scripts/run_py.sh <script.py> [args...]
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$SCRIPT_DIR/common.sh"
"$PYTHON" "$(to_win_path "$SCRIPT_DIR")/$1" "${@:2}"
