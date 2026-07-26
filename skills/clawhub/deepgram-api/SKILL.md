---
name: deepgram-api
description: Deepgram speech-to-text, text-to-speech, voice agents, and audio intelligence — API reference, docs navigator, recipes, starters, and MCP setup. Triggered when working with Deepgram APIs, transcription, TTS, or voice agent integrations.
---

# Deepgram API Skills

This workspace skill provides structured Deepgram API reference material pulled directly from the official [deepgram/skills](https://github.com/deepgram/skills) repository.

## Included sub-skills

| Sub-skill | Purpose |
|---|---|
| `api/` | Full REST + WebSocket API reference — Nova STT, Flux STT, TTS, Voice Agent, Read intelligence, models, projects, auth, self-hosted |
| `docs/` | Topic-by-topic documentation navigator with pointers to official docs |
| `recipes/` | Minimal runnable feature snippets per language |
| `starters/` | Runnable starter apps (framework × feature matrix) |
| `setup-mcp/` | How to install and configure the Deepgram MCP server |

## Quick reference

**Base servers:**
- REST & STT/TTS WebSocket: `https://api.deepgram.com`
- Voice Agent WebSocket: `https://agent.deepgram.com`

**Primary models:**
- Nova (`/v1/listen`) — general transcription, rich feature set
- Flux (`/v2/listen`) — conversational audio, built-in turn detection

**STT WebSocket common mistakes (from the API skill):**
- Send `KeepAlive` as text frame, not binary
- Never send empty byte payloads
- `encoding` must match actual audio format

## When to use this

- Building or debugging Deepgram integrations
- Looking up endpoint params, error codes, message formats
- Designing voice agent or transcription pipelines
- Setting up the Deepgram MCP server for AI tool access
