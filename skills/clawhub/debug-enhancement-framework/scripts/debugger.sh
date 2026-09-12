#!/bin/bash
# Debug Enhancement Framework - Shell Interface
# Source this file in your scripts to get debugging capabilities

DEBUG_LEVEL="${DEBUG_LEVEL:-info}"
DEBUG_LOG="${DEBUG_LOG:-/tmp/skill-debug.log}"
DEBUG_SESSION_ID="$(date +%s)_$$"

# ============================================================================
# LOGGING
# ============================================================================

dbg_log() {
    local level="$1"
    shift
    local message="$*"
    local timestamp
    timestamp=$(date -Iseconds)
    
    # Convert level to numeric for comparison
    case "$level" in
        debug) local lvl=10 ;;
        info) local lvl=20 ;;
        warn) local lvl=30 ;;
        error) local lvl=40 ;;
        fatal) local lvl=50 ;;
        *) local lvl=20 ;;
    esac
    
    # Check if we should log at this level
    case "$DEBUG_LEVEL" in
        debug) ;;
        info) [ "$lvl" -lt 20 ] && return ;;
        warn) [ "$lvl" -lt 30 ] && return ;;
        error) [ "$lvl" -lt 40 ] && return ;;
        *) [ "$lvl" -lt 50 ] && return ;;
    esac
    
    # Log to file
    echo "[$timestamp] [$level] [$DEBUG_SESSION_ID] $message" >> "$DEBUG_LOG"
    
    # Log to stderr for visibility
    echo "[$level] $message" >&2
}

dbg_info() { dbg_log "info" "$@"; }
dbg_warn() { dbg_log "warn" "$@"; }
dbg_error() { dbg_log "error" "$@"; }
dbg_debug() { dbg_log "debug" "$@"; }
dbg_fatal() { dbg_log "fatal" "$@"; exit 1; }

# ============================================================================
# ERROR HANDLING
# ============================================================================

# Set up error trap
dbg_setup_error_handler() {
    trap 'dbg_handle_error $? $LINENO' ERR
}

dbg_handle_error() {
    local exit_code=$1
    local line_no=$2
    dbg_error "Error at line $line_no (exit code: $exit_code)"
    dbg_error "Command: ${BASH_COMMAND}"
    dbg_error "Stack trace:"
    local i=0
    while caller $i 2>/dev/null; do
        i=$((i + 1))
    done
}

# ============================================================================
# RETRY LOGIC
# ============================================================================

DBG_RETRY_MAX_DELAY="${DBG_RETRY_MAX_DELAY:-60}"

dbg_retry() {
    local max_attempts="${1:-3}"
    local delay="${2:-1}"
    local cmd="$3"
    local attempt=1
    
    while [ $attempt -le $max_attempts ]; do
        dbg_info "Attempt $attempt/$max_attempts: $cmd"
        
        if eval "$cmd"; then
            dbg_info "Success on attempt $attempt"
            return 0
        fi
        
        if [ $attempt -lt $max_attempts ]; then
            # BUG FIXED (v2.1.0): this was LINEAR backoff (delay * attempt) while
            # the documentation promised exponential, and it had no jitter - so
            # every client retried in lock-step. Now exponential with full jitter:
            #   sleep = random(0, min(cap, base * 2^(attempt-1)))
            local cap_exp=$(( delay * (2 ** (attempt - 1)) ))
            [ "$cap_exp" -gt "$DBG_RETRY_MAX_DELAY" ] && cap_exp="$DBG_RETRY_MAX_DELAY"
            local sleep_time
            sleep_time=$(awk -v c="$cap_exp" -v s="$RANDOM" 'BEGIN{srand(s); printf "%.2f", rand()*c}')
            dbg_warn "Failed, retrying in ${sleep_time}s (exponential + full jitter)..."
            sleep "$sleep_time"
        fi
        
        attempt=$((attempt + 1))
    done
    
    dbg_error "All $max_attempts attempts failed"
    return 1
}

# ============================================================================
# TIMEOUT WRAPPER
# ============================================================================

dbg_with_timeout() {
    local timeout_secs="$1"
    local cmd="$2"
    local timeout_pid
    
    (
        sleep "$timeout_secs"
        kill $$ 2>/dev/null
    ) &
    timeout_pid=$!
    
    # BUG FIXED (v2.1.0): this used to install its own EXIT trap and then run
    # `trap - EXIT`, which DELETED whatever EXIT trap the caller had set. This
    # file is meant to be SOURCED, so a caller's cleanup/rollback handler was
    # silently disabled by calling dbg_with_timeout once. Reproduced: a caller's
    # cleanup function never ran. Save the existing trap and restore it exactly.
    local _dbg_prev_exit_trap
    _dbg_prev_exit_trap="$(trap -p EXIT)"
    trap "kill \"$timeout_pid\" 2>/dev/null" EXIT

    eval "$cmd"
    local result=$?

    kill "$timeout_pid" 2>/dev/null
    if [ -n "$_dbg_prev_exit_trap" ]; then
        eval "$_dbg_prev_exit_trap"      # restore the caller's handler verbatim
    else
        trap - EXIT                      # there was none: leave it clean
    fi

    return $result
}

