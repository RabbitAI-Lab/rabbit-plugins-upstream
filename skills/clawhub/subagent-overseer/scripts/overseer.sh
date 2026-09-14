#!/usr/bin/env bash
# subagent-overseer — Pull-based sub-agent monitor daemon.
#
# Accumulates process-level and session-level data every INTERVAL seconds.
# Writes a machine-readable status file. The heartbeat handler reads it.
# Zero AI tokens. Zero push notifications. Pure bash + /proc + openclaw CLI.
#
# Usage: overseer.sh [--interval 180] [--workdir /path] [--labels l1,l2,...]
#                    [--max-stale 4] [--voice] [--voice-files] [--no-filenames]
#                    [--status-dir DIR] [--status-path] [--stop] [--cleanup]
# Defaults: interval=180, max-stale=4 (~12min), workdir=cwd
#
# Privacy note: the status file records how many files changed under --workdir and
# the basenames of up to five of them. Those names can say a lot about what you are
# working on, so the runtime directory is per-user and mode 0700 by default, and
# --no-filenames drops the names entirely. Voice alerts never read filenames aloud
# unless you ask for that with --voice-files.

set -euo pipefail

# ── Defaults ──────────────────────────────────────────────────────────────────
INTERVAL=180
WORKDIR="$(pwd)"
LABELS=""
MAX_STALE=4
VOICE=false
VOICE_FILES=false
RECORD_FILENAMES=true
DO_STOP=false
DO_CLEANUP=false
PRINT_STATUS_PATH=false

# Where the daemon keeps its state. The old default, /tmp/overseer, is one shared
# directory for every user on the machine — and it holds the names of files your
# agents just touched. Prefer the per-user runtime directory; fall back to a
# uid-suffixed path in /tmp. Either way it is created 0700.
default_status_dir() {
    if [[ -n "${XDG_RUNTIME_DIR:-}" && -d "${XDG_RUNTIME_DIR}" ]]; then
        echo "${XDG_RUNTIME_DIR}/overseer"
    else
        echo "/tmp/overseer-$(id -u)"
    fi
}
STATUS_DIR="${OVERSEER_DIR:-$(default_status_dir)}"

# ── Parse args ────────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
    case "$1" in
        --interval)  INTERVAL="$2";   shift 2 ;;
        --workdir)   WORKDIR="$2";    shift 2 ;;
        --labels)    LABELS="$2";     shift 2 ;;
        --max-stale) MAX_STALE="$2";  shift 2 ;;
        --voice)     VOICE=true;      shift   ;;
        --voice-files)  VOICE=true; VOICE_FILES=true; shift ;;
        --no-filenames) RECORD_FILENAMES=false;       shift ;;
        --status-dir)   STATUS_DIR="$2";  shift 2 ;;
        --status-path)  PRINT_STATUS_PATH=true;       shift ;;
        --stop)         DO_STOP=true;                 shift ;;
        --cleanup)      DO_CLEANUP=true;              shift ;;
        --help|-h)
            cat <<'USAGE'
Usage: overseer.sh [options]

Watch OpenClaw sub-agents from the OS side and write a status file the heartbeat
handler can read for free. Run it in the background when you spawn sub-agents.

Options:
  --interval SEC    Seconds between checks (default 180)
  --workdir DIR     Directory watched for file changes (default: cwd).
                    Scope this narrowly — its filenames end up in the status file.
  --labels l1,l2    Only track these sub-agent labels
  --max-stale N     Cycles with no file changes before a label is "stuck" (default 4)
  --voice           Speak alerts locally via the `jarvis` command. Counts only.
  --voice-files     Speak alerts AND read changed filenames aloud. Implies --voice.
                    Anyone within earshot hears what you are working on.
  --no-filenames    Never record filenames anywhere: the status file gets the
                    change count and nothing else.
  --status-dir DIR  Where to keep status/log/pid (default: per-user runtime dir)
  --status-path     Print the path of the status file and exit
  --stop            Stop the running overseer and exit
  --cleanup         Stop it, then delete its status, log, marker and pid files
  --help, -h        This text

Environment:
  OVERSEER_DIR      Same as --status-dir.

