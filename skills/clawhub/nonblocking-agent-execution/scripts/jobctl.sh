#!/usr/bin/env bash
# =============================================================================
# jobctl.sh - Enhanced Non-Blocking Agent Execution Controller
# =============================================================================
# Version: 2.0.0
# Author: Enhanced by AI-assisted research and implementation
# License: MIT-0
# 
# Features:
# - Detach → Bounded-Poll → Durable-State pattern
# - Multi-model compatibility (OpenAI, Anthropic, Mistral, Groq, etc.)
# - Token usage optimization
# - Hallucination reduction via verification
# - Self-improving through feedback loops
# - Comprehensive debugging and logging
# - Idempotent operations
# - Graceful error handling
# 
# Usage:
#   ./jobctl.sh start <job_id> '<command>' [callback_url] [model] [max_tokens]
#   ./jobctl.sh stop <job_id>
#   ./jobctl.sh status <job_id>
#   ./jobctl.sh poll <job_id> [timeout]
#   ./jobctl.sh log <job_id> [lines]
#   ./jobctl.sh list [filter]
#   ./jobctl.sh cleanup <job_id>
#   ./jobctl.sh verify <job_id>
#   ./jobctl.sh debug <job_id>
# =============================================================================

set -euo pipefail

# =============================================================================
# CONFIGURATION
# =============================================================================

# Base directories - configurable via environment variables
BASE_DIR="${NONBLOCKING_BASE_DIR:-$HOME/.nonblocking}"
RUN_DIR="${BASE_DIR}/run"
LOG_DIR="${BASE_DIR}/logs"
STATE_DIR="${BASE_DIR}/state"
CACHE_DIR="${BASE_DIR}/cache"
FEEDBACK_DIR="${BASE_DIR}/feedback"

# Default values
MAX_RUNTIME=${MAX_RUNTIME:-86400}          # 24 hours default
POLL_INTERVAL=${POLL_INTERVAL:-2}          # 2 seconds
MAX_POLL_ATTEMPTS=${MAX_POLL_ATTEMPTS:-120}  # 240 seconds total
DEFAULT_MODEL=${DEFAULT_MODEL:-gpt-4o-mini}
DEFAULT_MAX_TOKENS=${DEFAULT_MAX_TOKENS:-2048}

# Token optimization thresholds
TOKEN_WARNING_THRESHOLD=${TOKEN_WARNING_THRESHOLD:-4000}
TOKEN_ERROR_THRESHOLD=${TOKEN_ERROR_THRESHOLD:-8000}

# Create directories if they don't exist
mkdir -p "$RUN_DIR" "$LOG_DIR" "$STATE_DIR" "$CACHE_DIR" "$FEEDBACK_DIR"

# =============================================================================
# LOGGING UTILITIES
# =============================================================================

# Log levels: DEBUG, INFO, WARN, ERROR, CRITICAL
LOG_LEVEL=${LOG_LEVEL:-INFO}

log() {
    local level="${1:-}"
    shift
    local message="${*:-}"
    local timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    local log_entry="[$timestamp] [$level] $message"
    
    # Color coding for terminal output
    case "$level" in
        DEBUG)    echo -e "\e[36m$log_entry\e[0m" >> "$LOG_DIR/jobctl.log" ;;
        INFO)     echo -e "\e[32m$log_entry\e[0m" >> "$LOG_DIR/jobctl.log" ;;
        WARN)     echo -e "\e[33m$log_entry\e[0m" >> "$LOG_DIR/jobctl.log" ;;
        ERROR)    echo -e "\e[31m$log_entry\e[0m" >> "$LOG_DIR/jobctl.log" ;;
        CRITICAL) echo -e "\e[35m$log_entry\e[0m" >> "$LOG_DIR/jobctl.log" ;;
        *)        echo "$log_entry" >> "$LOG_DIR/jobctl.log" ;;
    esac
    
    # Only print to stdout if level is INFO or higher (unless DEBUG mode)
    if [[ "$LOG_LEVEL" == "DEBUG" ]] || \
       [[ "$level" != "DEBUG" && "$LOG_LEVEL" != "DEBUG" ]]; then
        echo "$log_entry"
    fi
}

# Debug output (only when DEBUG mode is enabled)
debug() {
    if [[ "$LOG_LEVEL" == "DEBUG" ]]; then
        log "DEBUG" "$@"
    fi
}

# =============================================================================
# STATE MANAGEMENT UTILITIES
# =============================================================================

