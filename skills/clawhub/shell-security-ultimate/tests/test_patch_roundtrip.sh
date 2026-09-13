#!/usr/bin/env bash
#
# Focused tests for patch-openclaw.sh / unpatch-openclaw.sh against a throwaway
# fake OpenClaw checkout. Nothing here touches a real one.
#
# The cases that matter are the failure modes: a patch that only half-applies,
# and an unpatch whose end marker is missing. Both used to report success — the
# first leaving uncompilable source, the second after deleting to end of file.
#
# Run:  bash tests/test_patch_roundtrip.sh

set -u

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SCRIPTS="$HERE/../scripts"
PATCH="$SCRIPTS/patch-openclaw.sh"
UNPATCH="$SCRIPTS/unpatch-openclaw.sh"

PASS=0
FAIL=0

ok()   { PASS=$((PASS + 1)); echo "  ok   — $1"; }
bad()  { FAIL=$((FAIL + 1)); echo "  FAIL — $1"; }
check() { if [ "$1" = "$2" ]; then ok "$3"; else bad "$3 (expected '$2', got '$1')"; fi; }

WORK=""
cleanup() { [ -n "$WORK" ] && rm -rf "$WORK"; }
trap cleanup EXIT

# ── A minimal checkout that looks enough like OpenClaw to be patchable ────────
make_checkout() {
    WORK="$(mktemp -d)"
    mkdir -p "$WORK/src/agents"
    cat > "$WORK/package.json" <<'JSON'
{ "name": "openclaw", "version": "0.0.0" }
JSON
    cat > "$WORK/src/agents/pi-tool-definition-adapter.ts" <<'TS'
import { z } from "zod";
import { logger } from "../logger.js";

export async function callTool(toolCallId, params, signal, onUpdate) {
  const tool = registry.get(normalizedName);
  if (!tool) {
    return jsonResult({ status: "error", error: "no such tool" });
  }
  return await tool.execute(toolCallId, params, signal, onUpdate);
}
TS
    cp "$WORK/src/agents/pi-tool-definition-adapter.ts" "$WORK/pristine.ts"
}

target() { echo "$WORK/src/agents/pi-tool-definition-adapter.ts"; }

run_patch()   { OPENCLAW_DIR="$WORK" bash "$PATCH" "$@" >/dev/null 2>&1; echo $?; }
run_unpatch() { OPENCLAW_DIR="$WORK" bash "$UNPATCH" "$@" >/dev/null 2>&1; echo $?; }
unchanged()   { cmp -s "$(target)" "$WORK/pristine.ts" && echo yes || echo no; }

echo "== happy path: patch then unpatch restores the file byte-for-byte"
make_checkout
check "$(run_patch --yes)" "0" "patch exits 0"
check "$(grep -c 'EXEC-DISPLAY-PATCH: before_tool_call hook' "$(target)")" "1" "one hook block inserted"
check "$(grep -c 'getGlobalHookRunner' "$(target)")" "2" "import plus one call site"
check "$(unchanged)" "no" "the file really changed"
check "$(run_unpatch)" "0" "unpatch exits 0"
check "$(unchanged)" "yes" "unpatch restored the original exactly"
cleanup

echo "== patch is idempotent and reports it"
make_checkout
run_patch --yes >/dev/null
check "$(run_patch --yes)" "0" "second patch exits 0 (already patched)"
check "$(grep -c 'EXEC-DISPLAY-PATCH: before_tool_call hook' "$(target)")" "1" "still only one block"
cleanup

echo "== --dry-run modifies nothing"
make_checkout
check "$(run_patch --dry-run)" "0" "dry run exits 0"
check "$(unchanged)" "yes" "dry run left the file alone"
cleanup

echo "== half-applied patch is refused, not reported as success"
make_checkout
# No logger import to anchor to: the hook would land, the import would not.
grep -v 'logger' "$(target)" > "$WORK/tmp.ts" && mv "$WORK/tmp.ts" "$(target)"
cp "$(target)" "$WORK/pristine.ts"
check "$(run_patch --yes)" "1" "patch fails when the import anchor is missing"
check "$(unchanged)" "yes" "the source was left untouched"
check "$(ls "$WORK/src/agents/" | grep -c 'backup' || true)" "0" "no backup litter from a refused patch"
cleanup

echo "== patch is refused when the tool.execute anchor is missing"
make_checkout
grep -v 'return await tool.execute' "$(target)" > "$WORK/tmp.ts" && mv "$WORK/tmp.ts" "$(target)"
cp "$(target)" "$WORK/pristine.ts"
check "$(run_patch --yes)" "1" "patch fails without the hook anchor"
check "$(unchanged)" "yes" "the source was left untouched"
cleanup

echo "== non-OpenClaw tree is refused"
make_checkout
echo '{ "name": "someone-elses-project" }' > "$WORK/package.json"
check "$(run_patch --yes)" "1" "patch refuses an unrelated checkout"
check "$(unchanged)" "yes" "the source was left untouched"
cleanup

echo "== unpatch refuses a block with no end marker instead of deleting to EOF"
make_checkout
run_patch --yes >/dev/null
LINES_BEFORE=$(wc -l < "$(target)")
grep -v 'END EXEC-DISPLAY-PATCH' "$(target)" > "$WORK/tmp.ts" && mv "$WORK/tmp.ts" "$(target)"
cp "$(target)" "$WORK/pristine.ts"
check "$(run_unpatch)" "1" "unpatch refuses when the end marker is gone"
check "$(unchanged)" "yes" "nothing was deleted"
LINES_AFTER=$(wc -l < "$(target)")
check "$LINES_AFTER" "$((LINES_BEFORE - 1))" "file kept its length (no run to end of file)"
cleanup

echo "== unpatch refuses an unexpected block size, and --force-range overrides"
make_checkout
run_patch --yes >/dev/null
awk '/const hookRunner = getGlobalHookRunner/ { print; print "        // someone added this line"; next } { print }' \
    "$(target)" > "$WORK/tmp.ts" && mv "$WORK/tmp.ts" "$(target)"
cp "$(target)" "$WORK/pristine.ts"
check "$(run_unpatch)" "1" "unpatch refuses a block it did not write"
check "$(unchanged)" "yes" "nothing was deleted"
check "$(run_unpatch --force-range)" "0" "--force-range removes it deliberately"
check "$(grep -c 'EXEC-DISPLAY-PATCH' "$(target)" || true)" "0" "markers are gone"
cleanup

echo "== unpatch on an unpatched file is a no-op"
make_checkout
check "$(run_unpatch)" "0" "unpatch exits 0 when there is nothing to remove"
check "$(unchanged)" "yes" "file untouched"
cleanup

echo "== the two scripts agree on how long the inserted block is"
DECLARED=$(grep -E '^EXPECTED_BLOCK_LINES=' "$UNPATCH" | cut -d= -f2)
ACTUAL=$(awk 'f && /^SNIPPET$/ { exit } f { n++ } /^HOOK_SNIPPET=/ { f = 1 } END { print n }' "$PATCH")
check "$DECLARED" "$ACTUAL" "EXPECTED_BLOCK_LINES matches the snippet in patch-openclaw.sh"

echo ""
echo "passed: $PASS   failed: $FAIL"
[ "$FAIL" -eq 0 ]
