# Structured Data — Tables, SQL, And Graphs

Vector search retrieves passages. It cannot count, sum, join, or traverse. When the question needs one of those, no chunk size fixes it — the fix is a different retriever behind a router.

**Contents:** [The Questions Vector Search Cannot Answer](#the-questions-vector-search-cannot-answer) · [Routing](#routing) · [Text-to-SQL](#text-to-sql) · [Tables Inside a Document Corpus](#tables-inside-a-document-corpus) · [Graph Retrieval](#graph-retrieval) · [Building the Graph](#building-the-graph) · [Hybrid Answers](#hybrid-answers) · [What This Costs to Maintain](#what-this-costs-to-maintain)

**Before proposing a graph or a SQL route**, read `## Corpus` in `~/Clawic/data/rag/memory.md`: whether the corpus has an entity-dense, relational core is a property of the sources already listed, and adding an extraction pipeline over a corpus that does not is the most expensive mistake on this page.

## The Questions Vector Search Cannot Answer

| Question shape | Why retrieval fails | Destination |
|---|---|---|
| "How many contracts expire in Q3" | Counting requires seeing all rows, retrieval returns `k` | SQL |
| "Total spend by vendor last year" | Aggregation over the full set | SQL |
| "Which customers have no support ticket" | Negation over a set; nothing to retrieve | SQL |
| "Highest, latest, first, top 5 by X" | Ranking by a field, not by similarity | SQL |
| "Who approved every exception signed off by Ana" | Multi-hop over relationships | Graph |
| "What depends on the payments service" | Transitive traversal | Graph |
| "Summarize the themes across all 400 reviews" | Global summarization; `k` chunks are a sample, not the corpus | Hierarchical summarization or a graph community summary |
| "What does the refund policy say" | A passage answers it | Vector retrieval |

The tell is quantifiers and relationships: *all, none, how many, total, every, which of, depends on, between*. A question containing one of them and answered from `context_k` chunks produces a number that is confidently wrong, because the model summed the five rows it was shown.

## Routing

A classifier in front of the pipeline, run before retrieval (`retrieval.md`). Three destinations is enough for most systems: SQL, graph, passages. Practical shape:

- Route with a small model given the schema summary and a handful of examples per destination, or with rules when the surface is narrow.
- Default to passages on low confidence, and say which route was taken in the answer. A user who sees "answered from the contracts table" can tell you it should have been the policy documents.
- Allow two routes for one question: "how many exceptions were approved, and what does the policy say about them" is one SQL query plus one retrieval, merged (see Hybrid Answers).
- The route is a logged field. Route-level accuracy is a separate metric from retrieval accuracy, and it is the one that explains a whole class of wrong answers (`evaluation.md`).

## Text-to-SQL

- **Give the model the schema, not the database**: table and column names, types, a one-line description per column, and 3-5 example rows per table. Example rows are what teach it that `status` holds `active | churned`, which no type declaration conveys.
- **Read-only credentials, always**, plus a statement timeout and a row limit. This is not a stylistic preference: generated SQL will eventually contain a cross join.
- **Validate before executing**: parse the SQL, reject anything that is not a `SELECT`, reject unknown tables and columns. Catching a hallucinated column at parse time is cheaper than a database error the model then tries to repair in a loop.
- **Return the query with the answer.** The SQL is the citation; a number without it is unverifiable, and `answer_policy: cite-or-refuse` applies here exactly as it does to passages (`generation.md`).
- **Repair once, then stop.** One retry with the error message attached fixes most syntax mistakes; a loop past that burns budget and converges on nonsense (`agentic.md`).
- Retrieval still helps: embed the schema documentation and retrieve the relevant tables first when the schema is too large to fit in the prompt. That is vector retrieval serving SQL, not competing with it.

## Tables Inside a Document Corpus

Most tables are not a database — they are a table in a PDF, and the question is which of the two they should be treated as.

| Situation | Treatment |
|---|---|
| Small table, questions are about its content in context | Chunk it whole, header repeated, caption prepended (`ingestion.md`) |
| Many similar tables, questions aggregate across them | Extract into a real table, route with SQL |
| Large table, questions look up one row | Chunk per row group with header repeated; add the row's key fields to metadata for filtering |
| Table whose meaning depends on surrounding prose | Chunk table plus its explanatory paragraph together |

The failure to avoid: embedding a 400-row table as ten chunks and then answering "what is the total" from the three chunks that were retrieved. Detect it by routing, not by hoping.

## Graph Retrieval

A graph stores entities as nodes and relationships as edges, so multi-hop questions become traversals instead of lucky retrievals.

- **Local retrieval**: find the entities named in the question, expand N hops, return the subgraph plus the source passages attached to those nodes. This is the version that pays for itself on relational questions.
- **Global retrieval**: cluster the graph into communities, summarize each offline, and answer corpus-wide questions from the summaries. This is what makes "what are the main themes" answerable at all — but the summarization pass runs over the whole corpus and is the expensive half.
- **Keep the passages.** Nodes and edges answer the relationship; the citation still has to point at text a human can read. A graph that discards its source passages cannot be audited.
- Hop limit is a real parameter: 2 hops usually, 3 rarely, more never — the subgraph explodes and the context fills with distant entities.

## Building the Graph

The maintenance cost lives here, and it is what the decision should be made on.

- Entity and relationship extraction is one LLM call per chunk at ingestion — the same order of cost as generated chunk context (`chunking.md`), and it must re-run for every changed document.
- **Entity resolution is the hard part**: "Ana Ruiz", "A. Ruiz" and "aruiz@" are one node or three, and three is a graph that answers nothing. Normalize aggressively, keep aliases on the node, and accept that this is where the quality ceiling sits.
- Define the schema up front — which entity types and which relation types — and constrain extraction to it. Open-ended extraction produces thousands of near-synonymous relation labels and a graph nobody can query.
- Incremental updates: deleting a document means deleting its extracted edges, which requires provenance on every edge (`doc_id`). Without it, retracted documents leave their claims in the graph forever.
- Budget the rebuild: a schema change re-extracts the corpus, at the same cost as the first pass.

## Hybrid Answers

When one question needs two routes, merge deliberately:

- Run the routes in parallel when neither depends on the other; sequentially when the SQL result determines what to retrieve ("which vendor spent most" → then retrieve that vendor's contract).
- Label each part of the context by origin — query result, passage, subgraph — so the generator can cite each correctly.
- Reconcile disagreement explicitly. When the table says 14 and the policy document says 30, the answer names both and says which is which; silently preferring one is how a RAG system loses an audit (`generation.md`).

## What This Costs to Maintain

Before adding either route, price the ongoing cost honestly:

| Route | Ingestion cost | Ongoing cost | Breaks when |
|---|---|---|---|
| SQL | Zero if the data is already relational; an ETL if not | Schema drift breaks generated queries silently | A column is renamed |
| Graph | One extraction call per chunk, plus community summarization | Re-extraction on every document change; entity resolution decay | The schema changes, or new entity types appear |
| Passages | Embedding only | Reindex on model change | The model changes |

Graph RAG earns its cost when the questions are genuinely relational and recurring. A single multi-hop question per week is answered more cheaply by decomposition over the vector index (`agentic.md`).

**After adding a route**, record the decision in `~/Clawic/data/rag/artifacts/decision-<route>-routing.md` with the question classes that justified it, the maintenance cost, and what was rejected — plus its `## Boxes` line in the same turn. Add the SQL schema source or the graph store to `## Corpus` in `memory.md` as its own row with its refresh cadence, and put a self-hosted graph or analytics node in `~/Clawic/data/servers/servers.md` (`memory-template.md`).
