---
name: agent-memory-system
description: "Three-layer storage + four mechanisms + P0-P3 truth hierarchy for AI agent memory. MEMORY.md central index, memory/core/ structured facts, local vector DB. Engramory curation, WAL protocol, context management. Pure local filesystem + SQLite + LanceDB, no external API."
metadata:
  tags: [memory, architecture, agent]
  license: MIT
---

# Agent Memory System

A structured memory architecture for AI agents. Three-layer file-based storage with P0-P3 truth hierarchy.

## Architecture

- **Layer 1**: MEMORY.md central index (200 line limit)
- **Layer 2**: memory/core/ structured JSON files (identity, lessons, preferences, profile, strategies)
- **Layer 3**: Local LanceDB vector DB for semantic search

## Four Mechanisms

1. **Engramory Curation**: Deduplicate, update over insert, delete on error, hard limits
2. **WAL Protocol**: Write-ahead logging before replying on corrections/decisions/preferences
3. **Working Buffer**: Context fuse at 60% usage, auto-summarize to working-buffer.md
4. **Auto Promotion**: High-value memories auto-promote from daily logs to central index

## Truth Hierarchy

| Level | Source | Usage |
|-------|--------|-------|
| P0 | SQLite state.db | Operational data, single source of truth |
| P1 | core/*.json | Structured cache, validated |
| P2 | sessions/*.md | History only, not for decisions |
| P3 | learnings/*.md | Post-mortem analysis |

**Author**: Dawn
**License**: MIT
