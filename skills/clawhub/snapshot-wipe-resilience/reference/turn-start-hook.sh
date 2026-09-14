#!/bin/bash
# turn-start-hook.sh — auto-heal a partially-wiped workspace at the start of a turn.
#
# Usage: bash reference/turn-start-hook.sh [--quiet]
# Exit:  0 = workspace healthy (possibly after repair), 1 = still damaged.
#
# Drop this at the top of your agent's per-turn routine. Safe to run every turn:
# when nothing is broken it prints one line and exits in milliseconds (checking
# is local I/O only — no network).

set -uo pipefail

SWR="${SWR_BIN:-$HOME/skills/snapshot-wipe-resilience/scripts/swr.py}"
[ -f "$SWR" ] || SWR="$HOME/skill_inventions/snapshot-wipe-resilience/scripts/swr.py"
MANIFEST="${SWR_MANIFEST:-$HOME/.swr/manifest.json}"
QUIET=0
[ "${1:-}" = "--quiet" ] && QUIET=1

log() { [ "$QUIET" = 1 ] || echo "$@"; }

if [ ! -f "$SWR" ]; then
  echo "swr: tool not found (set SWR_BIN)" >&2; exit 1
fi
if [ ! -f "$MANIFEST" ]; then
  echo "swr: no manifest at $MANIFEST — run: python3 $SWR autopilot" >&2; exit 1
fi

# Fast path: silent when healthy. Use a unique file; a fixed /tmp path would
# be vulnerable to symlink clobbering by another local process.
TMP_OUT="$(mktemp "${TMPDIR:-/tmp}/swr-check.XXXXXX")" || {
  echo "swr: cannot create a private temporary report" >&2; exit 1
}
trap 'rm -f -- "$TMP_OUT"' EXIT HUP INT TERM
if SWR_MANIFEST="$MANIFEST" NO_COLOR=1 python3 "$SWR" --quiet check >"$TMP_OUT" 2>&1; then
  log "workspace: $(grep -o '[0-9]*/[0-9]* healthy' "$TMP_OUT" | tail -1)"
  exit 0
fi

echo "workspace damage detected:"
grep -E "MISSING|CORRUPT|STRIPPED|EMPTY|BROKENLNK|SMOKEFAIL|signature" "$TMP_OUT" \
  || cat "$TMP_OUT"

echo "repairing (tier order)..."
if SWR_MANIFEST="$MANIFEST" python3 "$SWR" --quiet doctor --resume; then
  echo "workspace restored"
  exit 0
fi

cat <<'EOF'

Some entries could not be auto-restored. Likely causes:
  * a restore recipe needs network/credentials that are also missing (check tier 0 first)
  * an entry has no restore recipe — add one, or `swr escrow` it if small
  * a rebuild exceeded available RAM (retry with -j 1)
  * the manifest signature does not verify -> run `swr sign` (or `swr verify` to inspect)
Run `python3 swr.py why --only <id>` for per-entry detail.
EOF
exit 1
