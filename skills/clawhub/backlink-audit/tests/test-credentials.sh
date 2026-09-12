#!/usr/bin/env bash
# Focused tests: the backlinks.sh API key lives in the OS keychain or nowhere.
# HOME is redirected to a temp dir for every run, so the real keychain entry and the
# real ~/.config are never touched.
set -uo pipefail
SRC="$(cd "$(dirname "$0")/.." && pwd)"
S="$SRC/scripts/backlink-audit.mjs"
H=$(mktemp -d /tmp/bl-test.XXXXXX)
CRED="$H/.config/backlinks-sh/credentials.json"
pass=0; fail=0
ok(){ printf '  \033[32mPASS\033[0m %s\n' "$1"; pass=$((pass+1)); }
no(){ printf '  \033[31mFAIL\033[0m %s\n       %s\n' "$1" "$2"; fail=$((fail+1)); }
run(){ HOME="$H" node "$S" "$@" 2>&1; }

echo "== --login refuses instead of writing a plaintext file =="
out=$(printf %s 'sk-secret-value' | run --login); rc=$?
if [[ $rc -ne 0 ]]; then ok "--login exits non-zero when no keychain is available"; else no "--login exit code" "rc=$rc"; fi
if [[ ! -e "$CRED" ]]; then ok "no credentials.json was created (was: written silently at 0600)"; else no "no plaintext file created" "$CRED exists: $(cat "$CRED")"; fi
echo "$out" | grep -q "will not fall back to a plaintext file" && ok "--login says why it refused" || no "--login explains refusal" "$out"
echo "$out" | grep -q "BACKLINKS_SH_API_KEY" && ok "--login offers the env-var route instead" || no "--login offers alternative" "$out"
if ! grep -rq 'sk-secret-value' "$H" 2>/dev/null; then ok "the key appears nowhere under HOME"; else no "key leaked to disk" "$(grep -rl 'sk-secret-value' "$H")"; fi

echo "== --login still refuses a key on argv (stdin only) =="
out=$(HOME="$H" node "$S" --login </dev/null 2>&1); rc=$?
echo "$out" | grep -q "STDIN" && ok "--login with no stdin points at STDIN, never argv" || no "--login stdin guidance" "$out"

echo "== a legacy plaintext file is NOT accepted as a credential =="
mkdir -p "$(dirname "$CRED")"
printf '{"api_key":"legacy-plaintext-key"}' > "$CRED"; chmod 600 "$CRED"
out=$(run example.com --source backlinks 2>&1); rc=$?
if [[ $rc -ne 0 ]]; then ok "backlinks source fails rather than using the plaintext file"; else no "should not authenticate from file" "$out"; fi
echo "$out" | grep -q "NO LONGER READ" && ok "explains the legacy file is no longer read" || no "legacy-file explanation" "$out"
echo "$out" | grep -qi "keychain" && ok "points at --login / the keychain for migration" || no "migration guidance" "$out"
if ! echo "$out" | grep -q "legacy-plaintext-key"; then ok "the stale key is never echoed to the terminal"; else no "key echoed" "$out"; fi

echo "== --logout still deletes the legacy file (off switch keeps working) =="
out=$(run --logout); rc=$?
if [[ ! -e "$CRED" ]]; then ok "--logout deleted the legacy credentials.json"; else no "--logout deletes file" "still present"; fi
echo "$out" | grep -qi "does NOT revoke\|rotate or delete" && ok "--logout says local removal is not server-side revocation" || no "--logout revoke note" "$out"

echo "== env var still works and never touches disk =="
out=$(HOME="$H" BACKLINKS_SH_API_KEY=env-only-key node "$S" example.com --source backlinks 2>&1)
if ! echo "$out" | grep -q "NO LONGER READ"; then ok "env var short-circuits the legacy warning"; else no "env var precedence" "$out"; fi
if [[ ! -e "$CRED" ]]; then ok "using the env var writes no credential file"; else no "env var wrote a file" "exists"; fi

echo "== source-level guarantees =="
if ! grep -qE 'writeFileSync\([^)]*CRED_FILE' "$S"; then ok "no code path writes CRED_FILE any more"; else no "CRED_FILE is still written" "$(grep -n 'writeFileSync.*CRED_FILE' "$S")"; fi
if grep -q 'unlinkSync(CRED_FILE)' "$S"; then ok "CRED_FILE is still DELETED by --logout (cleanup preserved)"; else no "--logout no longer deletes CRED_FILE" "missing"; fi
# macOS branch: the secret must reach `security` on stdin, never as an argv element.
if grep -q '"add-generic-password", "-U", "-s", KC_SERVICE, "-a", KC_ACCOUNT, "-w", key' "$S"; then
  no "macOS keychain write keeps the key off argv" "still passes key as an argv element"
else ok "macOS keychain write no longer passes the key as an argv element"; fi
if grep -q 'execFileSync("security", \["-i"\]' "$S"; then ok "macOS uses \`security -i\` (command on stdin)"; else no "macOS uses security -i" "not found"; fi
if grep -q 'input: `add-generic-password' "$S"; then ok "the add-generic-password command is fed via stdin"; else no "stdin input" "not found"; fi
if grep -q 'if (kcGet() !== key) return false' "$S"; then ok "macOS write is verified by read-back (security -i exits 0 on failure)"; else no "read-back verification" "not found"; fi

find "$H" -mindepth 1 -delete 2>/dev/null; rmdir "$H" 2>/dev/null
echo; echo "backlink-audit: $pass passed, $fail failed"
[[ $fail -eq 0 ]]