Writes only inside the status directory. No network calls. No credentials.
USAGE
            exit 0 ;;
        *) echo "Unknown arg: $1" >&2; exit 1 ;;
    esac
done

LOGFILE="$STATUS_DIR/overseer.log"
STATUS_FILE="$STATUS_DIR/status.json"
LOCKFILE="$STATUS_DIR/overseer.lock"
PIDFILE="$STATUS_DIR/overseer.pid"
MARKER="$STATUS_DIR/fs-marker"

mkdir -p "$STATUS_DIR"
chmod 700 "$STATUS_DIR" 2>/dev/null || true

if [[ "$PRINT_STATUS_PATH" == "true" ]]; then
    echo "$STATUS_FILE"
    exit 0
fi

# ── Stop / cleanup: the off switch the daemon used to be missing ─────────────
stop_running() {
    if [[ ! -f "$PIDFILE" ]]; then
        echo "No overseer pid file in $STATUS_DIR — nothing to stop."
        return 1
    fi
    local pid
    pid="$(cat "$PIDFILE" 2>/dev/null || echo "")"
    if [[ -z "$pid" || ! -d "/proc/$pid" ]]; then
        echo "Overseer is not running (stale pid file removed)."
        rm -f "$PIDFILE"
        return 1
    fi
    kill "$pid" 2>/dev/null || true
    for _ in $(seq 1 50); do
        [[ -d "/proc/$pid" ]] || break
        sleep 0.1
    done
    if [[ -d "/proc/$pid" ]]; then
        echo "Overseer (pid $pid) did not stop on SIGTERM; sending SIGKILL."
        kill -9 "$pid" 2>/dev/null || true
    fi
    rm -f "$PIDFILE"
    echo "Overseer stopped (pid $pid)."
    return 0
}

if [[ "$DO_STOP" == "true" || "$DO_CLEANUP" == "true" ]]; then
    stop_running || true
    if [[ "$DO_CLEANUP" == "true" ]]; then
        # Named files only — never a recursive delete of a directory taken from
        # an argument or an environment variable.
        rm -f "$STATUS_FILE" "$LOGFILE" "$MARKER" "$PIDFILE" "$LOCKFILE"
        rmdir "$STATUS_DIR" 2>/dev/null || true
        echo "Removed overseer state from $STATUS_DIR"
    fi
    exit 0
fi

# ── Locking (one overseer per user) ──────────────────────────────────────────
exec 200>"$LOCKFILE"
if ! flock -n 200; then
    echo "Another overseer is already running. Exiting." >&2
    exit 0
fi

echo $$ > "$PIDFILE"

log() { echo "$(date -Iseconds) $*" >> "$LOGFILE"; }

# Clean up on any exit, including SIGTERM from --stop. The lock file itself is
# left in place: flock releases with the process, and deleting it could unlock a
# different overseer that already has it open.
STOPPING=0
on_exit() {
    [[ "$STOPPING" -eq 1 ]] && return
    STOPPING=1
    rm -f "$MARKER" "$PIDFILE"
    log "Overseer stopped after ${CYCLE:-0} cycles."
}
trap on_exit EXIT
trap 'on_exit; exit 0' INT TERM

log "Started: pid=$$ interval=${INTERVAL}s workdir=$WORKDIR labels=$LABELS max-stale=$MAX_STALE filenames=$RECORD_FILENAMES"
echo "Overseer running (pid $$). Status: $STATUS_FILE — stop with: $0 --status-dir '$STATUS_DIR' --stop" >&2

# ── Gateway PID detection ─────────────────────────────────────────────────────
find_gateway_pid() {
    pgrep -f "openclaw-gateway" | head -1 || echo ""
}

