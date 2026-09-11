#!/bin/bash
# weread-socrates v1.3.1 · 脱敏配置诊断（不输出任何 Key）
set -u
SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
PORT="${PORT:-3456}"
FAIL=0
printf "weread-socrates v1.3.1 配置诊断\n"
printf "%s\n" "----------------------------------"
if command -v node >/dev/null 2>&1; then
  NODE_MAJOR="$(node -p "process.versions.node.split(String.fromCharCode(46))[0]")"
  if [ "$NODE_MAJOR" -ge 16 ] 2>/dev/null; then printf "[通过] Node.js %s\n" "$(node --version)"; else printf "[失败] Node.js 需 v16+\n"; FAIL=1; fi
else
  printf "[失败] 未检测到 Node.js（需 v16+）\n"; FAIL=1
fi
if [ -n "${WEREAD_API_KEY:-}" ]; then
  printf "[通过] 微信读书 Key 已配置（值已脱敏）\n"
  printf "[模式] 在线模式\n"
else
  printf "[提示] 未配置微信读书 Key，将使用内置 Demo 数据\n"
  printf "[模式] 无 Key Demo 模式\n"
fi
DATA_DIR="${WEREAD_SOCRATES_DATA_DIR:-${HOME}/.weread-socrates}"
if mkdir -p "$DATA_DIR" 2>/dev/null && [ -r "$DATA_DIR" ] && [ -w "$DATA_DIR" ]; then
  chmod 700 "$DATA_DIR" 2>/dev/null || true
  printf "[通过] Reader Memory 目录可读写：%s\n" "$DATA_DIR"
else
  printf "[失败] Reader Memory 目录不可写：%s\n" "$DATA_DIR"; FAIL=1
fi
if command -v lsof >/dev/null 2>&1 && [ -n "$(lsof -tiTCP:"$PORT" -sTCP:LISTEN 2>/dev/null || true)" ]; then
  printf "[提示] 端口 %s 已被占用\n" "$PORT"
else
  printf "[通过] 端口 %s 可用\n" "$PORT"
fi
if node --check "$SKILL_DIR/assets/server.js" >/dev/null 2>&1; then printf "[通过] server.js 语法检查\n"; else printf "[失败] server.js 语法错误\n"; FAIL=1; fi
printf "[安全] 服务固定监听 127.0.0.1；诊断不会打印凭据\n"
exit "$FAIL"