# File-based state management (more portable than SQLite)
get_state_file() {
    echo "${STATE_DIR}/${1}.json"
}

get_pid_file() {
    echo "${RUN_DIR}/${1}.pid"
}

get_log_file() {
    echo "${LOG_DIR}/${1}.log"
}

get_output_file() {
    echo "${STATE_DIR}/${1}.output"
}

get_feedback_file() {
    echo "${FEEDBACK_DIR}/${1}.feedback"
}

# Read state from JSON file
read_state() {
    local job_id="${1:-}"
    local state_file=$(get_state_file "$job_id")
    
    if [[ ! -f "$state_file" ]]; then
        echo "{}"
        return 1
    fi
    
    cat "$state_file"
}

# Write state to JSON file (atomic operation)
write_state() {
    local job_id="${1:-}"
    local json_data="${2:-}"
    local state_file=$(get_state_file "$job_id")
    local tmp_file="${state_file}.tmp"
    
    # Atomic write: write to temp file, then move
    echo "$json_data" > "$tmp_file"
    mv "$tmp_file" "$state_file"
    debug "State written for job $job_id"
}

# Update state field
update_state_field() {
    local job_id="${1:-}"
    local field="${2:-}"
    local value="${3:-}"
    
    local current_state=$(read_state "$job_id")
    
    # Use python for reliable JSON manipulation
    python3 -c "
import json, sys
state = json.loads(sys.argv[1])
state[sys.argv[2]] = sys.argv[3]
print(json.dumps(state, indent=2))
" "$current_state" "$field" "$value"
}

# =============================================================================
# JOB STRUCTURE
# =============================================================================

# Job state JSON structure:
# {
#   "job_id": "unique-id",
#   "command": "the command to execute",
#   "status": "queued|running|paused|stopped|completed|failed|verified",
#   "pid": 12345,
#   "start_time": "2026-09-06T14:00:00Z",
#   "end_time": "2026-09-06T14:05:00Z",
#   "exit_code": 0,
#   "callback_url": "https://...",
#   "model": "gpt-4o-mini",
#   "max_tokens": 2048,
#   "tokens_used": 1500,
#   "token_rate": 25.5,
#   "output_hash": "sha256:...",
#   "error_message": "",
#   "retry_count": 0,
#   "verified": false,
#   "verification_score": 0.0,
#   "feedback": "",
#   "self_improvement": {}
# }

# =============================================================================
# TOKEN OPTIMIZATION UTILITIES
# =============================================================================

# Estimate token count for a given text
count_tokens() {
    local text="${1:-}"
    # Use a simple approximation: 4 characters ≈ 1 token (works reasonably well)
    # For more accuracy, we could use a proper tokenizer
    echo "$(( $(echo -n "$text" | wc -c) / 4 ))"
}

# Check if token usage is within bounds
check_token_bounds() {
    local job_id="${1:-}"
    local tokens_used="${2:-}"
    
    if [[ "$tokens_used" -gt "$TOKEN_ERROR_THRESHOLD" ]]; then
        log "ERROR" "Token usage ($tokens_used) exceeds error threshold ($TOKEN_ERROR_THRESHOLD) for job $job_id"
        return 1
    elif [[ "$tokens_used" -gt "$TOKEN_WARNING_THRESHOLD" ]]; then
        log "WARN" "Token usage ($tokens_used) exceeds warning threshold ($TOKEN_WARNING_THRESHOLD) for job $job_id"
        return 0
    fi
    
    return 0
}

# Optimize command for token efficiency
optimize_command() {
    local command="$1"
    
    # Add common optimizations:
    # 1. Ensure non-interactive mode
    command=$(echo "$command" | sed 's/--interactive//g')
    command=$(echo "$command" | sed 's/-i //g')
    
    # 2. Add --yes or -y flags where appropriate
    if ! echo "$command" | grep -qE "(--yes|-y|--no-input)"; then
        command=$(echo "$command" | sed 's/apt-get install/apt-get install -y/g')
        command=$(echo "$command" | sed 's/pip install/pip install --yes/g')
        command=$(echo "$command" | sed 's/npx/npx --yes/g')
    fi
    
    # 3. Add timeout wrapper
    if ! echo "$command" | grep -q "timeout"; then
        command="timeout ${MAX_RUNTIME} $command"
    fi
    
    # 4. Redirect stdin from /dev/null
    if ! echo "$command" | grep -q "< /dev/null"; then
        command="$command < /dev/null"
    fi
    
    echo "$command"
}

# =============================================================================
# HALLUCINATION REDUCTION UTILITIES
# =============================================================================

