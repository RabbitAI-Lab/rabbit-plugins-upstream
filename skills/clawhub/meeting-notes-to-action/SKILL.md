---
name: meeting-notes-to-action
description: "Turn raw meeting notes or transcripts into structured action: decisions log, action items with owner and deadline, open questions, and a distributable summary email. Extracts who-committed-to-what with date parsing (natural language dates resolved against the meeting date), deduplicates, tracks carryover between meetings, and generates per-owner task lists. Use when the user has meeting notes/transcripts and needs minutes, action items, or a follow-up summary."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [meetings, productivity, action-items, minutes, summarization, teams, workplace]
---

# Meeting Notes → Action 📋

Convert messy meeting notes into **structured, accountable output**: decisions made, action items with owner + deadline + confidence, open questions, and a ready-to-send summary email. Includes a deterministic extraction engine for clearly-stated commitments ("Sarah will send the report by Friday") plus carryover tracking between consecutive meetings.

## Overview

The universal post-meeting ritual: someone scrolls back through 40 minutes of
chat-log-style notes trying to figure out what was actually decided and who
promised what. Action items live in five people's heads and evaporate. This
skill systematizes it:

- **`meeting_extractor.py`** — deterministic NLP over raw notes:
  - **Action items**: subject-verb-commitment patterns ("X will do Y by DATE",
    "assign to X", "action item:", checkboxes, "follow up")
  - **Owner resolution**: names + @mentions + role aliases ("PM", "Sarah")
  - **Date parsing**: natural language ("by Friday", "next Tuesday",
    "end of month", "in two weeks") resolved against the meeting date
  - **Decisions**: "decided/agreed/going with", "approved", "rejected"
  - **Open questions**: "question:", "?", "TBD", "discuss next time"
  - **Dedup**: similar items merged; question-vs-action discrimination
  - **Carryover**: compare with a previous meeting's JSON — unfinished items
    roll forward with age and staleness warnings
- Outputs: terminal digest, JSON, **Markdown minutes**, and a **summary email draft** with per-owner action lists

## When to Use

- "Here are my meeting notes — pull out the action items"
- Weekly team meeting → minutes + assignment emails
- "What did we decide last week?" — decisions log from stored JSON
- Tracking recurring meetings: carryover of unfinished items with aging
- Post-standup: converting chat-style notes into tickets

**Don't use for:** verbatim transcription (needs a transcription tool first),
calendar scheduling, or project management sync (Jira/Linear have their own
skills) — this produces the structured intermediate those tools consume.

## Quick Start

```bash
# Basic extraction
python3 scripts/meeting_extractor.py notes.txt --meeting-date 2026-08-12

# Full outputs: JSON + Markdown minutes + email draft
python3 scripts/meeting_extractor.py notes.txt --meeting-date 2026-08-12 \
  --title "Product sync" --json out.json --minutes minutes.md --email email.md

# Weekly carryover: items from last week's JSON that didn't complete
python3 scripts/meeting_extractor.py notes.txt --meeting-date 2026-08-19 \
  --previous lastweek.json --minutes minutes.md
```

Notes formats accepted: free text, chat-style lines ("10:42 Sarah: I'll send
the deck"), checkbox lists, "Action items:" sections — commonly mixed.

## Extraction Patterns

| Signal | Example | Extracts |
|---|---|---|
| `<name> will <verb>` | "Sarah will send the report" | action, owner Sarah |
| `@name` mention + commitment | "@tom can you review?" | action, owner tom (question form) |
| `by <date>` / `due <date>` | "by Friday", "due 2026-08-20" | deadline |
| `action item[s]:` section | "Action items: - ..." | everything listed |
| checkbox | "- [ ] call vendor" | action, unassigned |
| `assign(ed)? to <name>` | "assigned to Priya" | owner |
| `decided\|agreed\|going with` | "we agreed to postpone launch" | decision |
| `TBD\|question\|?` | "pricing TBD" | open question |

Ambiguity handling: "we should probably" → low-confidence (flagged for
review); imperatives without owner → owner `Unassigned`.

## Common Pitfalls

1. **Trusting extraction as ground truth.** The engine is deterministic, not
   telepathic — review the confidence flags before sending the email out.
2. **Relative dates without `--meeting-date`.** "By Friday" is meaningless
   without knowing which Friday; pass the meeting date or dates resolve to
   today's context (and get flagged).
3. **Chat transcripts with overlapping speakers.** Timestamp lines are
   stripped; speaker prefixes (Name:) become owner candidates automatically.
4. **Sending the full minutes to everyone.** The email draft contains
   per-owner sections — trim for exec recipients; keep decisions prominent.
5. **Ignoring carryover staleness.** An item carried 3+ meetings is either
   blocked (needs escalation) or dead (kill it). The report flags both.
6. **Mixing decisions with discussion.** "We discussed X" is not "we decided
   X" — only commitment verbs produce decisions.

## Verification Checklist

- [ ] Every action item has: description, owner (or Unassigned flag), due date where stated
- [ ] Relative dates resolved against the correct meeting date
- [ ] Low-confidence items reviewed by a human before distribution
- [ ] Carryover (if any) checked — completed items marked, stale items escalated
- [ ] Email draft's per-owner sections match actual attendees

## References

- `references/extraction-patterns.md` — full grammar, confidence scoring, edge cases
- `references/minutes-templates.md` — minutes + email formats for different meeting types
