---
name: failure-forensics
description: "Use when an agent task fails or produces unexpected results. Performs structured post-mortem root cause analysis: categorizes the failure, traces the exact failure point through tool-call logs, reconstructs the decision chain, generates a post-mortem report, and saves lessons to prevent recurrence."
version: 1.0.0
author: Denis Voronin
license: MIT
metadata:
  hermes:
    tags: [debugging, post-mortem, forensics, root-cause-analysis, failure-analysis, agent-reliability]
    related_skills: [systematic-debugging, debugging-hermes-tui-commands]
---

# Failure Forensics

## Overview

When an agent task fails, the default response is to retry — hoping for a different outcome. **Failure Forensics** rejects that reflex. Instead, the agent performs structured root cause analysis *before* retrying, treating every failure as evidence to be collected, categorized, and learned from.

The workflow has four phases:

1. **Triage** — Categorize the failure using the taxonomy in [`references/failure-taxonomy.md`](references/failure-taxonomy.md).
2. **Timeline Reconstruction** — Parse tool-call logs and agent decision points to build a chronological failure timeline. The script [`scripts/failure_forensics.py`](scripts/failure_forensics.py) automates this from JSON or JSONL log formats.
3. **Causal Chain Analysis** — Trace the chain of decisions, assumptions, and actions that led from the task kickoff to the failure point. Identify the *root cause*, not just the proximate symptom.
4. **Post-Mortem Report** — Generate a structured report from the template in [`references/post-mortem-template.md`](references/post-mortem-template.md) and persist it so future sessions can learn.

This skill turns a single failure into a permanent, reusable lesson.

## When to Use

- **An agent task failed** and retrying without understanding *why* is risky.
- **A failure recurs** across attempts — you suspect a systemic cause, not bad luck.
- **You need an artifact** documenting what went wrong for a team review or audit.
- **A complex multi-step task** partially completed then broke — you need to understand which step is safe to resume from.
- **You want to improve agent reliability** by building a corpus of past failure patterns.

### Don't use for:

- **Trivial failures with obvious fixes** (typo in a command, missing flag). Fix and move on.
- **Live debugging** of an actively failing process — use `systematic-debugging` for that. Run forensics *after* the process is dead or the task is abandoned.
- **Human performance reviews.** This skill analyzes agent + tool behavior, not people.

## The Forensics Workflow

### Phase 1: Triage — Categorize the Failure

Read the full taxonomy in [`references/failure-taxonomy.md`](references/failure-taxonomy.md). At a high level, every failure falls into one of six categories:

| Category | Signature | First Question |
|---|---|---|
| **Network** | Connection refused, timeout, DNS, TLS, 5xx HTTP | "Is the endpoint reachable *right now*?" |
| **Permissions** | 401/403, EACCES, "permission denied", "unauthorized" | "Does the credential/token have the needed scope?" |
| **Logic** | Code runs but output is wrong; assertions fail; data is corrupt | "What assumption did the code make that was false?" |
| **Environment** | Missing binary, wrong version, missing env var, wrong OS | "What does `env`/`which`/`uname` say vs. what was expected?" |
| **Dependency** | ImportError, version conflict, package not found, ABI mismatch | "What changed in the dependency graph?" |
| **Resource** | OOM, disk full, too many open files, rate limit, quota exhausted | "What was the ceiling, and what hit it?" |

Record the category — it determines the questions you ask next.

### Phase 2: Timeline Reconstruction

Collect the evidence:

1. **Tool-call logs.** If the agent session logged tool calls (JSON or JSONL with timestamps, tool name, args, result/error), feed them to the analyzer:

   ```bash
   python3 scripts/failure_forensics.py analyze \
     --log session.jsonl \
     --output timeline.md
   ```

   The script produces a chronological timeline with:
   - Each tool call, its timestamp, duration, and outcome (success/failure)
   - The **first failure point** flagged
   - Error messages and exit codes extracted
   - A summary of the failure category (inferred from error signatures)

2. **Manual reconstruction.** If no structured logs exist, reconstruct the timeline from memory of the session. List each decision and action in order. Be honest about uncertainty — mark gaps explicitly.

3. **What to capture for each step:**
   - Timestamp (or relative ordering)
   - The action or decision taken
   - The *intent* behind it (what the agent was trying to achieve)
   - The actual outcome
   - Any assumption the agent made

### Phase 3: Causal Chain Analysis

This is the core of forensics. You're looking for the **causal chain** — the sequence where each link made the next failure more likely.

Ask these questions in order:

1. **What was the immediate (proximate) cause of failure?**
   - The error message, the crash point, the wrong output. This is the *symptom*.

2. **What was the agent doing when it failed?**
   - The specific tool call or action. What was the goal of that action?