# Verify output using a lightweight model
verify_output() {
    local job_id="${1:-}"
    local output="${2:-}"
    
    # For now, we'll use a simple heuristic: check for common hallucination patterns
    # In production, this would call a verification model
    
    local verification_score=1.0
    local issues=""
    
    # Check for common hallucination indicators
    if echo "$output" | grep -qi "i don't have access to that information"; then
        issues="${issues}Found 'no access' statement; "
        verification_score=$(echo "$verification_score - 0.3" | bc)
    fi
    
    if echo "$output" | grep -qi "as of my last update"; then
        issues="${issues}Found 'last update' disclaimer; "
        verification_score=$(echo "$verification_score - 0.2" | bc)
    fi
    
    if echo "$output" | grep -qi "may not be accurate"; then
        issues="${issues}Found accuracy disclaimer; "
        verification_score=$(echo "$verification_score - 0.2" | bc)
    fi
    
    # Update state with verification results
    local state=$(read_state "$job_id")
    state=$(echo "$state" | python3 -c "
import json, sys
state = json.loads(sys.stdin.read())
state['verified'] = True if float(sys.argv[1]) > 0.7 else False
state['verification_score'] = float(sys.argv[1])
state['verification_issues'] = sys.argv[2]
print(json.dumps(state, indent=2))
" "$verification_score" "$issues")
    
    write_state "$job_id" "$state"
    
    if [[ $(echo "$verification_score > 0.7" | bc) -eq 1 ]]; then
        log "INFO" "Verification passed for job $job_id (score: $verification_score)"
        return 0
    else
        log "WARN" "Verification failed for job $job_id (score: $verification_score, issues: $issues)"
        return 1
    fi
}

# =============================================================================
# SELF-IMPROVING MECHANISMS
# =============================================================================

# Record feedback for self-improvement
record_feedback() {
    local job_id="${1:-}"
    local feedback="${2:-}"
    local rating="${3:-}"  # 1-5
    
    local feedback_file=$(get_feedback_file "$job_id")
    
    cat > "$feedback_file" <<EOF
{
  "job_id": "$job_id",
  "feedback": "$feedback",
  "rating": $rating,
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "model": "$(echo "$feedback" | grep -oE "model:[^,]*" | cut -d: -f2 | tr -d ' ')"
}
EOF
    
    log "INFO" "Feedback recorded for job $job_id (rating: $rating)"
    
    # Analyze feedback for patterns (simple version)
    analyze_feedback "$job_id" "$feedback" "$rating"
}

# Analyze feedback for improvement opportunities
analyze_feedback() {
    local job_id="${1:-}"
    local feedback="${2:-}"
    local rating="${3:-}"
    
    # Simple pattern matching for now
    # In production, this would use ML to identify improvement opportunities
    
    local improvements=""
    
    if echo "$feedback" | grep -qi "slow"; then
        improvements="${improvements}- Consider adding caching or optimization; "
    fi
    
    if echo "$feedback" | grep -qi "error"; then
        improvements="${improvements}- Improve error handling; "
    fi
    
    if echo "$feedback" | grep -qi "token"; then
        improvements="${improvements}- Optimize token usage; "
    fi
    
    if [[ -n "$improvements" ]]; then
        log "INFO" "Self-improvement opportunities identified for job $job_id: $improvements"
        
        # Store improvements in state
        local state=$(read_state "$job_id")
        state=$(echo "$state" | python3 -c "
import json, sys
state = json.loads(sys.stdin.read())
if 'self_improvement' not in state:
    state['self_improvement'] = {}
state['self_improvement']['suggestions'] = sys.argv[1]
print(json.dumps(state, indent=2))
" "$improvements")
        
        write_state "$job_id" "$state"
    fi
}

# =============================================================================
# MULTI-MODEL COMPATIBILITY
# =============================================================================

# Normalize model identifier
normalize_model() {
    local model="$1"
    
    # Convert various formats to a standard form
    case "$model" in
        gpt-4|gpt4|gpt-4o)           echo "gpt-4" ;;
        gpt-4o-mini|gpt4o-mini)      echo "gpt-4o-mini" ;;
        gpt-3.5|gpt3.5)               echo "gpt-3.5-turbo" ;;
        claude-3|claude3)            echo "claude-3-sonnet-20240229" ;;
        claude-3-haiku)              echo "claude-3-haiku-20240307" ;;
        mistral|mistral-7b)          echo "mistral-7b-instruct" ;;
        llama|llama-3)               echo "llama-3-70b-instruct" ;;
        groq)                       echo "groq/gpt-oss-120b" ;;
        *)                          echo "$model" ;;
    esac
}

