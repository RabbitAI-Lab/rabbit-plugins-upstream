#!/usr/bin/env bash
set -u

SKILL_DIR="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd -P)"
NODE_BIN="${NODE_BIN:-node}"
FIXTURE="$SKILL_DIR/scripts/self-test-fixture.mjs"
TRANSACTION="$SKILL_DIR/scripts/memory-transaction.mjs"
GATE="$SKILL_DIR/scripts/curation-gate.mjs"
LIST="$SKILL_DIR/scripts/transaction-list.mjs"
PREFLIGHT="$SKILL_DIR/scripts/migration-preflight.mjs"

PASS=0
FAIL=0
BASE=""

pass() {
  PASS=$((PASS + 1))
}
fail() {
  FAIL=$((FAIL + 1))
  printf 'FAIL: %s\n' "$1" >&2
}
expect_ok() {
  label="$1"
  shift
  if "$@" >/dev/null 2>&1; then pass; else fail "$label"; fi
}
expect_fail() {
  label="$1"
  shift
  if "$@" >/dev/null 2>&1; then fail "$label accepted unexpectedly"; else pass; fi
}
cleanup() {
  if [ -n "$BASE" ]; then "$NODE_BIN" "$FIXTURE" cleanup "$BASE" >/dev/null 2>&1 || true; fi
}
trap cleanup EXIT HUP INT TERM

if ! BASE="$("$NODE_BIN" "$FIXTURE" init)"; then
  printf '{"ok":false,"error":"fixture init failed"}\n'
  exit 1
fi

# Gate: initial, marked no-op, changed, and 10 KiB threshold.
W_GATE="$("$NODE_BIN" "$FIXTURE" workspace "$BASE" gate)"
OUT="$("$NODE_BIN" "$GATE" check "$W_GATE")"
printf '%s' "$OUT" | "$NODE_BIN" "$FIXTURE" assert-json fire true && pass || fail "initial gate"
printf '%s' "$OUT" | "$NODE_BIN" "$FIXTURE" assert-json-includes reasons no_successful_v2_review && pass || fail "initial gate reason"
expect_ok "gate mark" "$NODE_BIN" "$GATE" mark "$W_GATE" gate-baseline
OUT="$("$NODE_BIN" "$GATE" check "$W_GATE")"
printf '%s' "$OUT" | "$NODE_BIN" "$FIXTURE" assert-json fire false && pass || fail "marked gate no-op"
expect_ok "gate live edit" "$NODE_BIN" "$FIXTURE" write-live "$W_GATE" MEMORY.md memory-edited
OUT="$("$NODE_BIN" "$GATE" check "$W_GATE")"
printf '%s' "$OUT" | "$NODE_BIN" "$FIXTURE" assert-json-includes reasons memory_changed && pass || fail "gate changed reason"
W_BIG_GATE="$("$NODE_BIN" "$FIXTURE" workspace "$BASE" gate-big)"
expect_ok "large gate fixture" "$NODE_BIN" "$FIXTURE" write-live "$W_BIG_GATE" MEMORY.md large
OUT="$("$NODE_BIN" "$GATE" check "$W_BIG_GATE")"
printf '%s' "$OUT" | "$NODE_BIN" "$FIXTURE" assert-json-includes reasons memory_over_10k && pass || fail "10 KiB gate reason"

