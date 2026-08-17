# Reranking — Buying Precision With Latency

The retriever's job is to not lose the answer. The reranker's job is to put it first. Confusing the two is why people rerank a top-5 list and see nothing change.

**Contents:** [Why a Cross-Encoder Wins](#why-a-cross-encoder-wins) · [Candidate Depth](#candidate-depth) · [Choosing a Reranker](#choosing-a-reranker) · [LLM Rerankers](#llm-rerankers) · [The Latency Budget](#the-latency-budget) · [Score Semantics](#score-semantics) · [When Not to Rerank](#when-not-to-rerank) · [Measuring the Gain](#measuring-the-gain)

**Before adding a reranker**, read `## Baseline` in `~/Clawic/data/rag/memory.md`: a reranker cannot raise recall@`retrieve_k`, so if that number is the problem, this page is the wrong page (`retrieval.md`).

## Why a Cross-Encoder Wins

A bi-encoder embeds the query and the document separately, so the document vector was computed before your query existed and cannot depend on it. A cross-encoder reads query and passage together and outputs one relevance score — it can see that the passage mentions the exact entity, that the negation applies, that the date matches.

The trade is exactly the trade that makes the two-stage design necessary: cross-encoding is not precomputable, so it costs one forward pass per candidate at query time, so it can only run on tens of candidates, so something cheap must produce those candidates first.

## Candidate Depth

`retrieve_k = context_k × 6`, floor 20, capped by `latency_budget_ms` (SKILL.md Rule 3). Default 30 → 5.

| Depth | What it buys | What it costs |
|---|---|---|
| 10 | Almost nothing — you are reranking what you would have sent anyway | Latency for no precision |
| 20-30 | The working range for most corpora | The baseline rerank cost |
| 50-100 | Recovers answers the bi-encoder ranked in the middle; worth it when recall@10 is much worse than recall@100 | Latency scales linearly with candidates |
| >100 | Diminishing on most corpora | The reranker becomes the dominant latency term |

Derive the depth instead of guessing: plot recall@k for k in {5, 10, 20, 50, 100} on the golden set. Set `retrieve_k` where the curve flattens — that is the point past which the retriever is no longer finding anything new and the reranker has nothing more to rescue.

With hybrid retrieval, take candidates from the fused list, not `retrieve_k` from each leg (`retrieval.md`).

## Choosing a Reranker

| Option | Where it runs | Trade |
|---|---|---|
| Hosted rerank API | Provider | No infrastructure, priced per search rather than per token, and every query leaves the perimeter |
| Open cross-encoder, self-hosted | Your GPU | Cheapest per query at volume, needs a GPU box that becomes an inventory item |
| Small open cross-encoder, CPU | Your CPU | Viable at low QPS and short passages; measure before believing it |
| Late interaction (ColBERT-family) | Your store | Reranking quality at retrieval time, paid in index size (`embeddings.md`) |
| LLM reranker | Provider or local | Most flexible, slowest, most expensive — see below |
| None | — | Correct when the latency budget is tight and precision is adequate |

Selection order: perimeter constraint first (can passages leave?), then latency budget, then quality on the golden set. Passage length matters more than candidate count in the cost model, so a reranker that looks affordable on 200-token chunks may not be on 800-token ones.

## LLM Rerankers

Three shapes, in ascending cost:

- **Pointwise**: score each passage independently, 1-10. Parallelizable, and the scores are not comparable across calls unless the rubric is tightly specified.
- **Pairwise**: compare two passages at a time. Accurate and quadratic — usable only on a handful of candidates.
- **Listwise**: hand the model the whole candidate list and ask for a reordering. One call, best quality of the three, and it fails in a specific way worth knowing: the model omits or invents passage ids. Validate the returned list against the input ids and fall back to the original order on mismatch.

Use an LLM reranker when relevance requires reasoning the cross-encoder cannot do — regulatory applicability, "which of these applies to a contractor in Spain" — and accept that it turns a ~100 ms stage into a full generation call.

## The Latency Budget

End-to-end p95 is `latency_budget_ms`. Spend it explicitly:

| Stage | Typical share | Notes |
|---|---|---|
| Query transformation, if any | An LLM call, blocking | The most expensive optional stage in the pipeline (`retrieval.md`) |
| Query embedding | Small, network-dominated for hosted models | Cache repeated queries |
| ANN search | Small; grows with `ef_search` | `indexing.md` |
| Reranking | Linear in `candidates × passage_tokens` | Usually the second-largest term |
| Generation | Usually the largest | Streaming hides it from perceived latency; reranking happens before the first token and cannot be hidden |

Consequences: reranking is paid before the user sees anything, which is why a reranker that doubles time-to-first-token feels worse than a generator that is slower overall. Measure each stage separately and store the split — a single end-to-end number tells you nothing about which stage to cut.

Levers when the budget is blown, in order: reduce `retrieve_k`; truncate passages sent to the reranker to their first N tokens; batch candidates in one request instead of N; move the reranker onto the same network as the app; drop to no reranker and raise `context_k` instead.

## Score Semantics

- Reranker scores are not similarity scores and not comparable to them. A relevance score of 0.4 from a cross-encoder means something entirely different from a cosine of 0.4.
- Do not mix them. If a threshold is needed after reranking, calibrate it on the reranker's own distribution (`evaluation.md`).
- Some rerankers output calibrated probabilities and some output raw logits. Check which, because a threshold set on logits breaks the day the provider changes its output convention.
- The reranker's score is a good refusal signal precisely because it is query-aware: "the best of 30 candidates scores below the floor" is stronger evidence of a coverage gap than any similarity number (`generation.md`).

## When Not to Rerank

- Recall@`retrieve_k` is the bottleneck. Fix retrieval first; reranking a list that lacks the answer produces a better-ordered wrong list.
- `latency_budget_ms` under roughly 500 with a hosted reranker on the far side of a network hop.
- The corpus has one obvious answer per query and the bi-encoder already ranks it first — measure before assuming, but some corpora genuinely do.
- Cost per query is the binding constraint and the reranker is the largest line (`costs.md`).

## Measuring the Gain

Reranking moves precision metrics and leaves recall@`retrieve_k` untouched by construction. Measure it accordingly:

- nDCG@`context_k` and MRR before and after, same queries, paired (SKILL.md Rule 9).
- Recall@`context_k` — the fraction of queries whose answer survived into the final context — is the number that predicts answer quality, and the one most worth watching.
- Report the latency delta in the same row as the quality delta. A reranker is a purchase; the eval row is the receipt.

**After adding, removing or changing a reranker**, write the paired run to `~/Clawic/data/rag/evals/<year>.md` with nDCG@`context_k`, recall@`context_k` and the p95 delta, and record the model, the depth and where it runs in `## Index Registry` in `memory.md` (`memory-template.md`). A hosted reranker with a monthly plan is also a row in `~/Clawic/data/finances/subscriptions.md`, keyed on the service name with the amount carrying its currency.
