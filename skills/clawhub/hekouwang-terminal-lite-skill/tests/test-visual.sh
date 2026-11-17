#!/bin/bash
# 视觉层回归：色板门禁 + 预览金标，各跑一次正例和反例。
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/hkw-terminal-visual-test.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT

# 1) 仓里现有色板必须过门禁
python3 "$ROOT/config/themes/_audit.py" --gate >/dev/null

# 2) 反例：把一套正常色板改成 normal=bright，门禁必须红
python3 - "$ROOT" <<'PY'
import json, sys
sys.path.insert(0, sys.argv[1] + "/config/themes")
from palettes import _audit
p = {"bg": "1e1e2e", "fg": "cdd6f4",
     "ansi": ["45475a", "f38ba8", "a6e3a1", "f9e2af", "89b4fa", "f5c2e7", "94e2d5", "bac2de",
              "585b70", "f38ba8", "a6e3a1", "f9e2af", "89b4fa", "f5c2e7", "94e2d5", "a6adc8"]}
r = _audit.evaluate("broken", p)
assert not r["ok"], "audit accepted six bright=normal pairs"
assert r["score"] < 100
PY

# 2b) 反例：选区/搜索/光标都等于底色，视觉门禁必须红
python3 - "$ROOT" <<'PY'
import sys
sys.path.insert(0, sys.argv[1] + "/config/themes")
from palettes import _audit, load

palettes, _ = load()
p = dict(palettes["catppuccin-mocha"])
p["selbg"] = p["bg"]
p["selfg"] = p["fg"]
p["matchbg"] = p["bg"]
p["cursor"] = p["bg"]
r = _audit.evaluate("broken-selection", p)
assert not r["ok"], "audit accepted an invisible selection / search / cursor"
assert any("selection" in x for x in r["issues"]), r["issues"]
PY

# 2c) 反例：红绿同色 + diff 底同明度，色盲/灰度门禁必须红
python3 - "$ROOT" <<'PY'
import sys
sys.path.insert(0, sys.argv[1] + "/config/themes")
from palettes import _audit, load

palettes, _ = load()
p = dict(palettes["catppuccin-mocha"])
p["ansi"] = list(p["ansi"])
p["ansi"][2] = p["ansi"][1]          # green = red
p["surfaces"] = {"diff_add": p["bg"], "diff_delete": p["bg"]}  # ΔL = 0
r = _audit.evaluate("broken-cvd", p)
assert not r["ok"], "audit accepted identical red/green and flat diff surfaces"
assert any("cvd" in x for x in r["issues"]), r["issues"]
assert any("diff ΔL" in x for x in r["issues"]), r["issues"]
PY

# 2d) 反例：关键字/函数/类型同色，语法角色门禁必须红
python3 - "$ROOT" <<'PY'
import sys
sys.path.insert(0, sys.argv[1] + "/config/themes")
from palettes import _audit, load

palettes, _ = load()
p = dict(palettes["catppuccin-mocha"])
p["syntax"] = {
    "keyword": "ff0000", "function": "ff0000", "type": "ff0000",
    "string": "00ff00", "number": "0000ff", "operator": "ffffff",
}
r = _audit.evaluate("broken-syntax", p)
assert not r["ok"], "audit accepted identical keyword / function / type colors"
assert any("syntax" in x for x in r["issues"]), r["issues"]
PY

# 2e) 反例：语义表面等于背景，error/success 同色，门禁必须红
python3 - "$ROOT" <<'PY'
import sys
sys.path.insert(0, sys.argv[1] + "/config/themes")
from palettes import _audit, load

palettes, _ = load()
p = dict(palettes["catppuccin-mocha"])
flat = {
    "error_bg": p["bg"], "error_fg": p["fg"],
    "warn_bg": p["bg"], "warn_fg": p["fg"],
    "success_bg": p["bg"], "success_fg": p["fg"],
    "info_bg": p["bg"], "info_fg": p["fg"],
}
p["surfaces"] = flat
r = _audit.evaluate("broken-surfaces", p)
assert not r["ok"], "audit accepted invisible semantic surfaces"
assert any("surface" in x or "error/success" in x for x in r["issues"]), r["issues"]
PY

# 2f) 反例：中性梯三档全部等于背景，门禁必须红
python3 - "$ROOT" <<'PY'
import sys
sys.path.insert(0, sys.argv[1] + "/config/themes")
from palettes import _audit, load

palettes, _ = load()
p = dict(palettes["catppuccin-mocha"])
p["neutrals"] = {
    "surface": p["bg"], "overlay": p["bg"],
    "border": p["bg"], "muted": p["bg"],
}
r = _audit.evaluate("broken-neutral", p)
assert not r["ok"], "audit accepted a flat neutral ramp"
assert any("neutral" in x for x in r["issues"]), r["issues"]
PY

# 2g) 反例：语法色落在语义表面上读不出来，语法×表面门禁必须红
python3 - "$ROOT" <<'PY'
import sys
sys.path.insert(0, sys.argv[1] + "/config/themes")
from palettes import _audit, load

palettes, _ = load()
p = dict(palettes["catppuccin-mocha"])
p["syntax"] = {"string": p["fg"]}
p["surfaces"] = {"diff_add": p["fg"]}
r = _audit.evaluate("broken-syntax-surface", p)
assert not r["ok"], "audit accepted syntax colors on an unreadable surface"
assert any("syntax/surface" in x for x in r["issues"]), r["issues"]
assert r["syntax_surface"]["ok"] is False, r["syntax_surface"]
PY

# 3) 金标一致（开放仓不含 tests/golden：金标里是付费主题的真实色值）
if [ -d "$ROOT/tests/golden" ]; then
  python3 "$ROOT/config/themes/_preview.py" --regress "$ROOT/tests/golden" >/dev/null

  # 4) 反例：改坏一份金标，回归必须红
  cp -R "$ROOT/tests/golden" "$TMP/golden"
  # ⛔ 别写死主题名：导出会剔掉本机试色主题，被剔的那套不在回归范围里，
  #    改坏它不会让回归变红 —— 反例门静默失效但整个测试仍然红（2026-11-09 实测）。
  #    取金标目录里实际存在的一份，保证改的正是回归会读的那份。
  victim="$(find "$TMP/golden" -name '*.card.txt' | sort | head -1)"
  [ -n "$victim" ] || { echo "visual: no golden card to corrupt" >&2; exit 1; }
  python3 - "$victim" <<'PY'
import sys
p = sys.argv[1]
s = open(p, encoding="utf-8").read()
open(p, "w", encoding="utf-8").write(s.replace("❯", ">", 1))
PY
  if python3 "$ROOT/config/themes/_preview.py" --regress "$TMP/golden" >/dev/null 2>&1; then
    echo "preview regression accepted a deliberate change" >&2
    exit 1
  fi
else
  echo "visual: golden snapshots not present, skipped regression" >&2
fi

printf 'visual: ok\n'
