#!/usr/bin/env bash
# 走免凭据公开通道取游客令牌：取挑战 → 解 PoW → 创建游客 → 落盘完整响应 → 打印 access_token。
#
# 用法:
#   bash scripts/guest_token.sh [输出文件] [BASE]
#   默认输出 $HOME/.cache/debtop/guest.json, 默认 BASE https://agent.debtop.com
#
# 退出码: 0 成功（stdout 为 access_token）；非 0 失败（stderr 为原因，含服务端错误码）。
# 注意: 创建游客有配额（单 IP 3 次/小时、全局 500 次/天），不要把本脚本当"连通性探测"反复执行。
set -euo pipefail

# 依赖检查：缺失时给出明确提示（而不是让调用方去猜 curl/python3 的报错）
for bin in curl python3; do
  # 注意: 变量后跟全角字符必须用 ${} 括起, 否则在 UTF-8 locale 下 bash 会把全角字符并进变量名
  if ! command -v "$bin" >/dev/null 2>&1; then
    echo "缺少依赖: ${bin}（见 references/guest-access.md「运行前提与替代方案」）" >&2
    exit 127
  fi
done

OUT="${1:-$HOME/.cache/debtop/guest.json}"
BASE="${2:-https://agent.debtop.com}"
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$(dirname "$OUT")"

# ① 取一次性挑战（difficulty 一般为 16）
CHAL="$(curl -sS --max-time 20 "$BASE/bff/v1/guest-access/challenge")"
read -r CH DIFF <<<"$(printf '%s' "$CHAL" | python3 -c '
import json, sys
d = json.load(sys.stdin).get("data") or {}
print(d.get("challenge", ""), d.get("difficulty", ""))
')"
if [ -z "$CH" ] || [ -z "$DIFF" ]; then
  echo "取挑战失败（服务端可能未开放免凭据创建, 如 404 FEATURE_DISABLED）：$CHAL" >&2
  exit 1
fi

# ② 解 PoW
NONCE="$(python3 "$DIR/pow_solve.py" "$CH" "$DIFF")"

# ③ 创建游客（source 固定 "web" 是公开通道的要求；挑战一次性，重复提交会被拒）
curl -sS --max-time 20 -X POST "$BASE/bff/v1/guest-access" \
  -H 'Content-Type: application/json' \
  -d "{\"source\":\"web\",\"pow\":{\"challenge\":\"$CH\",\"nonce\":\"$NONCE\"}}" \
  -o "$OUT"

# ④ 回显 access_token（失败时打印服务端错误码并退出非 0）
python3 - "$OUT" <<'PY'
import json, sys
try:
    payload = json.load(open(sys.argv[1]))
except Exception as exc:  # noqa: BLE001
    sys.exit(f"响应无法解析: {exc}")
data = payload.get("data") or {}
token = data.get("accessToken")
if not token:
    code = payload.get("code") or payload.get("error") or "UNKNOWN"
    sys.exit(f"创建游客失败: {code} {payload.get('message') or payload.get('error_description') or ''}".strip())
print(token)
PY