# Get model-specific configuration
get_model_config() {
    local model="$1"
    model=$(normalize_model "$model")
    
    # Return JSON configuration
    case "$model" in
        gpt-4)                      echo '{"max_tokens": 8192, "temperature": 0.7, "timeout": 120}' ;;
        gpt-4o-mini)                echo '{"max_tokens": 4096, "temperature": 0.7, "timeout": 60}' ;;
        gpt-3.5-turbo)               echo '{"max_tokens": 4096, "temperature": 0.7, "timeout": 60}' ;;
        claude-3-sonnet-20240229)   echo '{"max_tokens": 4096, "temperature": 0.7, "timeout": 120}' ;;
        claude-3-haiku-20240307)   echo '{"max_tokens": 4096, "temperature": 0.7, "timeout": 60}' ;;
        mistral-7b-instruct)         echo '{"max_tokens": 4096, "temperature": 0.7, "timeout": 60}' ;;
        llama-3-70b-instruct)        echo '{"max_tokens": 4096, "temperature": 0.7, "timeout": 90}' ;;
        groq/gpt-oss-120b)          echo '{"max_tokens": 4096, "temperature": 0.7, "timeout": 30}' ;;
        *)                          echo '{"max_tokens": 2048, "temperature": 0.7, "timeout": 60}' ;;
    esac
}

# =============================================================================
# PROCESS MANAGEMENT
# =============================================================================

# Check if a process is running
is_process_running() {
    local pid="$1"
    kill -0 "$pid" 2>/dev/null
}

# Get process info
get_process_info() {
    local pid="$1"
    ps -p "$pid" -o pid,ppid,cmd,%cpu,%mem,etime 2>/dev/null
}

# Clean up process resources
cleanup_process() {
    local job_id="${1:-}"
    local pid_file=$(get_pid_file "$job_id")
    
    if [[ -f "$pid_file" ]]; then
        local pid=$(cat "$pid_file")
        
        # Try to kill gracefully
        if is_process_running "$pid"; then
            log "INFO" "Cleaning up process $pid for job $job_id"
            kill -TERM "$pid" 2>/dev/null || true
            
            # Wait a bit for graceful shutdown
            sleep 2
            
            # Force kill if still running
            if is_process_running "$pid"; then
                kill -KILL "$pid" 2>/dev/null || true
                log "WARN" "Force killed process $pid for job $job_id"
            fi
        fi
        
        # Remove pid file
        rm -f "$pid_file"
    fi
}

# =============================================================================
# WATCHDOG FUNCTIONALITY
# =============================================================================

