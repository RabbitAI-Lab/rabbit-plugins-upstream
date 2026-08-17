# Production — Keeping It Correct After It Ships

A RAG system does not stay correct on its own. The corpus moves, the models move, the index accumulates tombstones, and nothing errors.

**Contents:** [The Latency Budget](#the-latency-budget) · [Caching](#caching) · [Incremental Sync](#incremental-sync) · [Deletes and Retractions](#deletes-and-retractions) · [Reindex as a Migration](#reindex-as-a-migration) · [Drift Monitoring](#drift-monitoring) · [Alarms Worth Having](#alarms-worth-having) · [Failure Handling](#failure-handling) · [Cadences](#cadences) · [Production Readiness Gate](#production-readiness-gate)

**Before any operational change**, read `## Due` and `## Index Registry` in `~/Clawic/data/rag/memory.md`, and check whether a cadence is overdue — state it in one line rather than asking. `## Baseline` is what any drift claim is measured against.

## The Latency Budget

`latency_budget_ms` is p95 end to end. Measure each stage separately and store the split; a single number tells you nothing about what to cut.

| Stage | Behavior | Lever when it dominates |
|---|---|---|
| Query rewrite / transform | One blocking LLM call | Skip it on turn 1 and on classified single-topic questions (`conversation.md`) |
| Query embedding | Network-dominated for hosted models | Cache; co-locate; batch when the surface allows |
| ANN search | Grows with `ef_search` and filter cost | Lower `ef_search`, index the filter fields (`indexing.md`) |
| Reranking | Linear in `candidates × passage_tokens` | Lower `retrieve_k`, truncate passages (`reranking.md`) |
| Generation | Usually the largest | Streaming hides it; nothing hides the stages above it |

Everything before the first generated token is dead time the user watches. That is why a reranker that adds 300 ms feels worse than a generator that is 300 ms slower.

Measure at p95 and p99, never at the mean: the mean of a pipeline with a cache is the cache-hit path, and the complaint comes from the miss path.

## Caching

| Cache | Key | Hit rate driver | Danger |
|---|---|---|---|
| Embedding cache (documents) | Content hash | Re-ingestion of unchanged documents | None — pure saving, and it makes reindexes cheap |
| Embedding cache (queries) | Normalized query string | Repeated queries | None |
| Retrieval cache | Query + filter + index version | Popular queries | Must be invalidated on index change, or it serves the previous corpus |
| Semantic cache | Nearest cached query above a threshold | Paraphrase volume | The dangerous one, below |
| Answer cache | Query + context ids + prompt version | Stable corpora | Stale on prompt change |

**Semantic caching** serves a cached answer when a new query is close enough to an old one. The failure is silent and confident: "Q3 revenue" and "Q4 revenue" are neighbors in embedding space. Rules if you use it — a very high similarity threshold calibrated on this corpus, the tenant and every active filter in the cache key, a short TTL, and never for questions containing numbers, dates or named entities. The safe version of this idea is an exact-match cache on the normalized query string.

Every cache key must include the index version. A cache that survives a reindex is a machine for serving the old corpus.

## Incremental Sync

- Compare `source_version` — a content hash — not modification timestamps. Timestamps change when nothing did, and re-embedding an unchanged corpus is the most common avoidable cost in this domain.
- Process order per document: **delete by `doc_id`, then upsert**. Reversed, both versions are live in the window between them (SKILL.md Rule 8).
- Track sync freshness per source and expose it. A source that stopped syncing three weeks ago produces confident answers from a frozen corpus and looks exactly like a working system.
- Handle source deletions explicitly: a document that disappears upstream will never appear in a sync feed. Reconcile the full id list periodically, not just the change feed.
- Checkpoint by `doc_id` so a failed run resumes rather than restarting (`ingestion.md`).

## Deletes and Retractions

- Deletion by `doc_id` filter must work today, in one call, or the design has already failed (SKILL.md Rule 8).
- Most ANN indexes tombstone rather than reclaim. Recall degrades slowly as tombstones accumulate, and no alarm fires. Schedule compaction or a rebuild on a cadence proportional to the delete rate.
- Verify deletions: query for the `doc_id` after deleting. A delete that silently matched nothing — wrong field name, wrong namespace — is the failure behind "it still quotes the retracted policy".
- For a legal erasure, deletion from the index is not sufficient on its own: caches, logs, and eval sets hold the same content (`security.md`).

## Reindex as a Migration

Triggered by any change to the six fingerprint fields, the chunker, or quantization. Never in place.

1. Build the new index alongside the live one, with a new name carrying the fingerprint.
2. Run the golden set against both. The new index must match or beat the baseline before anything is repointed (`evaluation.md`).
3. Shadow-run production traffic against both if the surface allows, and compare top-k overlap. A large disagreement rate with equal scores is a signal to look harder before switching.
4. Repoint by configuration, not by code deploy, so rollback is one value.
5. Keep the old index for at least one full eval cycle. Deleting it the same day removes the only rollback that exists.
6. Invalidate every cache keyed on the index version, in the same operation.

Budget the window: `chunks ÷ embedding_throughput_per_s` plus index build time, plus the cost of re-embedding the corpus (`costs.md`). A document-embedding cache keyed by content hash makes the second reindex dramatically cheaper than the first.

## Drift Monitoring

Nothing here errors, so all of it must be watched deliberately.

| Signal | Baseline | What a move means |
|---|---|---|
| Mean top-1 similarity | From `## Baseline` | Down: corpus dilution, a model change, or a query-mix shift |
| Score distribution shape | Stored histogram | A changed shape with a stable mean is a model change |
| Empty-result rate | Production baseline | Coverage gap opening (`retrieval.md`) |
| Refusal rate | Production baseline | Threshold, corpus, or index moved |
| Citation-verification failure rate | Near zero | The earliest available alarm for anything upstream |
| Reformulation rate | Production baseline | Quality regression users feel before any metric shows it |
| Corpus size and per-source freshness | Expected counts | A source silently stopped syncing |
| Latency per stage | p95 per stage | Which stage regressed, immediately |

**Probe vectors**: embed a fixed set of ten sentences on a cadence and compare against stored vectors. A provider that updated a model behind a stable name shows up here and nowhere else. Two lines of code, and it is the only direct detector of the most confusing failure in the domain.

## Alarms Worth Having

Thresholds are set from each system's own baseline, not from a table of universal numbers. What to alarm on:

- Empty-result rate above its baseline band — a coverage or filter break.
- Citation-verification failures above near-zero — grounding is broken.
- Mean similarity moving beyond the noise band of repeat runs — drift or a model change.
- Any source whose freshness exceeds its stated refresh cadence by 2× — sync is dead.
- p95 latency above `latency_budget_ms` — with the per-stage split attached, or the alarm is not actionable.
- Cost per query above its budget — usually context growth or a loop that stopped terminating (`agentic.md`, `costs.md`).

## Failure Handling

Each dependency fails differently and needs a decided behavior, not a stack trace:

| Failure | Behavior |
|---|---|
| Embedding API timeout | Retry with backoff and jitter, then fall back to the BM25 leg alone and say the answer is keyword-only |
| Vector store unavailable | Fail closed with an explicit message. Answering from parametric memory when retrieval is down is the worst available outcome |
| Reranker unavailable | Degrade to fused order, log the degradation, keep serving |
| Generator rate-limited | Queue with backpressure; never silently drop the retrieval work already paid for |
| Context overflow | Drop history first, then the lowest-ranked chunks — never truncate mid-chunk (`generation.md`) |
| Partial index after a failed reindex | Do not repoint. The old index is still correct |

## Cadences

Every accepted cadence becomes a row in the `## Due` table of `memory.md`, checked at the start of a session.

| What | Typical every | Why |
|---|---|---|
| Golden-set eval | Month, and on every retrieval change | Catches slow regressions |
| Corpus freshness sweep | Week | Detects a source that stopped syncing |
| Drift check against baseline | Week | Score distribution and probe vectors |
| Index compaction or rebuild | Quarter, or scaled to the delete rate | Tombstone recall decay |
| Permission resync from the source system | Month | Access drift (`security.md`) |
| Embedding and reranker model review | Quarter | New models, deprecations, price changes |
| Cost review | Month | `costs.md` |

## Production Readiness Gate

Before a RAG system takes real traffic:

- Golden set exists, with negatives, and the baseline is recorded with its date
- Recall@`retrieve_k` measured and above the bar; ANN recall against exact search measured
- The six fingerprint fields recorded in `## Index Registry`, and the query path verified against them
- Deletion by `doc_id` tested end to end, including cache invalidation
- Access filter applied from the session on every path, with an isolation test in CI (`security.md`)
- Per-stage latency measured at p95, inside `latency_budget_ms`
- Cost per query measured and inside budget
- Retrieval logging on, with 100% of refusals, empty results and failed citation checks captured
- Alarms wired for empty-result rate, citation-verification failures, drift, and source freshness
- Reindex procedure written and rehearsed once, with the rollback path named
- Cadences written into `## Due`

**After a reindex, a migration, or an incident**, write the outcome to `~/Clawic/data/rag/evals/<year>.md` (the golden-set run that gated the switch) and update `## Index Registry` in `memory.md` with the new index and a retirement date on the old row. Save the reindex procedure and any incident runbook to `~/Clawic/data/rag/artifacts/`, with their `## Boxes` lines in the same turn, and record the cadence in `## Due` (`memory-template.md`).
