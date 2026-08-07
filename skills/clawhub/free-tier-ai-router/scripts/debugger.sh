#!/bin/bash
set -euo pipefail
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
            local sleep_time=$((delay * attempt))
            dbg_warn "Failed, retrying in ${sleep_time}s..."
            sleep $sleep_time
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
    
    trap "kill $timeout_pid 2>/dev/null" EXIT
    
    eval "$cmd"
    local result=$?
    
    kill $timeout_pid 2>/dev/null
    trap - EXIT
    
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
    curl -s --connect-timeout 5 https://clawhub.ai >/dev/null 2>&1 && echo "✅ Internet access OK" || echo "❌ No internet"
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
# AUTOMATIC INITIALIZATION
# ============================================================================

# Initialize debug logging when sourced
if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
    mkdir -p "$(dirname "$DEBUG_LOG")"
    dbg_info "Debug framework initialized (level=$DEBUG_LEVEL)"
    dbg_setup_error_handler
fi
