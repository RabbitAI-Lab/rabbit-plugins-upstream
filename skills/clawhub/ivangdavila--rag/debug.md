# Debug — Symptom To Cause

Work down the pipeline in order. Each stage's output is the next stage's input, so the first stage where the data is already wrong is the only stage worth investigating.

**Contents:** [The Ten-Minute Triage](#the-ten-minute-triage) · [Stage Isolation](#stage-isolation) · [Symptom Table](#symptom-table) · [A Document That Will Not Surface](#a-document-that-will-not-surface) · [Empty Results](#empty-results) · [Non-Deterministic Answers](#non-deterministic-answers) · [Works Locally, Fails in Production](#works-locally-fails-in-production) · [It Was Fine Last Week](#it-was-fine-last-week) · [What to Log](#what-to-log)

**Before diagnosing anything**, read `## Known Failures` in `~/Clawic/data/rag/memory.md` — or `failures.md` if the `## Boxes` index points there. The same symptom recurs with different causes, and the table says which causes were already ruled out on this system.

## The Ten-Minute Triage

Four questions, in this order. Each one eliminates a stage.

1. **Is the answer in the retrieved chunks?** Print them. No → retrieval. Yes → generation. This single step resolves most reports (SKILL.md Rule 1).
2. **Is the document in the index at all?** Query by `doc_id` filter, no vector search. Absent → ingestion.
3. **Does the document surface at k=100?** Yes → ranking, so the reranker or the fusion. No → embedding or chunking.
4. **Does it surface with BM25 but not dense, or the reverse?** Names which leg is failing and therefore which page to open (`retrieval.md`).

Ten minutes of this beats an afternoon of parameter changes, and it produces a `## Known Failures` row that is worth keeping.

## Stage Isolation

Reproduce with the smallest possible configuration and add stages back one at a time. The stage that changes the outcome is the stage that owns the bug.

```
raw query → dense only, no filter, no rerank, k=100     ← is the answer anywhere?
        → add the filter                                 ← did the filter remove it? (Rule 6)
        → add the BM25 leg and fusion                    ← did fusion demote it?
        → add reranking                                  ← did the reranker demote it?
        → add query rewriting                            ← did the rewrite change the question?
        → generate                                       ← does the model use what it was given?
```

Rewriting is last on purpose: it is the stage most likely to be silently responsible and the easiest to forget is running (`conversation.md`).

## Symptom Table

| Symptom | Check first | Then | Cause it usually is |
|---|---|---|---|
| Wrong documents, confidently | Are the right ones at k=100? | Reranker and fusion | Ranking, not retrieval (`reranking.md`) |
| Right documents, wrong answer | Context ordering and prompt | Model and contract | Generation (`generation.md`) |
| Nothing relevant at any k | Is the document indexed? | Chunk boundaries, then vocabulary | Ingestion or chunking |
| Zero results | Filter selectivity and post-filtering | Score floor | Filtering (`indexing.md`) |
| All scores in a narrow band | Random-pair baseline for this model | Normalization | The band is the model's floor, not relevance (`evaluation.md`) |
| Exact identifiers never match | Is BM25 running? | Analyzer tokenization | Dense-only, or an analyzer splitting the identifier |
| Answers cite deleted content | Delete-then-upsert order | Tombstones and compaction | Two versions live (SKILL.md Rule 8) |
| Five near-identical results | Duplicates at ingestion | Overlap setting | Deduplication (`ingestion.md`) |
| Long documents never match | Model max sequence length vs p99 chunk length | Splitter config | Silent truncation (`embeddings.md`) |
| Only some users see nothing | Access field coverage on older chunks | Session filter derivation | Metadata backfill gap (`security.md`) |
| Slow only sometimes | Per-stage latency split | `ef_search`, rerank depth, cold cache | One stage, and the split names it (`production.md`) |
| Cost jumped, quality flat | Per-query token and call counts | Loop iterations, context size | An agentic path or context growth (`costs.md`) |
| Anything else | Re-run with full retrieval logging | Compare against a known-good query | See the log fields below |

## A Document That Will Not Surface

The most common report, and it has five distinct causes. Walk them in this order — each check is cheaper than the next.

1. **Not ingested.** Filter by `doc_id`. If it is absent, the parser failed, the file was excluded by a path pattern, or the batch upsert dropped it silently (`ingestion.md`).
2. **Ingested as garbage.** Fetch the chunk text. Whitespace, interleaved columns, or a caption-only chunk from a scan all embed fine and match nothing.
3. **Split badly.** The answer straddles a boundary, so neither chunk contains a complete statement of it. Read the two adjacent chunks (`chunking.md`).
4. **Truncated at embedding.** Chunk longer than the model's max sequence length; the tail is not searchable (`embeddings.md`).
5. **Vocabulary mismatch.** The chunk says "termination for convenience" and the query says "cancel early". Confirm by searching with the chunk's own wording: if that retrieves it, the fix is hybrid retrieval, enrichment, or query expansion — not chunk size.

Only after all five is "the embedding model is bad" a supportable conclusion.

## Empty Results

| Cause | How to confirm |
|---|---|
| Post-filtering after ANN | Re-run the same query with no filter; if results appear, this is it (SKILL.md Rule 6) |
| Score floor too high | Log the top score before the floor is applied |
| Filter field missing on older chunks | Count chunks lacking the field |
| Access filter correct, corpus genuinely lacks it | Run the same query as an unrestricted principal |
| Namespace or collection wrong | Count vectors in the collection actually being queried |
| Index empty or half built | Indexed count versus expected chunk count (`ingestion.md`) |

The last one is worth checking early despite feeling unlikely: a reindex that failed halfway leaves a working system with a partial corpus, and every symptom above appears at once.

## Non-Deterministic Answers

Same query, different answer. Sources, in order of frequency:

- **Tied or near-tied scores** broken by whatever order the store returned. Stable-sort with `chunk_id` as the final tiebreaker.
- **Generator sampling.** Set temperature to 0 for the diagnosis; if the variation disappears, it was never retrieval.
- **An unpinned model.** Embedding, reranker or generator resolving to "latest" behind a stable name (`embeddings.md`).
- **A live-syncing corpus.** The index changed between the two runs; check `ingested_at` on the differing chunks.
- **Approximate search itself** with a low `ef_search`: the graph walk can take different paths under concurrency. Raise it and re-test (`indexing.md`).

## Works Locally, Fails in Production

Compare, in this order — the first difference found is almost always the cause:

1. Index name, namespace, and vector count.
2. The six fingerprint fields on both sides (`embeddings.md`).
3. The active filter, including the access filter that only exists in production.
4. Corpus contents — production has documents the dev snapshot does not, and they compete for the top-k.
5. Model versions and provider region.
6. `retrieve_k`, `context_k`, reranker presence — configuration drift between environments.

## It Was Fine Last Week

No deploy, worse answers. Ordered by likelihood:

- **Corpus grew.** New documents changed the neighborhood of existing queries. Compare the score distribution against the stored baseline (`production.md`).
- **A provider updated a model** behind the same name. Re-embed a fixed probe text and compare the vector against a stored one — this is why keeping a probe vector is worth the two lines it costs.
- **Documents were updated or retracted** upstream and the sync did not delete the old versions.
- **Tombstones accumulated** in the ANN index and recall degraded gradually (`indexing.md`).
- **A quota or rate limit** is causing silent partial results in one leg of hybrid retrieval — check error rates per leg, not just overall.

## What to Log

The fields that make every investigation above possible without a reproduction attempt:

`query` as received · `rewritten_query` · `route` · `filter` applied · candidate `chunk_id`s with scores **per leg** · fused order · reranked order with scores · final `context_k` ids · per-stage latency · model ids and versions used · answer · cited ids · citation-verification result.

Sample rather than logging everything if volume forbids, but never sample away the failures: log 100% of refusals, empty results, thumbs-down and failed citation checks. Those are also the free labels the golden set wants (`evaluation.md`).

**After diagnosing a failure down to its cause**, add a row to `## Known Failures` in `~/Clawic/data/rag/memory.md` — date, symptom, the real cause, the fix, and whether it is still open — and keep the row after it is fixed (`memory-template.md`). When the diagnosis produced a procedure worth repeating, save it as `~/Clawic/data/rag/artifacts/runbook-<symptom>.md` with its `## Boxes` line in the same turn.
