#!/bin/bash
# integrate.sh — wire this skill into an Arena/OpenClaw workspace.
#
# Idempotent and MAKES ZERO API CALLS. Everything it needs is either on disk
# already or shipped in health.json. Run it after installing the skill.
#
#   bash skills/free-tier-ai-router/integrate.sh
#
# What it does:
#   1. finds the skill wherever ClawHub installed it
#   2. creates ~/ai as a stable entry point
#   3. verifies which provider credentials exist (file checks only — no network)
#   4. seeds the cooldown state from health.json so the first real request
#      never wastes calls on routes already proven dead
#   5. prints exactly what is usable, and what is missing and why

set -u
SELF="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROUTER="$SELF/router.py"
HOME_DIR="${HOME:-/home/user}"

echo "🎛️  free-tier-ai-router — workspace integration"
echo "    skill dir: $SELF"

[ -f "$ROUTER" ] || { echo "    ❌ router.py not found next to this script"; exit 1; }

# ── 0. STALE-INSTALL GUARD ───────────────────────────────────────────────────
# The ClawHub registry can pin `latestVersion` to an older release even after a
# newer one publishes successfully (observed: 1.2.0/1.3.0 published OK, installs
# kept serving 1.1.0). A stale copy is missing the concurrency lock and the
# known-dead-route table, so it CRASHES under parallel use and wastes API calls.
# Detect it from the code itself rather than trusting the version string.
# Compare the installed router.py against the checksum recorded in the shipped
# blob. FIX 16: the previous detector grepped for specific features (fcntl,
# DEAD_ROUTES). Any copy containing those passed — even when it lacked NEWER
# fixes. A v1.5 install silently kept the key-in-`ps` vulnerability. Checksum
# comparison is version-agnostic: it detects ANY drift, now and in future.
STALE=0
BLOB=""
[ -f "$SELF/router_fixed.json" ] && BLOB="$SELF/router_fixed.json"
[ -z "$BLOB" ] && [ -f "$SELF/router_fixed.b64" ] && BLOB="$SELF/router_fixed.b64"
if [ -n "$BLOB" ]; then
  case "$BLOB" in
    *.json) WANT=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['sha256'])" "$BLOB" 2>/dev/null) ;;
    *)      WANT=$(grep -m1 '^# sha256:' "$BLOB" | awk '{print $3}') ;;
  esac
  HAVE=$(python3 -c "import hashlib,sys;print(hashlib.sha256(open(sys.argv[1],'rb').read()).hexdigest())" "$ROUTER" 2>/dev/null)
  [ -n "$WANT" ] && [ "$WANT" != "$HAVE" ] && STALE=1
else
  # no blob to compare against — fall back to feature detection
  grep -q "fcntl"       "$ROUTER" || STALE=1
  grep -q "DEAD_ROUTES" "$ROUTER" || STALE=1
fi
if [ "$STALE" = "1" ]; then
  echo "    ⚠️  STALE INSTALL DETECTED — this copy predates the concurrency and"
  echo "        zero-waste fixes (registry served an older version)."
  # PRIMARY REPAIR: the correct router.py ships INSIDE this package as a
  # base64 blob, so a clean machine with no local source can still self-repair.
  # (Without this the skill was dead on arrival for every new user — verified.)
  if [ -n "$BLOB" ]; then
    if python3 - "$SELF" "$BLOB" <<'EOF_PATCH'
import base64, hashlib, os, sys, json
skill, blob = sys.argv[1], sys.argv[2]
if blob.endswith('.json'):
    j = json.load(open(blob)); want = j['sha256']; data = base64.b64decode(j['router_py_b64'])
else:
    raw = open(blob).read(); want = None; b64 = []
    for line in raw.splitlines():
        if line.startswith('# sha256:'): want = line.split(':', 1)[1].strip()
        elif line and not line.startswith('#'): b64.append(line.strip())
    data = base64.b64decode(''.join(b64))
got = hashlib.sha256(data).hexdigest()
if want and got != want:
    print(f'    checksum mismatch ({got[:12]} != {want[:12]})'); sys.exit(1)
