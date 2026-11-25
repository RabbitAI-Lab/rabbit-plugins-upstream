---
name: meeting-notes-to-actions
version: 1.0.0
description: Convert raw meeting notes or a transcript into decisions, owned action items, and open questions. Use right after any meeting whose notes will otherwise rot.
---

# Meeting Notes To Actions

## Overview

Meetings produce three things worth keeping: decisions made, actions owed, and questions left open. This workflow extracts exactly those, with owners and dates, and discards the rest without losing anything that matters.

## When to use

After calls, standups, planning sessions — anywhere commitments were made verbally.

## Workflow

1. **Extract decisions** — each stated as 'we decided X because Y', attributed to who decided
2. **Extract actions** — each with one owner, one deliverable, one date; split anything with two owners
3. **Extract open questions** — each with who can answer it and what blocks until then
4. **Flag ambiguities** — anything two attendees would summarize differently goes back for confirmation, not into the record as fact
5. **Write the recap** — decisions first, then actions by owner, then open questions; under one page

## Guardrails

- Never invent an owner or a date that was not stated — mark them TBD and flag for confirmation
- Do not upgrade a suggestion made in passing into a decision
- Quote exact figures and names; do not paraphrase numbers

## Output format

A recap: decisions, action items (owner, deliverable, date), open questions, ambiguities to confirm.

---

Part of the Manteclaw free skill series. These workflow skills are free forever; Manteclaw's paid automation tools (runnable code, not just prompts) live at payhip.com/Manteclaw.
