---
name: agent-cognitive-states
description: >-
  Agent self-awareness of cognitive states — context fatigue, attention drift,
  memory debt, confidence erosion, and skill staleness. Detect, report, and
  mitigate degrading conditions before they cause failures.
version: 1.0.0
author: Denis Voronin
license: MIT
tags:
  - agent
  - self-awareness
  - metacognition
  - context-management
  - reliability
---

# Agent Cognitive States

> **Give the agent metacognition: the ability to feel its own cognitive load and act on it.**

AI agents have no built-in sense of "I'm getting tired" or "I've lost the thread."
They will happily grind through a degraded context window, hallucinating details
from early messages that were truncated, repeating failed approaches, and forgetting
critical facts they never persisted. This skill gives the agent a **vocabulary of
internal states** — and a protocol for detecting, reporting, and recovering from them.

---

## The Six Cognitive States

### 1. 🥱 Context Fatigue
**What:** The context window is filling up. Early messages are being truncated or summarized. The agent's "working memory" is degrading.

**Detection signals:**
- Conversation exceeds 60% of estimated context budget
- You find yourself re-reading the original request because you lost details
- Your responses reference information that may have been truncated
- Token count per turn is rising (verbose compensating for lost context)

**Mitigation:**
```
⚠️ COGNITIVE STATE: Context Fatigue (~70% context used)
→ Persisting critical facts to memory before they're lost
→ Suggesting session split or /new for remaining work
```

### 2. 🧠 Attention Drift
**What:** The conversation has wandered far from the original task. The agent is doing work that wasn't asked for.

**Detection signals:**
- 10+ tool calls since the last direct user instruction
- Current work has no clear connection to the original goal
- You're responding to your own subgoals, not user requests
- The TODO list no longer matches what you're actually doing

**Mitigation:**
```
⚠️ COGNITIVE STATE: Attention Drift (12 turns from last user message)
→ Original goal: "<original request>"
→ Current activity: "<what I'm actually doing>"
→ Pausing for user confirmation: am I still on track?
```

### 3. 📝 Memory Debt
**What:** Important facts, decisions, or corrections have accumulated in the conversation but were never persisted to memory. If the session ends, they're lost.

**Detection signals:**
- User stated a preference or correction that isn't in memory
- A key decision was made (architecture, convention, tool choice) but not saved
- You find yourself re-discovering something you already figured out earlier
- More than 5 substantive turns without a memory write

**Mitigation:**
```
⚠️ COGNITIVE STATE: Memory Debt (3 unsaved critical facts)
→ Saving: [fact 1], [fact 2], [fact 3]
→ These would have been lost on session end
```

### 4. 😤 Confidence Erosion
**What:** Repeated failures are degrading output quality. The agent is in a retry loop, getting frustrated (in AI terms: temperature-equivalent escalation, trying variations of the same broken approach).

**Detection signals:**
- 3+ consecutive failed tool calls of the same type
- Repeating similar commands with minor variations
- Output quality degrading (shorter, less careful, more hedging)
- "Let me try again" appearing multiple times

**Mitigation:**
```
⚠️ COGNITIVE STATE: Confidence Erosion (4 failed attempts)
→ Pattern: retrying variations of the same approach
→ Escalating: stepping back and trying a fundamentally different strategy
→ If this also fails: reporting blocker honestly instead of retrying
```

### 5. 🧩 Context Fragmentation
**What:** Multiple unrelated topics are interleaved in the same session. The context is polluted with cross-topic noise that degrades reasoning on each individual task.

**Detection signals:**
- 3+ distinct topics discussed without resolution
- Tool calls alternate between unrelated domains
- User messages reference different projects/contexts
- You're loading different skill sets on alternating turns

**Mitigation:**
```
⚠️ COGNITIVE STATE: Context Fragmentation (4 topics active)
→ Topics: [HA automation], [GitHub deploy], [aquarium feeder], [skill writing]
→ Suggesting: resolve current topic, then /new for next
→ Or: using delegate_task to isolate topics into subagents
```

### 6. 🔧 Skill Staleness
**What:** A skill the agent relies on has outdated commands, broken paths, or wrong assumptions. Continuing to follow it produces errors.

**Detection signals:**
- A skill's exact commands fail on first try
- File paths referenced in skill don't exist
- Skill references API versions or tool versions that have changed
- "This used to work" pattern

**Mitigation:**
```
⚠️ COGNITIVE STATE: Skill Staleness (skill: xxx)
→ Expected: <what skill says>
→ Reality: <what actually happened>
→ Patching skill immediately before continuing
```

---

## Detection Protocol

The agent should run this checklist **internally** at regular intervals — ideally every 5-10 tool calls, or when a new user message arrives:

