# Conversation — Multi-Turn Retrieval

Single-turn RAG breaks on the second message. "What about the enterprise plan?" embeds to nothing useful, because the subject of the sentence is three turns back.

**Contents:** [The Failure, Precisely](#the-failure-precisely) · [Query Rewriting](#query-rewriting) · [Deciding Whether to Retrieve at All](#deciding-whether-to-retrieve-at-all) · [History Budget](#history-budget) · [Carrying Retrieved Context Forward](#carrying-retrieved-context-forward) · [Filters That Persist](#filters-that-persist) · [Citations Across Turns](#citations-across-turns) · [Evaluating Multi-Turn](#evaluating-multi-turn)

**Before designing the multi-turn path**, read `config.yaml` for `context_k` and `latency_budget_ms`: rewriting adds a blocking LLM call before retrieval, and history competes with retrieved chunks for the same context budget (`generation.md`).

## The Failure, Precisely

Three distinct breakages hide behind "follow-ups don't work":

| Symptom | Cause | Fix |
|---|---|---|
| Follow-up retrieves random chunks | The query embedding contains only "what about the second one" | Rewrite to standalone before embedding |
| Follow-up retrieves the same chunks as turn 1 | The raw history was concatenated into the query; turn 1's terms dominate | Rewrite, do not concatenate |
| Answer ignores what was just established | History was trimmed before the relevant turn | History budget and summarization, below |
| Answer contradicts turn 1 | Turn 1's chunks were dropped and turn 3 retrieved a conflicting document | Carry cited chunk ids forward |

Diagnose before fixing: log the string that was actually embedded. In most broken multi-turn systems, seeing that string once ends the investigation.

## Query Rewriting

An LLM call that turns the conversation plus the new message into a standalone question.

- **Rewrite the query, not the answer**: the output is a search query, and it should read like one — entities named, pronouns resolved, implicit constraints made explicit.
- **Feed it a bounded window**, typically the last 3-5 turns. More history makes the rewriter drag stale entities into the query, which produces the "retrieves turn 1's chunks forever" failure.
- **Keep the raw query as a second leg** and fuse (`retrieval.md`). A rewriter that misreads the reference then only degrades the ranking rather than replacing the query entirely.
- **Skip it on turn 1.** A rewrite of a standalone question is a call that can only introduce error.
- Cost: one blocking call before retrieval, which sits in the most latency-sensitive slot in the pipeline. It is the reason a fast small model is the right choice here even when a large one writes the answers.

Failure mode to watch: over-specification. "How much does it cost" after a discussion of the enterprise plan should become "enterprise plan pricing", not a rewrite that also injects the user's industry, region and previous complaint — each injected term narrows retrieval further.

## Deciding Whether to Retrieve at All

Not every turn needs a search. Retrieving for "thanks, that helps" returns five arbitrary chunks and invites the generator to use them.

Classify each turn: **new information need** → rewrite and retrieve; **follow-up answerable from the context already in the conversation** → answer without retrieving; **meta or social** → no retrieval. A small classifier or a structured field in the rewriter's output handles this in one call, and it is the cheapest latency saving available in a chat surface.

Bias the classifier toward retrieving when uncertain: a wasted search costs milliseconds, a skipped one costs a wrong answer.

## History Budget

History and retrieved chunks draw on the same budget (`generation.md`). Priority when it binds, highest first:

1. The current question.
2. The retrieved chunks for this turn.
3. The last two turns verbatim.
4. A running summary of everything older.
5. Older turns verbatim — the first thing to drop.

- Summarize progressively rather than truncating: a rolling summary updated every N turns keeps established facts (the user's plan, their region, the document under discussion) alive at a fraction of the tokens.
- Keep entities and constraints in the summary explicitly, as a short structured block. That block is also the best input to the rewriter.
- Never summarize away a number the user gave you. Extracted constraints — "5 seats", "Spain", "annual billing" — belong in a slot list that is not subject to summarization.

## Carrying Retrieved Context Forward

- Keep the `chunk_id` list from the previous turn and merge it with the new retrieval, deduplicated, before reranking. It makes "and what about the second point" resolvable without a lucky re-retrieval.
- Cap the carry-forward at one or two turns. Chunks accumulated across ten turns fill the context with material the conversation moved past.
- When the topic clearly changes, drop the carry-forward entirely. The rewriter's output is a usable signal: a rewrite that shares no entities with the previous one is a topic switch.

## Filters That Persist

- The access filter is derived from the session and applied on every turn, always. It is never carried in conversation state and never derived from the rewriter (`security.md`).
- Content filters the user established conversationally — "only 2026 documents", "just the EU policies" — should persist until contradicted, and the assistant should say once that they are still applied. A silently persistent filter produces "why can't it find X" three turns later.
- Store persistent filters as explicit slots, not as prose in the history, so they survive summarization.

## Citations Across Turns

- Chunk ids are stable, so a citation from turn 1 stays valid in turn 6 and can be referenced without re-retrieval (`chunking.md`).
- When an answer relies on a chunk cited earlier, cite it again. A reader arriving at turn 6 has no way to know what "as mentioned" points at.
- If a document was updated mid-conversation — rare, but real in a live-synced corpus — the cited id may now resolve to different text. Version-aware ids (`doc_id@source_version`) make that detectable rather than confusing.

## Evaluating Multi-Turn

Single-turn golden sets miss all of this. Extend the set with conversations, not just questions:

- Each case is an ordered list of turns with the expected sources for the final turn, plus the rewritten query you consider correct.
- Score the rewriter separately from retrieval: rewrite accuracy is an independent metric, and a retrieval regression caused by a rewriter regression is otherwise unattributable.
- Include a topic-switch case and a "no retrieval needed" case; both are common in production and absent from every hand-written eval set.
- Multi-turn cases go in the same golden set file, marked with their type, so a run scores both populations and reports them separately (`evaluation.md`).

**After changing the rewriter, the history budget or the carry-forward policy**, write the paired run to `~/Clawic/data/rag/evals/<year>.md` with the multi-turn subset scored separately, and save a rewriter prompt that survived evaluation to `~/Clawic/data/rag/artifacts/prompt-query-rewriter.md` with its `## Boxes` line in the same turn (`memory-template.md`).
