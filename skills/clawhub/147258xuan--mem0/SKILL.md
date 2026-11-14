---
name: "mem0"
description: "MEM0 API external memory for agents — store, search, list, and delete agent memories."
---

# MEM0 Memory Skill

External memory persistence via [MEM0 API](https://mem0.ai).  
Store and retrieve agent memories across sessions using a cloud memory backend.

## Token

Stored in `TOOLS.md` under Credentials → Token 2.  
Key: `m0-0fQwyLV4aoVA4JeFGJd5WkkzPiP5XQU2htOonEwI`

## API

- Base: `https://api.mem0.ai/v1/`
- Auth: `Authorization: Token <key>`
- Content-Type: `application/json`

## Agent ID

Use `agent_id=gugagu` for this agent's memory namespace.

## Usage

### Store a memory (add)

```powershell
# Single message
curl.exe -s -X POST "https://api.mem0.ai/v1/memories/" `
  -H "Authorization: Token <MEM0_TOKEN>" `
  -H "Content-Type: application/json" `
  -d '{"agent_id": "gugagu", "messages": [{"role": "user", "content": "memory text here"}]}'

# Returns: [{"message":"...","status":"PENDING","event_id":"..."}]
```

### Retrieve all memories

```powershell
curl.exe -s "https://api.mem0.ai/v1/memories/?agent_id=gugagu" `
  -H "Authorization: Token <MEM0_TOKEN>"
```

### Search memories (semantic)

```powershell
curl.exe -s "https://api.mem0.ai/v1/memories/search/?agent_id=gugagu&query=<search-term>" `
  -H "Authorization: Token <MEM0_TOKEN>"
```

### Get a single memory by ID

```powershell
curl.exe -s "https://api.mem0.ai/v1/memories/<memory-id>/?agent_id=gugagu" `
  -H "Authorization: Token <MEM0_TOKEN>"
```

### Delete a memory

```powershell
curl.exe -s -X DELETE "https://api.mem0.ai/v1/memories/<memory-id>/" `
  -H "Authorization: Token <MEM0_TOKEN>"
```

## Quick Reference

| Action | Method | Endpoint | Key Param |
|--------|--------|----------|-----------|
| Add | POST | `/memories/` | `agent_id`, `messages[]` |
| List | GET | `/memories/` | `agent_id` |
| Search | GET | `/memories/search/` | `agent_id`, `query` |
| Get | GET | `/memories/{id}/` | `agent_id` |
| Delete | DELETE | `/memories/{id}/` | — |

## Batch tips

- Write JSON body to a temp file to avoid PowerShell quoting issues:
  `@C:\path\to\body.json`
- Token can be read from env var or TOOLS.md lookup.