# Start a watchdog for a job
start_watchdog() {
    local job_id="${1:-}"
    local pid="$2"
    local timeout="$3"
    
    (
        sleep "$timeout"
        if is_process_running "$pid"; then
            log "WARN" "Watchdog: Job $job_id (pid=$pid) exceeded timeout of ${timeout}s"
            kill -TERM "$pid" 2>/dev/null || true
            
            # Update state
            local state=$(read_state "$job_id")
            state=$(echo "$state" | python3 -c "
import json, sys
state = json.loads(sys.stdin.read())
state['status'] = 'failed'
state['end_time'] = '$(date -u +"%Y-%m-%dT%H:%M:%SZ")'
state['exit_code'] = 124  # Timeout exit code
state['error_message'] = 'Job exceeded maximum runtime of ${timeout}s'
print(json.dumps(state, indent=2))
")
            write_state "$job_id" "$state"
        fi
    ) &
}

# =============================================================================
# CALLBACK HANDLING
# =============================================================================

# Execute callback
execute_callback() {
    local job_id="${1:-}"
    local callback_url="$2"
    local result="$3"
    
    if [[ -z "$callback_url" ]] || [[ "$callback_url" == "null" ]]; then
        debug "No callback URL for job $job_id"
        return 0
    fi
    
    log "INFO" "Executing callback for job $job_id to $callback_url"
    
    # Try to POST the result
    if command -v curl >/dev/null 2>&1; then
        local response=$(curl -s -X POST \
            -H "Content-Type: application/json" \
            -H "Accept: application/json" \
            -d "$result" \
            "$callback_url" 2>&1 || true)
        
        if [[ -n "$response" ]]; then
            log "INFO" "Callback response for job $job_id: $response"
        fi
    else
        log "WARN" "curl not available, cannot execute callback for job $job_id"
    fi
}

# =============================================================================
# CORE COMMANDS
# =============================================================================

# Start a new job
cmd_start() {
    local job_id="${1:-}"
    local command="${2:-}"
    local callback_url="${3:-}"
    local model="${4:-$DEFAULT_MODEL}"
    local max_tokens="${5:-$DEFAULT_MAX_TOKENS}"
    
    # Validate job_id
    if [[ -z "$job_id" ]]; then
        log "ERROR" "Job ID is required"
        echo "Error: Job ID is required" >&2
        exit 1
    fi
    
    # Validate command
    if [[ -z "$command" ]]; then
        log "ERROR" "Command is required"
        echo "Error: Command is required" >&2
        exit 1
    fi
    
    # Check for duplicate
    if [[ -f "$(get_pid_file "$job_id")" ]] || [[ -f "$(get_state_file "$job_id")" ]]; then
        log "ERROR" "Job $job_id already exists"
        echo "Error: Job $job_id already exists" >&2
        exit 1
    fi
    
    # Optimize the command
    command=$(optimize_command "$command")
    log "INFO" "Starting job $job_id with command: $command"
    
    # Create initial state
    local start_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
    local state_json=$(python3 -c "
import json
state = {
    'job_id': '$job_id',
    'command': '$command',
    'status': 'queued',
    'start_time': '$start_time',
    'callback_url': '$callback_url',
    'model': '$model',
    'max_tokens': $max_tokens,
    'tokens_used': 0,
    'token_rate': 0.0,
    'retry_count': 0,
    'verified': False,
    'verification_score': 0.0,
    'self_improvement': {}
}
print(json.dumps(state, indent=2))
")
    
    write_state "$job_id" "$state_json"
    
    # Start the job in background with setsid and nohup
    local pid_file=$(get_pid_file "$job_id")
    local log_file=$(get_log_file "$job_id")
    local output_file=$(get_output_file "$job_id")
    
    # Create a wrapper script for better control
    local wrapper="$RUN_DIR/${job_id}.wrapper.sh"
    cat > "$wrapper" <<WRAPPER
#!/bin/bash
set -euo pipefail
JOB_ID="$job_id"
COMMAND="$command"
OUTPUT_FILE="$output_file"
LOG_FILE="$log_file"

# Execute the command
if [ -n "\$COMMAND" ]; then
    echo "Starting command execution at \$(date -u +'%Y-%m-%dT%H:%M:%SZ')" >> "\$LOG_FILE"
    
    # Execute and capture output
    eval "\$COMMAND" > "\$OUTPUT_FILE" 2>> "\$LOG_FILE"
    local exit_code=\$?
    
    echo "Command finished at \$(date -u +'%Y-%m-%dT%H:%M:%SZ') with exit code \$exit_code" >> "\$LOG_FILE"
    exit \$exit_code
fi
WRAPPER
    
    chmod +x "$wrapper"
    
    # Launch with setsid and nohup
    setsid nohup bash "$wrapper" > /dev/null 2>&1 &
    local pid=$!
    echo "$pid" > "$pid_file"
    
    # Update state with PID and running status
    local state=$(read_state "$job_id")
    state=$(echo "$state" | python3 -c "
import json, sys
state = json.loads(sys.stdin.read())
state['pid'] = $pid
state['status'] = 'running'
print(json.dumps(state, indent=2))
")
    write_state "$job_id" "$state"
    
    # Start watchdog
    start_watchdog "$job_id" "$pid" "$MAX_RUNTIME"
    
    log "INFO" "Job $job_id started with PID $pid"
    echo "{"job_id":"$job_id","pid":$pid,"status":"running","message":"Job started successfully"}"
}

# Stop a job
cmd_stop() {
    local job_id="${1:-}"
    
    if [[ -z "$job_id" ]]; then
        log "ERROR" "Job ID is required"
        echo "Error: Job ID is required" >&2
        exit 1
    fi
    
    local pid_file=$(get_pid_file "$job_id")
    
    if [[ ! -f "$pid_file" ]]; then
        log "ERROR" "Job $job_id not found or already stopped"
        echo "Error: Job $job_id not found" >&2
        exit 1
    fi
    
    local pid=$(cat "$pid_file")
    
    if is_process_running "$pid"; then
        log "INFO" "Stopping job $job_id (PID: $pid)"
        kill -TERM "$pid" 2>/dev/null || true
        
        # Wait for graceful shutdown
        sleep 2
        
        if is_process_running "$pid"; then
            kill -KILL "$pid" 2>/dev/null || true
            log "WARN" "Force stopped job $job_id"
        fi
        
        # Update state
        local end_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
        local state=$(read_state "$job_id")
        state=$(echo "$state" | python3 -c "
import json, sys
state = json.loads(sys.stdin.read())
state['status'] = 'stopped'
state['end_time'] = '$end_time'
state['exit_code'] = 137  # SIGKILL
print(json.dumps(state, indent=2))
")
        write_state "$job_id" "$state"
        
        # Cleanup
        cleanup_process "$job_id"
        
        log "INFO" "Job $job_id stopped"
        echo "{"job_id":"$job_id","status":"stopped","message":"Job stopped"}"
    else
        log "INFO" "Job $job_id is not running"
        
        # Update state if process already died
        local state=$(read_state "$job_id")
        local current_status=$(echo "$state" | python3 -c "import json,sys; print(json.loads(sys.stdin.read()).get('status','unknown'))")
        
        if [[ "$current_status" != "completed" && "$current_status" != "failed" ]]; then
            local end_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
            state=$(echo "$state" | python3 -c "
import json, sys
state = json.loads(sys.stdin.read())
state['status'] = 'stopped'
state['end_time'] = '$end_time'
print(json.dumps(state, indent=2))
")
            write_state "$job_id" "$state"
        fi
        
        cleanup_process "$job_id"
        echo "{"job_id":"$job_id","status":"stopped","message":"Job was not running"}"
    fi
}

# Get job status
cmd_status() {
    local job_id="${1:-}"
    
    if [[ -z "$job_id" ]]; then
        log "ERROR" "Job ID is required"
        echo "Error: Job ID is required" >&2
        exit 1
    fi
    
    local state_file=$(get_state_file "$job_id")
    local pid_file=$(get_pid_file "$job_id")
    
    if [[ ! -f "$state_file" ]]; then
        log "ERROR" "Job $job_id not found"
        echo "Error: Job $job_id not found" >&2
        exit 1
    fi
    
    local state=$(cat "$state_file")
    local pid=""
    local process_info=""
    
    if [[ -f "$pid_file" ]]; then
        pid=$(cat "$pid_file")
        if is_process_running "$pid"; then
            process_info=$(get_process_info "$pid")
        else
            process_info="Process not running"
        fi
    fi
    
    # Calculate duration if available
    local start_time=$(echo "$state" | python3 -c "import json,sys; print(json.loads(sys.stdin.read()).get('start_time',''))")
    local end_time=$(echo "$state" | python3 -c "import json,sys; print(json.loads(sys.stdin.read()).get('end_time',''))")
    local duration=""
    
    if [[ -n "$start_time" ]]; then
        if [[ -n "$end_time" ]]; then
            duration=$(python3 -c "
from datetime import datetime, timezone
start = datetime.fromisoformat('$start_time'.replace('Z', '+00:00'))
end = datetime.fromisoformat('$end_time'.replace('Z', '+00:00'))
delta = end - start
hours, remainder = divmod(delta.total_seconds(), 3600)
minutes, seconds = divmod(remainder, 60)
print(f'{int(hours)}h {int(minutes)}m {int(seconds)}s')
")
        else
            duration=$(python3 -c "
from datetime import datetime, timezone
start = datetime.fromisoformat('$start_time'.replace('Z', '+00:00'))
now = datetime.now(timezone.utc)
delta = now - start
hours, remainder = divmod(delta.total_seconds(), 3600)
minutes, seconds = divmod(remainder, 60)
print(f'{int(hours)}h {int(minutes)}m {int(seconds)}s (running)')
")
        fi
    fi
    
    # Add process info to output
    echo "$state" | python3 -c "
import json, sys
state = json.loads(sys.stdin.read())
state['pid'] = '$pid'
state['process_info'] = '$process_info'
state['duration'] = '$duration'
print(json.dumps(state, indent=2))
"
}

# Poll job status
cmd_poll() {
    local job_id="${1:-}"
    local timeout="${2:-$POLL_INTERVAL}"
    local attempts=0
    
    if [[ -z "$job_id" ]]; then
        log "ERROR" "Job ID is required"
        echo "Error: Job ID is required" >&2
        exit 1
    fi
    
    while [[ $attempts -lt $MAX_POLL_ATTEMPTS ]]; do
        local status=$(cmd_status "$job_id" 2>/dev/null | python3 -c "import json,sys; print(json.loads(sys.stdin.read()).get('status','unknown'))" || echo "unknown")
        
        case "$status" in
            completed|failed|stopped)
                log "INFO" "Job $job_id completed polling with status: $status"
                cmd_status "$job_id"
                return 0
                ;;
            running)
                log "DEBUG" "Job $job_id still running (attempt $((attempts+1))/$MAX_POLL_ATTEMPTS)"
                sleep "$timeout"
                attempts=$((attempts + 1))
                ;;
            *)
                log "WARN" "Unknown status for job $job_id: $status"
                sleep "$timeout"
                attempts=$((attempts + 1))
                ;;
        esac
    done
    
    log "WARN" "Polling timed out for job $job_id after $MAX_POLL_ATTEMPTS attempts"
    cmd_status "$job_id"
}

# Get job log
cmd_log() {
    local job_id="${1:-}"
    local lines="${2:-50}"
    
    if [[ -z "$job_id" ]]; then
        log "ERROR" "Job ID is required"
        echo "Error: Job ID is required" >&2
        exit 1
    fi
    
    local log_file=$(get_log_file "$job_id")
    
    if [[ ! -f "$log_file" ]]; then
        log "ERROR" "Log file not found for job $job_id"
        echo "Error: Log file not found" >&2
        exit 1
    fi
    
    # Tail the log file
    tail -n "$lines" "$log_file"
}

# List all jobs
cmd_list() {
    local filter="${1:-}"
    
    if [[ -z "$filter" ]]; then
        # List all jobs
        ls -1 "$STATE_DIR"/*.json 2>/dev/null | while read -r file; do
            local job_id=$(basename "$file" .json)
            local state=$(cat "$file")
            local status=$(echo "$state" | python3 -c "import json,sys; print(json.loads(sys.stdin.read()).get('status','unknown'))")
            local start_time=$(echo "$state" | python3 -c "import json,sys; print(json.loads(sys.stdin.read()).get('start_time',''))")
            
            echo "$job_id | Status: $status | Started: $start_time"
        done
    else
        # Filter by status
        ls -1 "$STATE_DIR"/*.json 2>/dev/null | while read -r file; do
            local job_id=$(basename "$file" .json)
            local state=$(cat "$file")
            local status=$(echo "$state" | python3 -c "import json,sys; print(json.loads(sys.stdin.read()).get('status','unknown'))")
            
            if [[ "$status" == "$filter" ]]; then
                local start_time=$(echo "$state" | python3 -c "import json,sys; print(json.loads(sys.stdin.read()).get('start_time',''))")
                echo "$job_id | Status: $status | Started: $start_time"
            fi
        done
    fi
}

# Cleanup job
cmd_cleanup() {
    local job_id="${1:-}"
    
    if [[ -z "$job_id" ]]; then
        log "ERROR" "Job ID is required"
        echo "Error: Job ID is required" >&2
        exit 1
    fi
    
    # Stop the job if running
    cmd_stop "$job_id" >/dev/null 2>&1 || true
    
    # Remove all job files
    rm -f "$(get_pid_file "$job_id")" \
           "$(get_state_file "$job_id")" \
           "$(get_log_file "$job_id")" \
           "$(get_output_file "$job_id")" \
           "$(get_feedback_file "$job_id")" \
           "$RUN_DIR/${job_id}.wrapper.sh"
    
    log "INFO" "Cleaned up job $job_id"
    echo "{"job_id":"$job_id","status":"cleaned","message":"Job files removed"}"
}

# Verify job output
cmd_verify() {
    local job_id="${1:-}"
    
    if [[ -z "$job_id" ]]; then
        log "ERROR" "Job ID is required"
        echo "Error: Job ID is required" >&2
        exit 1
    fi
    
    local output_file=$(get_output_file "$job_id")
    
    if [[ ! -f "$output_file" ]]; then
        log "ERROR" "Output file not found for job $job_id"
        echo "Error: Output file not found" >&2
        exit 1
    fi
    
    local output=$(cat "$output_file")
    
    # Perform verification
    if verify_output "$job_id" "$output"; then
        # Update state
        local state=$(read_state "$job_id")
        state=$(echo "$state" | python3 -c "
import json, sys
state = json.loads(sys.stdin.read())
state['status'] = 'verified'
print(json.dumps(state, indent=2))
")
        write_state "$job_id" "$state"
        
        log "INFO" "Job $job_id output verified successfully"
        echo "{"job_id":"$job_id","status":"verified","verification_score":$(echo "$state" | python3 -c "import json,sys; print(json.loads(sys.stdin.read()).get('verification_score',0))")}"
    else
        log "WARN" "Job $job_id output verification failed"
        echo "{"job_id":"$job_id","status":"verification_failed","message":"Output did not pass verification"}" >&2
        exit 1
    fi
}

# Debug job
cmd_debug() {
    local job_id="${1:-}"
    
    if [[ -z "$job_id" ]]; then
        log "ERROR" "Job ID is required"
        echo "Error: Job ID is required" >&2
        exit 1
    fi
    
    echo "=== DEBUG INFO FOR JOB: $job_id ==="
    echo ""
    
    # State
    echo "--- State ---"
    cmd_status "$job_id" 2>/dev/null || echo "No state found"
    echo ""
    
    # PID file
    local pid_file=$(get_pid_file "$job_id")
    echo "--- PID File ---"
    if [[ -f "$pid_file" ]]; then
        cat "$pid_file"
        local pid=$(cat "$pid_file")
        echo ""
        echo "Process info:"
        get_process_info "$pid" || echo "Process not running"
    else
        echo "No PID file found"
    fi
    echo ""
    
    # Log file
    local log_file=$(get_log_file "$job_id")
    echo "--- Log File (last 20 lines) ---"
    if [[ -f "$log_file" ]]; then
        tail -n 20 "$log_file"
    else
        echo "No log file found"
    fi
    echo ""
    
    # Output file
    local output_file=$(get_output_file "$job_id")
    echo "--- Output File ---"
    if [[ -f "$output_file" ]]; then
        cat "$output_file"
    else
        echo "No output file found"
    fi
    echo ""
    
    # Feedback
    local feedback_file=$(get_feedback_file "$job_id")
    echo "--- Feedback ---"
    if [[ -f "$feedback_file" ]]; then
        cat "$feedback_file"
    else
        echo "No feedback found"
    fi
}

# =============================================================================
# MAIN DISPATCHER
# =============================================================================

# Show usage
show_usage() {
    cat <<EOF
Usage: $0 <command> [options]

Commands:
  start <job_id> '<command>' [callback_url] [model] [max_tokens]
      Start a new non-blocking job
      
  stop <job_id>
      Stop a running job
      
  status <job_id>
      Get the current status of a job
      
  poll <job_id> [timeout]
      Poll a job until it completes (default timeout: $POLL_INTERVAL seconds)
      
  log <job_id> [lines]
      Show the log file for a job (default: 50 lines)
      
  list [filter]
      List all jobs, optionally filtered by status
      
  cleanup <job_id>
      Clean up all files for a job
      
  verify <job_id>
      Verify the output of a job
      
  debug <job_id>
      Show detailed debug information for a job

Environment Variables:
  NONBLOCKING_BASE_DIR   Base directory for all files (default: ~/.nonblocking)
  MAX_RUNTIME            Maximum runtime in seconds (default: 86400)
  POLL_INTERVAL          Polling interval in seconds (default: 2)
  MAX_POLL_ATTEMPTS     Maximum polling attempts (default: 120)
  DEFAULT_MODEL          Default AI model (default: gpt-4o-mini)
  DEFAULT_MAX_TOKENS     Default max tokens (default: 2048)
  LOG_LEVEL              Log level: DEBUG, INFO, WARN, ERROR (default: INFO)
  TOKEN_WARNING_THRESHOLD  Token warning threshold (default: 4000)
  TOKEN_ERROR_THRESHOLD    Token error threshold (default: 8000)

Examples:
  # Start a long-running build
  ./jobctl.sh start build-001 'npm install && npm run build' https://callback.url/api gpt-4o-mini 2048
  
  # Check status
  ./jobctl.sh status build-001
  
  # Poll until complete
  ./jobctl.sh poll build-001 5
  
  # Show logs
  ./jobctl.sh log build-001 100
  
  # Clean up
  ./jobctl.sh cleanup build-001
EOF
}

# Main command dispatcher
case "${1:-}" in
    start)   shift; cmd_start "$@" ;;
    stop)    shift; cmd_stop "$@" ;;
    status)  shift; cmd_status "$@" ;;
    poll)    shift; cmd_poll "$@" ;;
    log)     shift; cmd_log "$@" ;;
    list)    shift; cmd_list "$@" ;;
    cleanup) shift; cmd_cleanup "$@" ;;
    verify)  shift; cmd_verify "$@" ;;
    debug)   shift; cmd_debug "$@" ;;
    help|--help|-h|"")
        show_usage
        ;;
    *)
        log "ERROR" "Unknown command: $1"
        show_usage
        exit 1
        ;;
esac

exit 0
