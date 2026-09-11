#!/bin/sh
# selfheal_runner.sh — POSIX sh library for snapshot-wipe-resistant local inference.
# Source it (bash/sh/zsh) or execute:  ./selfheal_runner.sh preflight
# Design rules: no set -e, no global cd, no bashisms — sourcing must never
# mutate or kill the caller's shell. Every failure returns a code; nothing hangs.
#
# Exit codes: 0 ok · 2 inference failed · 3 model unavailable ·
#             4 binary unavailable · 5 preflight degraded (usable, check log)
#
# CONSENT MODEL (registry-audit requirement):
#   SELFHEAL_MODE=check (default) — read-only probes; logs what it WOULD change
#   ("DRY: ..." lines); mutates nothing except its own log under ~/.selfheal.
#   SELFHEAL_MODE=fix — permits: apt installs (sudo -n only), npx-shim creation,
#   llama.cpp rebuilds, model downloads, cache/state writes.
#   Enable fix mode ONLY with explicit human consent.

SELFHEAL_MODE="${SELFHEAL_MODE:-check}"
[ -n "${SELFHEAL_HOME:-}" ] || SELFHEAL_HOME="$HOME/.selfheal"
SELFHEAL_LOG="$SELFHEAL_HOME/selfheal.log"
SELFHEAL_STATE="$SELFHEAL_HOME/state"
SELFHEAL_MANIFEST="${SELFHEAL_MANIFEST:-$(CDPATH= cd -- "$(dirname -- "$0")/.." 2>/dev/null && pwd)/manifest.json}"
SELFHEAL_MODELS_DIR="${SELFHEAL_MODELS_DIR:-$HOME}"
SELFHEAL_LLAMA_DIR="${SELFHEAL_LLAMA_DIR:-$HOME/llama.cpp}"
SELFHEAL_THREADS="${SELFHEAL_THREADS:-2}"

selfheal_fix_mode() { [ "$SELFHEAL_MODE" = fix ]; }
selfheal_ensure_dirs() { mkdir -p "$SELFHEAL_STATE" 2>/dev/null || :; chmod 700 "$SELFHEAL_HOME" "$SELFHEAL_STATE" 2>/dev/null || :; }
# check mode writes NOTHING (stderr only); fix mode persists to $SELFHEAL_LOG
selfheal_log() {
  _ts=$(date -Iseconds 2>/dev/null || date)
  if selfheal_fix_mode; then selfheal_ensure_dirs; printf '%s %s\n' "$_ts" "$1" >>"$SELFHEAL_LOG" 2>/dev/null || :
  else printf '%s %s\n' "$_ts" "$1" >&2; fi
}
selfheal_fix_mode && selfheal_ensure_dirs

# --- capability probes (never assert, always detect) -------------------------
selfheal_have() { command -v "$1" >/dev/null 2>&1; }

selfheal_sudo_ok() {  # stdin-closed sandboxes: interactive sudo would HANG
  selfheal_have sudo || return 1
  sudo -n true 2>/dev/null
}

selfheal_ensure_pkgs() {  # best effort; no hang, no failure cascade
  for b in "$@"; do
    if ! selfheal_have "$b"; then
      if ! selfheal_fix_mode; then selfheal_log "DRY: would install pkg: $b (SELFHEAL_MODE=fix to allow)"; continue; fi
      if selfheal_sudo_ok; then
        # throttle apt-get update: at most once per 600s (stamp file)
        _stamp="$SELFHEAL_STATE/apt.stamp"; _now=$(date +%s); _last=0
        [ -f "$_stamp" ] && _last=$(cat "$_stamp" 2>/dev/null || echo 0)
        if [ $((_now - ${_last:-0})) -gt 600 ]; then
          sudo -n apt-get update -qq >/dev/null 2>&1 && echo "$_now" >"$_stamp"
        fi
        selfheal_log "installing pkg: $b"
        sudo -n apt-get install -y -qq "$b" >/dev/null 2>&1 \
          || selfheal_log "WARN: apt install $b failed (continuing)"
      else
        selfheal_log "WARN: missing '$b' and no non-interactive sudo — skipping (no hang)"
      fi
    fi
  done
}

