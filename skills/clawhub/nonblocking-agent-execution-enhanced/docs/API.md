# 📡 API Documentation - Non-Blocking Agent Execution v2.0.0

This document describes the API and interface for the **nonblocking-agent-execution** skill.

---

## 📋 Table of Contents

1. [Command Line Interface (CLI)](#-command-line-interface-cli)
2. [Environment Variables](#-environment-variables)
3. [State File Format](#-state-file-format)
4. [Log File Format](#-log-file-format)
5. [Callback Format](#-callback-format)
6. [Feedback Format](#-feedback-format)
7. [Exit Codes](#-exit-codes)
8. [Error Handling](#-error-handling)

---

## 💻 Command Line Interface (CLI)

### Usage

```bash
./scripts/jobctl.sh <command> [options]
```

### Commands

#### `start` - Start a new job

**Syntax:**
```bash
./scripts/jobctl.sh start <job_id> '<command>' [callback_url] [model] [max_tokens]
```

**Parameters:**
- `job_id` (required): Unique identifier for the job
- `command` (required): Command to execute (in quotes)
- `callback_url` (optional): URL to POST results to when job completes
- `model` (optional): AI model to use (default: `gpt-4o-mini`)
- `max_tokens` (optional): Maximum tokens (default: `2048`)

**Returns:**
```json
{
  "job_id": "<job_id>",
  "pid": <pid>,
  "status": "running",
  "message": "Job started successfully"
}
```

**Example:**
```bash
./scripts/jobctl.sh start my-job 'echo hello' https://callback.url gpt-4o-mini 1024
```

---

#### `stop` - Stop a running job

**Syntax:**
```bash
./scripts/jobctl.sh stop <job_id>
```

**Parameters:**
- `job_id` (required): Job identifier

**Returns:**
```json
{
  "job_id": "<job_id>",
  "status": "stopped",
  "message": "Job stopped"
}
```

**Example:**
```bash
./scripts/jobctl.sh stop my-job
```

---

#### `status` - Get job status

**Syntax:**
```bash
./scripts/jobctl.sh status <job_id>
```

**Parameters:**
- `job_id` (required): Job identifier

**Returns:**
```json
{
  "job_id": "<job_id>",
  "command": "<command>",
  "status": "queued|running|paused|stopped|completed|failed|verified",
  "pid": <pid>,
  "start_time": "2026-09-06T14:00:00Z",
  "end_time": "2026-09-06T14:05:00Z",
  "exit_code": 0,
  "callback_url": "<callback_url>",
  "model": "<model>",
  "max_tokens": <max_tokens>,
  "tokens_used": <tokens_used>,
  "token_rate": <token_rate>,
  "output_hash": "<hash>",
  "error_message": "<error_message>",
  "retry_count": 0,
  "verified": true,
  "verification_score": 0.95,
  "verification_issues": "<issues>",
  "self_improvement": {
    "suggestions": "<suggestions>"
  },
  "process_info": "<process_info>",
  "duration": "<duration>"
}
```

**Example:**
```bash
./scripts/jobctl.sh status my-job
```

---

#### `poll` - Poll job until completion

**Syntax:**
```bash
./scripts/jobctl.sh poll <job_id> [timeout]
```

**Parameters:**
- `job_id` (required): Job identifier
- `timeout` (optional): Polling interval in seconds (default: `2`)

**Returns:**
Same as `status` command, but blocks until job completes or max attempts reached.

**Example:**
```bash
./scripts/jobctl.sh poll my-job 5
```

---

#### `log` - View job logs

**Syntax:**
```bash
./scripts/jobctl.sh log <job_id> [lines]
```

**Parameters:**
- `job_id` (required): Job identifier
- `lines` (optional): Number of lines to show (default: `50`)

**Returns:**
Plain text log output from the job.

**Example:**
```bash
./scripts/jobctl.sh log my-job 100
```

---

#### `list` - List all jobs

**Syntax:**
```bash
./scripts/jobctl.sh list [filter]
```

**Parameters:**
- `filter` (optional): Filter by status (`queued`, `running`, `completed`, `failed`, `stopped`, `verified`)

**Returns:**
```
<job_id_1> | Status: <status> | Started: <start_time>
<job_id_2> | Status: <status> | Started: <start_time>
...
```

**Example:**
```bash
./scripts/jobctl.sh list
./scripts/jobctl.sh list running
./scripts/jobctl.sh list failed
```

---

#### `cleanup` - Clean up job files

**Syntax:**
```bash
./scripts/jobctl.sh cleanup <job_id>
```

**Parameters:**
- `job_id` (required): Job identifier

**Returns:**
```json
{
  "job_id": "<job_id>",
  "status": "cleaned",
  "message": "Job files removed"
}
```

**Example:**
```bash
./scripts/jobctl.sh cleanup my-job
```

---

#### `verify` - Verify job output

**Syntax:**
```bash
./scripts/jobctl.sh verify <job_id>
```

**Parameters:**
- `job_id` (required): Job identifier

**Returns:**
```json
{
  "job_id": "<job_id>",
  "status": "verified",
  "verification_score": <score>
}
```

**Example:**
```bash
./scripts/jobctl.sh verify my-job
```

---

#### `debug` - Get debug information

**Syntax:**
```bash
./scripts/jobctl.sh debug <job_id>
```

**Parameters:**
- `job_id` (required): Job identifier

**Returns:**
```
=== DEBUG INFO FOR JOB: <job_id> ===

--- State ---
<state_json>

--- PID File ---
<pid>

Process info:
<process_info>

--- Log File (last 20 lines) ---
<log_lines>

--- Output File ---
<output>

--- Feedback ---
<feedback>
```

**Example:**
```bash
./scripts/jobctl.sh debug my-job
```

---

#### `help` - Show help

**Syntax:**
```bash
./scripts/jobctl.sh help
./scripts/jobctl.sh --help
./scripts/jobctl.sh -h
```

**Returns:**
Usage information and command descriptions.

---

## ⚙️ Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `NONBLOCKING_BASE_DIR` | `~/.nonblocking` | Base directory for all files |
| `MAX_RUNTIME` | `86400` | Maximum runtime in seconds (24 hours) |
| `POLL_INTERVAL` | `2` | Polling interval in seconds |
| `MAX_POLL_ATTEMPTS` | `120` | Maximum polling attempts |
| `DEFAULT_MODEL` | `gpt-4o-mini` | Default AI model |
| `DEFAULT_MAX_TOKENS` | `2048` | Default max tokens |
| `LOG_LEVEL` | `INFO` | Log level (DEBUG, INFO, WARN, ERROR, CRITICAL) |
| `TOKEN_WARNING_THRESHOLD` | `4000` | Token usage warning threshold |
| `TOKEN_ERROR_THRESHOLD` | `8000` | Token usage error threshold |

---

## 📄 State File Format

State files are stored in JSON format at:
```
$NONBLOCKING_BASE_DIR/state/<job_id>.json
```

**Format:**
```json
{
  "job_id": "string",
  "command": "string",
  "status": "queued|running|paused|stopped|completed|failed|verified",
  "pid": "integer",
  "start_time": "ISO 8601 timestamp",
  "end_time": "ISO 8601 timestamp",
  "exit_code": "integer",
  "callback_url": "string",
  "model": "string",
  "max_tokens": "integer",
  "tokens_used": "integer",
  "token_rate": "float",
  "output_hash": "string",
  "error_message": "string",
  "retry_count": "integer",
  "verified": "boolean",
  "verification_score": "float",
  "verification_issues": "string",
  "self_improvement": "object"
}
```

**Fields:**
- `job_id`: Unique job identifier
- `command`: Original command string
- `status`: Current job status
- `pid`: Process ID of the running job
- `start_time`: When the job started (ISO 8601 format)
- `end_time`: When the job ended (ISO 8601 format)
- `exit_code`: Exit code of the command (0 = success)
- `callback_url`: URL for async notifications
- `model`: AI model used
- `max_tokens`: Maximum tokens allowed
- `tokens_used`: Number of tokens used
- `token_rate`: Tokens per second
- `output_hash`: SHA-256 hash of output
- `error_message`: Error message if job failed
- `retry_count`: Number of retry attempts
- `verified`: Whether output has been verified
- `verification_score`: Verification confidence score (0.0 - 1.0)
- `verification_issues`: Detected issues during verification
- `self_improvement`: Self-improvement suggestions

---

## 📝 Log File Format

Log files are stored at:
```
$NONBLOCKING_BASE_DIR/logs/<job_id>.log
```

**Format:**
```
[2026-09-06T14:00:00Z] [INFO] Starting command execution
<command output>
[2026-09-06T14:05:00Z] [INFO] Command finished with exit code 0
```

**Log Levels:**
- `DEBUG`: Detailed debugging information
- `INFO`: Normal operational messages
- `WARN`: Warning messages
- `ERROR`: Error messages
- `CRITICAL`: Critical errors

---

## 📤 Callback Format

When a job completes and a callback URL is provided, a POST request is made with the following JSON payload:

**Format:**
```json
{
  "job_id": "<job_id>",
  "status": "completed|failed|stopped",
  "exit_code": <exit_code>,
  "output": "<output>",
  "tokens_used": <tokens_used>,
  "duration": "<duration>"
}
```

**Fields:**
- `job_id`: Job identifier
- `status`: Final job status
- `exit_code`: Exit code of the command
- `output`: Command output (stdout)
- `tokens_used`: Number of tokens used
- `duration`: Human-readable duration (e.g., "2m 30s")

**Headers:**
```
Content-Type: application/json
Accept: application/json
```

**Example:**
```json
{
  "job_id": "my-job",
  "status": "completed",
  "exit_code": 0,
  "output": "Hello, World!",
  "tokens_used": 50,
  "duration": "0h 0m 1s"
}
```

---

## 💬 Feedback Format

Feedback files are stored at:
```
$NONBLOCKING_BASE_DIR/feedback/<job_id>.feedback
```

**Format:**
```json
{
  "job_id": "<job_id>",
  "feedback": "<feedback_text>",
  "rating": <rating>,
  "timestamp": "ISO 8601 timestamp",
  "model": "<model>"
}
```

**Fields:**
- `job_id`: Job identifier
- `feedback`: User feedback text
- `rating`: Rating (1-5)
- `timestamp`: When feedback was recorded
- `model`: AI model used

**Example:**
```json
{
  "job_id": "my-job",
  "feedback": "Output was helpful but could be more detailed",
  "rating": 4,
  "timestamp": "2026-09-06T14:30:00Z",
  "model": "gpt-4o-mini"
}
```

---

## 🔢 Exit Codes

| Exit Code | Meaning | Description |
|-----------|--------|-------------|
| 0 | Success | Job completed successfully |
| 1 | Error | General error |
| 124 | Timeout | Job exceeded maximum runtime |
| 137 | Killed | Job was killed (SIGKILL) |
| 143 | Terminated | Job was terminated (SIGTERM) |
| 130 | Interrupted | Job was interrupted (SIGINT) |

---

## ❌ Error Handling

### Error Response Format

When an error occurs, commands return a non-zero exit code and may output an error message to stderr.

**Format:**
```
Error: <error_message>
```

**Or JSON:**
```json
{
  "error": "<error_message>"
}
```

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `Job ID is required` | Missing job_id parameter | Provide a job_id |
| `Command is required` | Missing command parameter | Provide a command |
| `Job <job_id> already exists` | Duplicate job_id | Use a unique job_id |
| `Job <job_id> not found` | Job doesn't exist | Check job_id spelling |
| `Job <job_id> not running` | Job already stopped | Job may have completed |
| `Log file not found` | No log file exists | Job may not have started yet |
| `Output file not found` | No output file exists | Job may not have completed yet |

---

## 🎯 Best Practices

### 1. Always Check Return Codes

```bash
if ! ./scripts/jobctl.sh start my-job 'command'; then
    echo "Failed to start job"
    exit 1
fi
```

### 2. Parse JSON Output

```bash
# Using jq
STATUS=$(./scripts/jobctl.sh status my-job | jq -r '.status')

# Using python
STATUS=$(./scripts/jobctl.sh status my-job | python3 -c "import json,sys; print(json.load(sys.stdin)['status'])")
```

### 3. Handle Errors Gracefully

```bash
if ! result=$(./scripts/jobctl.sh start my-job 'command' 2>&1); then
    echo "Error: $result" >&2
    exit 1
fi
```

### 4. Use Timeouts

```bash
# Timeout after 10 seconds
timeout 10 ./scripts/jobctl.sh poll my-job
```

### 5. Validate Inputs

```bash
if [[ -z "$JOB_ID" ]]; then
    echo "Error: Job ID is required" >&2
    exit 1
fi

if [[ -z "$COMMAND" ]]; then
    echo "Error: Command is required" >&2
    exit 1
fi
```

---

## 📚 Examples

### Example 1: Basic Job Execution

```bash
# Start a job
./scripts/jobctl.sh start my-job 'echo hello' > /dev/null

# Check status
STATUS=$(./scripts/jobctl.sh status my-job | jq -r '.status')

if [[ "$STATUS" == "completed" ]]; then
    echo "Job completed!"
fi

# Get output
OUTPUT=$(cat ~/.nonblocking/state/my-job.output)
echo "Output: $OUTPUT"

# Cleanup
./scripts/jobctl.sh cleanup my-job
```

### Example 2: With Error Handling

```bash
# Start job with error handling
if ! ./scripts/jobctl.sh start my-job 'echo hello' > /dev/null 2>&1; then
    echo "Failed to start job" >&2
    exit 1
fi

# Poll with timeout
if ! timeout 30 ./scripts/jobctl.sh poll my-job 2 > /dev/null; then
    echo "Job timed out or failed" >&2
    exit 1
fi

# Check exit code
STATUS=$(./scripts/jobctl.sh status my-job)
EXIT_CODE=$(echo "$STATUS" | jq -r '.exit_code')

if [[ "$EXIT_CODE" != "0" ]]; then
    echo "Job failed with exit code: $EXIT_CODE" >&2
    exit 1
fi

# Cleanup
trap './scripts/jobctl.sh cleanup my-job > /dev/null 2>&1' EXIT
```

### Example 3: With Callback

```bash
# Start job with callback
./scripts/jobctl.sh start webhook-job 'long-task' https://my-api.com/callback

# The callback will receive:
# POST /callback
# Content-Type: application/json
#
# {
#   "job_id": "webhook-job",
#   "status": "completed",
#   "exit_code": 0,
#   "output": "...",
#   "tokens_used": 1500,
#   "duration": "2m 30s"
# }
```

---

**For more information, see:**
- [SKILL.md](../SKILL.md) - Complete skill documentation
- [README.md](../README.md) - Quick start guide
- [INTEGRATION.md](./INTEGRATION.md) - Integration guide
- [BEST_PRACTICES.md](./BEST_PRACTICES.md) - Best practices guide