# Commit, rollback, new-file quarantine.
W_COMMIT="$("$NODE_BIN" "$FIXTURE" workspace "$BASE" commit)"
BEFORE="$("$NODE_BIN" "$FIXTURE" sha "$W_COMMIT" MEMORY.md)"
expect_ok "begin commit" "$NODE_BIN" "$TRANSACTION" begin "$W_COMMIT" commit-run MEMORY.md memory/new.md
expect_ok "stage commit memory" "$NODE_BIN" "$FIXTURE" write-stage "$W_COMMIT" commit-run MEMORY.md memory-edited
expect_ok "stage commit topic" "$NODE_BIN" "$FIXTURE" write-stage "$W_COMMIT" commit-run memory/new.md topic-edited
expect_ok "verify commit" "$NODE_BIN" "$TRANSACTION" verify "$W_COMMIT" commit-run
expect_ok "commit" "$NODE_BIN" "$TRANSACTION" commit "$W_COMMIT" commit-run
expect_ok "committed status" "$NODE_BIN" "$FIXTURE" assert-status "$W_COMMIT" commit-run committed
expect_ok "new topic committed" "$NODE_BIN" "$FIXTURE" assert-exists "$W_COMMIT" memory/new.md
expect_ok "rollback" "$NODE_BIN" "$TRANSACTION" rollback "$W_COMMIT" commit-run --confirm commit-run
expect_ok "rollback status" "$NODE_BIN" "$FIXTURE" assert-status "$W_COMMIT" commit-run rolled_back
expect_ok "memory restored" "$NODE_BIN" "$FIXTURE" assert-sha "$W_COMMIT" MEMORY.md "$BEFORE"
expect_ok "new topic removed" "$NODE_BIN" "$FIXTURE" assert-missing "$W_COMMIT" memory/new.md
expect_ok "new topic quarantined" "$NODE_BIN" "$FIXTURE" assert-exists "$W_COMMIT" .backup/memory-dreams/commit-run/quarantine/pre-rollback/memory/new.md

# Abort.
W_ABORT="$("$NODE_BIN" "$FIXTURE" workspace "$BASE" abort)"
BEFORE="$("$NODE_BIN" "$FIXTURE" sha "$W_ABORT" MEMORY.md)"
expect_ok "begin abort" "$NODE_BIN" "$TRANSACTION" begin "$W_ABORT" abort-run MEMORY.md
expect_ok "stage abort" "$NODE_BIN" "$FIXTURE" write-stage "$W_ABORT" abort-run MEMORY.md memory-edited
expect_ok "abort" "$NODE_BIN" "$TRANSACTION" abort "$W_ABORT" abort-run --confirm abort-run
expect_ok "abort status" "$NODE_BIN" "$FIXTURE" assert-status "$W_ABORT" abort-run aborted
expect_ok "abort preserves live" "$NODE_BIN" "$FIXTURE" assert-sha "$W_ABORT" MEMORY.md "$BEFORE"

# Concurrent edit rejection.
W_CONCURRENT="$("$NODE_BIN" "$FIXTURE" workspace "$BASE" concurrent)"
expect_ok "begin concurrent" "$NODE_BIN" "$TRANSACTION" begin "$W_CONCURRENT" concurrent-run MEMORY.md
expect_ok "stage concurrent" "$NODE_BIN" "$FIXTURE" write-stage "$W_CONCURRENT" concurrent-run MEMORY.md memory-edited
expect_ok "concurrent live edit" "$NODE_BIN" "$FIXTURE" write-live "$W_CONCURRENT" MEMORY.md concurrent
expect_fail "concurrent verify" "$NODE_BIN" "$TRANSACTION" verify "$W_CONCURRENT" concurrent-run

# Interrupted commit discovery and recovery.
W_CRASH="$("$NODE_BIN" "$FIXTURE" workspace "$BASE" crash)"
BEFORE="$("$NODE_BIN" "$FIXTURE" sha "$W_CRASH" MEMORY.md)"
expect_ok "legacy snapshot fixture" "$NODE_BIN" "$FIXTURE" legacy-snapshot "$W_CRASH" legacy-2026
expect_ok "begin crash" "$NODE_BIN" "$TRANSACTION" begin "$W_CRASH" crash-run MEMORY.md memory/crash.md
expect_ok "stage crash memory" "$NODE_BIN" "$FIXTURE" write-stage "$W_CRASH" crash-run MEMORY.md memory-edited
expect_ok "stage crash topic" "$NODE_BIN" "$FIXTURE" write-stage "$W_CRASH" crash-run memory/crash.md topic-edited
expect_ok "verify crash" "$NODE_BIN" "$TRANSACTION" verify "$W_CRASH" crash-run
expect_ok "simulate crash" "$NODE_BIN" "$FIXTURE" simulate-crash "$W_CRASH" crash-run
OUT="$("$NODE_BIN" "$LIST" "$W_CRASH")"
printf '%s' "$OUT" | "$NODE_BIN" "$FIXTURE" assert-json activeLock.runId crash-run && pass || fail "discover active lock"
printf '%s' "$OUT" | "$NODE_BIN" "$FIXTURE" assert-json unfinished.0.runId crash-run && pass || fail "discover unfinished run"
printf '%s' "$OUT" | "$NODE_BIN" "$FIXTURE" assert-json-includes legacySnapshots legacy-2026 && pass || fail "preserve legacy snapshot listing"
expect_ok "crash rollback" "$NODE_BIN" "$TRANSACTION" rollback "$W_CRASH" crash-run --confirm crash-run
expect_ok "crash memory restored" "$NODE_BIN" "$FIXTURE" assert-sha "$W_CRASH" MEMORY.md "$BEFORE"
expect_ok "crash new topic absent" "$NODE_BIN" "$FIXTURE" assert-missing "$W_CRASH" memory/crash.md
OUT="$("$NODE_BIN" "$LIST" "$W_CRASH")"
printf '%s' "$OUT" | "$NODE_BIN" "$FIXTURE" assert-json activeLock null && pass || fail "recovery releases lock"
printf '%s' "$OUT" | "$NODE_BIN" "$FIXTURE" assert-json unfinished '[]' && pass || fail "recovery clears unfinished"

