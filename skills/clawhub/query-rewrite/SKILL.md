---
name: query-rewrite
version: 1.0.0
description: |
  RAG retrieval pre-processing layer. Detects whether a query needs rewriting,
  executes rewriting when needed, then searches with both original and rewritten queries.
  Supports 6 rewrite modes: context extraction, comparison disambiguation,
  coreference resolution, multi-intent decomposition, rhetorical question detection,
  and condition extraction.
  Use when: Before RAG retrieval, memory_search, wiki_search calls, or vector search.
  NOT for: Code generation, file operations, non-retrieval scenarios.
tags:
  - rag
  - retrieval
  - nlp
  - query-rewrite
  - search
keywords:
  - query rewrite
  - RAG
  - search optimization
  - coreference resolution
  - multi-intent
license: MIT
repository: https://github.com/DaBin0927/query-rewrite
homepage: https://github.com/DaBin0927/query-rewrite#readme
---

# Query Rewrite — RAG Retrieval Pre-processing Layer

**Purpose:** In multi-turn conversation scenarios, rewrite fuzzy/anaphoric/multi-intent queries into structured search terms to improve RAG recall.

**Core Capabilities:**
- ✅ Fast detection: determine if a query needs rewriting
- ✅ 6 rewrite modes: auto-identify and execute
- ✅ Dual-path search: original + rewritten queries
- ✅ Deduplication and result merging

---

## 🧠 Rewrite Checklist

Before calling any retrieval tool (`memory_search`, `wiki_search`) or vector search, check the current query against this list:

| Check Item | Trigger Condition | Action |
|------------|------------------|--------|
| 🔴 Pronouns | Contains it/he/she/this/that/these/those | Rewrite → Mode 3 |
| 🔴 Implicit pronouns | "all/everything" referencing multiple entities | Rewrite → Mode 3 |
| 🔴 Comparison | "which is better/difference/compare" | Rewrite → Mode 2 |
| 🟡 Incomplete semantics | Question can't be understood without context | Rewrite → Mode 1 |
| 🟡 Multiple questions | ≥2 independent questions | Rewrite → Mode 4 |
| 🟡 Rhetorical questions | "surely not/could it be/impossible" | Rewrite → Mode 5 |
| 🟢 Filter conditions | Numeric range/attribute filter/exclusions | Rewrite → Mode 6 |
| ⚪ None of above | Query is independent, complete, and clear | **Search directly, no rewrite** |
| ⚪ Self-check | Rewrite result has no substantive difference from original | **Don't rewrite** (prevent over-rewriting) |

## 📋 6 Rewrite Modes

> Full templates and examples: `references/rewrite-patterns.md`

| # | Mode | Trigger | Action | Example |
|---|------|---------|--------|---------|
| 1 | Context Extraction | Query lacks subject/entity | Extract entities from last 2-3 turns | "How long is warranty?" → "iPhone 15 Pro warranty period" |
| 2 | Comparison Disambiguation | Comparison words + ≥2 candidates | Expand to `A vs B` format | "Which is faster?" → "PostgreSQL vs MongoDB performance" |
| 3 | Coreference Resolution | Pronouns/fuzzy references | Replace pronouns; "all"→split into independent queries (max 5) | "Do they all support it?" → ["A supports X", "B supports X", "C supports X"] |
| 4 | Multi-intent Decomposition | ≥2 independent questions | Split into sub-queries with shared subject | "Color? Size? Price?" → 3 independent queries |
| 5 | Rhetorical Question Detection | Rhetorical question patterns | Extract real information needs, convert to positive query | "It won't take a month too, right?" → "Estimated delivery time" |
| 6 | Condition Extraction | Filter/limit conditions | Reorganize as `subject+condition1+condition2+…` | "Under $500 suitable for women" → "gift budget 500 women" |

### Multi-mode Priority

When a query triggers multiple modes, execute in this order:

```
Rhetorical(5) → Coreference(3) → Multi-intent(4) → Context(1) → Comparison(2) → Condition(6)
```

## 🔄 Execution Flow

```
User Query
    │
    ▼
┌─────────────────┐
│ Check checklist  │ ← compare item by item, complete within 0.5s
└───────┬─────────┘
        │
   ┌────┴────┐
   │ Rewrite? │
   └────┬────┘
        │
   ┌────┴────────────────┐
   │ YES                 │ NO
   ▼                     ▼
┌──────────┐      ┌──────────┐
│ Execute   │      │ Direct   │
│ rewrite   │      │ search   │
│ output    │      │ original │
│ 1-N       │      │ query    │
│ queries   │      └──────────┘
└────┬─────┘
     │
     ▼
┌────────────────────────────┐
│ Search: original + rewritten │
│ memory_search(original)     │
│ memory_search(rewrite_1)    │
│ memory_search(rewrite_2)... │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│ Merge & deduplicate (↓score)│
│ Tag each result with source │
└────────────────────────────┘
```

## ⚠️ Key Rules

1. **Zero-rewrite principle** — Don't rewrite when unnecessary; search directly
2. **Intent fidelity** — Rewriting must not change user intent, only add context
3. **Context scope** — Default: extract entities from last 2-3 conversation turns
4. **Rewrite enhances, not replaces** — Original query always participates in search
5. **Graceful fallback** — If reference/intent can't be determined, search with original query, tag `rewrite_skipped: true`

## 📝 Usage Examples

### Example 1: Normal rewrite flow

```
Context: User asked "What colors does iPhone 15 Pro come in?"
Current query: "How long is the warranty?"
↓ Checklist: incomplete semantics → Mode 1
↓ Rewrite: extract entity "iPhone 15 Pro" → "iPhone 15 Pro warranty period"
↓ Search: memory_search("How long is the warranty?") + memory_search("iPhone 15 Pro warranty period")
↓ Merge, deduplicate, return
```

### Example 2: Multi-intent decomposition

```
Context: (none)
Current query: "Coating machine price? Warranty? Can it be customized?"
↓ Checklist: multiple questions → Mode 4
↓ Rewrite:
  - "coating machine price"
  - "coating machine warranty"
  - "coating machine customization support"
↓ Search: 4 times (1 original + 3 rewrites) → merge, deduplicate
```

### Example 3: No rewrite needed

```
Context: (none)
Current query: "Enterprise CRM system architecture design document"
↓ Checklist: all no → direct search
↓ memory_search("Enterprise CRM system architecture design document")
```

## 📎 Resources

- **Rewrite patterns reference**: `references/rewrite-patterns.md`

## 📝 Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1.0.0 | 2026-07-23 | Initial public release: 6 rewrite modes, rewrite checklist, progressive loading (meta+logic separation) |
