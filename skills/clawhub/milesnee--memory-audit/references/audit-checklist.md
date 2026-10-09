# Audit Checklist — Full 15 Items

> The complete DDIA + DDD audit checklist. Each item maps to a fix script.

## P0 — Data Integrity (4 items)

### P0-1: Core file GC
- **Lens**: DDD (bounded context overflow)
- **Symptom**: MEMORY.md or AGENTS.md > 20KB
- **Diagnosis**: Operational docs, stale status, superseded content mixed in
- **Fix**: `memory_gc.py` → extract ops to TOOLS.md, supersede stale, update status
- **Verify**: file size < 15KB, no SUPERSEDED content visible

### P0-2: Bounded context separation
- **Lens**: DDD (aggregate boundaries)
- **Symptom**: AGENTS.md contains theory + ops + rules
- **Diagnosis**: Section-by-section analysis, identify what's rules vs reference
- **Fix**: theory → docs/, ops → TOOLS.md, rules + cross-ref stay
- **Verify**: AGENTS.md < 300 lines, all content findable via docs/ links

### P0-3: Log Front Matter
- **Lens**: DDIA (schema enforcement)
- **Symptom**: <90% of memory/*.md have YAML Front Matter
- **Fix**: `batch_add_frontmatter.py` — auto-detect date/topics/projects
- **Verify**: FM coverage ≥ 95%

### P0-4: Search dedup
- **Lens**: DDIA (query correctness)
- **Symptom**: Same log appears multiple times in search results
- **Fix**: Add (date, title) unique key in `search_memories()`
- **Verify**: No duplicates in search output

## P1 — Consistency (4 items)

### P1-1: MEMORY.md auto-GC
- **Lens**: DDIA (lifecycle management)
- **Symptom**: Manual MEMORY.md maintenance is unreliable
- **Fix**: `memory_gc.py` — scan logs, suggest updates
- **Verify**: Script runs, produces meaningful suggestions

### P1-2: References INDEX auto-gen
- **Lens**: DDD (aggregate index)
- **Symptom**: references/ unindexed or manually maintained
- **Fix**: `gen_references_index.py`
- **Verify**: INDEX.md regenerates idempotently

### P1-3: Knowledge routing rules
- **Lens**: DDD (context routing)
- **Symptom**: Ambiguity about where to store new content
- **Fix**: Routing table in AGENTS.md (6 content types → 6 destinations)
- **Verify**: Any new content has unambiguous destination

### P1-4: Staleness detection
- **Lens**: DDIA (TTL / expiry)
- **Symptom**: Old project status never marked as stale
- **Fix**: `staleness_check.py` — 60-day threshold
- **Verify**: Stale items flagged

## P2 — Query Capability (3 items)

### P2-1: Tag filtering
- **Lens**: DDIA (query filtering)
- **Fix**: `tag_filter` param + `--tag` CLI
- **Verify**: Tagged search returns only matching results

### P2-2: Federated search
- **Lens**: DDIA (cross-source join)
- **Fix**: `unified_search.py` — memory + aiwiki + references
- **Verify**: Results from all three sources, normalized scores

### P2-3: Archive searchability
- **Lens**: DDIA (completeness)
- **Fix**: Include `memory/archive/*.md` in index
- **Verify**: Archived files appear in search with [归档] prefix

## P3 — Architecture Decoupling (4 items)

### P3-1: AGENTS.md slim down
- **Fix**: Migrate large sections to docs/
- **Verify**: < 300 lines, cross-refs valid

### P3-2: TOOLS.md creation
- **Fix**: Consolidate ops notes from MEMORY.md
- **Verify**: TOOLS.md exists, referenced by AGENTS.md

### P3-3: Review agent cron
- **Fix**: Nightly cron job, scan logs, write review/
- **Verify**: cron enabled, review/ files appear nightly

### P3-4: Duplicate cleanup
- **Fix**: Merge same-date files
- **Verify**: 0 duplicate dates

## P4 — Knowledge Systematization (3 items)

### P4-1: Knowledge graph
- **Fix**: `knowledge_graph.py` — extract nodes + edges
- **Verify**: JSON valid, Mermaid renders, subgraph filter works

### P4-2: aiwiki reflux
- **Fix**: `aiwiki_reflux.py` — detect + ingest gap
- **Verify**: 0 gap after run

### P4-3: Execution traces
- **Fix**: `trace_logger.py` — record agent task execution
- **Verify**: trace JSON valid, all required fields present
