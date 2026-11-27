---
name: daily-standup-summarizer
version: 1.0.0
description: Turn yesterday's activity (commits, messages, task logs) into a three-line standup: done, doing, blocked. Use each morning for yourself or a team.
---

# Daily Standup Summarizer

## Overview

A standup is a compression task: everything that happened, squeezed into what a busy reader needs. This workflow gathers the raw material and applies a strict format so nothing important hides in the noise.

## When to use

Every morning, for solo builders summarizing agent work or for teams sharing status.

## Workflow

1. **Gather sources** — commits, closed tasks, sent messages, calendar; facts only from records, not from memory
2. **Done** — only items with evidence of completion (merged, sent, published), each in five words or fewer plus a link
3. **Doing** — the top three in-progress items, each with its next visible milestone
4. **Blocked** — each blocker with its owner and what would unblock it; 'waiting on X' must name X
5. **Cut ruthlessly** — if it does not change what anyone does today, it does not belong

## Guardrails

- Never list started work as done
- Never hide a blocker to make the summary look clean
- Keep it under 150 words — the format is the value

## Output format

Three headed lists (Done / Doing / Blocked), each item one line, blockers with owners.

---

Part of the Manteclaw free skill series. These workflow skills are free forever; Manteclaw's paid automation tools (runnable code, not just prompts) live at payhip.com/Manteclaw.