selfheal_npx_shim() {  # Arena stdin-closed => npx needs --yes; resolve REAL npx first
  selfheal_have npx || { selfheal_log "npx absent — shim skipped"; return 0; }
  if [ ! -x "$HOME/.shim/npx" ]; then
    if ! selfheal_fix_mode; then selfheal_log "DRY: would create npx --yes shim (SELFHEAL_MODE=fix to allow)"; return 0; fi
    _real_npx=$(PATH="$(printf '%s' "$PATH" | tr ':' '\n' | grep -v -x "$HOME/.shim" | paste -sd: -)" command -v npx 2>/dev/null)
    [ -n "$_real_npx" ] || return 0
    mkdir -p "$HOME/.shim"
    printf '#!/bin/sh\nexec "%s" --yes "$@"\n' "$_real_npx" >"$HOME/.shim/npx" && chmod +x "$HOME/.shim/npx"
    selfheal_log "npx shim recreated -> $_real_npx"
  fi
  return 0
}

# --- llama.cpp binary: find, verify, or rebuild ------------------------------
selfheal_find_binary() {  # prints path on stdout, rc 0/4
  for name in llama-completion llama-cli; do
    for dir in "$SELFHEAL_LLAMA_DIR/build/bin" "$SELFHEAL_LLAMA_DIR/build"; do
      if [ -x "$dir/$name" ] && "$dir/$name" --version >/dev/null 2>&1; then
        printf '%s' "$dir/$name"; return 0
      fi
    done
  done
  return 4
}

selfheal_source_trusted() {  # rc 0: provenance ok; rc 4: unknown/untrusted origin
  [ -d "$SELFHEAL_LLAMA_DIR/.git" ] || { selfheal_log "llama.cpp is not a git checkout — provenance unknown"; return 4; }
  _remote=$(git -C "$SELFHEAL_LLAMA_DIR" config --get remote.origin.url 2>/dev/null || echo "")
  case "$_remote" in
    *github.com/ggml-org/llama.cpp*|*github.com/ggerganov/llama.cpp*) return 0 ;;
    *) selfheal_log "untrusted llama.cpp remote '$_remote' (expecting github.com/ggml-org/llama.cpp)"; return 4 ;;
  esac
}

selfheal_rebuild_llama() {  # only if a TRUSTED source checkout exists; portable fallback
  [ -f "$SELFHEAL_LLAMA_DIR/CMakeLists.txt" ] || { selfheal_log "no llama.cpp checkout at $SELFHEAL_LLAMA_DIR"; return 4; }
  if ! selfheal_fix_mode; then selfheal_log "DRY: would rebuild llama.cpp (SELFHEAL_MODE=fix to allow)"; return 4; fi
  if ! selfheal_source_trusted && [ "${SELFHEAL_LLAMA_ANY_REMOTE:-0}" != 1 ]; then
    selfheal_log "refusing to build unverified source (set SELFHEAL_LLAMA_ANY_REMOTE=1 to override with consent)"
    return 4
  fi
  selfheal_ensure_pkgs cmake g++ || :
  _blog="$SELFHEAL_HOME/build.log"   # verbose build output goes here, one summary line in main log
  selfheal_log "llama.cpp rebuild (native) — details: $_blog"
  if ( cd "$SELFHEAL_LLAMA_DIR" && cmake -B build ${SELFHEAL_CMAKE_FLAGS:-"-DGGML_NATIVE=ON -DCMAKE_BUILD_TYPE=Release"} >>"$_blog" 2>&1 \
       && cmake --build build --target llama-completion llama-cli llama-bench -j"$SELFHEAL_THREADS" >>"$_blog" 2>&1 ); then
    selfheal_log "native build ok"; return 0
  fi
  selfheal_log "native build failed — retry portable (-DGGML_NATIVE=OFF); details: $_blog"
  ( cd "$SELFHEAL_LLAMA_DIR" && cmake -B build -DGGML_NATIVE=OFF -DCMAKE_BUILD_TYPE=Release >>"$_blog" 2>&1 \
    && cmake --build build --target llama-completion llama-cli llama-bench -j"$SELFHEAL_THREADS" >>"$_blog" 2>&1 ) \
    && { selfheal_log "portable build ok"; return 0; } || { selfheal_log "ERROR: build failed (see $_blog)"; return 4; }
}

selfheal_extra_flags() {  # feature-detect from --help; never hallucinate flags
  _bin=$1; _out=""
  _help=$("$_bin" --help 2>&1 || :)
  case "$_help" in *flash-attn*|*"-fa"*) _out="$_out -fa";; esac
  case "$_help" in *no-warmup*) _out="$_out --no-warmup";; esac
  printf '%s' "$_out"
}

# --- model files: verify (magic+bytes), download w/ circuit breaker ----------
selfheal_model_field() {  # $1=role $2=field -> stdout (python3); "" if unavailable
  selfheal_have python3 || return 1
  python3 - "$SELFHEAL_MANIFEST" "$1" "$2" <<'PY' 2>/dev/null
import json,sys
m=json.load(open(sys.argv[1]))["models"][sys.argv[2]]
f=sys.argv[3]; v=m.get(f)
print("" if v is None else (v if isinstance(v,(int,str)) else json.dumps(v)))
PY
}

