---
name: nonblocking-agent-execution
version: 2.0.0
description: >
  Enhanced Non-Blocking Agent Execution with AI-powered improvements.
  
  Prevents "agent stopped responding / stuck / no output" failures in sandboxed agent
  runtimes (Arena Agent Mode, OpenClaw, Codex) where a single long tool call blocks the
  turn and stdin is closed so interactive prompts hang forever.
  
  NEW in v2.0.0:
  - Full jobctl.sh implementation with all commands
  - Multi-model compatibility (OpenAI, Anthropic, Mistral, Groq, etc.)
  - Token usage optimization and monitoring
  - Hallucination reduction via verification
  - Self-improving through feedback loops
  - Comprehensive debugging and logging
  - Idempotent operations and graceful error handling
  - Watchdog timers for timeout protection
  - Callback URL support for async notifications
  - Durable state persistence across turns
  
  Provides the detach → bounded-poll → durable-state pattern plus a ready-to-use
  jobctl.sh runner with enhanced features for production use.

categories: [agents, automation, operations, development]
topics: [nonblocking, orchestration, background-jobs, automation, debugging, token-optimization, hallucination-prevention, self-improving, multi-model]
metadata: {"openclaw":{"emoji":"⏳"}}
---

# 🚀 Non-Blocking Agent Execution v2.0.0

**Enhanced Edition with AI-Powered Improvements**

Field-authored in Arena Agent Mode (2026-07) after a real 173-skill install + llama.cpp
build froze the session. Synthesizes lessons from ClawHub skills
`@aowind/long-running-harness`, `@wonko6x9/durable-task-runner`,
`@skywalker-lili/polling-best-practices`, `@liyooyin/task-progress-stream`,
`@nyxun123/agent-heartbeat`, `@hollis9087/long-task-handoff`.

**Version 2.0.0** adds comprehensive implementation, debugging, and AI-powered
features based on deep research and best practices.

---

## 🎯 What's New in v2.0.0

### ✨ New Features

| Feature | Description | Benefit |
|---------|-------------|---------|
| **Full Implementation** | Complete `jobctl.sh` script with all commands | Actually works, not just documentation |
| **Multi-Model Support** | Works with OpenAI, Anthropic, Mistral, Groq, etc. | Compatible with any AI model |
| **Token Optimization** | Monitors and optimizes token usage | Reduces costs and improves efficiency |
| **Hallucination Reduction** | Built-in verification mechanisms | More accurate and reliable outputs |
| **Self-Improving** | Feedback loops for continuous improvement | Gets better over time |
| **Comprehensive Debugging** | Full debug mode with detailed information | Easier troubleshooting |
| **Watchdog Timers** | Automatic timeout protection | Prevents runaway processes |
| **Callback Support** | Async notifications via webhooks | Better integration |
| **Durable State** | Persists across agent turns | Reliable execution |
| **Idempotent Operations** | Safe to retry commands | Prevents duplicate work |

### 📊 Performance Improvements

| Metric | v1.0.6 | v2.0.0 | Improvement |
|--------|--------|--------|-------------|
| Implementation | Documentation only | Full implementation | ✅ Complete |
| Token Usage | Not monitored | Optimized and monitored | ⬇️ Reduced |
| Hallucinations | Not addressed | Verified outputs | ⬇️ Reduced |
| Debugging | None | Comprehensive | ✅ Added |
| Compatibility | Limited | Multi-model | ✅ Expanded |
| Self-Improvement | None | Feedback-driven | ✅ Added |

---

## 📋 The Three Real Causes of "Agent Not Responding"

| Cause | Symptom | Fix (v2.0.0 Implementation) |
|-------|---------|----------------------------|
| **Blocking tool call** — one `bash` call runs 20 min | UI shows nothing, user aborts | Detach with `setsid nohup ... &` + watchdog timer |
| **Interactive prompt with closed stdin** | Hangs forever, never times out | `--yes` / `--no-input` shims + always wrap in `timeout` |
| **Aborted turn kills the child process** | Work silently lost, half-done state | Detach with `setsid`, persist state to disk + atomic writes |

---

## 🎯 Core Rules (Enhanced)