open(os.path.join(skill, 'router.py'), 'wb').write(data)
sys.exit(0)
EOF_PATCH
    then
      echo "    🔧 repaired from bundled blob (checksum verified)"
      STALE=0
    fi
  fi

  FRESH=""
  for c in "$HOME_DIR/skill_inventions/free-tier-ai-router/router.py" \
           "$SELF/../free-tier-ai-router/router.py"; do
    if [ -f "$c" ] && grep -q "DEAD_ROUTES" "$c"; then FRESH="$(dirname "$c")"; break; fi
  done
  if [ "$STALE" = "0" ]; then
    : # already repaired from the bundled blob
  elif [ -n "$FRESH" ]; then
    cp "$FRESH/router.py" "$ROUTER"
    [ -f "$FRESH/health.json" ] && cp "$FRESH/health.json" "$SELF/health.json"
    # Sync the DOCS too. Patching only the code leaves the user reading stale
    # v1.1.0 instructions (no mention of integrate.sh) while running new code.
    [ -f "$FRESH/SKILL.md" ] && cp "$FRESH/SKILL.md" "$SELF/SKILL.md"
    echo "    🔧 patched from local source: $FRESH (code + docs)"
  else
    # No blob and no local source. Report precisely WHICH fixes are missing so
    # the user can judge the risk, instead of a blanket refusal. The registry
    # can lag several releases behind what was published (observed: 1.8.0
    # published, installs still served 1.6.1), so this path is reachable in
    # normal use and must stay informative rather than fatal.
    echo "    ⚠️  no repair payload available (registry may be serving an older"
    echo "        release). Checking which fixes this copy is missing:"
    grep -q "fcntl.flock"                 "$ROUTER" || echo "        ❌ concurrency lock — DO NOT run in parallel"
    grep -q "aihdr"                       "$ROUTER" || echo "        ❌ key-in-process-list fix — avoid on shared hosts"
    grep -q "DEAD_ROUTES"                 "$ROUTER" || echo "        ❌ dead-route table — wastes API calls"
    grep -q "cd - time.time() > 86400"    "$ROUTER" || echo "        ⚠️  cooldown clamp — a corrupt timestamp can brick a route"
    grep -q "max-tokens must be >= 1"     "$ROUTER" || echo "        ⚠️  input validation — bad args cost API calls"
    echo "        Single-process use is safe if only the ⚠️ items are listed."
  fi
fi
command -v python3 >/dev/null || { echo "    ❌ python3 required"; exit 1; }
command -v curl    >/dev/null || { echo "    ❌ curl required"; exit 1; }

# ── 0b. FIX AUDIT (always runs) ──────────────────────────────────────────────
# Even a copy that passes the staleness check may lack the newest fixes when the
# registry lags behind what was published. Report precisely what is missing so
# the user can judge risk, rather than assuming "not stale" means "current".
MISSING_CRIT=0
grep -q "fcntl.flock"              "$ROUTER" || { echo "    ❌ MISSING concurrency lock — do NOT run in parallel"; MISSING_CRIT=1; }
grep -q "aihdr"                    "$ROUTER" || { echo "    ❌ MISSING key-hiding fix — key visible in \`ps\` on shared hosts"; MISSING_CRIT=1; }
grep -q "DEAD_ROUTES"              "$ROUTER" || { echo "    ❌ MISSING dead-route table — wastes API calls"; MISSING_CRIT=1; }
grep -q "cd - time.time() > 86400" "$ROUTER" || echo "    ⚠️  missing cooldown clamp (fix 17) — a corrupt timestamp can brick a route"
grep -q "max-tokens must be >= 1"  "$ROUTER" || echo "    ⚠️  missing input validation — bad args cost API calls"
[ "$MISSING_CRIT" = "0" ] && echo "    ✅ all critical fixes present"

