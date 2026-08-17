# Detection Heuristics

Detailed scoring system for each cognitive state. Use these as guidelines — 
the agent should apply judgment, not just mechanical thresholds.

---

## Scoring Model

Each state produces a **0-100 score**. Severity maps as:

| Score | Severity | Action |
|-------|----------|--------|
| 0-29 | none | No action |
| 30-59 | low | Internal note, continue |
| 60-79 | medium | Report to user, suggest mitigation |
| 80-100 | high | Execute mitigation immediately |

---

## 1. Context Fatigue Score

```
fatigue_score = (estimated_tokens_used / context_window_size) * 100

Adjustments:
  +10  if you've re-read earlier messages in the last 5 turns
  +10  if responses are getting longer (compensating verbosity)
  +5   if conversation spans multiple days
  -10  if a /new or context reset happened recently
```

**Estimating token usage without an API:**
- Rough heuristic: 1 token ≈ 4 characters of English text
- Count characters in conversation history / 4
- Add ~20% for system prompt, skills, and tool results overhead
- When in doubt, overestimate — fatigue is more dangerous than false alarms

---

## 2. Attention Drift Score

```
drift_score = base + adjustments

base = min(turns_since_last_user_message * 7, 70)

Adjustments:
  +15  if current tool calls are unrelated to original goal keywords
  +10  if TODO list was modified without user prompting
  +5   if working in a different directory/project than original task
  -20  if user explicitly asked for exploratory/investigative work
  -10  per user confirmation received during the drift period
```

**Detecting "unrelated":**
- Extract keywords from the original user request
- Check if recent tool calls reference those keywords
- If <30% keyword overlap: likely drift

---

## 3. Memory Debt Score

```
debt_score = min(unsaved_facts * 20, 100)

unsaved_facts = count of items in conversation that match:
  - User stated a preference ("I prefer X", "always do Y")
  - User made a correction ("no, not Z — use W instead")
  - Architecture/tool decision was made ("let's use PostgreSQL")
  - Environment detail discovered ("the server is at 192.168.x.x")
  - Password, token, or credential shared
  - Project naming convention established

Adjustments:
  +15  if a correction was made but old behavior persists in memory
  +10  per day since the facts were stated (staleness)
  -30  if a memory write happened in the last 3 turns
```

---

## 4. Confidence Erosion Score

```
erosion_score = min(consecutive_failures * 22, 100)

consecutive_failures = count of back-to-back tool calls that returned errors

Adjustments:
  +10  if using the same tool type repeatedly
  +10  if error messages are similar (same root cause)
  +15  if response quality is visibly degrading (shorter, more hedging)
  +20  if the "retry with minor variation" pattern is detected
  -15  if a successful tool call happened (resets momentum)
  -30  if a fundamentally different approach was tried (not just variation)
```

**Pattern detection — "same approach variations":**
```
extract command/action signature from last N failed attempts
if >70% structural similarity: flag as "variation loop"
```

---

## 5. Context Fragmentation Score

```
fragmentation_score = min(active_topics * 18, 100)

active_topics = count of distinct subjects in recent conversation

Topic detection:
  - Different projects/repos mentioned
  - Different tools being used (HA vs GitHub vs filesystem)
  - Different skill sets being loaded
  - User messages about unrelated subjects

Adjustments:
  +10  if tool calls alternate between topics (interleaved)
  +5   per unresolved (neither completed nor cancelled) topic
  -15  per topic that was explicitly completed or deferred
```

---

## 6. Skill Staleness Score

```
staleness_score = 0

Trigger evaluation (any one sets score to 60+):
  +60  if a skill's primary command failed on first execution
  +70  if file path in skill doesn't exist
  +50  if API version mismatch detected (error mentions version)
  +40  if skill references a tool not installed

Additional:
  +15  if skill was last updated >90 days ago
  +10  per additional failed command from same skill
  -20  if skill was patched/updated in this session
```

---

## Composite Cognitive Load Index

For overall agent state awareness:

```
CLI = (fatigue + drift + debt + erosion + fragmentation + staleness) / 6

CLI < 30:  🟢 Healthy — operating normally
CLI 30-50: 🟡 Degraded — some states active, monitor
CLI 50-70: 🟠 Strained — multiple states active, consider intervention
CLI > 70:  🔴 Critical — likely to produce low-quality output, pause and reset
```

The agent should report CLI alongside individual state scores when asked about its status.
