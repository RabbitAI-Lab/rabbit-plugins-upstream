#!/usr/bin/env bash
#
# Focused tests for overseer.sh's runtime directory, privacy controls and
# lifecycle commands. Everything runs against a throwaway status directory and a
# throwaway workdir; no real overseer and no real workspace is touched.
#
# Run:  bash tests/test_overseer.sh

set -u

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OVERSEER="$HERE/../scripts/overseer.sh"

PASS=0
FAIL=0
ok()    { PASS=$((PASS + 1)); echo "  ok   — $1"; }
bad()   { FAIL=$((FAIL + 1)); echo "  FAIL — $1"; }
check() { if [ "$1" = "$2" ]; then ok "$3"; else bad "$3 (expected '$2', got '$1')"; fi; }
checkne() { if [ "$1" != "$2" ]; then ok "$3"; else bad "$3 (did not expect '$2')"; fi; }

SDIR=""
WDIR=""
teardown() {
    [ -n "$SDIR" ] && bash "$OVERSEER" --status-dir "$SDIR" --cleanup >/dev/null 2>&1
    [ -n "$WDIR" ] && rm -rf "$WDIR"
    SDIR=""; WDIR=""
}
trap teardown EXIT

setup() {
    SDIR="$(mktemp -d)/overseer"
    WDIR="$(mktemp -d)"
    echo "seed" > "$WDIR/seed.txt"
}

# Start the daemon and wait for the first status file. Interval is long enough
# that it is still alive when the lifecycle assertions run.
start_daemon() {
    setsid bash "$OVERSEER" --status-dir "$SDIR" --workdir "$WDIR" \
        --interval 5 "$@" >/dev/null 2>&1 &
    for _ in $(seq 1 60); do
        [ -s "$SDIR/status.json" ] && return 0
        sleep 0.2
    done
    return 1
}

status_field() { python3 -c "import json,sys;print(json.load(open(sys.argv[1]))${2})" "$1" 2>/dev/null; }

echo "== the default runtime directory is per-user, not the shared /tmp/overseer"
DEFAULT_PATH="$(bash "$OVERSEER" --status-path)"
checkne "$DEFAULT_PATH" "/tmp/overseer/status.json" "default status path is not the shared directory"
check "$(dirname "$(dirname "$DEFAULT_PATH")" | grep -c .)" "1" "default path resolves to something"
check "$(stat -c '%a' "$(dirname "$DEFAULT_PATH")")" "700" "the runtime directory is mode 0700"

echo "== --status-dir and --status-path agree"
setup
check "$(bash "$OVERSEER" --status-dir "$SDIR" --status-path)" "$SDIR/status.json" "--status-path honours --status-dir"
teardown

echo "== --stop on a directory with no daemon is harmless"
setup
mkdir -p "$SDIR"
check "$(bash "$OVERSEER" --status-dir "$SDIR" --stop >/dev/null 2>&1; echo $?)" "0" "--stop exits 0 when nothing is running"
teardown

echo "== a running daemon writes parseable status, a pid file, and stops on request"
setup
if start_daemon; then
    ok "status file appeared"
    check "$(status_field "$SDIR/status.json" "['cycle']" | grep -c '^[0-9]')" "1" "status.json is valid JSON with a cycle number"
    check "$([ -f "$SDIR/overseer.pid" ] && echo yes || echo no)" "yes" "a pid file was written"
    PID="$(cat "$SDIR/overseer.pid")"
    check "$([ -d "/proc/$PID" ] && echo yes || echo no)" "yes" "that pid is alive"
    bash "$OVERSEER" --status-dir "$SDIR" --stop >/dev/null 2>&1
    sleep 0.5
    check "$([ -d "/proc/$PID" ] && echo yes || echo no)" "no" "--stop stopped the daemon"
    check "$(grep -c 'Overseer stopped' "$SDIR/overseer.log" || true)" "1" "the exit trap logged the stop"
    check "$([ -f "$SDIR/overseer.pid" ] && echo yes || echo no)" "no" "--stop removed the pid file"
else
    bad "daemon never wrote a status file"
fi
teardown

echo "== filenames are recorded by default and suppressed by --no-filenames"
setup
if start_daemon; then
    sleep 0.2
    echo "change" > "$WDIR/a-revealing-project-name.txt"
    sleep 6
    check "$(status_field "$SDIR/status.json" "['filesystem']['filenames_recorded']")" "True" "filenames_recorded is true by default"
    bash "$OVERSEER" --status-dir "$SDIR" --stop >/dev/null 2>&1
else
    bad "daemon never wrote a status file"
fi
teardown

setup
if start_daemon --no-filenames; then
    sleep 0.2
    echo "change" > "$WDIR/a-revealing-project-name.txt"
    sleep 6
    check "$(status_field "$SDIR/status.json" "['filesystem']['filenames_recorded']")" "False" "--no-filenames sets filenames_recorded false"
    check "$(status_field "$SDIR/status.json" "['filesystem']['recent_files']")" "" "--no-filenames records no basenames"
    checkne "$(status_field "$SDIR/status.json" "['filesystem']['changes_since_last']")" "" "the change count is still reported"
    bash "$OVERSEER" --status-dir "$SDIR" --stop >/dev/null 2>&1
else
    bad "daemon never wrote a status file"
fi
teardown

echo "== a quote in a filename does not corrupt the status JSON"
setup
if start_daemon; then
    sleep 0.2
    touch "$WDIR/od\"d\\name.txt" 2>/dev/null || touch "$WDIR/oddname.txt"
    sleep 6
    check "$(status_field "$SDIR/status.json" "['cycle']" | grep -c '^[0-9]')" "1" "status.json still parses"
    bash "$OVERSEER" --status-dir "$SDIR" --stop >/dev/null 2>&1
else
    bad "daemon never wrote a status file"
fi
teardown

echo "== --cleanup removes the daemon's state"
setup
if start_daemon; then
    bash "$OVERSEER" --status-dir "$SDIR" --cleanup >/dev/null 2>&1
    check "$([ -f "$SDIR/status.json" ] && echo yes || echo no)" "no" "status file removed"
    check "$([ -f "$SDIR/overseer.log" ] && echo yes || echo no)" "no" "log removed"
    check "$([ -f "$SDIR/overseer.pid" ] && echo yes || echo no)" "no" "pid file removed"
else
    bad "daemon never wrote a status file"
fi
teardown

echo "== --help documents the controls a reviewer looks for"
HELP="$(bash "$OVERSEER" --help)"
for flag in --stop --cleanup --no-filenames --voice-files --status-dir; do
    MENTIONS="$(printf '%s' "$HELP" | grep -c -- "$flag" || true)"
    if [ "${MENTIONS:-0}" -ge 1 ]; then ok "--help mentions $flag"; else bad "--help does not mention $flag"; fi
done

echo ""
echo "passed: $PASS   failed: $FAIL"
[ "$FAIL" -eq 0 ]
