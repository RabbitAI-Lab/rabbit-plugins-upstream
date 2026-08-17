# Embeddings — Choosing The Model And Matching It Forever

The embedding model is the one decision that cannot be changed without rebuilding everything. Choose it with the reindex cost already priced in.

**Contents:** [The Six Fingerprint Fields](#the-six-fingerprint-fields) · [Asymmetric Models and Prefixes](#asymmetric-models-and-prefixes) · [Max Sequence Length](#max-sequence-length) · [Choosing a Model](#choosing-a-model) · [Dimensions and Matryoshka Truncation](#dimensions-and-matryoshka-truncation) · [Normalization and Distance Metric](#normalization-and-distance-metric) · [Multilingual and Domain Corpora](#multilingual-and-domain-corpora) · [Fine-Tuning](#fine-tuning) · [Self-Hosting](#self-hosting) · [Sparse and Late-Interaction Alternatives](#sparse-and-late-interaction-alternatives)

**Before writing any query-side embedding call**, read `## Index Registry` in `~/Clawic/data/rag/memory.md` and match all six fields below. This is the single most expensive mistake in the domain because it produces no error at all.

## The Six Fingerprint Fields

| Field | Failure when it differs between index and query |
|---|---|
| Model id | Vectors from two models are unrelated points in unrelated spaces; results look random but plausible |
| Model version | Providers update models behind a stable name; a re-embedded query lands elsewhere than the year-old index |
| Output dimension | Hard error if the store enforces it, silent garbage if a truncation is applied on one side only |
| Normalization | Cosine and dot rank identically only on normalized vectors; mixing them reorders by magnitude, which encodes length, not relevance |
| Instruction prefix | Documented below; the most commonly missed field |
| Distance metric | An index built for cosine and queried with L2 returns a different neighborhood |

Record all six at build time in `## Index Registry` in `~/Clawic/data/rag/memory.md`. When any of them changes, the correct operation is a new index and a migration, not an update (`production.md`).

## Asymmetric Models and Prefixes

Some models are trained so that queries and documents are encoded differently. Using the same call for both is not an error and is not free.

| Family | Query side | Document side |
|---|---|---|
| E5 | `query: ` prefix | `passage: ` prefix |
| BGE (English) | An instruction prefix on the query only | No prefix |
| Instruction-tuned generalists | A task instruction on the query | Usually none |
| OpenAI text-embedding-3 | None | None |

Rules: prefixes are part of the fingerprint, so record the exact string; never prepend a query prefix to documents at ingestion; and if a model's card does not mention prefixes, do not invent one. The observable when this is wrong is a modest, uniform ranking degradation with no error and no obvious symptom — which is why it gets shipped.

## Max Sequence Length

The limit that truncates without telling you. Many open sentence-transformer models cap at 512 tokens; hosted models are typically far longer. Two consequences:

- A 900-token chunk sent to a 512-token model produces a vector for the first 512 tokens. The rest of the chunk is not searchable and nothing indicates it.
- `chunk_tokens` must sit under the model's limit *after* the enrichment prefix is added (`chunking.md`). Assert on the p99 of the chunk token distribution, not the mean.

Long context in an embedding model is not a substitute for chunking: a single vector over 8k tokens averages away the specific passage that answers the question. Long-context embedding models earn their keep with late chunking, not with giant chunks.

## Choosing a Model

Decide in this order; stop at the first constraint that binds.

1. **Can the data leave the perimeter?** No → self-hosted, and the list shortens to open models.
2. **What is the corpus language?** Non-English or mixed → a multilingual model, not an English model with translated queries.
3. **Max sequence length ≥ p99 chunk length?** Eliminates models before quality is ever discussed.
4. **Prefix and normalization requirements** — recordable and honored by both sides of the pipeline?
5. **Dimension** — memory and store cost scale linearly with it (SKILL.md Sizing formulas).
6. **Quality on this corpus**, measured on the golden set. Public leaderboards rank general-domain performance and routinely invert on a specific corpus, which is why this step is last and local.

Rejecting a model at step 3 for a hard reason is worth more than an hour of leaderboard reading.

## Dimensions and Matryoshka Truncation

- Memory scales linearly with dimension: `n × 4 × dims` bytes for the vectors alone. Halving the dimension halves the RAM bill and roughly halves ANN comparison cost.
- Matryoshka-trained models (the text-embedding-3 family among them) allow truncating the vector to a shorter prefix with graceful quality loss — unlike ordinary models, where slicing destroys the space.
- **Renormalize after truncating.** A truncated vector is no longer unit length, and cosine on unnormalized vectors ranks partly by magnitude.
- The truncated dimension is a fingerprint field. Index at 768 and query at 1536 and the store either errors or, worse, pads.
- Test the truncation on the golden set before adopting it: the loss is small on average and not uniform across query types.

## Normalization and Distance Metric

- Normalize to unit length at ingestion and at query time, on both sides, always. Then cosine and dot product rank identically and the choice stops mattering.
- Without normalization, dot product favors long vectors, and vector magnitude correlates with text length in most models — so the retriever develops a preference for long chunks that no one asked for.
- Euclidean (L2) on normalized vectors is monotonic with cosine, so ranking is identical; scores are not, and any threshold copied across metrics is meaningless.
- Score scales are model-specific. A cosine of 0.78 is excellent in one space and below the random-pair baseline in another. Calibrate every threshold against random pairs drawn from your own corpus (`evaluation.md`).

## Multilingual and Domain Corpora

- Multilingual models place translations near each other, which is the point — a Spanish query retrieving an English document is a feature in a mixed corpus and a bug in a corpus where language is a filter. Decide which, and put language in metadata either way.
- Cross-lingual quality is not uniform across the language list. Measure on the languages actually present, not on the model's advertised count.
- Domain vocabulary — chemical names, part numbers, legal citations, medical codes — is where general models are weakest and where a BM25 leg recovers most of the gap for free (SKILL.md Rule 5). Try hybrid before fine-tuning.

## Fine-Tuning

Worth it under three conditions together: domain vocabulary a general model never saw, at least a few thousand labeled query-passage pairs, and a measured ceiling that hybrid plus reranking did not reach. Below that bar, a reranker buys more precision per hour (`reranking.md`).

- Training pairs come from production logs: query, clicked or verified passage as positive, a hard negative mined from the current retriever's top-k that is not the answer. Random negatives teach almost nothing.
- Fine-tuning creates a new model version and therefore a full reindex, plus the obligation to re-embed every future document with the same checkpoint. Version and store the checkpoint reference — a fine-tuned index whose weights are lost is unmaintainable.
- Evaluate against the base model on the same golden set, paired (SKILL.md Rule 9).

## Self-Hosting

- Throughput on a single mid-range GPU runs in the low thousands of short texts per second for small models and drops by roughly an order of magnitude for large ones with long inputs. Measure yours before promising a reindex window (`costs.md`).
- Batch size is the main throughput lever; sequence length is the main cost driver, because attention cost grows faster than linearly with length.
- Pin the model revision by content hash. "Latest" on a model hub is a model change and therefore a reindex trigger.
- CPU-only inference is viable for small models and low volume; it is not viable for a first full-corpus ingestion of any size.
- The box that runs it is a host: it belongs in the shared server inventory, not in a note.

## Sparse and Late-Interaction Alternatives

- **BM25** is not a lesser embedding, it is a different failure profile: exact and lexical where dense is semantic. Hybrid is the default for that reason (`retrieval.md`).
- **Learned sparse** (SPLADE-family) expands terms into a sparse vector and often beats BM25 on the same lexical ground, at the cost of an inference pass at ingestion and a store that indexes sparse vectors.
- **Late interaction** (ColBERT-family) stores one vector per token and scores by maximum similarity per query term. Retrieval quality is strong; storage is the objection — per-token vectors multiply index size by roughly the token count of a chunk, which turns a 6 GB index into a capacity project.

**After building or repointing an index**, write its row to `## Index Registry` in `~/Clawic/data/rag/memory.md` with all six fingerprint fields, the chunker, the chunk count and the build date; the previous row gets a retirement date rather than being edited (`memory-template.md`). A self-hosted embedding server goes to `~/Clawic/data/servers/servers.md` as one row, identified by `Name` + `Provider`, with its monthly cost carrying its currency.