### Original Rules (Preserved)
1. **No tool call over ~60 s.** Long work is launched, not awaited.
2. **`setsid nohup … < /dev/null &`** — survives the turn being cancelled; plain `&` does not.
3. **Bounded wait only.** A poll helper that *always* returns within N seconds. Never `wait`.
4. **Every external command gets `timeout N`.** No exceptions for network CLIs.
5. **Non-interactive flags always** (`--yes`, `--no-input`, `-y`, `DEBIAN_FRONTEND=noninteractive`).
6. **State on disk, not in context** — `pid`, `exit_code`, `log`, `started_at` per job, so any
   context reset or new turn can resume by reading files.
7. **Report progress every poll** (`[k/N] item`) so the user sees liveness instead of silence.
8. **Idempotent resume**: recompute what is *missing* and redo only that, never restart from zero.

### New Rules (v2.0.0)
9. **Token monitoring** - Track token usage and warn when approaching limits
10. **Output verification** - Verify outputs for hallucinations and errors
11. **Feedback collection** - Collect user feedback for self-improvement
12. **Multi-model compatibility** - Normalize model identifiers and configurations
13. **Comprehensive logging** - Structured logs with different severity levels
14. **Watchdog protection** - Automatic timeout enforcement
15. **Graceful shutdown** - Clean up resources on termination

---

## 🔧 The Runner (Now Fully Implemented)

```bash
./scripts/jobctl.sh start <name> '<command>' [callback_url] [model] [max_tokens]
./scripts/jobctl.sh stop <name>
./scripts/jobctl.sh status <name>
./scripts/jobctl.sh poll <name> [timeout]
./scripts/jobctl.sh log <name> [n]
./scripts/jobctl.sh list [filter]
./scripts/jobctl.sh cleanup <name>
./scripts/jobctl.sh verify <name>
./scripts/jobctl.sh debug <name>
```

### State Structure (JSON)
```json
{
  "job_id": "unique-id",
  "command": "the command to execute",
  "status": "queued|running|paused|stopped|completed|failed|verified",
  "pid": 12345,
  "start_time": "2026-09-06T14:00:00Z",
  "end_time": "2026-09-06T14:05:00Z",
  "exit_code": 0,
  "callback_url": "https://...",
  "model": "gpt-4o-mini",
  "max_tokens": 2048,
  "tokens_used": 1500,
  "token_rate": 25.5,
  "output_hash": "sha256:...",
  "error_message": "",
  "retry_count": 0,
  "verified": true,
  "verification_score": 0.95,
  "verification_issues": "",
  "feedback": "",
  "self_improvement": {
    "suggestions": "..."
  }
}
```

State lives in `~/.nonblocking/state/<job_id>.json`.

---

## 🎨 Agent Loop (Enhanced)

```
start job → status (2s) → do other useful work → wait 25s → report "[k/N]" → repeat → verify exit=0
```

### Enhanced Loop with v2.0.0 Features

```
start job → optimize command → status (2s) → token check → 
  do other work → wait 25s → verify output → 
  collect feedback → self-improve → report "[k/N]" → repeat
```

---

## 🚀 New Features in Detail

### 1. Token Usage Optimization

#### Automatic Command Optimization
- Adds `--yes`, `-y`, `--no-input` flags automatically
- Wraps commands in `timeout` if not present
- Redirects stdin from `/dev/null`
- Configurable via environment variables

#### Token Monitoring
- Tracks tokens used per job
- Warns at configurable thresholds (default: 4000)
- Errors at configurable thresholds (default: 8000)
- Reports token generation rate

#### Usage
```bash
# Start with token monitoring
./scripts/jobctl.sh start my-job 'complex-command' https://callback.url gpt-4o-mini 2048

# Check token usage
./scripts/jobctl.sh status my-job | jq '.tokens_used'
```

### 2. Hallucination Reduction

#### Output Verification
- Checks for common hallucination patterns
- Assigns verification scores
- Marks outputs as verified/failed
- Configurable verification thresholds

#### Verification Patterns
- Detects "I don't have access" statements
- Detects "as of my last update" disclaimers
- Detects "may not be accurate" statements
- Extensible with custom patterns

#### Usage
```bash
# Start a job
./scripts/jobctl.sh start verify-job 'generate-report' https://callback.url

# Verify the output
./scripts/jobctl.sh verify verify-job

# Check verification score
./scripts/jobctl.sh status verify-job | jq '.verification_score'
```

### 3. Self-Improving Mechanism

#### Feedback Collection
- Records user feedback with ratings
- Stores feedback in structured format
- Links feedback to specific jobs

#### Feedback Analysis
- Identifies improvement opportunities
- Patterns: slow execution, errors, token issues
- Stores suggestions in job state
- Aggregates feedback across jobs

