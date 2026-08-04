---
name: learning-memory
description: Give AI agents Remember courses and lessons learned. using BlueColumn persistent memory. Use when an agent tracks learning and skill growth; when the user wants to store, recall, or search learning memory context. Requires a BlueColumn API key (bc_live_*).
---

# Learning Memory — BlueColumn Skill

Remember courses and lessons learned.. Powered by BlueColumn (bluecolumn.ai) persistent vector memory.

## Setup
Read `TOOLS.md` or the platform secret store for the BlueColumn API key (`bc_live_*`). Base URL: `https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1`

## Store
```bash
curl -X POST .../agent-remember \
  -H "Authorization: Bearer <key>" \
  -H "Content-Type: application/json" \
  -d '{"text": "Completed: 'Prompt Engineering' course. Key lessons: chain-of-thought, few-shot.", "title": "learning-memory - note"}'
```

## Quick note
```bash
curl -X POST .../agent-note \
  -H "Authorization: Bearer <key>" \
  -H "Content-Type: application/json" \
  -d '{"text": "Completed: 'Prompt Engineering' course. Key lessons: chain-of-thought, few-shot.", "tags": ["learning-memory"]}'
```

## Recall
```bash
curl -X POST .../agent-recall \
  -H "Authorization: Bearer <key>" \
  -H "Content-Type: application/json" \
  -d '{"q": "What have I been learning and what stuck?"}'
```

## Workflow
1. On new context, first recall: `What have I been learning and what stuck?`
2. Use the answer to personalize the response
3. After the interaction, store the summary via `/agent-remember`

## Docs
Full API reference: https://bluecolumn.ai/docs — fields are `text`, `q`, `tags` (not `content`/`query`/`note`).