selfheal_gguf_ok() {  # $1=path $2=expected_bytes -> rc 0/1  (fast: size + magic)
  [ -f "$1" ] || return 1
  _sz=$(wc -c <"$1" 2>/dev/null | tr -d ' ')
  [ "$_sz" = "$2" ] || { selfheal_log "model size mismatch ($1: $_sz != $2)"; return 1; }
  [ "$(head -c 4 "$1" 2>/dev/null)" = "GGUF" ] || { selfheal_log "model bad magic ($1)"; return 1; }
  return 0
}

selfheal_sha_ok() {  # $1=path $2=expected_sha256 ("" = skip) -> rc 0/1 (deep: content hash)
  [ -z "$2" ] && return 0
  if selfheal_have sha256sum; then _h=$(sha256sum "$1" 2>/dev/null | cut -d' ' -f1)
  elif selfheal_have shasum; then _h=$(shasum -a 256 "$1" 2>/dev/null | cut -d' ' -f1)
  else selfheal_log "no sha256 tool — deep verify skipped"; return 0; fi
  [ "$_h" = "$2" ] || { selfheal_log "model hash mismatch ($1)"; return 1; }
  return 0
}

selfheal_breaker_open() {  # $1=role -> rc 0 if downloads suppressed
  _f="$SELFHEAL_STATE/fail_$1"; [ -f "$_f" ] || return 1
  _n=$(sed -n 1p "$_f" 2>/dev/null); _t=$(sed -n 2p "$_f" 2>/dev/null); _now=$(date +%s)
  [ $((_now - ${_t:-0})) -lt 1800 ] && [ "${_n:-0}" -ge 3 ] && { selfheal_log "breaker OPEN for $1 (${_n} fails)"; return 0; }
  return 1
}

selfheal_breaker_record() { selfheal_ensure_dirs; _f="$SELFHEAL_STATE/fail_$1"; _n=$(sed -n 1p "$_f" 2>/dev/null); printf '%s\n%s\n' "$(( ${_n:-0} + 1 ))" "$(date +%s)" >"$_f"; }
selfheal_breaker_reset()  { selfheal_fix_mode && rm -f "$SELFHEAL_STATE/fail_$1"; return 0; }  # deletions are fix-mode only, even state-cleanup

selfheal_ensure_model() {  # $1=role -> prints path rc 0, or rc 3
  _file=$(selfheal_model_field "$1" file); _bytes=$(selfheal_model_field "$1" bytes)
  _url=$(selfheal_model_field "$1" url); _hash=$(selfheal_model_field "$1" sha256)
  _path="$SELFHEAL_MODELS_DIR/$_file"
  if [ -z "$_file" ] || [ -z "$_bytes" ]; then selfheal_log "ERROR: role $1 unknown (manifest unreadable?)"; return 3; fi
  if selfheal_gguf_ok "$_path" "$_bytes"; then
    # deep content re-verify is opt-in (slow on purpose); fast gate already passed
    if [ "${SELFHEAL_DEEP_VERIFY:-0}" = 1 ] && ! selfheal_sha_ok "$_path" "$_hash"; then
      selfheal_log "deep verify failed -> re-download"
    else
      selfheal_breaker_reset "$1"; printf '%s' "$_path"; return 0
    fi
  fi
  if ! selfheal_fix_mode; then selfheal_log "DRY: would download $_file ($_bytes bytes, sha256 $_hash) (SELFHEAL_MODE=fix to allow)"; return 3; fi
  selfheal_breaker_open "$1" && return 3
  selfheal_ensure_pkgs curl || :
  selfheal_log "downloading $_file ($_bytes bytes)"
  if curl -sSL --fail --connect-timeout 15 --max-time 900 -o "$_path.part" "$_url" 2>/dev/null \
     && mv "$_path.part" "$_path" \
     && selfheal_gguf_ok "$_path" "$_bytes" && selfheal_sha_ok "$_path" "$_hash"; then
    selfheal_log "downloaded + verified (bytes+magic+sha256) $_file"; selfheal_breaker_reset "$1"; printf '%s' "$_path"; return 0
  fi
  rm -f "$_path.part" "$_path" 2>/dev/null   # NEVER leave a failed-verification artifact in place
  selfheal_breaker_record "$1"
  selfheal_log "ERROR: download/verify failed for $_file (artifact removed; breaker count updated)"
  return 3
}