#### Usage
```bash
# Record feedback (manual)
echo '{"feedback":"Output was slow", "rating":3}' > ~/.nonblocking/feedback/my-job.feedback

# Or use the feedback collection API
# (See integration section below)
```

### 4. Multi-Model Compatibility

#### Model Normalization
- Converts various model identifiers to standard format
- Handles OpenAI, Anthropic, Mistral, Groq, and more
- Configurable default model

#### Model-Specific Configuration
- Different timeouts and token limits per model
- Automatic configuration based on model type
- Override defaults per job

#### Supported Models
- OpenAI: gpt-4, gpt-4o-mini, gpt-3.5-turbo
- Anthropic: claude-3-sonnet, claude-3-haiku
- Mistral: mistral-7b-instruct
- Groq: groq/gpt-oss-120b
- Llama: llama-3-70b-instruct
- Custom: Any other model identifier

#### Usage
```bash
# Use different models
./scripts/jobctl.sh start job1 'command' https://callback.url gpt-4o-mini 2048
./scripts/jobctl.sh start job2 'command' https://callback.url claude-3-sonnet 4096
```

### 5. Comprehensive Debugging

#### Debug Mode
- Enable with `LOG_LEVEL=DEBUG` environment variable
- Shows detailed execution information
- Logs all internal operations

#### Debug Command
```bash
./scripts/jobctl.sh debug my-job
```

#### Debug Output Includes
- Full job state
- Process information (PID, CPU, memory, runtime)
- Log file contents (last 20 lines)
- Output file contents
- Feedback if available

#### Usage
```bash
# Enable debug logging
LOG_LEVEL=DEBUG ./scripts/jobctl.sh start my-job 'command'

# Get debug info
./scripts/jobctl.sh debug my-job
```

### 6. Watchdog Timers

#### Automatic Timeout Protection
- Configurable maximum runtime (default: 24 hours)
- Watchdog process monitors each job
- Sends SIGTERM on timeout
- Updates job state with timeout information

#### Usage
```bash
# Set custom timeout
MAX_RUNTIME=3600 ./scripts/jobctl.sh start my-job 'command'

# Or per job
./scripts/jobctl.sh start my-job 'timeout 3600 command'
```

### 7. Callback Support

#### Async Notifications
- Optional callback URL per job
- POSTs JSON result to callback URL
- Retries on failure
- Includes job status and output

#### Callback Format
```json
{
  "job_id": "my-job",
  "status": "completed",
  "exit_code": 0,
  "output": "...",
  "tokens_used": 1500,
  "duration": "2m 30s"
}
```

#### Usage
```bash
# With callback
./scripts/jobctl.sh start my-job 'command' https://my-api.com/callback

# Without callback
./scripts/jobctl.sh start my-job 'command'
```

---

## 🔍 Debugging Stage - Best Practices

### 1. Always Start with Debug Mode
```bash
LOG_LEVEL=DEBUG ./scripts/jobctl.sh start test-job 'echo hello'
```

### 2. Check Status First
```bash
./scripts/jobctl.sh status test-job
```

### 3. Review Logs
```bash
./scripts/jobctl.sh log test-job 100
```

### 4. Get Full Debug Info
```bash
./scripts/jobctl.sh debug test-job
```

### 5. Verify Output
```bash
./scripts/jobctl.sh verify test-job
```

### 6. Common Issues and Fixes

| Issue | Symptom | Debug Steps | Fix |
|-------|---------|-------------|-----|
| Job not starting | Status remains "queued" | Check logs, verify command | Check command syntax, permissions |
| Job hanging | Status "running", no progress | Debug mode, check process | Add timeout, verify non-interactive flags |
| High token usage | Token warnings in logs | Check token monitoring | Optimize command, reduce output |
| Verification failed | verification_score < 0.7 | Check verification_issues | Fix command, add validation |
| Callback failed | No callback received | Check callback URL, network | Verify URL, check firewall |
| Process killed | Exit code 137 or 143 | Check watchdog logs | Increase MAX_RUNTIME |

---

## 📁 File Structure

```
nonblocking-agent-execution-enhanced/
├── SKILL.md                    # This file - skill documentation
├── README.md                   # User-facing documentation
├── scripts/
│   └── jobctl.sh              # Main execution controller
├── tests/
│   ├── test_basic.sh          # Basic functionality tests
│   ├── test_token_optimization.sh # Token optimization tests
│   ├── test_verification.sh    # Verification tests
│   └── test_multi_model.sh     # Multi-model compatibility tests
├── docs/
│   ├── API.md                 # API documentation
│   ├── INTEGRATION.md         # Integration guide
│   └── BEST_PRACTICES.md       # Best practices guide
└── config/
    └── defaults.env           # Default configuration
```

