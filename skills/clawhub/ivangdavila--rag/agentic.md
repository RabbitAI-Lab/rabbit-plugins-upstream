# Agentic Retrieval — When One Pass Is Not Enough

Multi-step retrieval answers questions a single search cannot, and multiplies latency and cost on the questions a single search already answered. The design problem is not the loop, it is the gate in front of it.

**Contents:** [Which Questions Need It](#which-questions-need-it) · [Decomposition](#decomposition) · [The Retrieve-Critique-Retry Loop](#the-retrieve-critique-retry-loop) · [Budgets and Termination](#budgets-and-termination) · [Retrieval as a Tool](#retrieval-as-a-tool) · [Multi-Corpus Routing](#multi-corpus-routing) · [Failure Modes of the Loop](#failure-modes-of-the-loop) · [Evaluating a Loop](#evaluating-a-loop)

**Before offering an agentic path**, read `latency_budget_ms` in `config.yaml`. A loop with three iterations spends three retrievals and three generations; if the budget cannot hold that, the answer is decomposition with a fixed shape, not a loop.

## Which Questions Need It

| Question shape | Single pass | Multi-step |
|---|---|---|
| "What does the refund policy say" | Yes | Waste |
| "Compare the refund policy with the enterprise SLA" | No — two topics, one embedding | Decompose into two retrievals |
| "Who signed the contract that superseded the 2024 agreement" | No — the answer to hop 1 is the query for hop 2 | Sequential |
| "Is our retention policy compliant with the new rule" | No — needs both documents and a comparison | Decompose, then reason |
| "Find anything that contradicts the handbook on parental leave" | No — the target is defined by its relationship to another document | Retrieve, then search against what was found |
| Anything answered by one passage | Yes | Waste |

Gate by shape, not by difficulty rating. The observable trigger for multi-step is that the question contains **two topics**, or that **the query for the second search is the answer to the first**. Both are detectable in one cheap classification call, and that call is what keeps the median query fast (`retrieval.md`).

## Decomposition

The cheapest multi-step pattern, and the one to reach for first because it is bounded and parallel.

1. Split the question into independent sub-questions with one LLM call.
2. Retrieve for each, in parallel.
3. Merge the contexts, deduplicated by `chunk_id`, and rerank as one pool.
4. Generate one answer that addresses every sub-question, citing per part.

- Cap the number of sub-questions — three or four. A decomposer given no limit will produce eight, and the context budget will then drop most of what it retrieved.
- Preserve the original question in the final prompt. Answering the sub-questions is not the same as answering what was asked.
- If a sub-question retrieves nothing above the floor, say so per part rather than dropping it silently — a partial answer that hides its gap is the worst output of this pattern (`generation.md`).
- Comparisons are the canonical case: "A versus B" needs A's chunks and B's chunks, and a single embedding of "A versus B" reliably retrieves neither well.

## The Retrieve-Critique-Retry Loop

For questions where the first retrieval cannot be known to be sufficient until it is read.

```
retrieve → assess sufficiency → if insufficient: reformulate → retrieve again → ...
                             → if sufficient: generate → verify → if unsupported: retry or refuse
```

- **The sufficiency check is a small, cheap call**, and it must be allowed to say "no". A checker that always approves turns the loop into an expensive single pass.
- **Reformulation must change something observable** — a different entity, a different filter, a different route. A reformulation that returns the same candidate set is a wasted iteration, and the loop should detect it by comparing candidate ids and stop.
- **Verification after generation** is the same citation check as always (`generation.md`), and here it has somewhere to go: a failed check can trigger one more retrieval instead of a refusal.
- Keep every iteration's candidate ids. Without them the loop is unauditable and the eval cannot say which iteration helped.

## Budgets and Termination

A loop without a hard stop is an outage waiting for a corpus gap.

| Budget | Default | Why |
|---|---|---|
| Max iterations | 3 | Past three, the additional answer rate is small and the tail latency is not |
| Max total retrievals | 6 | Decomposition inside iterations multiplies faster than people expect |
| Wall-clock deadline | `latency_budget_ms` | Enforced by the caller, not by the loop's own accounting |
| Token ceiling per question | Set from `costs.md` | The only bound that survives an infinite reformulation cycle |

Terminate on any of: sufficiency reached, budget exhausted, or **no new candidates** — the last is the most useful and the most often omitted. On exhaustion, answer with what was found and state what was missing. Silently returning a partial answer as if it were complete is worse than the refusal it was avoiding.

## Retrieval as a Tool

When the generator itself decides when to search, the design shifts from a pipeline to a tool contract.

- **Describe the tool by corpus, not by mechanism**: "search the customer support knowledge base (product docs, macros, 2024-present)" is a description the model can route with; "vector_search(query)" is not.
- **One tool per corpus** beats one tool with a corpus parameter. The model chooses better between named things than between values of an enum.
- **Return chunks with ids and sources**, so the citation chain survives the tool boundary.
- **Bound the calls.** A model that can search will search repeatedly when the corpus lacks the answer; the retrieval budget above applies unchanged.
- Everything about untrusted retrieved content applies with more force here: tool output is being fed back to a model that is deciding what to do next, which is the highest-value target for an injected instruction (`security.md`).

## Multi-Corpus Routing

Several indexes with different content, freshness and permissions.

- Route by description, and allow multiple corpora per question. "What is our policy and what did the vendor promise" is two corpora, one answer.
- Merge across corpora by rank fusion, never by raw score: two indexes built with different models produce scores that cannot be compared (`retrieval.md`).
- Keep the access filter per corpus. Corpora have different permission models, and a filter written for one applied to another is a leak (`security.md`).
- Record each corpus's freshness in the answer when it matters. An answer merging a live index with one that stopped syncing in March is wrong in a way nobody will notice.

## Failure Modes of the Loop

| Failure | Cause | Fix |
|---|---|---|
| Loop never terminates on a corpus gap | No "no new candidates" stop | Compare candidate ids between iterations |
| Every question takes three iterations | The sufficiency check approves nothing | Calibrate the checker against cases known to be answerable in one pass |
| Cost per question varies 10× | No gate in front of the loop | Classify first, route the median question to the single pass |
| Later iterations retrieve worse | Reformulation drifts from the original question | Keep the original query in every reformulation's fusion |
| Answer cites chunks from a discarded iteration | Context accumulated across iterations without pruning | Rebuild the final context from the surviving chunks only |
| Injected instruction changes the plan mid-loop | Tool output treated as instruction | Fence retrieved content at every hop (`security.md`) |

## Evaluating a Loop

- Score the gate separately: what fraction of single-pass questions were sent to the loop, and what fraction of multi-step questions were not? Both errors are expensive in opposite directions.
- Report cost and latency **distributions**, not means. The point of the gate is the tail, and a mean hides it entirely.
- Add multi-hop cases to the golden set with their expected final sources, and mark them so single-pass and multi-step populations score separately (`evaluation.md`).
- Compare against the honest baseline: decomposition with a fixed shape, not the naive single pass. Many "agentic RAG beats RAG" results are decomposition beating a single embedding of a two-topic question.

**After shipping or changing a loop**, record the gate rule, the budgets and the termination conditions in `~/Clawic/data/rag/artifacts/decision-agentic-retrieval.md` with its `## Boxes` line, and write the paired run to `~/Clawic/data/rag/evals/<year>.md` with p50 and p95 cost and latency alongside the quality delta (`memory-template.md`). A loop whose budgets live only in code is the one that produces a surprise bill.
