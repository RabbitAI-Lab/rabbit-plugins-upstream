---
name: crm-memory
description: Give AI agents CRM memory for sales teams. using BlueColumn persistent memory. Use when an agent manages deals, contacts, and pipeline; when the user wants to store, recall, or search crm memory context. Requires a BlueColumn API key (bc_live_*).
---

# Crm Memory — BlueColumn Skill

Crm memory for sales teams.. Powered by BlueColumn (bluecolumn.ai) persistent vector memory.

## Setup
Read `TOOLS.md` or the platform secret store for the BlueColumn API key (`bc_live_*`). Base URL: `https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1`

## Store
```bash
curl -X POST .../agent-remember \
  -H "Authorization: Bearer <key>" \
  -H "Content-Type: application/json" \
  -d '{"text": "Deal: Acme Corp $12k ARR. Stage: negotiation. Owner: Jane. Last touch: 7/29.", "title": "crm-memory - note"}'
```

## Quick note
```bash
curl -X POST .../agent-note \
  -H "Authorization: Bearer <key>" \
  -H "Content-Type: application/json" \
  -d '{"text": "Deal: Acme Corp $12k ARR. Stage: negotiation. Owner: Jane. Last touch: 7/29.", "tags": ["crm-memory"]}'
```

## Recall
```bash
curl -X POST .../agent-recall \
  -H "Authorization: Bearer <key>" \
  -H "Content-Type: application/json" \
  -d '{"q": "What deals are in negotiation and who owns them?"}'
```

## Workflow
1. On new context, first recall: `What deals are in negotiation and who owns them?`
2. Use the answer to personalize the response
3. After the interaction, store the summary via `/agent-remember`

## Docs
Full API reference: https://bluecolumn.ai/docs — fields are `text`, `q`, `tags` (not `content`/`query`/`note`).
