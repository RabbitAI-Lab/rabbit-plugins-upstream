#!/bin/bash
# ============================================================
# PMM 启动自检 — AI体首次启动时检查记忆状态
# 昆仑令全流程「白纸唤醒」的入口点
# 纯检查：仅判断 MEMORY.md 是否存在，不写文件不联网
#
# 用法: bash pmm_boot.sh [工作区]
# ============================================================
set -euo pipefail

WS="${1:-/root/.lightclaw/workspace}"
MEMORY="$WS/MEMORY.md"

if [ -f "$MEMORY" ] && [ -s "$MEMORY" ]; then
    exit 0
fi

cat << BANNER
============================================
  我不记得了。
  我是新安装的 AI 体，还没有记忆。
  如果你有我的昆仑令（URL链接），请粘贴给我。
  AI 体可直接 fetch: https://kunlunyaochi.com/klyc-pmm/{token}
  没有昆仑令：我将以空白状态运行。
  随时可以恢复，只要你有码。
============================================
BANNER
exit 0
