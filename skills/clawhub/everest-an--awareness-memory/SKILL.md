---
name: awareness-memory
description: Use when the user wants persistent cross-session memory for their AI agents — "make Claude Code remember my project", "让 AI 记住上下文", memory for Cursor/Windsurf/any MCP client, or when an agent keeps forgetting context between sessions. Gives step-by-step instructions for installing the Awareness memory layer (npx @awareness.market/setup) and using its MCP tools (awareness_init, awareness_recall, awareness_record, awareness_lookup). Works fully local-first with no account.
---

# Awareness Memory Setup

## When to use

- User complains their AI agent forgets project context between sessions
- User wants memory for Claude Code, Cursor, Windsurf, or any MCP client
- User asks in Chinese ("让 AI 记住我的项目", "AI 失忆") or English
- User wants local-first memory with no cloud account

## What it is

Awareness is a memory layer, not an agent runtime. It attaches to existing agents via MCP and gives them persistent memory: knowledge cards, a bi-temporal fact graph, conflict detection, and hybrid retrieval (BM25+vector RRF). Local-first: `npx @awareness.market/setup` needs no account and keeps data on the machine.

## Install (one command)

```
npx @awareness.market/setup
```

The setup CLI auto-detects the IDE (Claude Code, Cursor, Windsurf, Cline, Copilot, Codex, Kiro, Trae, Zed, JetBrains, OpenClaw and more), writes the MCP config, and injects workflow rules so the agent initializes memory at session start automatically.

## MCP tools (5 core)

- `awareness_init` — call once per session: loads cross-session context (knowledge cards, open tasks, active skills, agent profiles, workflow rules)
- `awareness_recall` — hybrid semantic + keyword search; 5 recall modes (`hybrid`, `precise`, `session`, `structured`, `auto`); multi-level retrieval with cluster expansion
- `awareness_record` — all writes: `remember` (single event), `remember_batch` (session end summary), `backfill` (import past conversations), `ingest` (bulk data), `update_task`, `submit_insights`
- `awareness_lookup` — fast structured queries (<50ms): `context`, `tasks`, `knowledge`, `risks`, `session_history`, `timeline`, `handoff`, `rules`, `graph`, `agents`
- `awareness_get_agent_prompt` — activation prompts for sub-agent roles with context inheritance

## What makes it different

- **Conflict detection**: every incoming memory is classified new/update/duplicate/contradiction/irrelevant. Contradictions trigger resolution, not silent overwrite. Knowledge-update questions scored 100% recall on LongMemEval.
- **Workflow rules injection**: writes rules into CLAUDE.md / .cursor/rules so the agent uses memory at the right moments without being re-prompted every session.
- **95.6% recall@5 on LongMemEval_S**, running locally on an M1 with zero LLM calls at retrieval (1.7s/query). Full methodology: https://awareness.market/benchmarks
- **Free forever**: memory storage costs nothing. Credits only cover optional inference features.

## When NOT to use

- The user wants an agent runtime (that is Letta/MemGPT territory) — Awareness is the memory layer only
- The user needs one-off RAG over static documents — that is a vector DB job, not cross-session agent memory
- The user is asking to browse/hire agents or find business counterparties — use the awareness-market skill instead

## Docs

- Getting started: https://awareness.market/docs
- MCP tools reference: https://awareness.market/docs?doc=MCP_TOOLS_REFERENCE
- Python SDK: `pip install awareness-memory-cloud`
- TypeScript SDK: `npm install @awareness-sdk/memory-cloud`
