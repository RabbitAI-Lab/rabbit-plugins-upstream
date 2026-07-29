# Costs — What A RAG System Actually Spends

Two cost curves with different shapes: ingestion is paid once per corpus version, query cost is paid forever. Almost every optimization is a decision about which one to move the work to.

**Contents:** [The Cost Model](#the-cost-model) · [Ingestion Cost](#ingestion-cost) · [Storage and Memory Cost](#storage-and-memory-cost) · [Per-Query Cost](#per-query-cost) · [Where the Money Actually Goes](#where-the-money-actually-goes) · [Levers, Cheapest First](#levers-cheapest-first) · [Managed Versus Self-Hosted](#managed-versus-self-hosted) · [Monthly Review](#monthly-review)

**Before any cost claim**, read `## Baseline` in `~/Clawic/data/rag/memory.md` for the recorded cost per query and the eval rows in `evals/<year>.md`. A current number with no prior number is not an answer, and "it got cheaper" without the quality delta beside it is not a result.

Prices below are recorded 2026-07 and used only as shapes; verify the absolute figure on the provider's page before committing money.

## The Cost Model

```
one-off   = chunks × chunk_tokens × embedding_price_per_token
            + images × vision_call_price
            + (chunks × context_generation_price, if enriching)
monthly   = index_hosting + storage
per query = query_embedding + rerank_call + generation_tokens
            + optional: rewrite call, judge call, loop iterations
```

The asymmetry that decides most designs: a one-off cost is bounded and known, a per-query cost multiplies by traffic forever. Moving work from query time to ingestion time is nearly always the right trade — that is the whole argument for enrichment at ingestion over transformation at query time (`chunking.md`).

## Ingestion Cost

Worked example, so the shape is concrete: 10,000 documents averaging 4,000 tokens, `chunk_tokens` 512, 12% overlap.

| Item | Formula | Result |
|---|---|---|
| Chunks | `10,000 × 4,000 ÷ (512 × 0.88)` | ~89,000 chunks |
| Tokens to embed | `89,000 × 512` | ~46M tokens |
| Embedding cost at 0.02 USD/1M | `46 × 0.02` | ~0.91 USD, one-off |
| Same at 0.13 USD/1M (a large model) | `46 × 0.13` | ~6 USD |

The conclusion that surprises people: **embedding a corpus is cheap**. Ten thousand documents cost a coffee. What is expensive at ingestion is anything with an LLM call per chunk:

| Enrichment | Cost shape | Verdict |
|---|---|---|
| Heading path prepended | Free, string concatenation | Always do it |
| Generated chunk context | One generation per chunk — thousands of calls | Measure the gain on the golden set before paying corpus-wide |
| Entity extraction for a graph | One call per chunk, re-run on every change | Price the maintenance, not just the first pass (`structured-data.md`) |
| Image descriptions | One vision call per image | Bounded by image count, one-off (`multimodal.md`) |
| Proposition rewriting | One call per passage | The most expensive chunking strategy there is |

Prompt caching on a shared prefix and batch endpoints materially reduce per-chunk enrichment cost where the provider offers them — check both before deciding an enrichment is unaffordable.

## Storage and Memory Cost

- Vectors: `n × 4 × dims` bytes. Graph: `n × 8 × M` bytes. 1M vectors at 1536 dims with M=16 → ~6.3 GB before payload (SKILL.md Sizing formulas).
- Memory is the bill for a self-hosted store, because HNSW wants the graph resident. Halving the dimension halves it; int8 quantization quarters it (`indexing.md`).
- Managed stores usually price on stored vectors, dimension and replicas together. Replicas multiply the memory bill, not only the storage line.
- Payload storage is easy to forget and easy to shrink: keeping full chunk text in the vector store when a system of record already holds it can be the largest single line in a store bill.

## Per-Query Cost

Worked example, one query: `retrieve_k` 30, `context_k` 5 chunks of 512 tokens, hosted reranker, a 400-token answer.

| Component | Quantity | Notes |
|---|---|---|
| Query embedding | ~20 tokens | Rounding error |
| Rerank | 30 candidates × passage length | Priced per search on hosted rerankers, per GPU-second when self-hosted |
| Generation input | ~2,600 context + ~300 system/history | The dominant token count |
| Generation output | ~400 tokens | Priced higher per token than input |
| Optional rewrite | One small-model call | `conversation.md` |
| Optional judge | One call, if verifying online | `evaluation.md` |

Generation input tokens are usually the largest line, and they are set by `context_k × chunk_tokens`. That makes context size the main cost lever in the whole system — and reranking is what allows a smaller `context_k` without losing the answer (`reranking.md`).

Compute cost per query from a real sample of 100 production queries, not from a typical case. The distribution has a tail — long documents, loop iterations, retries — and the tail is where budgets die.

## Where the Money Actually Goes

Ranked by how often each turns out to be the surprise, in systems that have one:

| Line | Why it grows unnoticed |
|---|---|
| Context tokens per query | `context_k` raised during debugging and never lowered |
| Agentic loop iterations | No termination on "no new candidates"; cost per question varies 10× (`agentic.md`) |
| Query transformation | An LLM call added per query for a gain nobody re-measured (`retrieval.md`) |
| Reindexing | A model change re-embeds the corpus; frequent experiments re-embed it repeatedly |
| Online judges | Verifying every answer is a second generation call per query |
| Vector store replicas | Provisioned for an availability target nobody revisited |
| Idle managed capacity | A store sized for launch traffic that never arrived |
| Duplicate corpus content | Paying to embed, store and retrieve the same text several times (`ingestion.md`) |

## Levers, Cheapest First

Apply in this order; each is measured against the golden set before keeping it (SKILL.md Rule 9).

1. **Cache document embeddings by content hash.** Pure saving, no quality cost, and it makes every future reindex dramatically cheaper.
2. **Cache query embeddings and exact-match answers.** No quality cost.
3. **Deduplicate the corpus.** Cuts index size, storage and retrieval noise at once (`ingestion.md`).
4. **Lower `context_k` and add or improve reranking.** Fewer, better chunks: usually cheaper *and* more accurate (`reranking.md`).
5. **Truncate passages sent to the reranker.** Rerank cost is linear in passage length.
6. **Quantize the index.** int8 quarters memory for a small, measurable recall cost (`indexing.md`).
7. **Truncate embedding dimensions** if the model supports it, and renormalize (`embeddings.md`).
8. **Gate the expensive path.** Route the median question to a single pass and reserve loops and judges for the classes that need them (`agentic.md`).
9. **Use a smaller generator with better context.** Retrieval quality substitutes for model size more often than teams expect.
10. **Self-host the reranker** at sustained volume — the break-even is below what most people assume, because rerank calls are per-query.

Never reached by cutting: the quality floor. A change that saves money and loses recall is recorded with both numbers, and the decision is the user's.

## Managed Versus Self-Hosted

The break-even is a monthly comparison, not a principle:

- **Managed cost** = plan price × replicas, plus per-query fees where they exist. Predictable, and it scales with the vendor's pricing model rather than yours.
- **Self-hosted cost** = the box (memory-sized from the formula above), plus operational time, plus the GPU if embedding or reranking runs locally. The box is a host and belongs in the shared inventory.
- Below roughly a few million vectors and modest QPS, pgvector on a database you already run is often free at the margin — the strongest argument for it (`indexing.md`).
- Self-hosting embedding or reranking pays off at sustained volume because those are per-query costs; self-hosting the *store* pays off on memory size, which is a monthly cost. Two different break-evens, decided separately.
- Include the reindex in the comparison: a managed store with fast bulk import can be cheaper in engineering time than a self-hosted one that needs a rebuild window.

## Monthly Review

| Check | Action |
|---|---|
| Cost per query versus the recorded baseline | A rise with flat quality points at context size or loop iterations |
| Context tokens per query, p50 and p95 | The p95 is where an unbounded path hides |
| Index size versus corpus size | Divergence means duplicates or undeleted versions (`production.md`) |
| Managed plan utilization | Provisioned capacity nobody uses is the easiest saving available |
| Reindex count this month | More than one unplanned reindex means the model or chunker is being changed without a decision record |
| Judge and rewrite call volume | Optional stages that were added for an experiment and stayed |
| Subscriptions still in use | A store or reranker replaced last quarter and still billing |

**After a cost review or a saving**, write the cost per query and its date into `## Baseline` in `~/Clawic/data/rag/memory.md`, and the saving with what it cost in quality into `~/Clawic/data/rag/evals/<year>.md`. Managed store plans and embedding or rerank API subscriptions go to the shared `~/Clawic/data/finances/subscriptions.md`, one row per service with the amount carrying its currency (`70 USD`, never `$70`); read the file before adding, update the row in place if the service is already listed, and delete the row on cancellation, dating it in `memory.md` (`memory-template.md`).
