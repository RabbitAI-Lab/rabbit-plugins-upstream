#!/bin/bash
# P3 广色域回归：--p3 打开后 iTerm2 Profile / Ghostty 都走 Display P3，
# 再去掉 --p3 必须完整退回 sRGB。全程只写 $TMP，不碰本机真实终端配置。
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/hkw-terminal-p3-test.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT

fail() { printf 'p3: %s\n' "$*" >&2; exit 1; }

# HOME 能隔离 iTerm2 / Ghostty / Warp / Tabby，但 theme.sh 还会顺手写
# com.apple.Terminal（defaults 走真实用户目录，不认 HOME），并把主题 source 进
# 正在跑的 tmux 会话。这里用假命令挡掉，保证测试不改本机真实终端配置。
mkdir -p "$TMP/bin"
for stub in defaults tmux; do
  printf '#!/bin/sh\nexit 1\n' > "$TMP/bin/$stub"
  chmod +x "$TMP/bin/$stub"
done

GHOSTTY_DIR="$TMP/.config/ghostty"
GHOSTTY_CFG="$GHOSTTY_DIR/config"
GHOSTTY_THEMES="$GHOSTTY_DIR/themes"
RUNTIME="$TMP/.config/hekouwang-terminal"
ACTIVE="$TMP/Library/Application Support/iTerm2/DynamicProfiles/hekouwang-active-theme.json"

mkdir -p "$GHOSTTY_THEMES"
printf 'theme = hekouwang-ember\nfont-family = Maple Mono NF CN\n' > "$GHOSTTY_CFG"

run_theme() {
  HOME="$TMP" PATH="$TMP/bin:$PATH" "$ROOT/scripts/theme.sh" "$@" >/dev/null 2>&1 \
    || fail "theme.sh $* 执行失败（见上方被抑制的输出，可单独重跑排查）"
}

assert_colorspace() {   # $1 = 期望的 Color Space
  python3 - "$ACTIVE" "$1" <<'PY' || fail "iTerm2 激活 Profile 未回到期望的 Color Space（详见上一行）"
import json, sys

path, want = sys.argv[1], sys.argv[2]
try:
    prof = json.load(open(path, encoding="utf-8"))["Profiles"][0]
except (OSError, ValueError, KeyError, IndexError) as exc:
    print(f"cannot read {path}: {exc}", file=sys.stderr)
    raise SystemExit(1)

bad = False
for key in ("Background Color", "Ansi 1 Color"):
    got = prof.get(key, {}).get("Color Space")
    if got != want:
        print(f"{key}: Color Space = {got!r}, want {want!r}", file=sys.stderr)
        bad = True
raise SystemExit(1 if bad else 0)
PY
}

# 1) --p3：iTerm2 侧
run_theme ember --p3

[ -f "$RUNTIME/p3" ] || fail "缺少 P3 标记：$RUNTIME/p3"
[ "$(cat "$RUNTIME/p3")" = "1" ] \
  || fail "P3 标记内容应为 1，实际是 '$(cat "$RUNTIME/p3")'"

assert_colorspace "Display P3"

# 2) --p3：Ghostty 侧（主题文件 + window-colorspace 必须成对切换）
grep -qxF 'theme = hekouwang-ember-p3' "$GHOSTTY_CFG" \
  || fail "Ghostty config 缺少 'theme = hekouwang-ember-p3'（实际内容：$(tr '\n' ' ' < "$GHOSTTY_CFG")）"
grep -qxF 'window-colorspace = display-p3' "$GHOSTTY_CFG" \
  || fail "Ghostty config 缺少 'window-colorspace = display-p3'（实际内容：$(tr '\n' ' ' < "$GHOSTTY_CFG")）"
[ -f "$GHOSTTY_THEMES/hekouwang-ember-p3" ] \
  || fail "Ghostty 主题文件未部署：$GHOSTTY_THEMES/hekouwang-ember-p3"

# 3) 去掉 --p3：标记、Ghostty、iTerm2 三处都要退回 sRGB
run_theme ember

[ ! -e "$RUNTIME/p3" ] || fail "去掉 --p3 后 P3 标记仍然存在：$RUNTIME/p3"
grep -qxF 'theme = hekouwang-ember' "$GHOSTTY_CFG" \
  || fail "Ghostty config 未回到 'theme = hekouwang-ember'（实际内容：$(tr '\n' ' ' < "$GHOSTTY_CFG")）"
if grep -qxF 'theme = hekouwang-ember-p3' "$GHOSTTY_CFG"; then
  fail "去掉 --p3 后 Ghostty config 仍残留 'theme = hekouwang-ember-p3'"
fi
grep -qxF 'window-colorspace = srgb' "$GHOSTTY_CFG" \
  || fail "Ghostty config 未回到 'window-colorspace = srgb'（实际内容：$(tr '\n' ' ' < "$GHOSTTY_CFG")）"

assert_colorspace "sRGB"

printf 'p3: ok\n'
