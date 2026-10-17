---
name: meeting-notes-formatter
description: >
  Turn rough meeting notes into a structured summary with decisions,
  action items, and owners. Use when the user pastes messy notes after a call.
metadata: {"clawdbot":{"emoji":"📝","requires":{"bins":[]}}}
---

# Meeting Notes Formatter

## Purpose / Overview
Converts unstructured meeting notes into a consistent Markdown summary.

## When to Use
- After a standup, planning, or 1:1 when notes are messy
- When the user asks to "clean up notes" or "extract action items"

## Usage / Instructions
1. Ask for the raw notes (paste or file path).
2. Identify attendees if mentioned; otherwise leave "Attendees: unknown".
3. Produce sections: Summary, Decisions, Action Items (owner + due if present), Open Questions.
4. Keep wording faithful; do not invent decisions.

## Examples
User: "Clean these notes: talked about launch delay, Alice owns blog post Friday"
Assistant: emits Summary + Action Items with Alice / Friday.

## Requirements / Dependencies
None beyond the chat model.

## Limitations / Caveats
Does not access calendars or send reminders.

## Security / Permissions
Read-only over user-provided text. No network or filesystem writes.

