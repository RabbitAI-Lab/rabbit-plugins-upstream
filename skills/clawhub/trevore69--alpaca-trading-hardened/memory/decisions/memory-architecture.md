# Decision: Memory architecture — layered

**Date:** 2026-07-15
**Decision:** Two-layer memory. Built-in (MEMORY.md + workspace memory/ daily logs + memory_search) stays the quick layer; the ClawHub `memory` skill (~/memory/) is the deep, organized layer.

**Why:** The 2026-07-15 Simmer mix-up showed the failure mode was retrieval + verification, not storage: facts were written down but sessions trusted one bad probe over notes. Fixes applied: TOOLS.md endpoint registry, "verify before declaring gone" lesson, durable cron for follow-ups.

**Rejected:** elite-longterm-memory-local and koompi-memory (fail ClawHub security scan); smart-memory-manager (heavier than needed today — revisit if ~/memory/ grows past easy grep).

**Integration (2026-07-15):** `agents.defaults.memorySearch.extraPaths=["/root/memory"]` + `provider:"none"` (FTS-only — no embedding API key configured) in openclaw.json. Index: 32/32 files, 89 chunks; session-start sync + file watch keep it current. Recall verified: deep-layer files surface as top `memory_search` hits. Config backup: `openclaw.json.pre-extrapaths`.
