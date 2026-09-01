---
name: log-analyzer
description: Parse, filter, and summarize log files for errors, warnings, patterns, and time-based anomalies. Works with standard text logs, JSON logs, and delimited formats. Use when triaging production issues, auditing system behavior, or extracting actionable signals from log dumps.
metadata:
  openclaw:
    emoji: "📋"
    requires:
      commands: ["grep", "awk", "sort", "uniq", "tail", "head"]
---

# Log Analyzer Skill

Fast, dependency-free log analysis using standard Unix tools.

## When to Use

- **Production triage**: Quickly find errors and their frequency
- **Pattern extraction**: Identify recurring issues across large log files
- **Time-based analysis**: Find errors within a specific time window
- **Log format conversion**: Parse JSON, CSV, or pipe-delimited logs into readable summaries

## Core Workflow

```bash
# 1. Find errors
grep -i "error\|fatal\|exception" /var/log/app.log | tail -100

# 2. Count error types
grep -i "error" app.log | awk '{print $1,$2,$3}' | sort | uniq -c | sort -rn | head -20

# 3. Time-window filter (last 30 minutes)
awk -v cutoff=$(date -d '30 minutes ago' '+%Y-%m-%dT%H:%M:%S') '$1 >= cutoff' app.log

# 4. JSON log parsing
grep '"level":"error"' app.json.log | jq -r '.timestamp + " " + .message'
```

## Key Commands

### Error Detection

```bash
# All error-level entries
grep -inE "error|fatal|critical|exception|panic" app.log

# Errors only (exclude warnings)
grep -inE "\b(error|fatal|panic)\b" app.log

# Exclude known noise
grep -iE "error" app.log | grep -v "expected disconnect" | grep -v "retrying"
```

### Frequency & Top-N Analysis

```bash
# Top 20 error messages
grep -i "error" app.log \
  | sed 's/[0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\} [0-9]\{2\}:[0-9]\{2\}:[0-9]\{2\}//' \
  | sort | uniq -c | sort -rn | head -20

# Top 10 IPs with errors
grep "error" access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -10

# Error count by hour
grep "error" app.log | awk '{print $1,$2}' | cut -d: -f1,2 | uniq -c
```

### Time-Window Analysis

```bash
# Errors in last hour
since=$(date -d '1 hour ago' '+%Y-%m-%dT%H:%M')
grep "error" app.log | awk -v s="$since" '$1" "$2 >= s'

# Errors between timestamps
awk '$1 >= "2024-01-15T10:00:00" && $1 <= "2024-01-15T11:00:00"' app.log

# Peak error time
grep "error" app.log | awk -F'T' '{print $2}' | cut -d: -f1 | uniq -c | sort -rn | head -5
```

### JSON Log Parsing

```bash
# Require jq for structured JSON logs
# Error entries
grep '"level":"error"' app.json.log | jq -r '.timestamp + " " + .message'

# Error count by service
jq -s 'group_by(.service) | map({service: .[0].service, count: length})' app.json.log

# Extract stack traces
jq -r 'select(.level=="error") | "\(.timestamp) \(.message)\n\(.stackTrace // "")"' app.json.log
```

### Correlation

```bash
# Correlate errors with specific user/request IDs
grep "error" app.log | grep "user_id=abc123"

# Find requests that errored and their full lifecycle
grep "request_id=xyz789" app.log

# Error followed by timeout
grep -A1 "error" app.log | grep "timeout"
```

### Health Check

```bash
# Summary stats
total=$(wc -l < app.log)
errors=$(grep -ciE "error|fatal" app.log)
warnings=$(grep -c "warn" app.log)
echo "Total: $total | Errors: $errors | Warnings: $warnings | Error rate: $(echo "scale=2; $errors*100/$total" | bc)%"
```

## Best Practices

1. **Always use `-i`** for case-insensitive matching unless you're sure of casing
2. **Pipe to `tail`** when checking recent activity — don't load entire files
3. **Filter noise early** with `grep -v` before aggregation
4. **Use `jq`** for JSON logs — never parse JSON with regex
5. **Save patterns** as shell aliases for recurring analyses

## Example: Full Triage

```bash
# Scenario: App is slow, need to find cause
LOG=/var/log/app/production.log

echo "=== Error count: $(grep -ciE 'error|fatal' $LOG) ==="
echo "=== Top 10 error types ==="
grep -iE "error|fatal" $LOG | sed 's/^[0-9-]* [0-9:]*//' | sort | uniq -c | sort -rn | head -10
echo "=== Errors in last 10 minutes ==="
since=$(date -d '10 min ago' '+%Y-%m-%dT%H:%M:%S')
awk -v s="$since" '$1" "$2 >= s' $LOG | grep -iE "error|fatal"
echo "=== Disk-related errors ==="
grep -iE "disk|no space|enospc" $LOG | tail -20
echo "=== Memory-related errors ==="
grep -iE "out of memory|oom|kill process" $LOG | tail -20
```
