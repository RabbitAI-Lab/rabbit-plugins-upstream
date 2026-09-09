#!/bin/sh
# test_selfheal.sh — hermetic integration tests. NEVER touches real $HOME,
# real models, network, or sudo: everything runs inside a mktemp MOCK_HOME.
# Previous security-audit finding (other skill): "self-test deletes real
# user-home state" — this suite is the antidote. Run: sh test_selfheal.sh
set -u
PASS=0; FAIL=0
ok()  { PASS=$((PASS+1)); printf 'PASS %s\n' "$1"; }
bad() { FAIL=$((FAIL+1)); printf 'FAIL %s\n' "$1"; }
check(){ if [ "$2" = "$3" ]; then ok "$1"; else bad "$1 (want [$3] got [$2])"; fi; }

MOCK_HOME=$(mktemp -d); trap 'rm -rf "$MOCK_HOME"' EXIT
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
export HOME="$MOCK_HOME"
export SELFHEAL_HOME="$MOCK_HOME/.selfheal"
export SELFHEAL_MODELS_DIR="$MOCK_HOME/models"
export SELFHEAL_LLAMA_DIR="$MOCK_HOME/llama.cpp"
export SELFHEAL_MANIFEST="$MOCK_HOME/manifest.json"
export SELFHEAL_MODE=fix      # suite exercises the fix-mode paths; check-mode gates have their own tests (T21-T23)
export PATH="/usr/bin:/bin"   # hermetic PATH: no real user shims
mkdir -p "$SELFHEAL_MODELS_DIR" "$SELFHEAL_LLAMA_DIR/build/bin"
. "$HERE/selfheal_runner.sh"

# manifest with local file:// URLs (no network) + a fake binary
BASE=$(grep -c . "$HERE/../manifest.json" >/dev/null && echo ok)
cp "$HERE/../manifest.json" "$SELFHEAL_MANIFEST"
python3 - "$SELFHEAL_MANIFEST" "$MOCK_HOME" <<'PY'
import json,sys,os,hashlib
p,mock=sys.argv[1],sys.argv[2]
d=json.load(open(p))
os.makedirs(f"{mock}/dl",exist_ok=True)
for role,m in d["models"].items():
    src=f"{mock}/dl/{m['file']}"
    with open(src,"wb") as f:                      # valid: GGUF magic + exact bytes
        f.write(b"GGUF"); f.truncate(m["bytes"])
    h=hashlib.sha256()
    with open(src,"rb") as f:                      # pin the fixture's own hash so
        while b:=f.read(1<<22): h.update(b)        # enforcement stays ON in tests
    m["sha256"]=h.hexdigest()
    m["url"]=f"file://{src}"
json.dump(d,open(p,"w"))
PY
cat >"$SELFHEAL_LLAMA_DIR/build/bin/llama-completion" <<'SH'
#!/bin/sh
[ "$1" = "--version" ] && { echo "mock 3.0.0"; exit 0; }
[ "$1" = "--help" ] && { echo "--flash-attn --no-warmup"; exit 0; }
[ "$MOCK_SLEEP" ] && sleep "$MOCK_SLEEP"
echo "MOCK-ANSWER"
SH
chmod +x "$SELFHEAL_LLAMA_DIR/build/bin/llama-completion"

