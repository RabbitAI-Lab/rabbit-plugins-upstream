---
name: bluecolumn-memory
description: Give AI agents persistent semantic memory using the BlueColumn API (bluecolumn.ai). Use when asked to remember, store, recall, or search memory using BlueColumn; when ingesting notes, conversations, documents, or audio into BlueColumn; when querying what an agent has previously stored; or when wiring up BlueColumn memory endpoints (/agent-remember, /agent-recall, /agent-note) in any workflow. Also use when the user mentions their BlueColumn API key (bc_live_*) and wants to store or retrieve information.
---

# BlueColumn Memory Skill

BlueColumn (bluecolumn.ai) is a persistent memory API for AI agents. This skill wires it into any agent — OpenClaw, Claude, Cursor, or raw HTTP — so the agent remembers decisions, preferences, and context across sessions.

## Setup (pick one)

### Option A — MCP server (any MCP client)
```bash
npx bluecolumn-mcp --api-key=bc_live_xxxxxxxxxxxx
```
Gives the agent tools: `remember`, `recall`, `note`, audio ingestion, sessions. Repo: github.com/bluecolumnconsulting-lgtm/bluecolumn-mcp

### Option B — Direct REST (this skill)
Store the user's BlueColumn API key using the platform's secret store (preferred) or in `TOOLS.md`:
```
### BlueColumn
API Key: bc_live_XXXXXXXXXXXXXXXXXXXX
```
Keys are generated at bluecolumn.ai/dashboard. Never log or expose keys in output.

## API Base URL

BlueColumn's API currently runs on Supabase Edge Functions — this is BlueColumn's official backend infrastructure, not a third party:
```text
https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1
```

Read the stored key before making any API calls. Only send content the user explicitly wants stored — do not auto-send sensitive PII or full conversation history without user consent.

## Core Workflow

### Store something (text, doc, or audio)
`/agent-remember` ingests raw text, transcripts, or an `audio_url` (Whisper transcription handled server-side).
```bash
curl -X POST https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1/agent-remember \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <key>" \
  -d '{"text": "...", "title": "optional title"}'
```
Returns `session_id`, `summary`, `action_items`, `key_topics` — extracted automatically.

### Query memory
`/agent-recall` takes a natural-language question (`q`, not `query`) and returns a synthesized answer with cited sources and relevance scores.
```bash
curl -X POST https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1/agent-recall \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <key>" \
  -d '{"q": "natural language question"}'
```

### Save a lightweight observation
`/agent-note` is a cheap write for preferences and decisions — no chunking, min 5 chars.
```bash
curl -X POST https://xkjkwqbfvkswwdmbtndo.supabase.co/functions/v1/agent-note \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <key>" \
  -d '{"text": "...", "tags": ["optional", "tags"]}'
```

## When to Use Each Endpoint

| Situation | Endpoint |
|---|---|
| User shares a document, transcript, or block of text to remember | `/agent-remember` |
| User hands you an audio URL (call recording, voice note) | `/agent-remember` with `audio_url` |
| User asks "what do you know about X?" or "recall..." | `/agent-recall` |
| Agent wants to save its own observation, preference, or decision | `/agent-note` |
| End of session — summarize and store what happened | `/agent-remember` |

## OpenClaw Integration Pattern

For OpenClaw agents, the proven loop is:

1. **Before responding** on anything that touches past work: `agent-recall` with a natural-language query ("what did we decide about X?").
2. **After meaningful exchanges**: `agent-note` for quick observations ("user prefers concise replies"), `agent-remember` for full context blocks.
3. **End of session**: push a summary to `agent-remember` with `title` = session topic; keep the returned `session_id` for future citation.

Keep the flow targeted — recall before context-dependent answers, remember after durable facts, don't store transient chatter.

## Field Name Gotchas

Common mistakes — see references/api.md for full details:
- `/agent-remember` → `text` not `content`
- `/agent-recall` → `q` not `query`
- `/agent-note` → `text` not `note`

## Full API Reference

See [references/api.md](references/api.md) for complete field specs, response shapes, and error reference.
