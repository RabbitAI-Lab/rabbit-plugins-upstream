# Multimodal — When The Answer Is In A Picture

A diagram, a chart, a scanned form, a slide. Text extraction returns the caption and loses the content, and the pipeline reports success.

**Contents:** [Decide What the Image Is](#decide-what-the-image-is) · [Caption-and-Index](#caption-and-index) · [Native Multimodal Embeddings](#native-multimodal-embeddings) · [Document-Screenshot Retrieval](#document-screenshot-retrieval) · [Charts](#charts) · [Scans and Forms](#scans-and-forms) · [Slides](#slides) · [Audio and Video](#audio-and-video) · [Citations for Non-Text](#citations-for-non-text) · [Cost and Latency](#cost-and-latency)

**Before building a multimodal path**, read `## Corpus` in `~/Clawic/data/rag/memory.md`: the fraction of documents whose answer actually lives in an image decides whether this is a pipeline or a special case for twelve files.

## Decide What the Image Is

Four categories, four different pipelines. Getting this classification right is most of the work.

| Category | Answer lives in | Pipeline |
|---|---|---|
| Decorative | Nowhere | Skip it; indexing stock photos adds noise |
| Text-as-image (scan, screenshot of a document) | The text | OCR, then the normal text pipeline (`ingestion.md`) |
| Data visualization (chart, table image) | The values and the trend | Structured description, and the underlying data when available |
| Diagram or schematic | The relationships | Generated description plus surrounding prose |

Classify at ingestion with a cheap vision call or with heuristics (aspect ratio, text density, file origin), and record the category in metadata. It is what lets you re-run one category later without reprocessing the corpus.

## Caption-and-Index

The default approach, and it survives most requirements: a vision model writes a text description of each image, that description is embedded and indexed like any other chunk, and the image is stored by reference.

- **Describe for retrieval, not for prose.** The prompt should ask for the entities, values, axis labels, relationships and any text visible in the image — not an aesthetic caption. "A bar chart showing quarterly revenue" retrieves nothing; "Bar chart, quarterly revenue 2025: Q1 1.2M, Q2 1.4M, Q3 1.1M, Q4 1.9M, EUR, source finance" retrieves the question that asks about Q3.
- **Include the surrounding text** in the description prompt. The paragraph that introduces a figure usually names what the figure means, and the description is far better with it.
- **Keep the image reference** in metadata so the answer can show it. A described image that cannot be displayed halves its own value.
- Cost: one vision call per image at ingestion, cached forever. This is the cheap approach precisely because it moves all the cost to ingestion.

## Native Multimodal Embeddings

A model that places images and text in one vector space, so a text query retrieves an image directly.

- Works well for "find the picture of X" retrieval over photo-like content, and poorly for dense information graphics, where the vector cannot represent the values.
- The fingerprint discipline applies unchanged: model, version, dimension, normalization, metric (`embeddings.md`). Mixed-modality indexes are still one index with one fingerprint.
- Mixing described-text vectors and native image vectors in one index means comparing scores from two different distributions. Keep them in separate legs and fuse by rank (`retrieval.md`).

Default: caption-and-index. Reach for native multimodal when the corpus is genuinely visual and queries are visual.

## Document-Screenshot Retrieval

Embedding a rendered page image directly, skipping parsing entirely (the ColPali-style approach). It preserves layout, tables and figures without an extraction pipeline, which is exactly what breaks in `ingestion.md`.

- Strong on layout-heavy documents where parsing loses the structure: forms, financial statements, technical datasheets.
- Costs: a page-level vector store that is much larger per document (late-interaction storage, `embeddings.md`), and a generator that must accept page images in the context.
- Retrieval granularity is the page, not the passage, so the context budget fills fast — `context_k` of 3-5 pages is a lot of tokens (`generation.md`).
- Consider it when the parsing pipeline has already failed on the corpus twice; not as a first move.

## Charts

The category where text extraction is most confidently wrong, because the caption exists and says nothing.

- Ask the vision model for the values as a table, and index that table as text. A chart converted to `Q1 1.2M, Q2 1.4M` is answerable; a chart described as "shows growth" is not.
- **The underlying data usually exists** — a spreadsheet, a query, a source file. Indexing the source beats describing the picture every time, and it also makes aggregation possible (`structured-data.md`).
- Vision models misread axis scales, log scales, and stacked series. For anything a decision depends on, verify the extracted numbers against a source before indexing them, or mark the description as model-extracted so the generator can hedge.

## Scans and Forms

- OCR first, with layout retention (`ingestion.md`). A form's meaning is in the field-to-value binding, which reading order destroys.
- Key-value extraction beats free-text OCR for forms: index `invoice_total: 1420 EUR` as metadata plus text, so it is filterable as well as searchable.
- Low-confidence OCR regions should be marked, not silently included. A misread digit in an invoice total is a wrong answer with a citation.
- Handwriting is not production-grade. Route it to a human queue and record the gap in `## Corpus` rather than pretending coverage.

## Slides

- One chunk per slide, with the deck title and the slide title prepended. Slide bodies are fragments and depend entirely on that header.
- Speaker notes are often the real content and are frequently dropped by parsers. Check for them explicitly.
- Diagram-heavy slides need the image description path; text-heavy slides do not. Classify per slide, not per deck.
- Decks are typically superseded rather than updated — keep the deck date and prefer status filtering over recency boosting (`retrieval.md`).

## Audio and Video

- Transcribe, then treat as a transcript: split by speaker turn, keep timestamps in metadata (`ingestion.md`).
- Keep the timestamp on every chunk so a citation can link to the moment. A citation to a two-hour recording without a timestamp is not a citation.
- For video where the visual channel matters — a screen recording, a demo — sample keyframes and describe them, aligned to the transcript by timestamp. Do not sample uniformly at a fixed interval on slide-based video; detect changes instead, or you index the same slide forty times.
- Diarization errors propagate into attribution errors. If who said it matters, verify speaker labels on a sample before trusting them.

## Citations for Non-Text

- Cite the image by `chunk_id` like anything else, and render it in the answer when the surface allows. Seeing the figure is what lets a human verify a claim about a figure.
- Make the provenance of the description visible: an answer derived from a model-written description is one inference further from the source than an answer derived from text, and the answer should say so when the number matters.
- Keep the image's page and coordinates in metadata when available, so a citation can point at the region rather than the document.

## Cost and Latency

- Vision calls at ingestion are the dominant cost of every approach here, and they are one-off per image. Estimate it as `images × price_per_vision_call` and put the figure in the design (`costs.md`).
- Re-describing the corpus is a reindex trigger: a better description prompt is as expensive as a model change.
- Query-time vision — sending page images to the generator — is a per-query cost that recurs forever. Prefer moving cost to ingestion whenever the retrieval quality is comparable.

**After building a multimodal path**, add the image-bearing sources to `## Corpus` in `~/Clawic/data/rag/memory.md` with their category and the description model used, record the description prompt in `~/Clawic/data/rag/artifacts/prompt-image-description.md` with its `## Boxes` line, and write the vision-call cost estimate with its date into the same artifact (`memory-template.md`). A description prompt that changes silently invalidates every image chunk in the index.