# ── 1. stable entry point ────────────────────────────────────────────────────
# GUARD: only (re)point ~/ai when this really is the user's installed skill.
# Running integrate.sh from a scratch copy used to silently repoint the main
# entry point at throwaway code (verified: skill dir /tmp/q3 rewrote ~/ai).
WRITE_ENTRY=1
case "$SELF" in
  "$HOME_DIR"/*) : ;;                       # inside HOME -> legitimate
  *) if [ -e "$HOME_DIR/ai" ]; then
       WRITE_ENTRY=0
       echo "    ↷ skill lives outside \$HOME ($SELF) and $HOME_DIR/ai already"
       echo "      exists — leaving it untouched. Run this copy directly:"
       echo "        python3 $ROUTER \"prompt\""
     fi ;;
esac
if [ "$WRITE_ENTRY" = "1" ]; then
cat > "$HOME_DIR/ai" <<EOF
#!/bin/bash
# ai — entry point for free-tier-ai-router (generated by integrate.sh)
exec python3 "$ROUTER" "\$@"
EOF
chmod +x "$HOME_DIR/ai"
echo "    ✅ entry point: $HOME_DIR/ai"
fi

# ── 2. credential discovery — file checks only, NO network ───────────────────
FOUND=0; MISSING=""
for p in mistral gemini openrouter kilo cerebras; do
  if [ -f "$HOME_DIR/.config/$p/credentials.json" ]; then
    if python3 -c "import json,sys;json.load(open('$HOME_DIR/.config/$p/credentials.json'))" 2>/dev/null; then
      FOUND=$((FOUND+1))
    else
      MISSING="$MISSING $p(corrupt-json)"
    fi
  else
    MISSING="$MISSING $p(absent)"
  fi
done
echo "    ✅ providers with valid credential files: $FOUND/5"
[ -n "$MISSING" ] && echo "    ⚠️  unavailable:$MISSING"

# restore from a workspace backup if present (survives snapshot wipes)
if [ "$FOUND" -eq 0 ] && [ -d "$HOME_DIR/cred_backup" ]; then
  echo "    🔧 no credentials found — restoring from cred_backup/"
  for p in mistral gemini openrouter kilo cerebras; do
    if [ -f "$HOME_DIR/cred_backup/$p/credentials.json" ]; then
      mkdir -p "$HOME_DIR/.config/$p"
      cp "$HOME_DIR/cred_backup/$p/credentials.json" "$HOME_DIR/.config/$p/credentials.json"
      chmod 600 "$HOME_DIR/.config/$p/credentials.json"
    fi
  done
fi

# ── 3. seed state from shipped health data (no API calls) ────────────────────
python3 - "$SELF" <<'PY'
import json, os, sys, time
skill = sys.argv[1]
state = os.path.expanduser('~/.cache/ai_router/state.json')
os.makedirs(os.path.dirname(state), exist_ok=True)
try:
    with open(os.path.join(skill, 'health.json')) as f: h = json.load(f)
except Exception:
    print('    ⚠️  health.json missing — dead routes will be rediscovered (costs calls)'); raise SystemExit
try:
    with open(state) as f: st = json.load(f)
except Exception:
    st = {}
n = 0
for d in h.get('dead_providers', []):
    st[f"PROVIDER|{d['provider']}"] = {'cooldown_until': time.time() + 86400,
                                       'reason': d.get('reason', 'known unavailable')}
    n += 1
for d in h.get('dead_routes', []):
    st[f"{d['provider']}|{d['model']}"] = {'cooldown_until': time.time() + 86400,
                                           'reason': d.get('reason', 'probed dead')}
    n += 1
tmp = f'{state}.{os.getpid()}.tmp'
with open(tmp, 'w') as f: json.dump(st, f)
os.replace(tmp, state)
print(f'    ✅ seeded {n} known-dead routes/providers — 0 API calls will be wasted on them')
PY

# ── 4. offline readiness report ──────────────────────────────────────────────
echo
if [ "$FOUND" -eq 0 ]; then
  # FIX 22: previously printed "Ready" and a list of ✅ routes with zero keys
  # installed, then failed with an opaque error on first use.
  echo "    ⚠️  NOT READY — no API keys installed yet."
  echo
  python3 "$ROUTER" --setup 2>/dev/null
  echo "    Shortcut once you have a key:"
  echo "        $HOME_DIR/ai --setup <your-key>     # provider auto-detected"
  echo "        $HOME_DIR/ai --doctor               # verify setup"
else
  python3 "$ROUTER" --plan 2>/dev/null | head -6
  echo
  echo "    Ready.  Try:  ai \"your question\"        (add -t code | -t best | -q 5)"
  echo "                  ai --doctor              (diagnose setup)"
  echo "                  ai --status              (live budgets)"
fi