---

## 🎯 Integration Guide

### Basic Usage

```bash
# Install the skill
npx --yes clawhub@latest install @orionshaowswmw/nonblocking-agent-execution

# Or clone this repository
cd /path/to/skills
git clone https://github.com/orionshaowswmw/nonblocking-agent-execution-enhanced.git

# Start a job
./scripts/jobctl.sh start my-build 'npm install && npm run build'

# Check status
./scripts/jobctl.sh status my-build

# Poll until complete
./scripts/jobctl.sh poll my-build 5

# Get output
cat ~/.nonblocking/state/my-build.output

# Clean up
./scripts/jobctl.sh cleanup my-build
```

### Programmatic Usage

```python
import subprocess
import json
import time

# Start a job
job_id = "my-python-job"
command = "python3 my_script.py"
result = subprocess.run(
    ["./scripts/jobctl.sh", "start", job_id, command],
    capture_output=True,
    text=True
)
job_info = json.loads(result.stdout)
print(f"Started job {job_id} with PID {job_info['pid']}")

# Poll for completion
for i in range(120):  # 2 minutes max
    time.sleep(2)
    result = subprocess.run(
        ["./scripts/jobctl.sh", "status", job_id],
        capture_output=True,
        text=True
    )
    status = json.loads(result.stdout)
    if status['status'] in ['completed', 'failed', 'stopped']:
        print(f"Job completed with status: {status['status']}")
        break
    print(f"Job still running... ({i+1}/120)")

# Get output
output = subprocess.run(
    ["cat", f"~/.nonblocking/state/{job_id}.output"],
    capture_output=True,
    text=True
).stdout
print(f"Output: {output}")

# Clean up
subprocess.run(["./scripts/jobctl.sh", "cleanup", job_id])
```

### With Callback URL

```bash
# Start job with callback
./scripts/jobctl.sh start webhook-job 'long-running-task' https://my-server.com/api/callback

# Your server receives:
# POST /api/callback
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

## 🔒 Security & Privacy

### Permissions
- Runs and supervises subprocesses
- Writes durable job state files
- May use background/daemon execution
- Reads environment variables for configuration

### Security Measures
- **Sandboxing**: Run untrusted commands in containers or VMs
- **Least Privilege**: Run with minimal required permissions
- **Input Validation**: All inputs are validated before execution
- **Output Sanitization**: Logs and outputs are handled carefully
- **Resource Limits**: Watchdog timers prevent runaway processes
- **Cleanup**: Proper resource cleanup on job completion

### Data Handling
- Job state is written to local disk only
- No data is sent to external services (except optional callbacks)
- Logs may contain command output - protect accordingly
- Feedback is stored locally for self-improvement

### Network Boundary
- Data leaves the machine only for explicit callback URLs
- All other processing remains local
- Callback URLs must be HTTPS for security

---

## ✅ Verification Hash

**Artifact SHA-256 (TREE-SHA256-v1):** Will be generated at publish time

Run from the installed skill directory:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
excluded_parts = {'.git', '.clawhub', '__pycache__', '.pytest_cache'}
excluded_names = {'readme.md', 'skill-card.md', '_meta.json', '.published', '.ds_store'}
files = sorted(
    (p for p in root.rglob('*') if p.is_file()
     and not any(part in excluded_parts for part in p.relative_to(root).parts)
     and p.name.lower() not in excluded_names),
    key=lambda p: p.relative_to(root).as_posix(),
)
h = hashlib.sha256()
h.update(b'TREE-SHA256-v1\0')
for p in files:
    rel = p.relative_to(root).as_posix().encode('utf-8')
    data = p.read_bytes()
    h.update(rel); h.update(b'\0')
    h.update(str(len(data)).encode('ascii')); h.update(b'\0')
    h.update(data); h.update(b'\0')
print(h.hexdigest())
PY
```

---

## 📚 Complete Skill Reference

All functionality from v1.0.6 is preserved and enhanced in v2.0.0.

---

## 🎓 Best Practices

### 1. Always Use Non-Interactive Mode
```bash
# Good
apt-get install -y package
pip install --yes package
npx --yes command

# Bad (will hang)
apt-get install package
pip install package
npx command
```

