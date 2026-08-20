# Retrieval — The Query Side

Everything here happens after the corpus is fixed. The lever is what you do with the question before and during the search.

**Contents:** [Hybrid Search](#hybrid-search) · [Fusing Two Result Lists](#fusing-two-result-lists) · [BM25 Tuning](#bm25-tuning) · [Query Transformation](#query-transformation) · [Metadata Extraction From the Query](#metadata-extraction-from-the-query) · [Routing](#routing) · [Diversity With MMR](#diversity-with-mmr) · [Recency and Authority](#recency-and-authority) · [Thresholds and Empty Results](#thresholds-and-empty-results) · [What to Log](#what-to-log)

**Before tuning retrieval**, read `## Baseline` in `~/Clawic/data/rag/memory.md` and the golden set its `## Boxes` line points to. Retrieval changes are the easiest in the pipeline to make and the easiest to fool yourself about.

## Hybrid Search

Dense and lexical retrieval fail on disjoint query types, which is why running both is the default rather than a refinement.

| Query type | Dense | BM25 |
|---|---|---|
| Paraphrased concept ("how do I stop being charged") | Strong | Weak |
| Exact identifier (`RG-4021`, part number, surname) | Weak — subword tokenization dissolves it | Strong |
| Rare domain term | Weak unless in-domain | Strong |
| Short keyword query | Mixed | Strong |
| Long natural-language question | Strong | Diluted by stopword-ish terms |
| Negation, comparison | Weak in both — needs reranking or decomposition | Weak |

Run both legs over the same corpus, fuse, then rerank. `retrieval_mode: dense` is justified only after measuring that the BM25 leg adds nothing on this corpus, which happens when there are no identifiers and vocabulary is uniform.

## Fusing Two Result Lists

**Reciprocal rank fusion, the default.** `score(d) = Σ_i 1 / (60 + rank_i(d))` across the lists that returned `d`. The constant 60 is the published default and rarely worth tuning. Properties that make it the right default: it needs no score normalization, it is robust to one leg being badly calibrated, and it has no parameter to overfit.

**Weighted score sum, the alternative.** `α × dense_norm + (1 − α) × bm25_norm` requires normalizing both legs per query — min-max over the returned list, which is unstable when all scores cluster, or z-score, which needs a distribution. It can beat RRF once `α` is fitted on labeled data, and it loses to RRF whenever `α` was guessed. If you fit it, fit it on the golden set and record the value and the set version in `## Index Registry`.

Practical detail: fuse over the union of both lists, not the intersection. A document found by only one leg is exactly the case hybrid exists for.

## BM25 Tuning

- Defaults `k1 = 1.2`, `b = 0.75` are fine for prose. Lower `b` toward 0.3-0.5 when chunk lengths vary a lot and long chunks are being over-penalized.
- Analyzer choices matter more than `k1`: stemming, lowercase folding, and how identifiers are tokenized. If `RG-4021` is split into `rg` and `4021`, the identifier advantage is gone — configure a keyword field or a pattern tokenizer for identifier-bearing fields.
- Stopword removal helps short-query precision and hurts phrase matching. On a mixed corpus, keep stopwords and let BM25's own term weighting handle them.

## Query Transformation

Each of these costs an LLM call before retrieval. Add them one at a time, measured, and only against a named failure.

| Technique | Mechanics | Fixes | Cost |
|---|---|---|---|
| Rewriting | Resolve pronouns and context into a standalone query | Multi-turn ("what about the second one") — the main use (`conversation.md`) | One call, blocking |
| Expansion | Add synonyms and domain terms | Keyword and acronym queries against verbose documents | One call |
| Multi-query | Generate 3-5 paraphrases, retrieve each, fuse with RRF | Vocabulary mismatch where one phrasing consistently misses | One call plus N searches |
| HyDE | Generate a hypothetical answer and embed *that* | Very short queries against long-form answers; question-answer asymmetry | One call, and it hallucinates plausibly — always fuse with the raw query, never replace it |
| Step-back | Ask a more general version first, retrieve both | Narrow questions whose answer lives in a general principle | One call |
| Decomposition | Split a multi-part question into sub-questions | Comparisons and multi-hop (`agentic.md`) | One call plus N searches |

Two rules that keep this honest: always keep the original query as one leg of the fusion, and never add a transformation that has not beaten the baseline on the golden set. Every one of these adds latency before the first byte of retrieval, which is the most expensive place in the budget to add anything.

## Metadata Extraction From the Query

Self-querying: an LLM extracts filters from the natural-language question — "policies changed after March 2026" becomes a semantic query plus `date > 2026-03-01`.

- Constrain extraction to a declared schema of fields and operators, and validate the output against it. A hallucinated field name produces either an error or, in permissive stores, a silently ignored filter.
- Fail open or closed deliberately: an ignored filter returns too much, a hallucinated restrictive filter returns nothing. In a permissioned corpus this decision is a security decision (`security.md`).
- Never let extracted filters touch the access-control filter. Access filters are applied by the application from the session, always, and are not derived from anything the user typed.

## Routing

Not every question is a retrieval question. Route before retrieving:

| Question shape | Destination |
|---|---|
| Aggregation, counting, "how many", "total" | SQL or an analytics store (`structured-data.md`) |
| Relational, multi-hop over entities | Graph traversal (`structured-data.md`) |
| Chit-chat, meta-questions about the assistant | No retrieval at all — retrieving for "hello" returns five random chunks and invites the model to use them |
| Multi-part or comparative | Decompose, then retrieve per part (`agentic.md`) |
| Everything else | The default hybrid pipeline |

A cheap classifier or a small model handles routing in tens of milliseconds. The failure it prevents — retrieving irrelevant context and letting the generator anchor on it — is one of the most common causes of confident wrong answers.

## Diversity With MMR

Maximal marginal relevance re-selects the final `context_k` from the candidate pool, penalizing similarity to what is already selected: `MMR = λ × sim(q, d) − (1 − λ) × max sim(d, selected)`.

- `λ` between 0.5 and 0.7 is the working range: closer to 1 is pure relevance, closer to 0 is pure novelty.
- Use it when the top-k is dominated by near-identical chunks that overlap or duplicate each other, and when the question plausibly has more than one answer.
- Do not use it when the question has exactly one correct source: MMR will push the second-best chunk from another document into the context and give the generator something to contradict itself with.
- MMR is not deduplication. Fix true duplicates at ingestion (`ingestion.md`); MMR handles legitimate near-neighbors.

## Recency and Authority

Corpora where documents supersede each other need a tiebreaker that similarity does not provide.

- **Recency boost**: multiply the score by a decay term such as `1 / (1 + age_days / half_life_days)`, with `half_life_days` set from how fast the corpus actually turns over — 90 for a product changelog, 1000 for legal policy. A boost tuned by feel will bury a stable canonical document under yesterday's draft.
- **Authority boost**: a small fixed multiplier for sources the organization treats as canonical (the handbook over a Slack thread). Keep it small; a large one makes the corpus unsearchable outside the canonical set.
- **Status filter beats both**: if documents carry `draft`, `archived` or `superseded`, filter them out rather than down-weighting. A hard filter is auditable, a boost is not.
- Any boost is part of the fingerprint of your results. Record it in `## Index Registry` alongside the retrieval config, or the next person cannot reproduce a ranking.

## Thresholds and Empty Results

- A similarity threshold is a per-corpus, per-model measurement, never a copied constant (`evaluation.md`). Derive it: score 200 random query-document pairs from this corpus, take a high percentile of that distribution, and set the floor above it.
- "No results above the floor" is a valid and useful outcome — it is what makes cite-or-refuse possible (`generation.md`). Return it as such rather than degrading to the best of a bad list.
- Track the empty-result rate as a production metric. A rising rate means the corpus stopped covering what users ask, which is a content problem no amount of retrieval tuning will fix (`production.md`).

## What to Log

The minimum that makes any retrieval bug diagnosable after the fact, and the reason `debug.md` can work at all: query text as received, rewritten query if any, the active filter, candidate ids with scores per leg, fused order, reranked order, final `context_k` ids, and per-stage latency. Without candidate ids and scores, every retrieval investigation restarts from a reproduction attempt.

**After a retrieval change that was measured**, write the run to `~/Clawic/data/rag/evals/<year>.md` naming the one variable that changed, and update the retrieval configuration in `## Index Registry` in `memory.md` — fusion method, `α` if fitted, boosts, MMR `λ`, threshold and the date it was calibrated (`memory-template.md`). A threshold with no calibration date is a number nobody will dare touch.
