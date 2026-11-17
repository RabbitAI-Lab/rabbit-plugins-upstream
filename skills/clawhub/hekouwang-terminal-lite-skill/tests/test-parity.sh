#!/bin/bash
set -eu
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d "${TMPDIR:-/tmp}/hkw-terminal-parity-test.XXXXXX")"
trap 'rm -rf "$TMP"' EXIT
FAKE_ROOT="$TMP/kit"; FAKE_HOME="$TMP/home"
mkdir -p "$FAKE_ROOT/config/themes" "$FAKE_HOME/.config/hekouwang-terminal" \
  "$FAKE_HOME/Library/Application Support/iTerm2/DynamicProfiles"
cp "$ROOT/config/themes/tokyo-night.json" "$FAKE_ROOT/config/themes/tokyo-night.json"
cp "$ROOT/config/themes/tokyo-night.json" "$FAKE_HOME/Library/Application Support/iTerm2/DynamicProfiles/hekouwang-active-theme.json"
printf 'tokyo-night\n' > "$FAKE_HOME/.config/hekouwang-terminal/theme"

HOME="$FAKE_HOME" python3 "$ROOT/lib/parity.py" "$FAKE_ROOT" > "$TMP/good"
grep -q $'^same\tiTerm2\t' "$TMP/good"

python3 - "$FAKE_HOME/Library/Application Support/iTerm2/DynamicProfiles/hekouwang-active-theme.json" <<'PY'
import json, sys
p=sys.argv[1]; d=json.load(open(p)); d['Profiles'][0]['Background Color']['Red Component']=0.123; json.dump(d,open(p,'w'))
PY
if HOME="$FAKE_HOME" python3 "$ROOT/lib/parity.py" "$FAKE_ROOT" > "$TMP/bad"; then
  echo "parity test accepted a deliberate color drift" >&2
  exit 1
fi
grep -q $'^drift\tiTerm2\t' "$TMP/bad"
printf 'parity: ok\n'
