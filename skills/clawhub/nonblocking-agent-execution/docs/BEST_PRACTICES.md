# 🏆 Best Practices Guide - Non-Blocking Agent Execution v2.0.0

This guide covers best practices for using the **nonblocking-agent-execution** skill effectively, safely, and efficiently.

---

## 📋 Table of Contents

1. [General Best Practices](#-general-best-practices)
2. [Command Design](#-command-design)
3. [Error Handling](#-error-handling)
4. [Token Optimization](#-token-optimization)
5. [Hallucination Prevention](#-hallucination-prevention)
6. [Performance Optimization](#-performance-optimization)
7. [Security Best Practices](#-security-best-practices)
8. [Monitoring and Observability](#-monitoring-and-observability)
9. [Testing Strategies](#-testing-strategies)
10. [Debugging Techniques](#-debugging-techniques)

---

## 🎯 General Best Practices

### 1. Always Use Non-Blocking Pattern

**✅ Do:**
```bash
# Start job in background
./scripts/jobctl.sh start my-job 'long-running-command'

# Continue with other work
./scripts/jobctl.sh start another-job 'another-command'

# Poll for completion later
./scripts/jobctl.sh poll my-job
```

**❌ Don't:**
```bash
# This blocks the agent
long-running-command
```

### 2. Always Check Job Status

**✅ Do:**
```bash
# Start job
./scripts/jobctl.sh start my-job 'command'

# Check status before assuming completion
STATUS=$(./scripts/jobctl.sh status my-job | jq -r '.status')
if [[ "$STATUS" == "completed" ]]; then
    echo "Job completed"
fi
```

**❌ Don't:**
```bash
# Assume job completed without checking
./scripts/jobctl.sh start my-job 'command'
sleep 10
# Assume it's done - it might still be running!
```

### 3. Always Clean Up

**✅ Do:**
```bash
# Clean up when done
./scripts/jobctl.sh cleanup my-job
```

**❌ Don't:**
```bash
# Leave job files accumulating
# (This fills up disk space over time)
```

### 4. Use Meaningful Job IDs

**✅ Do:**
```bash
# Use descriptive job IDs
./scripts/jobctl.sh start build-app-v1.2.3 'npm run build'
./scripts/jobctl.sh start process-data-2026-09-06 'python process.py'
```

**❌ Don't:**
```bash
# Use generic or random IDs
./scripts/jobctl.sh start job1 'command'
./scripts/jobctl.sh start abc123 'command'
```

### 5. Set Appropriate Timeouts

**✅ Do:**
```bash
# Set timeout based on expected duration
MAX_RUNTIME=3600 ./scripts/jobctl.sh start long-job 'command'  # 1 hour
MAX_RUNTIME=300 ./scripts/jobctl.sh start quick-job 'command'  # 5 minutes
```

**❌ Don't:**
```bash
# Use default timeout for everything
# (24 hours might be too long for quick jobs)
./scripts/jobctl.sh start quick-job 'command'
```

---

## 💻 Command Design

### 1. Make Commands Non-Interactive

**✅ Do:**
```bash
# Always add non-interactive flags
./scripts/jobctl.sh start my-job 'apt-get install -y package'
./scripts/jobctl.sh start my-job 'pip install --yes package'
./scripts/jobctl.sh start my-job 'npx --yes command'
```

**❌ Don't:**
```bash
# Interactive commands will hang
./scripts/jobctl.sh start my-job 'apt-get install package'
./scripts/jobctl.sh start my-job 'pip install package'
```

**Automatic Optimization:**
The skill automatically adds `--yes`, `-y`, and `--no-input` flags to common commands.

### 2. Handle stdin Properly

**✅ Do:**
```bash
# Redirect stdin from /dev/null
./scripts/jobctl.sh start my-job 'command < /dev/null'
```

**❌ Don't:**
```bash
# Command might wait for stdin
./scripts/jobctl.sh start my-job 'command'
```

**Automatic Handling:**
The skill automatically redirects stdin from `/dev/null` for all commands.

### 3. Use Absolute Paths

**✅ Do:**
```bash
# Use absolute paths for reliability
./scripts/jobctl.sh start my-job '/usr/bin/python3 /path/to/script.py'
```

**❌ Don't:**
```bash
# Relative paths might not work
./scripts/jobctl.sh start my-job 'python3 script.py'
```

### 4. Set Working Directory

**✅ Do:**
```bash
# Change to working directory first
./scripts/jobctl.sh start my-job 'cd /path/to/project && npm install'
```

**❌ Don't:**
```bash
# Command might fail if run from wrong directory
./scripts/jobctl.sh start my-job 'npm install'
```

### 5. Handle Dependencies

**✅ Do:**
```bash
# Install dependencies first
./scripts/jobctl.sh start install-deps 'npm install'

# Then run the command
./scripts/jobctl.sh start run-app 'npm start'
```

**❌ Don't:**
```bash
# Assume dependencies are installed
./scripts/jobctl.sh start run-app 'npm start'
```

### 6. Chain Commands Properly

**✅ Do:**
```bash
# Use && for sequential commands
./scripts/jobctl.sh start my-job 'command1 && command2 && command3'

# Use ; for independent commands
./scripts/jobctl.sh start my-job 'command1 ; command2 ; command3'
```

**❌ Don't:**
```bash
# Use && when commands should run independently
# (If command1 fails, command2 and command3 won't run)
./scripts/jobctl.sh start my-job 'command1 && command2 && command3'
```

### 7. Handle Errors in Commands

**✅ Do:**
```bash
# Check exit codes
./scripts/jobctl.sh start my-job 'command1 || echo "Failed" && exit 1'

# Or use set -e
./scripts/jobctl.sh start my-job 'set -e; command1; command2; command3'
```

**❌ Don't:**
```bash
# Ignore errors
./scripts/jobctl.sh start my-job 'command1; command2; command3'
```

---

## 🛡️ Error Handling

### 1. Check Exit Codes

**✅ Do:**
```bash
# Start job
./scripts/jobctl.sh start my-job 'command'

# Poll for completion
./scripts/jobctl.sh poll my-job

# Check exit code
STATUS=$(./scripts/jobctl.sh status my-job)
EXIT_CODE=$(echo "$STATUS" | jq -r '.exit_code')

if [[ "$EXIT_CODE" != "0" ]]; then
    echo "Job failed with exit code: $EXIT_CODE"
    ./scripts/jobctl.sh log my-job
fi
```

**❌ Don't:**
```bash
# Ignore exit codes
./scripts/jobctl.sh start my-job 'command'
# Assume it worked
```

### 2. Implement Retry Logic

**✅ Do:**
```bash
MAX_RETRIES=3
for attempt in $(seq 1 $MAX_RETRIES); do
    ./scripts/jobctl.sh start retry-job-$attempt 'flaky-command' >/dev/null
    
    # Wait and check
    sleep 5
    STATUS=$(./scripts/jobctl.sh status retry-job-$attempt | jq -r '.status')
    
    if [[ "$STATUS" == "completed" ]]; then
        EXIT_CODE=$(./scripts/jobctl.sh status retry-job-$attempt | jq -r '.exit_code')
        if [[ "$EXIT_CODE" == "0" ]]; then
            echo "Success on attempt $attempt"
            break
        fi
    fi
    
    # Cleanup failed attempt
    ./scripts/jobctl.sh cleanup retry-job-$attempt
done
```

**❌ Don't:**
```bash
# No retry logic
./scripts/jobctl.sh start my-job 'flaky-command'
```

### 3. Use Watchdog Timers

**✅ Do:**
```bash
# Set appropriate timeout
MAX_RUNTIME=300 ./scripts/jobctl.sh start timed-job 'command'
```

**❌ Don't:**
```bash
# No timeout - job could run forever
./scripts/jobctl.sh start my-job 'long-running-command'
```

### 4. Handle Timeouts Gracefully

**✅ Do:**
```bash
# Check if job was timed out
STATUS=$(./scripts/jobctl.sh status my-job)
EXIT_CODE=$(echo "$STATUS" | jq -r '.exit_code')

if [[ "$EXIT_CODE" == "124" ]]; then
    echo "Job timed out"
    # Handle timeout appropriately
fi
```

**❌ Don't:**
```bash
# Ignore timeout exit code
./scripts/jobctl.sh start my-job 'command'
```

### 5. Validate Inputs

**✅ Do:**
```bash
# Validate job ID
if [[ -z "$JOB_ID" ]]; then
    echo "Error: Job ID is required"
    exit 1
fi

# Validate command
if [[ -z "$COMMAND" ]]; then
    echo "Error: Command is required"
    exit 1
fi

# Then start job
./scripts/jobctl.sh start "$JOB_ID" "$COMMAND"
```

**❌ Don't:**
```bash
# No validation
./scripts/jobctl.sh start "$JOB_ID" "$COMMAND"
```

---

## 💰 Token Optimization

### 1. Monitor Token Usage

**✅ Do:**
```bash
# Check token usage regularly
STATUS=$(./scripts/jobctl.sh status my-job)
TOKENS=$(echo "$STATUS" | jq -r '.tokens_used')

if [[ "$TOKENS" -gt 4000 ]]; then
    echo "Warning: High token usage"
fi
```

**❌ Don't:**
```bash
# Ignore token usage
./scripts/jobctl.sh start my-job 'command'
```

### 2. Set Appropriate Token Limits

**✅ Do:**
```bash
# Set max_tokens based on task
./scripts/jobctl.sh start simple-job 'command' https://callback gpt-4o-mini 512
./scripts/jobctl.sh start complex-job 'command' https://callback gpt-4o-mini 2048
```

**❌ Don't:**
```bash
# Use default for everything
./scripts/jobctl.sh start my-job 'command' https://callback
```

### 3. Use Smaller Models When Possible

**✅ Do:**
```bash
# Use smaller model for simple tasks
./scripts/jobctl.sh start simple-job 'command' https://callback gpt-4o-mini 512

# Use larger model for complex tasks
./scripts/jobctl.sh start complex-job 'command' https://callback gpt-4 4096
```

**❌ Don't:**
```bash
# Always use largest model
./scripts/jobctl.sh start my-job 'command' https://callback gpt-4 4096
```

### 4. Optimize Command Output

**✅ Do:**
```bash
# Reduce output size
./scripts/jobctl.sh start my-job 'command | head -100'

# Or filter output
./scripts/jobctl.sh start my-job 'command | grep "important"'
```

**❌ Don't:**
```bash
# Let command produce unlimited output
./scripts/jobctl.sh start my-job 'command'
```

### 5. Cache Results

**✅ Do:**
```bash
# Check cache first
if [[ -f "cache/result.txt" ]]; then
    echo "Using cached result"
else
    ./scripts/jobctl.sh start my-job 'expensive-command'
    ./scripts/jobctl.sh poll my-job
    cp ~/.nonblocking/state/my-job.output cache/result.txt
fi
```

**❌ Don't:**
```bash
# Always recompute
./scripts/jobctl.sh start my-job 'expensive-command'
```

---

## 🤖 Hallucination Prevention

### 1. Always Verify Output

**✅ Do:**
```bash
# Start job
./scripts/jobctl.sh start my-job 'generate-report'

# Wait for completion
./scripts/jobctl.sh poll my-job

# Verify output
./scripts/jobctl.sh verify my-job

# Check verification score
SCORE=$(./scripts/jobctl.sh status my-job | jq -r '.verification_score')
if [[ $(echo "$SCORE < 0.7" | bc) -eq 1 ]]; then
    echo "Output verification failed"
fi
```

**❌ Don't:**
```bash
# Use output without verification
./scripts/jobctl.sh start my-job 'generate-report'
./scripts/jobctl.sh poll my-job
OUTPUT=$(cat ~/.nonblocking/state/my-job.output)
# Use output without checking
```

### 2. Check for Common Hallucination Patterns

**✅ Do:**
```bash
# Check for specific patterns
OUTPUT=$(cat ~/.nonblocking/state/my-job.output)
if echo "$OUTPUT" | grep -qi "i don't have access"; then
    echo "Hallucination detected: no access statement"
fi

if echo "$OUTPUT" | grep -qi "as of my last update"; then
    echo "Hallucination detected: last update disclaimer"
fi
```

**❌ Don't:**
```bash
# Don't check for hallucinations
OUTPUT=$(cat ~/.nonblocking/state/my-job.output)
# Use output as-is
```

### 3. Use Grounded Prompts

**✅ Do:**
```bash
# Include context in command
./scripts/jobctl.sh start my-job 'generate-report --context "$(cat context.txt)"'
```

**❌ Don't:**
```bash
# No context
./scripts/jobctl.sh start my-job 'generate-report'
```

### 4. Validate Against Known Facts

**✅ Do:**
```bash
# Validate output against known facts
OUTPUT=$(cat ~/.nonblocking/state/my-job.output)
if ! echo "$OUTPUT" | grep -q "known-fact"; then
    echo "Output doesn't contain expected fact"
fi
```

**❌ Don't:**
```bash
# Don't validate
OUTPUT=$(cat ~/.nonblocking/state/my-job.output)
# Use output without validation
```

---

## ⚡ Performance Optimization

### 1. Parallelize Independent Jobs

**✅ Do:**
```bash
# Start multiple independent jobs
for i in {1..5}; do
    ./scripts/jobctl.sh start job-$i "process_item $i"
done

# Monitor all
watch -n 2 './scripts/jobctl.sh list'
```

**❌ Don't:**
```bash
# Process sequentially
for i in {1..5}; do
    ./scripts/jobctl.sh start job-$i "process_item $i"
    ./scripts/jobctl.sh poll job-$i
    ./scripts/jobctl.sh cleanup job-$i
done
```

### 2. Use Appropriate Polling Intervals

**✅ Do:**
```bash
# Short interval for quick jobs
./scripts/jobctl.sh poll quick-job 1

# Long interval for long jobs
./scripts/jobctl.sh poll long-job 10
```

**❌ Don't:**
```bash
# Always use same interval
./scripts/jobctl.sh poll my-job 5
```

### 3. Optimize Command Execution

**✅ Do:**
```bash
# Use faster alternatives
./scripts/jobctl.sh start my-job 'fast-command --optimized'

# Or parallelize within command
./scripts/jobctl.sh start my-job 'parallel -j4 command'
```

**❌ Don't:**
```bash
# Use slow commands
./scripts/jobctl.sh start my-job 'slow-command'
```

### 4. Use Efficient Models

**✅ Do:**
```bash
# Use fastest model for time-sensitive tasks
./scripts/jobctl.sh start urgent-job 'command' https://callback groq/gpt-oss-120b 2048

# Use most accurate model for quality-sensitive tasks
./scripts/jobctl.sh start quality-job 'command' https://callback gpt-4 4096
```

**❌ Don't:**
```bash
# Always use same model
./scripts/jobctl.sh start my-job 'command' https://callback gpt-4o-mini 2048
```

---

## 🔒 Security Best Practices

### 1. Run with Least Privilege

**✅ Do:**
```bash
# Run as non-root user
sudo -u nobody ./scripts/jobctl.sh start my-job 'command'

# Or use dedicated user
sudo -u agentuser ./scripts/jobctl.sh start my-job 'command'
```

**❌ Don't:**
```bash
# Run as root
sudo ./scripts/jobctl.sh start my-job 'command'
```

### 2. Use Sandboxing

**✅ Do:**
```bash
# Use firejail for sandboxing
./scripts/jobctl.sh start my-job 'firejail --noprofile command'

# Or use containers
./scripts/jobctl.sh start my-job 'docker run --rm image command'
```

**❌ Don't:**
```bash
# Run without sandboxing
./scripts/jobctl.sh start my-job 'command'
```

### 3. Limit Resources

**✅ Do:**
```bash
# Use ulimit to limit resources
ulimit -t 300 -m 1000000 -v 1000000
./scripts/jobctl.sh start my-job 'command'

# Or use cgroups
cgcreate -g cpu,memory:/mygroup
cgset -r cpu.cfs_quota_us=100000 mygroup
./scripts/jobctl.sh start my-job 'cgexec -g cpu,memory:mygroup command'
```

**❌ Don't:**
```bash
# No resource limits
./scripts/jobctl.sh start my-job 'command'
```

### 4. Protect Sensitive Data

**✅ Do:**
```bash
# Use chmod to protect files
chmod 600 ~/.nonblocking/state/*.json
chmod 600 ~/.nonblocking/state/*.output

# Or use encrypted storage
./scripts/jobctl.sh start my-job 'command | gpg --encrypt > output.gpg'
```

**❌ Don't:**
```bash
# Leave files world-readable
# (Default permissions might be too open)
```

### 5. Validate All Inputs

**✅ Do:**
```bash
# Validate job ID (alphanumeric only)
if ! [[ "$JOB_ID" =~ ^[a-zA-Z0-9_-]+$ ]]; then
    echo "Invalid job ID"
    exit 1
fi

# Validate command (no dangerous characters)
if [[ "$COMMAND" =~ [\;\|\&\<\(] ]]; then
    echo "Invalid command"
    exit 1
fi

# Then start job
./scripts/jobctl.sh start "$JOB_ID" "$COMMAND"
```

**❌ Don't:**
```bash
# No input validation
./scripts/jobctl.sh start "$JOB_ID" "$COMMAND"
```

### 6. Use HTTPS for Callbacks

**✅ Do:**
```bash
# Use HTTPS callback URLs
./scripts/jobctl.sh start my-job 'command' https://my-server.com/callback
```

**❌ Don't:**
```bash
# Use HTTP (insecure)
./scripts/jobctl.sh start my-job 'command' http://my-server.com/callback
```

### 7. Clean Up Regularly

**✅ Do:**
```bash
# Clean up old jobs
find ~/.nonblocking/state -name "*.json" -mtime +7 -exec basename {} \; | \
  while read job_id; do
    ./scripts/jobctl.sh cleanup "${job_id%.json}"
  done

# Or use cron
0 3 * * * /path/to/cleanup_old_jobs.sh
```

**❌ Don't:**
```bash
# Never clean up
# (Disk space will fill up over time)
```

---

## 📊 Monitoring and Observability

### 1. Enable Debug Logging

**✅ Do:**
```bash
# Enable debug mode for troubleshooting
export LOG_LEVEL=DEBUG
./scripts/jobctl.sh start my-job 'command'
```

**❌ Don't:**
```bash
# Always run without debug info
./scripts/jobctl.sh start my-job 'command'
```

### 2. Monitor Job Status

**✅ Do:**
```bash
# Check status regularly
watch -n 5 './scripts/jobctl.sh list'

# Or use a monitoring script
while true; do
    ./scripts/jobctl.sh list
    sleep 30
done
```

**❌ Don't:**
```bash
# Never check status
./scripts/jobctl.sh start my-job 'command'
# Forget about it
```

### 3. Use Structured Logging

**✅ Do:**
```bash
# Logs are already structured JSON
cat ~/.nonblocking/logs/jobctl.log | jq '.'
```

**❌ Don't:**
```bash
# Ignore logs
```

### 4. Monitor Resource Usage

**✅ Do:**
```bash
# Check running processes
ps aux | grep jobctl

# Check memory usage
top -p $(cat ~/.nonblocking/run/*.pid)

# Check disk usage
du -sh ~/.nonblocking/
```

**❌ Don't:**
```bash
# Never check resource usage
```

### 5. Set Up Alerts

**✅ Do:**
```bash
# Alert on too many running jobs
RUNNING=$(./scripts/jobctl.sh list running | wc -l)
if [[ "$RUNNING" -gt 10 ]]; then
    echo "Alert: Too many running jobs" | mail -s "Alert" admin@example.com
fi

# Alert on failed jobs
FAILED=$(./scripts/jobctl.sh list failed | wc -l)
if [[ "$FAILED" -gt 0 ]]; then
    echo "Alert: Failed jobs detected" | mail -s "Alert" admin@example.com
fi
```

**❌ Don't:**
```bash
# No alerts
```

---

## 🧪 Testing Strategies

### 1. Test with Simple Commands First

**✅ Do:**
```bash
# Test with echo
./scripts/jobctl.sh start test-echo 'echo hello'
./scripts/jobctl.sh poll test-echo
./scripts/jobctl.sh verify test-echo
./scripts/jobctl.sh cleanup test-echo

# Then test with real commands
./scripts/jobctl.sh start test-real 'real-command'
```

**❌ Don't:**
```bash
# Test with complex command first
./scripts/jobctl.sh start complex-job 'complex-command-with-many-steps'
```

### 2. Test Error Cases

**✅ Do:**
```bash
# Test with failing command
./scripts/jobctl.sh start test-fail 'exit 1'
./scripts/jobctl.sh poll test-fail
STATUS=$(./scripts/jobctl.sh status test-fail | jq -r '.status')
if [[ "$STATUS" == "failed" ]]; then
    echo "Error handling works"
fi
./scripts/jobctl.sh cleanup test-fail
```

**❌ Don't:**
```bash
# Only test success cases
```

### 3. Test Timeout Cases

**✅ Do:**
```bash
# Test with command that takes too long
MAX_RUNTIME=5 ./scripts/jobctl.sh start test-timeout 'sleep 10'
sleep 6
STATUS=$(./scripts/jobctl.sh status test-timeout | jq -r '.status')
if [[ "$STATUS" == "failed" ]]; then
    EXIT_CODE=$(./scripts/jobctl.sh status test-timeout | jq -r '.exit_code')
    if [[ "$EXIT_CODE" == "124" ]]; then
        echo "Timeout handling works"
    fi
fi
./scripts/jobctl.sh cleanup test-timeout
```

**❌ Don't:**
```bash
# Don't test timeouts
```

### 4. Test with Different Models

**✅ Do:**
```bash
# Test with different models
for model in gpt-4o-mini claude-3-sonnet mistral-7b-instruct; do
    ./scripts/jobctl.sh start test-$model 'echo hello' https://callback $model 512
    ./scripts/jobctl.sh poll test-$model
    ./scripts/jobctl.sh cleanup test-$model
done
```

**❌ Don't:**
```bash
# Only test with one model
./scripts/jobctl.sh start my-job 'command' https://callback gpt-4o-mini 2048
```

### 5. Test Token Monitoring

**✅ Do:**
```bash
# Test token monitoring
TOKEN_WARNING_THRESHOLD=100 TOKEN_ERROR_THRESHOLD=200
./scripts/jobctl.sh start test-tokens 'echo hello' https://callback
STATUS=$(./scripts/jobctl.sh status test-tokens)
TOKENS=$(echo "$STATUS" | jq -r '.tokens_used')
echo "Tokens used: $TOKENS"
./scripts/jobctl.sh cleanup test-tokens
```

**❌ Don't:**
```bash
# Don't test token monitoring
```

---

## 🐞 Debugging Techniques

### 1. Use Debug Command

**✅ Do:**
```bash
# Get full debug info
./scripts/jobctl.sh debug my-job
```

This shows:
- Job state
- Process information
- Log file contents
- Output file contents
- Feedback if available

### 2. Check Logs

**✅ Do:**
```bash
# View log file
./scripts/jobctl.sh log my-job 100

# Or view directly
cat ~/.nonblocking/logs/my-job.log
```

### 3. Enable Debug Mode

**✅ Do:**
```bash
# Enable debug logging
export LOG_LEVEL=DEBUG
./scripts/jobctl.sh start my-job 'command'

# View debug logs
cat ~/.nonblocking/logs/jobctl.log | grep DEBUG
```

### 4. Check Process Information

**✅ Do:**
```bash
# Get process info
PID=$(cat ~/.nonblocking/run/my-job.pid)
ps -p $PID -o pid,ppid,cmd,%cpu,%mem,etime

# Or use debug command
./scripts/jobctl.sh debug my-job
```

### 5. Verify State Files

**✅ Do:**
```bash
# Check state file
cat ~/.nonblocking/state/my-job.json | jq '.'

# Validate JSON
cat ~/.nonblocking/state/my-job.json | jq empty
```

### 6. Test with Minimal Command

**✅ Do:**
```bash
# Test with simplest possible command
./scripts/jobctl.sh start test-minimal 'true'
./scripts/jobctl.sh status test-minimal
./scripts/jobctl.sh cleanup test-minimal
```

### 7. Check Environment Variables

**✅ Do:**
```bash
# Verify environment
echo "NONBLOCKING_BASE_DIR: $NONBLOCKING_BASE_DIR"
echo "MAX_RUNTIME: $MAX_RUNTIME"
echo "POLL_INTERVAL: $POLL_INTERVAL"
echo "LOG_LEVEL: $LOG_LEVEL"

# Check if directories exist
ls -la "$NONBLOCKING_BASE_DIR"
```

### 8. Use strace for Advanced Debugging

**✅ Do:**
```bash
# Trace system calls
strace -f -o debug.log ./scripts/jobctl.sh start my-job 'command'

# Analyze log
cat debug.log | grep -i error
```

### 9. Check for Resource Limits

**✅ Do:**
```bash
# Check ulimits
ulimit -a

# Check disk space
df -h

# Check memory
free -h
```

### 10. Common Debug Patterns

#### Issue: Job not starting
```bash
# Check if job exists
./scripts/jobctl.sh status my-job

# Check if PID file exists
ls -la ~/.nonblocking/run/my-job.pid

# Check logs
./scripts/jobctl.sh log my-job

# Try with debug mode
LOG_LEVEL=DEBUG ./scripts/jobctl.sh start my-job 'echo hello'
```

#### Issue: Job hanging
```bash
# Check process
PID=$(cat ~/.nonblocking/run/my-job.pid)
ps -p $PID

# Check what it's doing
strace -p $PID

# Or use gdb
gdb -p $PID
```

#### Issue: High token usage
```bash
# Check token usage
./scripts/jobctl.sh status my-job | jq '.tokens_used'

# Check command
cat ~/.nonblocking/state/my-job.json | jq -r '.command'

# Optimize command
./scripts/jobctl.sh start optimized-job 'optimized-command'
```

#### Issue: Verification failed
```bash
# Check verification score
./scripts/jobctl.sh status my-job | jq '.verification_score'

# Check verification issues
./scripts/jobctl.sh status my-job | jq -r '.verification_issues'

# View output
cat ~/.nonblocking/state/my-job.output
```

#### Issue: Callback not received
```bash
# Check callback URL
./scripts/jobctl.sh status my-job | jq -r '.callback_url'

# Check if callback was attempted
cat ~/.nonblocking/logs/jobctl.log | grep callback

# Test callback manually
curl -X POST -H "Content-Type: application/json" -d '{"test":"data"}' https://callback.url
```

---

## 📚 Summary Checklist

### Before Starting a Job
- [ ] Use meaningful job ID
- [ ] Validate inputs (job_id, command)
- [ ] Set appropriate timeout
- [ ] Set appropriate model and max_tokens
- [ ] Ensure command is non-interactive
- [ ] Check disk space and resources

### While Job is Running
- [ ] Monitor status regularly
- [ ] Check logs for errors
- [ ] Monitor token usage
- [ ] Handle timeouts appropriately
- [ ] Implement retry logic for failures

### After Job Completes
- [ ] Verify output
- [ ] Check exit code
- [ ] Handle errors appropriately
- [ ] Clean up job files
- [ ] Collect feedback for improvement

### For Production Use
- [ ] Set up monitoring
- [ ] Configure alerts
- [ ] Implement proper logging
- [ ] Set resource limits
- [ ] Use sandboxing for untrusted commands
- [ ] Regularly clean up old jobs
- [ ] Test with various models
- [ ] Optimize token usage

---

## 🎯 Quick Reference

### Essential Commands
```bash
# Start a job
./scripts/jobctl.sh start <job_id> '<command>' [callback] [model] [max_tokens]

# Check status
./scripts/jobctl.sh status <job_id>

# Poll until complete
./scripts/jobctl.sh poll <job_id> [interval]

# View logs
./scripts/jobctl.sh log <job_id> [lines]

# Stop a job
./scripts/jobctl.sh stop <job_id>

# List jobs
./scripts/jobctl.sh list [filter]

# Cleanup
./scripts/jobctl.sh cleanup <job_id>

# Verify output
./scripts/jobctl.sh verify <job_id>

# Debug
./scripts/jobctl.sh debug <job_id>
```

### Environment Variables
```bash
export NONBLOCKING_BASE_DIR=/path/to/base    # Base directory
export MAX_RUNTIME=3600                        # Max runtime in seconds
export POLL_INTERVAL=2                         # Poll interval in seconds
export MAX_POLL_ATTEMPTS=120                  # Max poll attempts
export DEFAULT_MODEL=gpt-4o-mini              # Default AI model
export DEFAULT_MAX_TOKENS=2048               # Default max tokens
export LOG_LEVEL=INFO                         # Log level (DEBUG, INFO, WARN, ERROR)
export TOKEN_WARNING_THRESHOLD=4000          # Token warning threshold
export TOKEN_ERROR_THRESHOLD=8000            # Token error threshold
```

---

**Follow these best practices to get the most out of the nonblocking-agent-execution skill! 🚀**

For more information, see:
- [SKILL.md](../SKILL.md) - Complete documentation
- [README.md](../README.md) - Quick start guide
- [INTEGRATION.md](./INTEGRATION.md) - Integration guide
