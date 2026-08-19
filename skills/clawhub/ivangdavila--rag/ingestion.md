# Ingestion — Getting Documents In Without Losing Them

Nothing downstream can recover what ingestion destroyed. A chunk of whitespace embeds fine, indexes fine, and never matches anything.

**Contents:** [The Assertions That Catch Silent Loss](#the-assertions-that-catch-silent-loss) · [Parser by Document Class](#parser-by-document-class) · [PDFs](#pdfs) · [Tables](#tables) · [HTML and Wiki Exports](#html-and-wiki-exports) · [Code](#code) · [Transcripts and Email Threads](#transcripts-and-email-threads) · [Metadata Schema](#metadata-schema) · [Deduplication](#deduplication) · [Batch and Rate Limits](#batch-and-rate-limits)

**Before ingesting a new source**, read `## Corpus` in `~/Clawic/data/rag/memory.md` — or `corpus.md` if the `## Boxes` index points there. A source already listed has a parser, an access field and a refresh cadence that were decided once; re-deciding them produces two incompatible ingestion paths over the same documents.

## The Assertions That Catch Silent Loss

Ingestion fails quietly. Four assertions catch nearly all of it, and each one is cheap:

| Assertion | Catches | Threshold |
|---|---|---|
| Extracted characters per page | Scanned PDFs, failed parsers, encrypted files | <20 chars/page → route to OCR, do not chunk |
| Chunks produced per document | Documents that parsed to nothing | 0 chunks on a non-empty file = hard error, not a warning |
| Indexed count vs expected chunk count | Per-item errors inside batch upserts | Any gap = read the per-item error array |
| Token-length distribution of chunks | Splitter misconfiguration, one giant unsplit blob | p99 above the embedding model's max sequence length = silent truncation |

The fourth one matters most, because it is the only failure that produces a valid-looking vector. Model max lengths differ by an order of magnitude — check yours before trusting a splitter's defaults (`embeddings.md`).

## Parser by Document Class

One default per class; switch only on the stated condition.

| Class | Default | Switch when |
|---|---|---|
| Digital PDF | A layout-aware text extractor (PyMuPDF-class) | Multi-column, forms, or tables that matter (→ a layout model) |
| Scanned PDF or image | OCR at 300 dpi with layout retention | Handwriting (→ route to a human; OCR accuracy on handwriting is not production-grade) |
| HTML | A boilerplate-removing extractor (Trafilatura-class) | The page is an app shell rendered by JS (→ headless render first) |
| Markdown | Parse the AST, keep the heading tree | — |
| Word / ODT | Native parser, keep heading styles as structure | — |
| Spreadsheet | Row-to-sentence rendering, header repeated per row | The sheet is a real database (→ `structured-data.md`, do not embed it) |
| Slides | Text plus per-slide image caption | The content lives in the diagrams (→ `multimodal.md`) |
| Code | Language-aware split by symbol | Documentation strings are the target (→ extract docstrings as prose) |
| Email / chat | Thread reconstruction, quoted-reply stripping | — |
| Anything else | Extract text, assert non-empty, chunk structure-aware | — |

## PDFs

The format that eats the most ingestion time, for three reasons that have three different fixes.

- **No text layer.** Pure image. Detect with the characters-per-page assertion; OCR at 300 dpi — below 200 dpi accuracy falls off, above 400 you pay time for nothing.
- **Multi-column layout.** Naive extraction reads across columns and interleaves two sentences into nonsense that is fluent enough to survive review. Layout-aware extraction, or detect column count from the x-coordinate histogram of text blocks.
- **Header/footer noise.** Repeated on every page, it dominates short chunks and makes hundreds of chunks look similar to each other. Strip lines that appear on more than ~70% of pages in the same y-band.

Page numbers are metadata, not content: keep `page` in the chunk metadata so citations can point at it, and keep it out of the embedded text where it adds a number the model must ignore.

## Tables

A table flattened to prose loses the column-to-value binding, and that binding is the answer to every question worth asking about it.

- **Small tables (fits in one chunk)**: render as Markdown, repeat the header row, prepend the caption and the section heading. One chunk, self-contained.
- **Long tables**: one chunk per row group, header row repeated in every chunk. A row without its header is an unlabeled list of numbers.
- **Tables that are really a dataset** (hundreds of rows, aggregation questions): do not embed them. Load them into a queryable store and route (`structured-data.md`). Vector search cannot compute a sum, and no chunk size fixes that.
- Never split a table across a chunk boundary (SKILL.md Rule 4). If the splitter is character-based, it will; use a structure-aware splitter or pre-extract tables as units.

## HTML and Wiki Exports

- Boilerplate — nav, footer, cookie banner, sidebar — is the single largest source of near-duplicate chunks in a wiki corpus. Strip before chunking, not after.
- Keep the heading hierarchy: it becomes the heading path prepended to each chunk (`chunking.md`), and it is the cheapest context enrichment available.
- Anchors and permalinks belong in metadata as `source_uri` with the fragment, so a citation lands on the section rather than the page.
- Wiki exports often carry a `redirect` or `archived` flag. Filter archived content at ingestion or accept that the assistant will quote deprecated policy.

## Code

- Split by symbol — function, class, method — never by line count. A half function retrieves as confidently as a whole one and answers nothing.
- Prepend the file path and the enclosing symbol chain: `src/auth/session.py :: SessionStore.refresh`. Path is often the strongest retrieval signal in a code corpus.
- Index docstrings and comments with their symbol, not separately: the question is asked in prose, the answer lives in the code, and only the pair contains both vocabularies.
- Generated files, vendored dependencies, lockfiles and minified bundles are corpus poison — exclude by path pattern at ingestion, or they will dominate every top-k by sheer volume.

## Transcripts and Email Threads

- Transcripts have no structure and no punctuation reliability. Split by speaker turn, then merge turns until `chunk_tokens`, keeping the speaker label in the text so "she said the deadline moved" stays attributable.
- Timestamps go in metadata, and one per chunk, so a temporal filter is possible later.
- Email threads: reconstruct the thread, strip quoted replies before chunking (otherwise the same paragraph is indexed once per reply), and keep participants in metadata as a filter field.
- Meeting transcripts are the corpus where semantic chunking earns its cost, because there is no structure to be aware of (`chunking.md`).

## Metadata Schema

Decided once, at ingestion, because adding a field later skips every chunk indexed before it existed (SKILL.md Trap table). The minimum that keeps future operations possible:

| Field | Why it is mandatory |
|---|---|
| `doc_id` | The unit of deletion and of re-ingestion (SKILL.md Rule 8) |
| `chunk_id` | Citation target, and the tiebreaker that makes ranking deterministic |
| `source_uri` | Where a human goes to verify the answer |
| `source_version` | Content hash; incremental sync compares this and nothing else |
| `ingested_at` | Distinguishes "not in the corpus" from "not yet ingested" |
| Access field | Whatever the source system uses for permissions — `team`, `space`, `classification` (`security.md`) |
| Temporal field | Document date, when the corpus has any notion of currency |

Field names are a `conventions` preference: record the user's scheme in `config.yaml` and use it everywhere rather than mixing `doc_id` and `source_id` across pipelines.

## Deduplication

Near-duplicates crowd the top-k and make a good retriever look broken — five results, one fact.

- Exact duplicates: hash the normalized text, drop at ingestion.
- Near duplicates (a page republished with a new date, a boilerplate-heavy wiki): MinHash or SimHash with a similarity threshold, decided by inspecting the borderline pairs in this corpus rather than by copying a number.
- Legitimate duplicates that must all stay (the same clause across ten contracts): keep them and handle diversity at query time with MMR (`retrieval.md`), because the answer depends on which contract was asked about.

## Batch and Rate Limits

- Batch embedding calls at 100-500 inputs per request: below that the per-request overhead dominates, above it a single failure re-costs the whole batch.
- Retry with exponential backoff and jitter on 429 and 5xx. A fixed-interval retry from a parallel ingestion job synchronizes into a thundering herd.
- Checkpoint by `doc_id` after each batch. A four-hour ingestion that dies at hour three and restarts from zero is how ingestion budgets get spent twice.
- Order matters for deletes: delete by `doc_id` before upserting the re-parsed version, never after — the window between them is when both versions are live (SKILL.md Rule 8).

**After ingesting or re-parsing a source**, write its row to `## Corpus` in `~/Clawic/data/rag/memory.md` — source, format, document count, refresh cadence, owner, access field — and, when the parser settings took real work to find, save them as `~/Clawic/data/rag/artifacts/ingest-<source>.md` with what was rejected, adding its `## Boxes` line in the same turn (`memory-template.md`). The next hostile PDF from the same source should cost minutes, not an afternoon.