# ============================================================================
# PERFORMANCE MEASUREMENT
# ============================================================================

dbg_time_command() {
    local cmd="$1"
    local start_time
    start_time=$(date +%s.%N)
    
    eval "$cmd"
    local result=$?
    
    local end_time
    end_time=$(date +%s.%N)
    local elapsed
    elapsed=$(echo "$end_time - $start_time" | bc 2>/dev/null || echo "0")
    
    dbg_info "Command took ${elapsed}s: $cmd"
    return $result
}

# ============================================================================
# STATE CAPTURE
# ============================================================================

dbg_capture_state() {
    local name="$1"
    local state_file="/tmp/skill-debug-state/${name}_$(date +%Y%m%d_%H%M%S).json"
    mkdir -p "$(dirname "$state_file")"
    
    cat > "$state_file" << STATE
{
    "name": "$name",
    "timestamp": "$(date -Iseconds)",
    "session_id": "$DEBUG_SESSION_ID",
    "environment": {
        "cwd": "$(pwd)",
        "user": "$(whoami)",
        "shell": "$SHELL"
    },
    "variables": {
STATE
    
    # Add selected environment variables
    for var in PATH HOME PYTHONPATH DEBUG_LEVEL; do
        echo "        \"$var\": \"${!var:-}\"," >> "$state_file"
    done
    
    echo "    }" >> "$state_file"
    echo "}" >> "$state_file"
    
    dbg_info "State captured to $state_file"
    echo "$state_file"
}

# ============================================================================
# DIAGNOSTICS
# ============================================================================

dbg_diagnose() {
    dbg_info "Running diagnostics..."
    
    echo "=== System Diagnostics ==="
    echo "Timestamp: $(date -Iseconds)"
    echo "User: $(whoami)"
    echo "Working Directory: $(pwd)"
    echo ""
    
    echo "=== Environment ==="
    echo "DEBUG_LEVEL: $DEBUG_LEVEL"
    echo "DEBUG_LOG: $DEBUG_LOG"
    echo "PATH: ${PATH:0:100}..."
    echo ""
    
    echo "=== Disk Space ==="
    df -h / 2>/dev/null || echo "df not available"
    echo ""
    
    echo "=== Memory ==="
    free -h 2>/dev/null || echo "free not available"
    echo ""
    
    echo "=== Processes ==="
    ps aux --sort=-%mem 2>/dev/null | head -10 || echo "ps not available"
    echo ""
    
    echo "=== Network ==="
    # PRIVACY FIX (v2.1.2): this used to curl the registry host on EVERY
    # dbg_diagnose run - silent outbound traffic to a fixed third-party host,
    # from a tool whose documentation claimed no network access. A diagnostics
    # command must not phone home. The check is now opt-in and the operator
    # chooses the endpoint.
    if [ -n "${DBG_CONNECTIVITY_URL:-}" ]; then
        if curl -s --connect-timeout 5 "$DBG_CONNECTIVITY_URL" >/dev/null 2>&1; then
            echo "connectivity to $DBG_CONNECTIVITY_URL: OK"
        else
            echo "connectivity to $DBG_CONNECTIVITY_URL: FAILED"
        fi
    else
        echo "skipped (no outbound request made); set DBG_CONNECTIVITY_URL to enable"
    fi
    echo ""
    
    dbg_info "Diagnostics complete"
}

# ============================================================================
# SIMULATE ERRORS (for testing)
# ============================================================================

dbg_simulate_error() {
    local error_type="$1"
    
    case "$error_type" in
        network)
            dbg_error "Simulating network error"
            return 1
            ;;
        timeout)
            dbg_error "Simulating timeout"
            sleep 30 &
            sleep 1
            kill %1 2>/dev/null
            return 124
            ;;
        validation)
            dbg_error "Simulating validation error"
            echo "Invalid input" >&2
            return 1
            ;;
        permission)
            dbg_error "Simulating permission denied"
            return 126
            ;;
    esac
}


# ============================================================================
# HELPERS DOCUMENTED IN SKILL.md THAT DID NOT EXIST BEFORE v2.1.0
# profile_command, monitor_memory, dbg_reproduce, dbg_fix, dbg_verify were all
# referenced by the documentation - three of them as steps of the published
# 5-step "Bug Fixing Workflow" - while none of them were implemented. Calling
# any of them produced "command not found". They are real now.
# ============================================================================

profile_command() {
    # Profile a command: wall time, exit code, peak RSS when /usr/bin/time is available.
    local cmd="$1"
    [ -z "$cmd" ] && { dbg_error "profile_command: no command given"; return 2; }
    local start end rc rss=""
    start=$(date +%s.%N)
    if command -v /usr/bin/time >/dev/null 2>&1; then
        local tmp; tmp="$(mktemp)"
        /usr/bin/time -f "%M" -o "$tmp" bash -c "$cmd"; rc=$?
        rss="$(cat "$tmp" 2>/dev/null)"; rm -f "$tmp"
    else
        bash -c "$cmd"; rc=$?
    fi
    end=$(date +%s.%N)
    local elapsed; elapsed=$(awk -v a="$start" -v b="$end" 'BEGIN{printf "%.3f", b-a}')
    printf '{"command":%s,"elapsed_s":%s,"exit_code":%d,"max_rss_kb":%s}\n' \
        "$(printf '%s' "$cmd" | python3 -c 'import json,sys;print(json.dumps(sys.stdin.read()))')" \
        "$elapsed" "$rc" "${rss:-null}"
    return $rc
}

