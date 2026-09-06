#!/bin/sh
# run_guarded.sh — one guarded inference call:
# light-mode routing -> prompt cache -> preflight -> timed call -> fallback -> latency log
# usage: run_guarded.sh "prompt" [role] [n_tokens]
# stdout: completion text. rc: 0 ok (cache or live), 2 failed, 3 no model, 4 no binary.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
# shellcheck source=scripts/selfheal_runner.sh
. "$HERE/selfheal_runner.sh"

if [ -z "${1:-}" ]; then
  echo "usage: run_guarded.sh \"prompt\" [role] [n_tokens]" >&2
  exit 64
fi
PROMPT=$1; ROLE=${2:-auto}; N=${3:-128}
ORIG_ROLE=""   # cache keys always use the ORIGINAL role, never a fallback label
WORDS=$(printf '%s' "$PROMPT" | wc -w | tr -d ' ')

# light-swarm: short casual input -> smallest/fastest model, small budget
if [ "$ROLE" = auto ]; then
  if [ "$WORDS" -le 8 ]; then ROLE=scout; [ "$N" -gt 120 ] && N=96
  else ROLE=spark; fi
fi

# 1. cache (0.0x s on hit = the only "infinite tok/s" that exists)
# model signature ties cache entries to the artifact: replaced model => new sig => miss
ORIG_ROLE=$ROLE
_file=$(selfheal_model_field "$ROLE" file 2>/dev/null)
if [ -n "$_file" ] && [ -f "$SELFHEAL_MODELS_DIR/$_file" ]; then
  SIG=$(stat -c '%s-%Y' "$SELFHEAL_MODELS_DIR/$_file" 2>/dev/null || echo nomodel)
else
  SIG=nomodel
fi
CACHE="$HERE/prompt_cache.py"
if command -v python3 >/dev/null 2>&1 && [ -f "$CACHE" ]; then
  if OUT=$(python3 "$CACHE" get "$ROLE" "$N" "$PROMPT" "$SIG" 2>/dev/null); then
    selfheal_log "cache HIT role=$ROLE"
    printf '%s' "$OUT"; exit 0
  fi
else
  CACHE=""
fi

# 2. preflight (idempotent, non-hanging)
selfheal_preflight >/dev/null 2>&1 || selfheal_log "preflight degraded (rc=$?)"

# 3. guarded call (wall-clock ms; validate %N gave digits — BusyBox may print %N literally)
T0=$(date +%s%N 2>/dev/null); case "$T0" in ''|*[!0-9]*) T0=$(( $(date +%s) * 1000000000 ));; esac
if ! OUT=$(run_with_timeout "$ROLE" "$PROMPT" "$N" 2>/dev/null); then
  # final fallback: smallest model once, if the failing role was bigger
  if [ "$ROLE" != scout ]; then
    selfheal_log "role $ROLE failed -> final fallback scout"
    OUT=$(run_with_timeout scout "$PROMPT" "$N" 2>/dev/null) || { selfheal_log "ERROR: all fallbacks failed"; exit 2; }
    ROLE="scout(fallback)"
  else
    exit 2
  fi
fi
T1=$(date +%s%N 2>/dev/null); case "$T1" in ''|*[!0-9]*) T1=$(( $(date +%s) * 1000000000 ));; esac

# 4. record latency (feeds selfheal_tune.sh EMA). Persistent write -> fix mode only.
if selfheal_fix_mode; then
  selfheal_ensure_dirs
  printf '{"ts":%s,"role":"%s","n":%s,"wall_ms":%s}\n' \
    "$(date +%s)" "$ROLE" "$N" "$(( (T1 - T0) / 1000000 ))" >>"$SELFHEAL_STATE/history.jsonl" 2>/dev/null || :
fi

# 5. populate cache under the ORIGINAL role key — a scout-fallback answer must
#    still be found by the next call that asked for the original role. Cache is
#    a persistent write: only in SELFHEAL_MODE=fix (consent model).
#    Note: $_flags is intentionally unquoted in the runner (single-word flags,
#    word-splitting is the mechanism).
if [ -n "$CACHE" ] && selfheal_fix_mode; then
  python3 "$CACHE" put "$ORIG_ROLE" "$N" "$PROMPT" "$OUT" "$SIG" 2>/dev/null || :
fi
printf '%s' "$OUT"