# ── Process-level health (no AI, no API — pure /proc) ────────────────────────
proc_health() {
    local pid="$1"
    if [[ -z "$pid" || ! -d "/proc/$pid" ]]; then
        echo '{"alive":false}'
        return
    fi
    local cpu mem threads state uptime_sec
    # CPU + MEM from ps
    read -r cpu mem < <(ps -p "$pid" -o %cpu,%mem --no-headers 2>/dev/null || echo "0 0")
    # Thread count from /proc
    threads=$(ls /proc/"$pid"/task 2>/dev/null | wc -l || echo 0)
    # Process state
    state=$(awk '/^State:/ {print $2}' /proc/"$pid"/status 2>/dev/null || echo "?")
    # Uptime
    uptime_sec=$(ps -p "$pid" -o etimes --no-headers 2>/dev/null | tr -d ' ' || echo 0)
    # FD count (proxy for activity)
    local fd_count
    fd_count=$(ls /proc/"$pid"/fd 2>/dev/null | wc -l || echo 0)

    cat <<-EOF
{"alive":true,"cpu":${cpu// /},"mem":${mem// /},"threads":$threads,"state":"$state","uptime_sec":$uptime_sec,"fd_count":$fd_count}
EOF
}

# ── Session-level sub-agent enumeration (one CLI call per cycle) ──────────────
list_subagents() {
    # Returns lines: label|age|model|tokens
    # Filter to recent sessions only (just now, seconds, or minutes — not hours/days)
    # `grep` exits 1 when nothing matches, and under `set -e -o pipefail` that
    # took the whole daemon down on the first quiet cycle — before it had written
    # a single status file, and without ever reaching the documented "no
    # sub-agents for two cycles, stop" path. Having no sub-agents is a normal
    # state, so the empty result is absorbed here.
    openclaw sessions list 2>/dev/null | grep "subag" | \
        grep -E "(just now|[0-9]+s ago|[0-9]+m ago)" | \
        while read -r kind key age model tokens flags; do
            local label="${key##*:}"
            label="${label:0:20}"
            echo "${label}|${age}|${model}|${tokens}"
        done || true
}

# ── Filesystem diff (cheap: find + stat) ──────────────────────────────────────
touch "$MARKER"

# Filenames are the one piece of real content this daemon handles, and they go
# into a JSON file. Escape them, or a quote or backslash in a filename produces a
# status file the heartbeat cannot parse.
json_escape() { printf '%s' "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g'; }

fs_changes() {
    find "$WORKDIR" -type f \
        -not -path '*/node_modules/*' \
        -not -path '*/.git/objects/*' \
        -not -path '*/dist/*' \
        -newer "$MARKER" \
        2>/dev/null | wc -l
}

fs_recent_files() {
    # --no-filenames: report that things changed, never what they were called.
    if [[ "$RECORD_FILENAMES" != "true" ]]; then
        echo ""
        return
    fi
    find "$WORKDIR" -type f \
        -not -path '*/node_modules/*' \
        -not -path '*/.git/objects/*' \
        -not -path '*/dist/*' \
        -newer "$MARKER" \
        2>/dev/null | xargs -I{} basename {} | sort -u | head -5 | tr '\n' ',' | sed 's/,$//'
}

# ── Per-label stale tracking ─────────────────────────────────────────────────
declare -A STALE_COUNTS

get_stale() { echo "${STALE_COUNTS[$1]:-0}"; }
set_stale() { STALE_COUNTS[$1]="$2"; }

# ── Main loop ─────────────────────────────────────────────────────────────────
CYCLE=0
while true; do
    CYCLE=$((CYCLE + 1))
    NOW=$(date -Iseconds)

    # 1. Gateway health
    GW_PID=$(find_gateway_pid)
    GW_HEALTH=$(proc_health "$GW_PID")

    # 2. Active sub-agents
    SUBAGENTS=$(list_subagents)
    # Counted with awk, not `grep -c`: grep exits 1 when the count is zero, which
    # under `set -e -o pipefail` killed the daemon on every quiet cycle, and the
    # old `|| echo 0` fallback appended a second zero that broke the arithmetic
    # tests below on "0\n0". awk always exits 0.
    SUBAGENT_COUNT=$(printf '%s\n' "$SUBAGENTS" | awk 'NF { n++ } END { print n + 0 }')

    # 3. Filesystem activity
    CHANGED=$(fs_changes)
    RECENT=$(fs_recent_files)

    # 4. Per-label staleness
    LABEL_STATUS=""
    if [[ -n "$SUBAGENTS" ]]; then
        while IFS='|' read -r label age model tokens; do
            [[ -z "$label" ]] && continue
            prev_stale=$(get_stale "$label")
            if [[ "$CHANGED" -gt 0 ]]; then
                set_stale "$label" 0
                LABEL_STATUS="${LABEL_STATUS}{\"label\":\"$(json_escape "$label")\",\"age\":\"$(json_escape "$age")\",\"stale\":0,\"status\":\"active\"},"
            else
                new_stale=$((prev_stale + 1))
                set_stale "$label" "$new_stale"
                local_status="idle"
                if [[ "$new_stale" -ge "$MAX_STALE" ]]; then
                    local_status="stuck"
                elif [[ "$new_stale" -ge 2 ]]; then
                    local_status="warning"
                fi
                LABEL_STATUS="${LABEL_STATUS}{\"label\":\"$(json_escape "$label")\",\"age\":\"$(json_escape "$age")\",\"stale\":$new_stale,\"status\":\"$local_status\"},"
            fi
        done <<< "$SUBAGENTS"
    fi
    # Trim trailing comma
    LABEL_STATUS="${LABEL_STATUS%,}"

    # 5. Write status file (atomic via temp + mv)
    TMP_STATUS=$(mktemp "$STATUS_DIR/status.XXXXXX")
    cat > "$TMP_STATUS" <<-STATUSEOF
{
  "timestamp": "$NOW",
  "cycle": $CYCLE,
  "interval_sec": $INTERVAL,
  "gateway": { "pid": ${GW_PID:-null}, "health": $GW_HEALTH },
  "subagents": { "count": $SUBAGENT_COUNT, "details": [$LABEL_STATUS] },
  "filesystem": { "changes_since_last": $CHANGED, "recent_files": "$(json_escape "$RECENT")", "filenames_recorded": $RECORD_FILENAMES },
  "max_stale_threshold": $MAX_STALE
}
STATUSEOF
    mv "$TMP_STATUS" "$STATUS_FILE"

    # 6. Append to rolling log (last 100 entries kept)
    echo "$NOW cycle=$CYCLE agents=$SUBAGENT_COUNT fs_changes=$CHANGED gw_pid=${GW_PID:-none}" >> "$LOGFILE"
    tail -100 "$LOGFILE" > "$LOGFILE.tmp" && mv "$LOGFILE.tmp" "$LOGFILE"

    # 7. Voice summary (optional, local only)
    if [[ "$VOICE" == "true" ]] && command -v jarvis &>/dev/null; then
        if [[ "$SUBAGENT_COUNT" -eq 0 ]]; then
            # No agents — stay silent after first announcement
            if [[ "$CYCLE" -eq 1 ]]; then
                setsid jarvis "No active sub-agents. Overseer watching." &>/dev/null &
            fi
        elif [[ "$CHANGED" -gt 0 ]]; then
            # Filenames are only read aloud when explicitly asked for: a speaker
            # announcing what you are working on is a different consent decision
            # from a status file on your own disk.
            if [[ "$VOICE_FILES" == "true" && -n "$RECENT" ]]; then
                setsid jarvis "$SUBAGENT_COUNT agents active. $CHANGED files changed: $RECENT." &>/dev/null &
            else
                setsid jarvis "$SUBAGENT_COUNT agents active. $CHANGED files changed." &>/dev/null &
            fi
        else
            # Check if any stuck
            STUCK_COUNT=$(printf '%s\n' "$LABEL_STATUS" | awk -v RS='"stuck"' 'END { print NR - 1 }')
            if [[ "$STUCK_COUNT" -gt 0 ]]; then
                setsid jarvis "Warning: $STUCK_COUNT agents appear stuck. No file changes." &>/dev/null &
            fi
        fi
    fi

    # 8. Reset marker
    touch "$MARKER"

    # 9. Exit if no sub-agents for 2 consecutive cycles
    if [[ "$SUBAGENT_COUNT" -eq 0 ]]; then
        if [[ "${PREV_EMPTY:-0}" -eq 1 ]]; then
            log "No sub-agents for 2 cycles. Exiting."
            break
        fi
        PREV_EMPTY=1
    else
        PREV_EMPTY=0
    fi

    sleep "$INTERVAL"
done

# Falling out of the loop (no sub-agents for two cycles) runs the EXIT trap,
# which removes the marker and the pid file and writes the closing log line.