monitor_memory() {
    # Report current process-tree RSS and warn past a threshold.
    # Usage: monitor_memory [--threshold 500MB] [--pid PID]
    local threshold_mb=500 pid=$$
    while [ $# -gt 0 ]; do
        case "$1" in
            --threshold) threshold_mb="$(printf '%s' "$2" | sed 's/[^0-9]//g')"; shift 2 ;;
            --pid) pid="$2"; shift 2 ;;
            *) shift ;;
        esac
    done
    local rss_kb; rss_kb=$(ps -o rss= -p "$pid" 2>/dev/null | tr -d ' ')
    [ -z "$rss_kb" ] && { dbg_error "monitor_memory: no such pid $pid"; return 2; }
    local rss_mb=$(( rss_kb / 1024 ))
    local over="false"; [ "$rss_mb" -gt "$threshold_mb" ] && over="true"
    printf '{"pid":%d,"rss_mb":%d,"threshold_mb":%d,"over_threshold":%s}\n' \
        "$pid" "$rss_mb" "$threshold_mb" "$over"
    [ "$over" = "true" ] && dbg_warn "memory ${rss_mb}MB exceeds ${threshold_mb}MB"
    return 0
}

dbg_reproduce() {
    # Step 1 of the bug-fixing workflow: run a command and capture the exact
    # failure state (exit code, output, environment) into a replayable file.
    local cmd="$1"
    [ -z "$cmd" ] && { dbg_error "dbg_reproduce: no command given"; return 2; }
    local dir="${DBG_STATE_DIR:-/tmp/dbg-states}"; mkdir -p "$dir"
    local stamp; stamp=$(date +%Y%m%d_%H%M%S)
    local out="$dir/repro_$stamp.log"
    { echo "# command: $cmd"; echo "# date: $(date -u +%FT%TZ)"; echo "# pwd: $PWD"; echo "---"; } > "$out"
    bash -c "$cmd" >>"$out" 2>&1
    local rc=$?
    echo "# exit_code: $rc" >> "$out"
    printf '{"reproduced":true,"exit_code":%d,"capture":"%s"}\n' "$rc" "$out"
    return 0
}

dbg_fix() {
    # Step 3: apply a candidate fix behind a backup so it can be undone.
    # Usage: dbg_fix <file> <sed-expression>
    local file="$1" expr="$2"
    [ -f "$file" ] || { dbg_error "dbg_fix: no such file: $file"; return 2; }
    [ -z "$expr" ] && { dbg_error "dbg_fix: no sed expression given"; return 2; }
    # SCOPING (v2.1.3): rewriting files anywhere on the filesystem is too broad a
    # default for a sourced helper. Confine edits to the working directory unless
    # the operator explicitly opts in.
    local _abs _cwd
    _abs="$(cd "$(dirname "$file")" 2>/dev/null && pwd)/$(basename "$file")"
    _cwd="$(pwd)"
    case "$_abs" in
        "$_cwd"/*) ;;
        *)
            if [ "${DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE:-}" != "1" ]; then
                dbg_error "dbg_fix: refusing to edit outside $_cwd ($_abs). Set DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE=1 to allow."
                return 3
            fi
            ;;
    esac
    cp "$file" "$file.dbgbak"
    if sed -i "$expr" "$file"; then
        # absolute paths: a relative path in machine-readable output is ambiguous
        # to any consumer that is not in this exact working directory (v2.1.3)
        printf '{"fixed":true,"file":"%s","backup":"%s.dbgbak"}\n' "$_abs" "$_abs"
        return 0
    fi
    mv "$file.dbgbak" "$file"
    dbg_error "dbg_fix: sed failed; original restored"
    return 1
}

dbg_verify() {
    # Step 4: re-run the reproducer and report whether the fix held.
    local cmd="$1" expected="${2:-0}"
    [ -z "$cmd" ] && { dbg_error "dbg_verify: no command given"; return 2; }
    bash -c "$cmd" >/dev/null 2>&1
    local rc=$?
    local verdict="FIXED"; [ "$rc" -ne "$expected" ] && verdict="STILL_FAILING"
    printf '{"verdict":"%s","exit_code":%d,"expected":%d}\n' "$verdict" "$rc" "$expected"
    [ "$verdict" = "FIXED" ] && return 0 || return 1
}

# ============================================================================
# AUTOMATIC INITIALIZATION
# ============================================================================

# Initialize debug logging when sourced
if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
    mkdir -p "$(dirname "$DEBUG_LOG")"
    dbg_info "Debug framework initialized (level=$DEBUG_LEVEL)"
    dbg_setup_error_handler
fi
