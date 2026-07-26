#!/bin/bash
# Generic Suno-direct album builder. Reads an album config JSON and
# generates each track with HRM-grounded lyrics, V4_5PLUS custom mode.
# Saves both variants per track. Resumable via per-track ledger.
#
# Usage:
#   ./suno_album_builder.sh <config.json>
#
# Config schema:
#   {
#     "name": "10000.00001",
#     "out_dir": ".../10000.00001-rebuild",
#     "ledger": ".../10000.00001-done.json",
#     "theme": "Mathematical mysticism — ...",
#     "default_style": "Ambient electronica, 90 BPM, ...",
#     "tracks": [
#       { "title": "Ten Thousand", "style": "..." (optional), "theme": "..." (optional) },
#       ...
#     ]
#   }
#
# Per-track config can override the album-level theme/default_style.

set -u
CONFIG="${1:-}"
if [ -z "$CONFIG" ] || [ ! -f "$CONFIG" ]; then
  echo "Usage: $0 <config.json>"
  exit 1
fi

LOG="$(dirname "$CONFIG")/$(basename "$CONFIG" .json).log"
exec >> "$LOG" 2>&1
echo
echo "===== Suno-direct album builder $(date -Iseconds) — $CONFIG ====="

SUNO_KEY="${SUNO_API_KEY:-$(cat "${SUNO_API_KEY_FILE:-$HOME/.suno_api_key}" | tr -d "[:space:]")}"

# Pull config
ALBUM_NAME=$(python3 -c "import json; print(json.load(open(r'$CONFIG'))['name'])")
OUT=$(python3 -c "import json; print(json.load(open(r'$CONFIG'))['out_dir'])")
LEDGER=$(python3 -c "import json; print(json.load(open(r'$CONFIG'))['ledger'])")
ALBUM_THEME=$(python3 -c "import json; print(json.load(open(r'$CONFIG'))['theme'])")
DEFAULT_STYLE=$(python3 -c "import json; print(json.load(open(r'$CONFIG'))['default_style'])")
N=$(python3 -c "import json; print(len(json.load(open(r'$CONFIG'))['tracks']))")

mkdir -p "$OUT"
[ ! -f "$LEDGER" ] && echo "[]" > "$LEDGER"

mark_done() {
  TITLE="$1" LEDGER_PATH="$LEDGER" python3 -c "
import json, os
p = os.environ['LEDGER_PATH']
title = os.environ['TITLE']
with open(p, 'r', encoding='utf-8') as f:
    arr = json.load(f)
if title not in arr:
    arr.append(title)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(arr, f, ensure_ascii=False)
"
}

EXISTING=$(python3 -c "import json; print('\n'.join(json.load(open(r'$LEDGER'))))")
has_done() { echo "$EXISTING" | grep -Fx -- "$1" >/dev/null 2>&1; }

# Per-track loop
for i in $(seq 0 $((N-1))); do
  TITLE=$(python3 -c "import json; print(json.load(open(r'$CONFIG'))['tracks'][$i]['title'])")
  STYLE=$(python3 -c "
import json
t = json.load(open(r'$CONFIG'))['tracks'][$i]
print(t.get('style','$DEFAULT_STYLE') or '$DEFAULT_STYLE')")
  THEME=$(python3 -c "
import json
t = json.load(open(r'$CONFIG'))['tracks'][$i]
print(t.get('theme','$ALBUM_THEME') or '$ALBUM_THEME')")

  if has_done "$TITLE"; then
    echo "[skip] $TITLE — already done"
    continue
  fi

  echo
  echo "--- TRACK: $TITLE at $(date -Iseconds) ---"
  CACHE="$OUT/lyrics_$(echo "$TITLE" | tr ' /' '_-' | tr -d "'").txt"
  if [ -f "$CACHE" ] && [ "$(wc -c < "$CACHE")" -gt 100 ]; then
    LYRICS=$(cat "$CACHE")
    echo "  using cached lyrics ($(wc -c < "$CACHE") chars)"
  else
    echo "  composing HRM-grounded lyrics..."
    LYRICS=$(python3 -c "
import sys
sys.path.insert(0, __import__('os').environ.get('HRM_LYRICS_SRC', ''))
from clipcannon.audio.hrm_lyrics import generate_lyrics
text = generate_lyrics(
    title=sys.argv[1], theme=sys.argv[2], recall_query=sys.argv[2],
    bars=16, structure='verse-chorus-verse-chorus', timeout_sec=300)
print(text)
" "$TITLE" "$THEME" 2>/dev/null)
    if [ -n "$LYRICS" ]; then
      echo "$LYRICS" > "$CACHE"
      echo "  ✓ lyrics: $(echo "$LYRICS" | wc -c) chars"
    else
      echo "  [skip] no lyrics generated"
      continue
    fi
  fi

  PAYLOAD=$(TITLE="$TITLE" STYLE="$STYLE" LYRICS="$LYRICS" python3 -c "
import json, os
print(json.dumps({
  'customMode': True,
  'instrumental': False,
  'model': 'V4_5PLUS',
  'title': os.environ['TITLE'][:100],
  'style': os.environ['STYLE'][:1000],
  'prompt': os.environ['LYRICS'][:5000],
  'callBackUrl': 'https://radio.ninja-portal.com/api/suno-callback',
}, ensure_ascii=False))")

  RESP=$(curl -s -X POST -H "Authorization: Bearer $SUNO_KEY" -H "Content-Type: application/json" \
    -d "$PAYLOAD" "https://api.sunoapi.org/api/v1/generate")
  echo "  init: $RESP"

  TASK_ID=$(echo "$RESP" | python3 -c "import json,sys
try: print(json.load(sys.stdin).get('data',{}).get('taskId',''))
except: print('')")
  if [ -z "$TASK_ID" ]; then
    echo "  [skip] no taskId"; continue
  fi
  echo "  taskId: $TASK_ID — polling..."

  for j in $(seq 1 30); do
    sleep 15
    SR=$(curl -s -H "Authorization: Bearer $SUNO_KEY" "https://api.sunoapi.org/api/v1/generate/record-info?taskId=$TASK_ID")
    STATUS=$(echo "$SR" | python3 -c "import json,sys
try: print(json.load(sys.stdin).get('data',{}).get('status','?'))
except: print('?')")
    echo "    $((j*15))s: $STATUS"
    if [ "$STATUS" = "SUCCESS" ]; then
      URLS=$(echo "$SR" | python3 -c "
import json, sys
d = json.load(sys.stdin)['data']
for t in d.get('response',{}).get('sunoData',[]):
    print(f\"{t.get('id','')}\\t{t.get('audioUrl','')}\\t{t.get('duration','')}\")")
      idx=1
      while IFS=$'\t' read -r tid url dur; do
        [ -z "$url" ] && continue
        SAFE=$(echo "$TITLE" | tr ' /' '_-' | tr -d "'")
        OUT_FILE="$OUT/${SAFE}_v${idx}.mp3"
        curl -sL "$url" -o "$OUT_FILE"
        SIZE=$(stat -c%s "$OUT_FILE" 2>/dev/null || stat -f%z "$OUT_FILE" 2>/dev/null || echo 0)
        echo "    saved: $OUT_FILE  ${SIZE}B  ${dur}s"
        idx=$((idx+1))
      done <<< "$URLS"
      mark_done "$TITLE"
      break
    fi
    if echo "$STATUS" | grep -qE "FAILED|ERROR"; then
      echo "    failed: $SR"; break
    fi
  done

  sleep 10
done

echo
echo "===== done at $(date -Iseconds) ====="
ls -la "$OUT" 2>/dev/null | tail -25
