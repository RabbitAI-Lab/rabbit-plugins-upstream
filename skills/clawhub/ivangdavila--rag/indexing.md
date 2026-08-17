# Indexing — The Vector Store, Its Parameters, And Its Filters

An ANN index trades recall for speed on purpose. Every parameter below moves that trade, and the default settings of every store choose speed.

**Contents:** [Choosing a Store](#choosing-a-store) · [HNSW Parameters](#hnsw-parameters) · [IVF and pgvector](#ivf-and-pgvector) · [Quantization](#quantization) · [Filtering — The Failure That Returns Zero](#filtering--the-failure-that-returns-zero) · [Metadata and Payload Design](#metadata-and-payload-design) · [Multi-Tenancy at the Index Level](#multi-tenancy-at-the-index-level) · [Capacity Planning](#capacity-planning) · [Index Build and Rebuild](#index-build-and-rebuild) · [Measuring Recall Against Exact Search](#measuring-recall-against-exact-search)

**Before proposing a store or an index parameter**, read `## Index Registry` in `~/Clawic/data/rag/memory.md` for what already exists, and `~/Clawic/data/servers/servers.md` when the store is self-hosted — the box it runs on decides the memory ceiling that decides everything on this page.

## Choosing a Store

Decide by the constraint that binds first, not by feature list.

| Constraint | Choice |
|---|---|
| The data already lives in Postgres and the corpus is under a few million vectors | pgvector — one system, transactional deletes, SQL filters that actually pre-filter |
| Filtered search dominates and filters are selective | A store with filtered-graph search (Qdrant-class); post-filtering stores will disappoint |
| Full-text and vector must be one query, plus mature ops | Elasticsearch or OpenSearch (`elasticsearch`) |
| Zero-ops and elastic scale matter more than cost | A managed service; price it monthly and add its row to `~/Clawic/data/finances/subscriptions.md` |
| Local prototyping, thousands of vectors | An embedded store; migrate before it becomes production by accident |
| Above ~100M vectors, or GPU-accelerated build required | A distributed store built for it (Milvus-class) |
| Anything else | pgvector until a measured limit forces a move |

The migration cost between stores is one reindex, which is real but bounded. The migration cost of a wrong embedding model is the same reindex, so store choice deserves less agonizing than model choice (`embeddings.md`).

## HNSW Parameters

Three parameters, two of which are fixed at build time.

| Parameter | What it does | Typical | Cost of raising |
|---|---|---|---|
| `M` | Edges per node; graph connectivity | 16 (32-64 for high-dim or high-recall needs) | Memory: `8 × M` bytes per vector, and slower build |
| `ef_construction` | Candidate list during build | 100-200 | Build time, roughly linearly; no query cost |
| `ef_search` | Candidate list at query time | ≥ `k`, commonly 2-4× `k` | Query latency, roughly linearly |

Consequences that decide designs:

- `ef_search < k` cannot return `k` good results, and some stores silently return fewer or worse. It is the first thing to check when recall looks impossible.
- `M` and `ef_construction` are baked into the graph. Changing them is a rebuild, so pick them for the recall target you will need in a year, not the one you need in the demo.
- Recall is not a setting; it is measured (see the last section). A store reporting "99% recall" is quoting a benchmark on someone else's distribution.

## IVF and pgvector

IVF partitions the space into lists and searches only the nearest few. Cheaper to build than HNSW, worse recall at the same speed, and sensitive to the data being there when the index is built.

- pgvector ivfflat: `lists = rows ÷ 1000` up to 1M rows, `sqrt(rows)` above; `probes ≈ sqrt(lists)`. 500k rows → 500 lists, ~22 probes.
- **Build the ivfflat index after loading data**, never before: the clustering is computed from the rows present at build time, and an index built on an empty table partitions nothing.
- pgvector HNSW builds are memory-hungry; raise `maintenance_work_mem` for the session or the build spills to disk and takes hours instead of minutes.
- With pgvector, a `WHERE` clause on an indexed column is a genuine pre-filter — this is its main advantage over stores that post-filter, and the reason it survives longer than its raw benchmark numbers suggest.

## Quantization

| Method | Size | Recall impact | When |
|---|---|---|---|
| float32 | `4 × dims` bytes/vector | Baseline | Under a few million vectors, when RAM is not the constraint |
| Scalar int8 | ÷4 | Small, measurable | The default first lever when memory binds |
| Product quantization | ÷8 to ÷32 | Moderate, tunable | Very large corpora with a rescoring stage |
| Binary | ÷32 | Large without rescoring | Only with oversampling plus a rescore against full vectors |

The pattern that makes aggressive quantization safe: retrieve `k × 3` to `k × 5` candidates from the quantized index, then rescore those candidates against full-precision vectors kept on disk. Cheap, and it recovers most of the loss. Quote the memory saving and the measured recall together or the saving is not a result.

## Filtering — The Failure That Returns Zero

Three implementations wear the same API and behave completely differently:

- **Post-filter**: ANN returns `k`, the filter discards non-matching hits. A filter matching 5% of the corpus returns roughly 5% of `k`, and a selective filter returns nothing while thousands of matching documents exist. This is the cause behind the "filter empties the result set" signature.
- **Pre-filter (exact)**: candidates are restricted before the search. Correct, and it degrades to a brute-force scan when the filtered subset is large.
- **Filtered graph traversal**: the ANN walk itself only visits matching nodes. Best of both; not every store has it.

Rules:

- Know which one your store does before designing around filters. Read its documentation, then verify with a deliberately selective filter and count the results.
- With post-filtering only, over-fetch by `k / selectivity` and treat the multiplier as a latency and cost line (SKILL.md Rule 6).
- Filter fields must be indexed in the store's payload index, or the pre-filter becomes a scan.
- Low-cardinality filters (`tenant`, `language`) are cheap; high-cardinality ones (`doc_id IN [...]` with thousands of ids) push the whole query toward brute force and belong in a partitioning decision instead.

## Metadata and Payload Design

- Store only what is filtered on, cited, or displayed. Payload size multiplies the memory footprint that the vector calculation already made expensive.
- Index the filter fields explicitly; most stores do not index payload by default.
- Keep chunk text out of the vector store when a system of record already holds it, and fetch by `chunk_id` for display — unless the extra hop breaks the latency budget, which for most stacks it does not.
- Timestamps stored as numbers are range-filterable; stored as strings they are not.
- A field added after indexing does not exist on older chunks. Backfill in the same operation or reindex; then assert field coverage as a count query, because the failure is invisible until a user with the wrong permissions sees nothing (`security.md`).

## Multi-Tenancy at the Index Level

| Approach | Isolation | Cost | Use when |
|---|---|---|---|
| Collection or index per tenant | Strong: cross-tenant leakage requires querying the wrong collection | Per-collection overhead; painful past thousands of tenants | Few, large tenants; regulated data |
| Namespace / partition per tenant | Strong in stores that implement it as a hard partition | Low | The default when the store supports it |
| Metadata filter on a shared index | Only as strong as the filter code, tested | Lowest | Many small tenants, with an automated isolation test in CI |

Whichever is chosen, the isolation test is not optional: a suite that queries as tenant A for content known to exist only in tenant B, and fails the build on a single hit (`security.md`).

## Capacity Planning

Compute before choosing, not after the box runs out of RAM.

- Vectors: `n × 4 × dims` bytes. Graph: `n × 8 × M` bytes. 1M vectors at 1536 dims, M=16 → ~6.3 GB before payload.
- Add payload, and add the store's own overhead — plan the box at roughly 1.5× the computed figure and verify against the store's documented factor.
- HNSW wants the graph resident in memory. A store that swaps turns a 20 ms query into a disk-bound one, and the symptom presents as "the vector database got slow" rather than as memory pressure.
- Replicas multiply the memory bill by the replica count, not the storage bill only.
- The growth curve matters more than today's number: `chunks_per_month × months` decides whether you are choosing a store for now or for the migration in eight months.

## Index Build and Rebuild

- Build once, after the data is loaded — for IVF this is correctness, for HNSW it is speed.
- Rebuild triggers: embedding model or version change, dimension change, distance metric change, chunker change, quantization change. All of them are fingerprint fields (`embeddings.md`).
- Never rebuild in place on a live index. Build the new one alongside, verify on the golden set, repoint, keep the old one until the next eval cycle passes (`production.md`).
- Deletes in most ANN indexes are tombstones: space is not reclaimed and recall degrades slowly as tombstones accumulate. Schedule a compaction or rebuild cadence in the `## Due` table for any corpus with regular deletions.

## Measuring Recall Against Exact Search

The only honest way to know what the index costs you:

1. Sample 200-500 queries from the golden set or production logs.
2. Run each with exact/brute-force search to get the true top-`k`. Most stores expose an exact mode; a full scan on a sample of the corpus works too.
3. Run each against the ANN index with production parameters.
4. Recall = mean overlap of the two top-`k` sets.

Below ~0.95 against exact, raise `ef_search` first (query-time, free to try), then `M` (rebuild). Report ANN recall separately from retrieval recall on the golden set: the first is what the index loses, the second is what the whole pipeline loses, and conflating them sends people to tune the wrong stage.

**After building, resizing, repointing or retiring an index**, write its row to `## Index Registry` in `~/Clawic/data/rag/memory.md` — store, index parameters, quantization, chunk count, build date — and put the ANN-vs-exact recall figure in the same row's notes (`memory-template.md`). A self-hosted store node goes to `~/Clawic/data/servers/servers.md`, one row per host, identified by `Name` + `Provider`, retired by deleting the row and dating it in `memory.md`.