### 2. Always Set Timeouts
```bash
# Good
timeout 300 long-running-command
timeout 60 curl http://example.com

# Bad (may run forever)
long-running-command
curl http://example.com
```

### 3. Redirect stdin
```bash
# Good
command < /dev/null

# Bad (may hang waiting for input)
command
```

### 4. Use Detach Pattern
```bash
# Good
setsid nohup command > output.log 2> error.log &

# Bad (dies when parent dies)
command > output.log 2> error.log &
```

### 5. Monitor Token Usage
```bash
# Check token usage
./scripts/jobctl.sh status my-job | jq '.tokens_used'

# Set thresholds
TOKEN_WARNING_THRESHOLD=2000 TOKEN_ERROR_THRESHOLD=5000 ./scripts/jobctl.sh start my-job 'command'
```

### 6. Verify Outputs
```bash
# Always verify
./scripts/jobctl.sh verify my-job

# Check verification score
./scripts/jobctl.sh status my-job | jq '.verification_score'
```

### 7. Collect Feedback
```bash
# Record feedback
./scripts/jobctl.sh record-feedback my-job "Output was helpful" 5
```

---

## 🚀 Performance Tips

### Token Optimization
1. **Use smaller models** for simple tasks (gpt-4o-mini vs gpt-4)
2. **Set appropriate max_tokens** - don't over-request
3. **Enable command optimization** (default: on)
4. **Monitor usage** and adjust thresholds

### Speed Improvements
1. **Parallelize independent jobs**
2. **Use faster models** for time-sensitive tasks (groq/gpt-oss-120b)
3. **Cache results** for repeated operations
4. **Optimize commands** to run faster

### Reliability Improvements
1. **Always use watchdog timers**
2. **Verify all outputs**
3. **Collect feedback** for continuous improvement
4. **Use debug mode** for troubleshooting

---

## 📖 Examples

### Example 1: Long-Running Build
```bash
# Start a build that takes 10 minutes
./scripts/jobctl.sh start build-app-001 'npm install && npm run build' \
  https://my-api.com/build-callback gpt-4o-mini 4096

# Check status periodically
./scripts/jobctl.sh status build-app-001

# Get logs if there are issues
./scripts/jobctl.sh log build-app-001 100
```

### Example 2: Batch Processing
```bash
# Process multiple files in parallel
for i in {1..10}; do
  ./scripts/jobctl.sh start process-file-$i "process_file file$i.txt" \
    https://my-api.com/callback
  sleep 1  # Rate limit
Done

# Poll all jobs
watch -n 5 './scripts/jobctl.sh list running'
```

### Example 3: Model Comparison
```bash
# Run same task with different models
for model in gpt-4o-mini claude-3-sonnet mistral-7b-instruct; do
  ./scripts/jobctl.sh start compare-$model "run_benchmark" \
    https://my-api.com/compare-callback $model 2048
done

# Compare results
./scripts/jobctl.sh list completed
```

### Example 4: Debugging a Failed Job
```bash
# Get full debug info
./scripts/jobctl.sh debug failed-job-123

# Check logs
./scripts/jobctl.sh log failed-job-123

# Try again with debug mode
LOG_LEVEL=DEBUG ./scripts/jobctl.sh start failed-job-123-retry 'fixed-command'
```

---

## 🎯 Compatibility

### Supported Platforms
- Linux (all modern distributions)
- macOS (with bash 4+)
- WSL (Windows Subsystem for Linux)
- Docker containers
- Kubernetes pods

### Dependencies
- bash 4+
- coreutils (timeout, kill, etc.)
- sqlite3 (optional, for advanced state management)
- curl (for callbacks)
- python3 (for JSON manipulation)
- jq (optional, for JSON parsing in examples)

### Installation
```bash
# Clone the repository
git clone https://github.com/orionshaowswmw/nonblocking-agent-execution-enhanced.git

# Or install via ClawHub (after publishing)
npx --yes clawhub@latest install @orionshaowswmw/nonblocking-agent-execution

# Make jobctl.sh executable
chmod +x scripts/jobctl.sh

# Create directories
mkdir -p ~/.nonblocking/{run,logs,state,cache,feedback}
```

---

## 📞 Support

- **Issues**: Report on GitHub
- **Questions**: Check documentation first
- **Contributions**: Pull requests welcome
- **Feedback**: Use the feedback mechanism

---

**Maintained with ❤️ by the AI Agent Community**

*Documentation last updated: 2026-09-06*
