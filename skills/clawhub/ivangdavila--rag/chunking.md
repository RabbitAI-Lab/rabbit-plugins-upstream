# Chunking — Splitting So The Piece Still Answers

A chunk is not a fragment of a document, it is a candidate answer. Judge every splitting decision by one question: read this chunk alone, with no context — does it answer something?

**Contents:** [Sizing From the Corpus](#sizing-from-the-corpus) · [The Strategies, and When Each Wins](#the-strategies-and-when-each-wins) · [Overlap Is Not Context](#overlap-is-not-context) · [Context Enrichment](#context-enrichment) · [Parent-Child Retrieval](#parent-child-retrieval) · [Boundaries You Never Cross](#boundaries-you-never-cross) · [Token Counting](#token-counting) · [Chunk Ids and Ordering](#chunk-ids-and-ordering)

**Before changing any chunk parameter**, read `## Index Registry` in `~/Clawic/data/rag/memory.md`: the chunker and its settings are one of the six fingerprint fields (SKILL.md Rule 2), and changing them means a reindex, not an edit.

## Sizing From the Corpus

`chunk_tokens` is derived, not chosen. Procedure, once per corpus:

1. Sample 20 real questions and find the passage that answers each.
2. Measure the token length of those passages. Take the p90.
3. `chunk_tokens` = p90 + heading overhead (~20-40 tokens).

Typical landings, as a sanity check rather than a default to copy:

| Corpus | Answer span | `chunk_tokens` |
|---|---|---|
| Reference docs, API pages, FAQs | Short, one section | 150-300 |
| Prose: handbooks, policies, reports | One or two paragraphs | 300-600 |
| Narrative: contracts, legal, research | Multi-paragraph argument | 600-1000, with parent-child |
| Code | One function | By symbol, not by count |
| Transcripts | A speaker turn or three | 200-400 |
| Q&A pairs, table rows, tickets | The unit already exists | One chunk per unit — do not split |

If a number came out of this procedure, write it and the p90 it came from into `## Index Registry`; otherwise the next person re-derives it or, worse, copies 512 from somewhere.

**Why not just make chunks small.** Small chunks raise precision and destroy the context an answer needs; large chunks carry context and dilute the embedding, because one vector must represent several topics and ends up near none of them. The p90 procedure is what puts the boundary at the answer, which is the only place it is right.

## The Strategies, and When Each Wins

| Strategy | Mechanics | Wins when | Costs |
|---|---|---|---|
| Fixed-size | Split every N tokens | Never the right answer alone; acceptable only as a fallback inside a structure-aware splitter | Cuts mid-sentence, mid-table |
| Recursive structure-aware | Try separators in order: headings → paragraphs → sentences → words | Default for everything with structure | None worth naming |
| Document-element | Split on parsed elements (heading, table, list, code block) | Markdown, HTML, wiki, code | Needs a real parser (`ingestion.md`) |
| Semantic | Embed sentences, cut where consecutive similarity drops | Unstructured prose: transcripts, OCR output | An embedding pass over the whole corpus at ingestion |
| Late chunking | Embed the long document once with a long-context model, then pool token embeddings per chunk | Chunks that depend heavily on earlier context | Requires a long-context embedding model; higher ingestion cost |
| Proposition | Rewrite passages into standalone atomic statements with an LLM | High-precision QA over dense reference material | An LLM call per passage at ingestion, and a rewriting-error surface |
| Fixed unit | One chunk per row, ticket, or Q&A pair | The corpus already has the unit | — |

Default: recursive structure-aware with heading context. Everything else needs the corpus to argue for it and a paired measurement to keep it (SKILL.md Rule 9).

## Overlap Is Not Context

Overlap exists for one reason: a sentence that straddles a boundary is otherwise in neither chunk. `chunk_overlap_pct` at 10-15% of `chunk_tokens` covers that — 12% of 512 ≈ 60 tokens, about two sentences.

What overlap does not do: tell you which document the chunk is from, which section, or what "it" refers to two paragraphs earlier. Raising overlap to 30% to fix a context problem inflates the index by 30%, produces near-duplicate top-k results, and leaves the context problem intact. Fix context with enrichment, below.

Zero overlap is correct for fixed-unit chunking: a table row does not straddle anything.

## Context Enrichment

The highest-yield change in most corpora, and the one that costs the least.

- **Heading path prepended.** `Handbook > Benefits > Parental leave\n\n<chunk text>`. Costs ~20-40 tokens per chunk. Fixes the chunk that says "eligibility begins after 12 months" and never names what for.
- **Document title and date.** Cheap, and it makes temporal disambiguation possible at all.
- **Generated chunk context.** An LLM writes one or two sentences situating the chunk inside its document, prepended before embedding. The strongest version of this idea and the most expensive: one generation per chunk at ingestion, cached forever. Measure it on the golden set before paying for a full corpus — the gain is large on cross-referencing prose and near zero on self-contained reference pages.
- **Keep the enrichment out of what gets shown.** Store the enriched text as the embedded field and the original as the display field, or the assistant quotes back your synthetic sentences as if they were the source.

## Parent-Child Retrieval

Search small, generate large. Two representations of the same document:

- **Child chunks** (150-300 tokens) are embedded and searched. Small = precise.
- **Parent chunks** (the section, or the whole document) are what gets sent to the model. Large = complete.
- The child's metadata carries `parent_id`; after retrieval, dedupe parents — five children of one section must yield that section once, not five times.

Use it when the answer needs surrounding context to be usable (contracts, procedures where step 4 is meaningless without steps 1-3), and skip it when chunks are already self-contained. Cost: a second store or a second field for parents, and a dedupe step that people forget, which is why `context_k` silently collapses to two distinct sections.

## Boundaries You Never Cross

Splitting inside any of these produces a chunk that is worse than no chunk, because it retrieves confidently and misleads:

- A table, or a table's header away from its rows
- A code block, or a function away from its signature
- A numbered procedure — step 3 alone reads like the whole instruction
- A sentence, in any corpus
- A definition away from the term it defines
- A negation away from what it negates ("this does **not** apply to contractors" split from the clause it modifies is the most dangerous chunk in a policy corpus)

## Token Counting

- Count tokens with the tokenizer of the embedding model, not with a character heuristic. `chars ÷ 4` is a workable estimate for English prose and badly wrong for code, CJK text, and identifier-dense content.
- The limit that matters is the embedding model's max sequence length, not the generator's context window. Exceeding it truncates silently and returns a vector for the first N tokens (`embeddings.md`).
- Budget the enrichment prefix inside `chunk_tokens`, not on top of it, or p99 chunk length quietly crosses the model limit after heading paths are added.

## Chunk Ids and Ordering

- `chunk_id` is stable and derived from `doc_id` plus position — `kb-114#0007` — so a citation survives re-ingestion of an unchanged document and a re-parse produces the same ids.
- Keep the ordinal in metadata. It is what lets `generation.md` reassemble adjacent chunks in document order rather than in score order, and what makes "the next paragraph" retrievable.
- A stable id is also the deterministic tiebreaker for equal scores (SKILL.md Failure Signatures).

**After changing any chunk parameter**, record the new `Chunker` value in `## Index Registry` (the split-out home is `indexes.md`), run the golden set, and write the paired result to `~/Clawic/data/rag/evals/<year>.md` with the single variable that changed named in its row (`memory-template.md`). A chunking change with no eval row is a change nobody can defend or undo.
