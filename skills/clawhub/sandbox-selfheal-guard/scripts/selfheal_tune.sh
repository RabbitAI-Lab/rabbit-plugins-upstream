#!/bin/sh
# selfheal_tune.sh — self-improvement loop: measure REAL tokens/sec on this host
# and fold it (EMA, alpha=0.4) into state/state.json, which selfheal_budget()
# uses instead of the generic manifest defaults. Run: after rebuild, after a
# model changes, or when budgets feel wrong. Requires llama bench-capable binary.
set -u
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
. "$HERE/selfheal_runner.sh"

command -v python3 >/dev/null 2>&1 || { echo "tune: python3 required" >&2; exit 5; }
selfheal_fix_mode || { echo "tune: writes measured state — requires SELFHEAL_MODE=fix (human consent)" >&2; exit 5; }
BIN=$(selfheal_find_binary) || { echo "tune: no inference binary" >&2; exit 4; }

measure_role() {  # $1 role -> prints measured tg tok/s (or nothing)
  _model=$(selfheal_ensure_model "$1" 2>/dev/null) || return 1
  selfheal_have timeout || { echo "tune: timeout(1) required" >&2; return 1; }
  _flags=$(selfheal_extra_flags "$BIN")   # Rule 4: feature-detect, never assume
  _t0=$(date +%s%N 2>/dev/null || echo 0)
  _out=$(timeout 180 "$BIN" -m "$_model" -p "Count from one to twenty." -n 96 -t "$SELFHEAL_THREADS" $_flags 2>/dev/null)
  _t1=$(date +%s%N 2>/dev/null || echo 0)
  [ -n "$_out" ] && [ "$_t0" != 0 ] || return 1
  python3 - "$_t0" "$_t1" <<'PY' 2>/dev/null
import sys
dt=(int(sys.argv[2])-int(sys.argv[1]))/1e9
if dt>0: print(f"{96/dt:.1f}")
PY
}

UPDATED=0
for ROLE in scout spark forge sage; do
  TPS=$(measure_role "$ROLE") || { echo "tune: $ROLE skipped (no model/binary)"; continue; }
  python3 - "$SELFHEAL_STATE/state.json" "$ROLE" "$TPS" <<'PY'
import json,sys,os
p,role,tps=sys.argv[1],sys.argv[2],float(sys.argv[3])
st=json.load(open(p)) if os.path.exists(p) else {}
ema=st.setdefault("ema_tps",{})
ema[role]=round(0.4*tps+0.6*ema.get(role,tps),1)   # EMA alpha=0.4
st["tuned_utc"]=__import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat()
json.dump(st,open(p,"w"),indent=1)
print(f"tune: {role} measured {tps} t/s -> EMA {ema[role]} t/s (budgets now use measured value)")
PY
  UPDATED=$((UPDATED+1))
done
[ "$UPDATED" -gt 0 ] && selfheal_log "tune: updated $UPDATED role EMA(s)" || exit 5