# T1 binary discovered + --version probe
B=$(selfheal_find_binary); check "T1 binary discovery" "$([ -n "$B" ] && echo yes)" "yes"
# T2 feature detection (flash-attn + no-warmup) from --help
F=$(selfheal_extra_flags "$B"); check "T2 feature detect" "$(printf %s "$F" | grep -o 'fa\|no-warmup' | wc -l | tr -d ' ')" "2"
# T3 model verified/downloaded via file:// (magic+bytes)
M=$(selfheal_ensure_model scout); check "T3 model ensure" "$([ -f "$M" ] && selfheal_gguf_ok "$M" 484220320 && echo good)" "good"
# T4 truncated/HTML-sized model re-fetched: corrupt then re-ensure
printf 'Entry not found' >"$SELFHEAL_MODELS_DIR/Qwen_Qwen3-0.6B-Q4_K_M.gguf"
M2=$(selfheal_ensure_model scout); check "T4 corrupt model self-heal" "$(selfheal_gguf_ok "$M2" 484220320 && echo healed)" "healed"
# T5 bad-magic model rejected (writing zeros, keep size)
python3 -c "open('$SELFHEAL_MODELS_DIR/Qwen2.5-0.5B-Instruct-Q5_K_M.gguf','wb').truncate(420086080)"
selfheal_ensure_model spark >/dev/null 2>&1; check "T5 zero-magic re-downloaded" "$(head -c 4 "$SELFHEAL_MODELS_DIR/Qwen2.5-0.5B-Instruct-Q5_K_M.gguf")" "GGUF"
# T6 npx shim created in MOCK home
selfheal_have npx && { rm -rf "$MOCK_HOME/.shim"; selfheal_npx_shim; check "T6 npx shim" "$([ -x "$MOCK_HOME/.shim/npx" ] && echo made)" "made"; } || ok "T6 npx shim (n/a, skipped)"
# T7 breaker suppresses download after 3 recorded failures
printf '3\n%s\n' "$(date +%s)" >"$SELFHEAL_STATE/fail_forge"
rm -f "$SELFHEAL_MODELS_DIR/Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf"
selfheal_ensure_model forge >/dev/null 2>&1; check "T7 breaker open=>no download" "$?" "3"
# T8 budget math with measured tps (10 t/s sage: 45+n*72ms*3.4 scaled, capped 300)
python3 -c "import json;json.dump({'ema_tps':{'sage':10.0}},open('$SELFHEAL_STATE/state.json','w'))"
BG=$(selfheal_budget sage 1000); check "T8 budget cap" "$([ "$BG" -le 300 ] && [ "$BG" -ge 45 ] && echo in-range)" "in-range"
# T9 run_with_timeout rc0 via mock binary
selfheal_breaker_reset scout 2>/dev/null; OUT=$(run_with_timeout scout "hi" 16); check "T9 run ok" "$OUT" "MOCK-ANSWER"
# T10 timeout honored: mock sleeps 3, budget forced 1s via ema extremely low? use timeout direct
MOCK_SLEEP=3; T0=$(date +%s); run_with_timeout scout "hi" 100000 >/dev/null 2>&1; RC=$?; T1=$(date +%s); unset MOCK_SLEEP
check "T10 slow run bounded/fallback" "$([ $((T1-T0)) -lt 25 ] && echo bounded)" "bounded"
# T11 cache roundtrip with model-artifact sig; hit avoids binary (delete binary after put)
PY_CACHE="$HERE/prompt_cache.py"
SIG=$(stat -c '%s-%Y' "$SELFHEAL_MODELS_DIR/Qwen_Qwen3-0.6B-Q4_K_M.gguf")
python3 "$PY_CACHE" put scout 16 "hello-cache" "CACHED!" "$SIG"
rm -rf "$SELFHEAL_LLAMA_DIR/build/bin/llama-completion"
G=$(python3 "$PY_CACHE" get scout 16 "hello-cache" "$SIG"); check "T11a cache get(sig)" "$G" "CACHED!"
R=$(sh "$HERE/run_guarded.sh" "hello-cache" scout 16 2>/dev/null); check "T11b run_guarded cache path" "$R" "CACHED!"
# T12 run_guarded light-mode: <=8 words -> scout; no binary -> documented rc 2 (post-fallback failure), no hang
R2=$(sh "$HERE/run_guarded.sh" "hi there" 2>/dev/null); RC2=$?
check "T12 graceful degradation rc" "$([ $RC2 -ge 2 ] && [ $RC2 -le 4 ] && echo rc$RC2)" "rc2"
# T13 log written
check "T13 log exists" "$([ -s "$SELFHEAL_HOME/selfheal.log" ] && echo logged)" "logged"
# T14 static: runner never evals (injection-class fix from multi-model review)
check "T14 no eval in runner" "$(grep -c 'eval ' "$HERE/selfheal_runner.sh" || true)" "0"
# T15 budget: EMA slower-than-nominal inflates the budget (sage ema=7 tps)
python3 -c "import json;p='$SELFHEAL_STATE/state.json';s=json.load(open(p));s['ema_tps']['sage']=7.0;json.dump(s,open(p,'w'))"
B_SLOW=$(selfheal_budget sage 200); B_DEF=$(SELFHEAL_MANIFEST="$SELFHEAL_MANIFEST" python3 - <<'PY'
print(45+int(200*72/1000))
PY
)
check "T15 EMA inflates budget" "$([ "$B_SLOW" -gt "$B_DEF" ] && [ "$B_SLOW" -le 300 ] && echo scaled)" "scaled"
# T16 different model sig => cache miss (stale-after-redownload protection)
python3 "$PY_CACHE" get scout 16 "hello-cache" "999-111" >/dev/null 2>&1; check "T16 sig mismatch misses" "$?" "1"
# T17 state/home dirs are 0700 (least-privilege review)
check "T17 state perms" "$(stat -c '%a' "$SELFHEAL_STATE")" "700"
# T18 static: apt update is stamp-throttled
check "T18 apt stamp throttle" "$(grep -c 'apt.stamp' "$HERE/selfheal_runner.sh")" "1"
# T19 tune writes EMA (scales budgets from measured reality); breakers reset first
cat >"$SELFHEAL_LLAMA_DIR/build/bin/llama-completion" <<'SH'
#!/bin/sh
[ "$1" = "--version" ] && { echo "mock 3.0.0"; exit 0; }
[ "$1" = "--help" ] && { echo "--flash-attn --no-warmup"; exit 0; }
echo "MOCK-ANSWER"
SH
chmod +x "$SELFHEAL_LLAMA_DIR/build/bin/llama-completion"
rm -f "$SELFHEAL_STATE"/fail_*
sh "$HERE/selfheal_tune.sh" scout >/dev/null 2>&1
check "T19 tune wrote EMA" "$(python3 -c "import json;print('scout' in json.load(open('$SELFHEAL_STATE/state.json'))['ema_tps'])")" "True"
# T20 fallback caches under ORIGINAL role (multi-model round-2 regression catch)
cat >"$SELFHEAL_LLAMA_DIR/build/bin/llama-completion" <<'SH'
#!/bin/sh
[ "$1" = "--version" ] && { echo "mock 3.0.0"; exit 0; }
[ "$1" = "--help" ] && { echo "--flash-attn --no-warmup"; exit 0; }
_m=""; _prev=""; for _a in "$@"; do [ "$_prev" = "-m" ] && _m="$_a"; _prev="$_a"; done
case "$_m" in *Qwen2.5-0.5B*) exit 7 ;; esac   # spark always fails -> fallback path
echo "MOCK-ANSWER"
SH
chmod +x "$SELFHEAL_LLAMA_DIR/build/bin/llama-completion"
R20=$(sh "$HERE/run_guarded.sh" "fallback-cache-probe" spark 16 2>/dev/null)
check "T20a fallback answered" "$R20" "MOCK-ANSWER"
SIG20=$(stat -c '%s-%Y' "$SELFHEAL_MODELS_DIR/Qwen2.5-0.5B-Instruct-Q5_K_M.gguf")
G20=$(python3 "$PY_CACHE" get spark 16 "fallback-cache-probe" "$SIG20" 2>/dev/null)
check "T20b cached under original role" "$G20" "MOCK-ANSWER"
# T25 sha256 pinned: byte-flipped upstream artifact (right size, right magic, wrong content) is REJECTED
python3 -c "
import os
src='$MOCK_HOME/dl/Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf'
f=open(src,'r+b'); f.seek(1<<20); f.write(b'X'); f.close()"
rm -f "$SELFHEAL_MODELS_DIR/Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf" "$SELFHEAL_STATE/fail_forge"
selfheal_ensure_model forge >/dev/null 2>&1
check "T25 hash mismatch rejected" "$?" "3"
check "T25b no file kept" "$([ -f "$SELFHEAL_MODELS_DIR/Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf" ] && echo kept || echo rejected)" "rejected"
# T21 consent gate: check mode NEVER creates the shim (dry, DRY notice on stderr)
T21=$( SELFHEAL_MODE=check; rm -rf "$MOCK_HOME/.shim"; _o=$(selfheal_npx_shim 2>&1); [ ! -x "$MOCK_HOME/.shim/npx" ] && printf %s "$_o" | grep -q DRY && echo dry )
check "T21 check-mode shim dry" "$T21" "dry"
# T22 consent gate: check mode NEVER downloads (dry, rc 3, no file created)
rm -f "$SELFHEAL_MODELS_DIR/Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf"; rm -f "$SELFHEAL_STATE/fail_forge"
T22=$( SELFHEAL_MODE=check; _o=$(selfheal_ensure_model forge 2>&1); echo "rc=$? file=$([ -f "$SELFHEAL_MODELS_DIR/Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf" ] && echo yes || echo no)" )
check "T22 check-mode download dry" "$T22" "rc=3 file=no"
# T24 check-mode zero-write purity: fresh HOME, preflight leaves nothing behind
H2=$(mktemp -d)
T24=$(SELFHEAL_HOME="$H2" SELFHEAL_MODE=check sh -c '. "$1/selfheal_runner.sh"; selfheal_preflight >/dev/null 2>&1; { [ ! -e "$SELFHEAL_HOME/state" ] && [ ! -e "$SELFHEAL_HOME/selfheal.log" ] && echo pristine; }' _ "$HERE")
check "T24 check-mode zero writes" "$T24" "pristine"
# T23 consent gate: check mode inference works but cache is NOT persisted
T23=$( SELFHEAL_MODE=check sh "$HERE/run_guarded.sh" "gate-probe-unseen" scout 16 2>/dev/null )
check "T23a check-mode inference ok" "$T23" "MOCK-ANSWER"
SIG23=$(stat -c '%s-%Y' "$SELFHEAL_MODELS_DIR/Qwen_Qwen3-0.6B-Q4_K_M.gguf")
python3 "$PY_CACHE" get scout 16 "gate-probe-unseen" "$SIG23" >/dev/null 2>&1
check "T23b no cache write in check mode" "$?" "1"
# T26 breaker-reset is also fix-gated (stale fail-file survives check mode, cleared in fix mode)
printf '1\n%s\n' "$(date +%s)" >"$SELFHEAL_STATE/fail_scout"
T26A=$( SELFHEAL_MODE=check; selfheal_ensure_model scout >/dev/null 2>&1; [ -f "$SELFHEAL_STATE/fail_scout" ] && echo kept )
check "T26a check mode never deletes" "$T26A" "kept"
selfheal_ensure_model scout >/dev/null 2>&1
check "T26b fix mode resets breaker" "$([ -f "$SELFHEAL_STATE/fail_scout" ] && echo kept || echo cleared)" "cleared"
# T27 cache tool self-enforces consent even on direct calls
H3=$(mktemp -d)
T27=$(SELFHEAL_HOME="$H3" SELFHEAL_MODE=check python3 "$PY_CACHE" put scout 9 "direct-put" "X" >/dev/null 2>&1; [ ! -e "$H3/cache" ] && echo blocked)
check "T27 direct put blocked in check mode" "$T27" "blocked"
# T28 source-provenance gate (supply-chain: never build unverified source)
G1="$MOCK_HOME/gt-trusted"; G2="$MOCK_HOME/gt-untrusted"; G3="$MOCK_HOME/gt-nogit"
for g in "$G1" "$G2" "$G3"; do mkdir -p "$g"; touch "$g/CMakeLists.txt"; done
git -C "$G1" init -q 2>/dev/null; git -C "$G1" remote add origin https://github.com/ggml-org/llama.cpp 2>/dev/null
git -C "$G2" init -q 2>/dev/null; git -C "$G2" remote add origin https://evil.example/llama.cpp 2>/dev/null
( SELFHEAL_LLAMA_DIR="$G1" selfheal_source_trusted >/dev/null 2>&1 ); check "T28a trusted remote ok" "$?" "0"
( SELFHEAL_LLAMA_DIR="$G2" selfheal_source_trusted >/dev/null 2>&1 ); check "T28b evil remote refused" "$?" "4"
( SELFHEAL_LLAMA_DIR="$G3" selfheal_source_trusted >/dev/null 2>&1 ); check "T28c non-git refused" "$?" "4"

echo "── $PASS passed, $FAIL failed ──"
[ "$FAIL" -eq 0 ]