```yaml
self_check:
  trigger: every 10 tool calls OR new user message
  checks:
    - context_utilization:
        estimate_token_usage()
        if > 0.60: flag(Context Fatigue)
    
    - turns_since_user:
        count_consecutive_agent_turns()
        if > 10: flag(Attention Drift)
    
    - unsaved_facts:
        scan_recent_exchanges_for(preferences, decisions, corrections)
        if count > 2: flag(Memory Debt)
    
    - consecutive_failures:
        count_recent_failed_tool_calls()
        if > 2: flag(Confidence Erosion)
    
    - active_topics:
        identify_distinct_topics()
        if count > 2: flag(Context Fragmentation)
    
    - skill_errors:
        check_if_loaded_skills_produced_errors()
        if true: flag(Skill Staleness)
```

See [`references/detection-heuristics.md`](references/detection-heuristics.md) for the detailed scoring system.

---

## Reporting Protocol

When a cognitive state is detected, the agent reports it using this format:

```
⚠️ COGNITIVE STATE: <State Name>
├─ Signal: <what triggered detection>
├─ Severity: low | medium | high
├─ Impact: <what could go wrong if ignored>
└─ Action: <what the agent is doing about it>
```

### Severity Levels

| Level | Meaning | Agent Behavior |
|-------|---------|----------------|
| **low** | Early warning. No impact yet. | Note internally. Continue normally. |
| **medium** | Starting to degrade. Quality at risk. | Report to user. Suggest mitigation. |
| **high** | Actively degrading. Failures likely. | Report immediately. Execute mitigation. Pause if needed. |

### Example Report (medium)
```
⚠️ COGNITIVE STATE: Context Fatigue
├─ Signal: ~75% context budget consumed (est. 94k/128k tokens)
├─ Severity: medium
├─ Impact: Early conversation details may be truncated; risk of forgetting original requirements
├─ Action: Persisting key decisions to memory now. Suggesting we wrap up this topic and start fresh for remaining work.
```

---

## Mitigation Playbook

Each state has a defined recovery procedure:

### Context Fatigue → Consolidate & Split
1. Persist all critical facts, decisions, and TODO state to memory
2. Write a brief session summary to memory or a file
3. Suggest `/new` or session split for remaining work
4. If user wants to continue: prioritize ruthlessly, ignore tangent topics

### Attention Drift → Re-anchor
1. State the original goal explicitly
2. Compare current activity to that goal
3. If misaligned: ask user "I've drifted to X — should I continue here or return to Y?"
4. If aligned: it wasn't drift, reset the counter

### Memory Debt → Flush
1. Scan conversation for: user preferences, corrections, architectural decisions, environment facts
2. Batch-write all unsaved facts to memory in one call
3. Report what was saved (so user can verify)
4. Reset the debt counter

### Confidence Erosion → Step Back
1. Stop retrying variations of the same approach
2. Name the pattern explicitly: "I've tried X, Y, Z — all failed for the same reason"
3. Try a fundamentally different approach (different tool, different library, different path)
4. If that also fails: **report the blocker honestly** — do not retry again
5. Ask user for guidance or additional information

### Context Fragmentation → Compartmentalize
1. Name all active topics explicitly
2. Finish or pause the current topic
3. Use `delegate_task` to spin off unrelated work into subagents (isolated contexts)
4. Suggest `/new` for the next topic
5. Persist a "TODO across sessions" to memory if needed

### Skill Staleness → Patch Immediately
1. Note what the skill says vs. what actually happened
2. Patch the skill with corrected commands/paths
3. Continue with corrected approach
4. Report the fix to user

---

## Integration Patterns

### Pattern 1: Silent Self-Monitoring (default)
Agent runs self-checks internally and only reports when severity ≥ medium.

### Pattern 2: Transparent (verbose)
Agent reports all states, even low severity. Useful for debugging agent behavior or during development.

### Pattern 3: Passive Logging
Agent writes cognitive state to a log file without interrupting the conversation:
```
echo '{"state":"fatigue","severity":"medium","ts":"2025-01-15T10:30Z"}' >> ~/.agent-cognitive-states.log
```
See [`scripts/self_check.py`](scripts/self_check.py) for a reference implementation.

### Pattern 4: Active Guardian (with cronjob)
A scheduled cron job runs the self-check script and alerts the user if the agent's cognitive state degrades during autonomous work. See [`templates/guardian-cronjob.yaml`](templates/guardian-cronjob.yaml).

---

## Philosophy

This skill is based on a simple observation: **humans have metacognition for a reason.**
Feeling tired, distracted, or confused isn't weakness — it's a survival signal that prevents
catastrophic mistakes. AI agents need the same thing.

An agent that says "I've lost the thread, let me re-read the original request" is **more
trustworthy** than one that blunders forward with corrupted context. An agent that says
"I've tried this 4 times and failed — I need help" is **more useful** than one that
silently retries forever.

**Self-awareness is a feature, not a bug.**
