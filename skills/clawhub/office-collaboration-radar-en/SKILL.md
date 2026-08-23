---
name: office-collaboration-radar-en
description: >-
  Extract an evidence-linked collaboration status card from chat logs, meeting notes, and project updates.
  Use when a user needs project progress, confirmed decisions, owner-and-deadline actions, blockers,
  cross-functional dependencies, human-review items, an executive summary, a radar chart, or stable JSON.
  Designed for English collaboration material; redacts PII and remains read-only by default.
---

# Office Collaboration Radar — English

Turn scattered collaboration records into a stable, auditable project status card. Extract only facts supported by the supplied material. Do not produce a full weekly report, judge individual performance, send reminders, or write to external systems.

Chinese version: [Office Collaboration Radar](https://clawhub.ai/yamyeed/skills/office-collaboration-radar)

## Capabilities

- Produce seven fixed modules: overview, progress, decisions, actions, risks and dependencies, cross-functional relationships, and human-review items.
- Attach evidence snippets of at most 80 characters; use `Not provided` when no reliable evidence exists.
- Redact phone numbers, email addresses, government IDs, bank-card numbers, and user-supplied entity names.
- Flag conflicting owners, deadlines, or statuses for human review.
- Rank actions as P0/P1/P2, synthesize an executive summary, and generate an SVG collaboration-health radar.
- Export the structured card to CSV, Feishu/Bitable mapping JSON, or Notion mapping JSON.

## Input

Accept Markdown, plain text, exported chats, meeting notes, or project logs. Label the source of each segment when combining materials. Optional metadata includes project name, time range, departments, and a list of known entities to redact.

If the material does not state a project name, time range, owner, deadline, or department, use `Not provided`. Do not infer or complete it.

## Workflow

1. Separate facts from opinions, questions, tentative statements, small talk, and duplicates.
2. Draft the seven-module card using the key order in `templates/json-output-schema.md`.
3. Keep owner and deadline values verbatim. If an exact value cannot be found in the supplied source, replace it with `Not provided`.
4. Enforce evidence, redaction, Markdown-cell sanitization, conflict checks, and priority ordering:

   ```bash
   python3 scripts/process.py enforce --card draft-card.json --source source.txt --out enforced-card.json
   ```

   Aggregate multiple cards first when needed:

   ```bash
   python3 scripts/process.py aggregate --cards card-1.json card-2.json --out aggregated.json
   ```

5. Optionally generate a radar chart:

   ```bash
   python3 scripts/radar_chart.py generate --card enforced-card.json --out collaboration-radar.svg
   ```

6. Optionally export a downstream mapping:

   ```bash
   python3 scripts/export_card.py export-card --card enforced-card.json --format csv --out actions.csv
   ```

7. Return the Markdown card, JSON result, and executive summary. Before publishing or changing the skill, run:

   ```bash
   python3 scripts/process.py selftest
   python3 scripts/validate_output.py
   ```

## Output contract

Keep every heading in this order, even when a section contains only `Not provided`:

```markdown
# Collaboration Status Card

## Project Overview
## Progress
## Confirmed Decisions
## Owner × Deadline Actions
## Risks / Blockers / Dependencies
## Cross-functional Relationships
## Human Review Required
## JSON Output
```

Use `templates/collaboration-status-card.md` for the Markdown layout and `templates/json-output-schema.md` for the machine-readable contract.

## Evidence and safety boundaries

- Do not turn tentative intent into a commitment or invent owners, deadlines, decisions, departments, or launch dates.
- Use `Conflict detected; human review required` consistently and add a matching human-review item.
- Sanitize all user-derived Markdown table values and escape CSV formula prefixes.
- Escape SVG titles before rendering them.
- Minimize and redact secrets, tokens, customer data, and sensitive HR information.
- Do not send messages, email, or calendar invitations, and do not modify Jira, Feishu, Notion, CRM, calendars, or other systems.
- Do not convert interpersonal friction or emotional language into performance judgments or blame.

The example under `examples/enterprise-ai-pilot/` is synthetic and redacted. It demonstrates extraction behavior only; it is not evidence of a production deployment or business outcome.