3. **Why did the agent take that action at that point?**
   - Trace back one decision. What information did the agent have? What did it assume?

4. **Was that assumption valid?**
   - Check against logs, file contents, environment state. A failed assumption here is a link in the causal chain.

5. **Continue backward** until you reach either:
   - A **root cause**: a decision or state that, if different, would have prevented the entire failure cascade. Stop here.
   - The **task kickoff**: if no single root cause emerges, the failure is *systemic* (multiple contributing factors).

6. **Look for contributing factors** that didn't *cause* the failure but made it worse or harder to recover from:
   - Missing retry logic
   - Poor error messages that obscured the real problem
   - Timeouts set too aggressively or too loosely
   - Insufficient logging that made diagnosis harder

**Anti-pattern: the "five whys" that stops at one.** The first "why" almost always produces the symptom, not the cause. Keep going. The root cause is usually 3-5 links back.

### Phase 4: Post-Mortem Report

Fill out the template in [`references/post-mortem-template.md`](references/post-mortem-template.md). Key sections:

- **Summary** — one paragraph, plain language. A reader who wasn't there should understand it.
- **Timeline** — the reconstructed failure timeline from Phase 2.
- **Root Cause** — the terminal link of the causal chain from Phase 3, stated plainly.
- **Contributing Factors** — the rest of the chain.
- **Action Items** — concrete, assigned, verifiable. "Add retry logic" is bad; "Add exponential backoff retry (max 3 attempts) to the `web_extract` call in `session.py:142`" is good.
- **Lessons Learned** — generalizable insights. These are the durable output.

**Save the report.** Write it to a persistent location (e.g., a `post-mortems/` directory, an issue tracker, or a knowledge base). A post-mortem that isn't saved didn't happen.

## Using the Forensics Script

The script `scripts/failure_forensics.py` has three subcommands:

### `analyze` — Build a failure timeline from logs

```bash
# JSONL log (one JSON object per line)
python3 scripts/failure_forensics.py analyze --log session.jsonl --format jsonl

# JSON array
python3 scripts/failure_forensics.py analyze --log session.json --format json

# Write report to file
python3 scripts/failure_forensics.py analyze --log session.jsonl --output report.md
```

### `categorize` — Classify an error message

```bash
python3 scripts/failure_forensics.py categorize --error "ConnectionRefusedError: [Errno 111] Connection refused"
# Output: network

python3 scripts/failure_forensics.py categorize --error "PermissionError: [Errno 13] Permission denied"
# Output: permissions
```

### `report` — Generate a post-mortem template pre-filled with timeline data

```bash
python3 scripts/failure_forensics.py report --log session.jsonl --title "Deploy failure 2024-01-15" --author "agent"
```

### Expected Log Format

The analyzer accepts JSON/JSONL where each entry is a tool call record:

```json
{
  "timestamp": "2024-01-15T10:23:45Z",
  "tool": "terminal",
  "args": {"command": "npm install"},
  "result": {"success": false, "error": "EACCES: permission denied, open '/usr/lib/node_modules'"},
  "duration_ms": 1200
}
```

Required fields: `timestamp` (ISO 8601), `tool`. The script tolerates missing optional fields (`result`, `duration_ms`, `args`).

## Common Pitfalls

1. **Confusing symptom with cause.** "The deploy failed because the build failed" is a symptom. "The build failed because `package-lock.json` was regenerated with a different Node version than CI" is a cause. Keep digging past the symptom.

2. **Stopping at human error.** "I made a mistake" is never a root cause. Ask *why* the mistake was possible — missing validation? Misleading documentation? Fatigue from context switching? Fix the system, not the human.

3. **Writing action items that aren't actionable.** "Be more careful" is worthless. Every action item must specify *what* to change, *where*, and *how to verify* it works.

4. **Skipping the timeline.** Without a chronological timeline, causal chain analysis becomes guessing. Build the timeline first, even if it's rough.

5. **Not saving the post-mortem.** A post-mortem kept in chat history is lost when the session ends. Write it to a durable artifact (file, issue, doc).

6. **Blame-oriented language.** Post-mortems are blameless by design. Describe what *happened*, not who *messed up*. This is especially important when the "who" is an agent — focus on the decision and the information available at the time.

7. **Retrying before forensics.** The whole point is to analyze before retrying. If you retry first, you lose the original failure state and may introduce changes that mask the real cause.

## Verification Checklist

- [ ] Failure categorized into one of the six taxonomy categories
- [ ] Timeline reconstructed (either via script or manually) with timestamps/ordering
- [ ] Causal chain traced backward to a root cause or identified as systemic
- [ ] Post-mortem report filled from the template
- [ ] Report saved to a durable location
- [ ] At least one concrete, verifiable action item identified
- [ ] Lessons learned phrased as generalizable insights, not task-specific notes