# Secret, raw transcript, and 10 KiB verify rejection.
for MODE in secret raw large; do
  W_REJECT="$("$NODE_BIN" "$FIXTURE" workspace "$BASE" "reject-$MODE")"
  expect_ok "begin $MODE" "$NODE_BIN" "$TRANSACTION" begin "$W_REJECT" "$MODE-run" MEMORY.md
  expect_ok "stage $MODE" "$NODE_BIN" "$FIXTURE" write-stage "$W_REJECT" "$MODE-run" MEMORY.md "$MODE"
  expect_fail "verify $MODE" "$NODE_BIN" "$TRANSACTION" verify "$W_REJECT" "$MODE-run"
done

# Forbidden daily/nested paths, traversal, and symlinks.
W_PATH="$("$NODE_BIN" "$FIXTURE" workspace "$BASE" paths)"
expect_fail "daily note target" "$NODE_BIN" "$TRANSACTION" begin "$W_PATH" daily-run MEMORY.md memory/2026-07-19.md
expect_fail "nested L2 target" "$NODE_BIN" "$TRANSACTION" begin "$W_PATH" nested-run MEMORY.md memory/projects/topic.md
expect_fail "traversal target" "$NODE_BIN" "$TRANSACTION" begin "$W_PATH" traversal-run MEMORY.md ../escape.md
expect_ok "create topic symlink" "$NODE_BIN" "$FIXTURE" symlink "$W_PATH" memory/link.md "$W_PATH/MEMORY.md"
expect_fail "symlink target" "$NODE_BIN" "$TRANSACTION" begin "$W_PATH" symlink-run MEMORY.md memory/link.md
expect_ok "create workspace alias" "$NODE_BIN" "$FIXTURE" symlink "$W_PATH" alias "$W_PATH"
expect_fail "symlinked workspace alias" "$NODE_BIN" "$GATE" check "$W_PATH/alias"

# Compatibility classifier: exact schema accepted, schema drift rejected.
W_PREFLIGHT="$("$NODE_BIN" "$FIXTURE" workspace "$BASE" preflight)"
if "$NODE_BIN" "$FIXTURE" preflight "$W_PREFLIGHT" good | "$NODE_BIN" "$PREFLIGHT" "$W_PREFLIGHT" >/dev/null 2>&1; then pass; else fail "good capability preflight"; fi
if "$NODE_BIN" "$FIXTURE" preflight "$W_PREFLIGHT" bad-schema | "$NODE_BIN" "$PREFLIGHT" "$W_PREFLIGHT" >/dev/null 2>&1; then fail "bad capability schema accepted"; else pass; fi

if [ "$FAIL" -eq 0 ]; then
  printf '{"ok":true,"passed":%s,"failed":0}\n' "$PASS"
  exit 0
fi
printf '{"ok":false,"passed":%s,"failed":%s}\n' "$PASS" "$FAIL"
exit 1