# --- measured-throughput budgets (self-improving, see selfheal_tune.sh) ------
selfheal_budget() {  # $1=role $2=n_tokens -> integer seconds (never evals untrusted data)
  _role=$1; _n=${2:-128}
  if selfheal_have python3 && [ -f "$SELFHEAL_MANIFEST" ]; then
    _ans=$(python3 - "$SELFHEAL_MANIFEST" "$SELFHEAL_STATE/state.json" "$_role" "$_n" <<'PY' 2>/dev/null
import json,sys,math,os
deflt={"scout":(30,30,150),"spark":(30,34,150),"forge":(30,33,150),"sage":(45,72,300)}
try:
    m=json.load(open(sys.argv[1]))["models"][sys.argv[3]]
    t=m["timeout"]; base,per_ms,mx=t["base_s"],t["per_token_ms"],t["max_s"]
    nominal=max(1.0,float(m.get("default_tps",34)))
except Exception:
    base,per_ms,mx=deflt.get(sys.argv[3],(30,40,300)); nominal=34.0
n=max(0,int(sys.argv[4]))
ema=None
try:
    if os.path.exists(sys.argv[2]): ema=json.load(open(sys.argv[2])).get("ema_tps",{}).get(sys.argv[3])
except Exception: ema=None
scale=nominal/max(1.0,float(ema)) if ema else 1.0   # measured slower -> bigger budget
print(min(max(int(math.ceil(base+n*per_ms/1000.0*scale)),5),mx))
PY
)
    case "$_ans" in ''|*[!0-9]*) ;; *) printf '%s' "$_ans"; return 0;; esac
  fi
  # no-python fallback: compiled-in defaults, worst-case sage cap
  _d=$(( 30 + (_n * 40 + 999) / 1000 )); [ "$_d" -gt 300 ] && _d=300; printf '%s' "$_d"
}

# --- inference: timeout always, fallback chain, never silent-hang ------------
run_with_timeout() {  # $1=role $2=prompt $3=n -> stdout completion; rc 0/2/3/4
  _role=$1; _prompt=$2; _n=${3:-128}
  selfheal_have timeout || { selfheal_log "ERROR: timeout(1) missing — refusing unbounded inference"; return 2; }
  _bin=$(selfheal_find_binary) || { selfheal_log "binary missing -> rebuild"; selfheal_rebuild_llama && _bin=$(selfheal_find_binary); }
  [ -n "$_bin" ] && [ -x "$_bin" ] || return 4
  _model=$(selfheal_ensure_model "$_role") || return 3
  _ctx=$(selfheal_model_field "$_role" ctx); _ctx=${_ctx:-2048}
  _budget=$(selfheal_budget "$_role" "$_n")
  _flags=$(selfheal_extra_flags "$_bin")
  selfheal_log "run role=$_role n=$_n budget=${_budget}s bin=$(basename "$_bin") flags=${_flags:-none}"
  if selfheal_fix_mode; then _elog="$SELFHEAL_LOG"; else _elog=/dev/null; fi  # check mode stays zero-write
  timeout --signal=TERM --kill-after=5 "$_budget" \
    "$_bin" -m "$_model" -p "$_prompt" -n "$_n" -t "$SELFHEAL_THREADS" -c "$_ctx" $_flags 2>>"$_elog"
  _rc=$?
  if [ "$_rc" -ne 0 ]; then
    selfheal_log "primary failed rc=$_rc — fallback: same model, minimal flags"
    timeout --signal=TERM --kill-after=5 60 "$_bin" -m "$_model" -p "$_prompt" -n "$_n" -t "$SELFHEAL_THREADS" 2>>"$_elog" \
      && return 0 || { selfheal_log "ERROR: inference failed rc=$? ; try smaller role (scout)"; return 2; }
  fi
  return 0
}

selfheal_preflight() {  # rc 0 healthy, 5 degraded-but-usable
  selfheal_log "preflight start"
  selfheal_ensure_pkgs curl
  selfheal_npx_shim
  _rc=0
  selfheal_find_binary >/dev/null || _rc=5
  selfheal_log "preflight done rc=$_rc"
  return $_rc
}

# executable mode (sourcing mode: caller picks functions)
if [ "${0##*/}" = "selfheal_runner.sh" ]; then
  case "${1:-}" in
    preflight) selfheal_preflight ;;
    run) shift; run_with_timeout "$@" ;;
    model) shift; selfheal_ensure_model "$@" ;;
    *) echo "usage: selfheal_runner.sh preflight|run <role> <prompt> [n]|model <role>" >&2; exit 64 ;;
  esac
fi
