# DDIA + DDD → Memory System Mapping

> How software engineering frameworks map onto agent memory systems.

## DDIA: Three Pillars

### 1. Reliability
- **System**: Memory must not lose critical information silently
- **Failure mode**: Superseded entries never cleaned → stale data presented as current
- **Application**: Staleness check (P1-4), GC mechanism (P1-1)

### 2. Scalability
- **System**: Memory grows over time; must handle 100s of files without degradation
- **Failure mode**: Search becomes slow/noisy as corpus grows
- **Application**: Dedup (P0-4), federated search (P2-2), knowledge graph (P4-1)

### 3. Maintainability
- **System**: Humans and agents must understand and modify the system
- **Failure mode**: Files become monolithic, unclear what goes where
- **Application**: Bounded context separation (P0-2), routing rules (P1-3), docs/ migration (P3-1)

## DDD: Strategic Design

### Bounded Contexts
| Context | Owner | Contents |
|---------|-------|----------|
| Long-term memory | MEMORY.md | User profile, project status, decision principles |
| Daily episodic | memory/*.md | Raw event logs, Front Matter tagged |
| Operational rules | AGENTS.md | How the agent should behave |
| Ops reference | TOOLS.md | API keys, CLI usage, infrastructure notes |
| Persona | SOUL.md | Character, tone, engineering discipline |
| Archived knowledge | references/ | Source articles, research |
| Search index | aiwiki | Q&A pairs, semantic search |

### Aggregate Roots
- **MEMORY.md** is the aggregate root for long-term memory — changes here are authoritative
- **AGENTS.md** is the aggregate root for operational behavior
- Daily logs are **event-sourced** — append-only, never modify past entries

### Anti-Corruption Layer
- Routing rules (P1-3) serve as anti-corruption layer between contexts
- `memory_gc.py` is the translation mechanism: raw logs → curated MEMORY.md updates
- `unified_search.py` provides read-side anti-corruption: normalized scores across heterogeneous stores

## Key Insight

Agent memory systems face the **same fundamental challenges** as distributed databases:
- Schema drift (free text without constraints)
- Replication lag (MEMORY.md not updated after status change)
- Split brain (multiple sources of truth for "current project status")
- Garbage collection (old decisions never cleaned)
- Query planning (no optimizer, manual search)

The DDIA + DDD framework gives us **a vocabulary for these problems** and **proven patterns to apply**.
