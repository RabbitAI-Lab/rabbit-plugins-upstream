# Streaming — Documents Bigger Than Memory

The decision is arithmetic, not taste: parsing materializes the whole document at 3-10× its byte size in maps and dictionaries (1-3× into typed structs). Above ~10% of free RAM, stream (Rule 6).

**Before processing a known feed**, read its `## Producers` row in `~/Clawic/data/json/memory.md`: the measured size, record count and parse ratio are the inputs to this decision, and somebody already paid to learn them.

**Contents:** [Measure the Ratio Once](#measure-the-ratio-once) · [Hard Ceilings](#hard-ceilings) · [NDJSON](#ndjson) · [Converting Between Array and NDJSON](#converting-between-array-and-ndjson) · [Streaming Parsers by Stack](#streaming-parsers-by-stack) · [Chunking and Resuming](#chunking-and-resuming) · [Streaming Output](#streaming-output) · [Over HTTP](#over-http) · [Operations Bigger Than Memory](#operations-bigger-than-memory)

## Measure the Ratio Once

Do not guess the multiplier — it varies by 3× across stacks and by shape (many small keys inflate more than long strings).

1. Take a 1% slice at record boundaries.
2. Parse it, measure resident memory before and after, divide by the slice's byte size.
3. Multiply by the full file size. Compare against free RAM, not total RAM.
4. Record the ratio in `## Producers` with the sample size (`memory-template.md`). It is stable for that producer's shape and saves the measurement forever.

Threshold: `expected_peak = file_bytes × ratio`. Stream when `expected_peak > 0.1 × free_bytes`, because the parse peak is not the only allocation in the process — the transform, the output buffer, and the runtime all want room, and a garbage collector needs headroom to avoid thrashing.

## Hard Ceilings

Limits that make "just parse it" impossible regardless of RAM:

| Ceiling | Value | Consequence |
|---|---|---|
| V8 maximum string length | ~512 MB (0x1fffffe8 chars) | `readFile` then `JSON.parse` throws before parsing starts; there is no flag |
| Python default recursion limit | ~1000 frames | Deep nesting raises `RecursionError` in the pure-Python decoder path |
| PHP `json_decode` depth | 512 by default | Fails with a depth error, which is at least a clear message |
| Go decoder | No document size limit; depth limited internally | Will happily consume all RAM — impose your own limit (`security.md`) |
| A single array element | Whatever one record costs | Streaming helps only if the *records* are small; one 2 GB record streams no better than a 2 GB file |

## NDJSON

One JSON value per line, `\n` separated, no raw newlines inside values (they must be escaped anyway). Media type `application/x-ndjson`.

Why it wins for anything record-shaped and large:

- **Constant memory**: one record at a time, whatever the file size.
- **Appendable**: adding records is a file append, no rewriting a closing `]`.
- **Resumable**: line N is a checkpoint; a crash costs one record.
- **Splittable**: any line boundary is a safe split, so parallel processing is trivial.
- **Greppable**: standard line tools work, which matters at 3am.
- **Recoverable**: one corrupt line loses one record; one corrupt byte in a 2 GB array loses the file.

Rules for producing it: compact each record (no pretty printing — an indented record spans lines and destroys the format), write `\n` not `\r\n` (`encoding.md`), always write a trailing newline, and never emit a blank line. Rules for consuming it: tolerate a missing final newline, skip blank lines, and report the line number on failure.

The one weakness: there is no closing delimiter, so a truncated file looks like a complete one. Producers should write a sibling marker or a final record with a count; consumers should verify it.

## Converting Between Array and NDJSON

- Array file to NDJSON: stream the array's elements and emit each compactly on its own line — with jq, `jq -c '.[]'`, which streams the input rather than materializing it whole.
- NDJSON to array: wrap and join with commas; `jq -s '.'` slurps, which materializes everything and is exactly what you were avoiding, so only do it for small inputs.
- A file that is *sometimes* an array and *sometimes* NDJSON is a producer bug: detect by the first non-whitespace byte (`[` = array) and handle both, then write it as a quirk in its `## Producers` row.
- Nested extraction: `jq -c '.data.items[]'` gets records out of a wrapper object without loading the wrapper's siblings — as long as the tool streams; `--stream` mode forces it when it does not (`querying.md`).

## Streaming Parsers by Stack

| Stack | Approach |
|---|---|
| Python | `ijson.items(f, 'data.item')` yields each matching object without materializing the parent; for NDJSON, plain iteration plus `json.loads` per line is faster and simpler |
| Node | Read as a stream and parse per line for NDJSON; for a single huge array, an event-based parser (`stream-json` family) that emits objects at a selected path |
| Go | `json.Decoder` in a loop: `dec.Token()` to step past the opening bracket, then `dec.Decode(&rec)` per element — decodes a stream of concatenated values, so it handles NDJSON unchanged |
| Java | Jackson's `JsonParser` token stream, or `ObjectMapper.readerFor(X.class).readValues(input)` for a document sequence |
| Rust | `serde_json::Deserializer::from_reader(r).into_iter::<T>()` for concatenated values |
| Shell | Line tools for NDJSON; for arrays, a streaming JSON tool — never `sed`, never a `,`-split (Traps in SKILL.md) |

The general shape is identical everywhere: **advance to the array, decode one element, process it, discard it.** Holding every decoded record in a list to "process at the end" reintroduces the memory problem you just solved.

## Chunking and Resuming

- Split at **record boundaries only**. Byte splits cut strings and produce two invalid halves plus one plausible-looking corrupt record.
- For NDJSON, the checkpoint is the line number and the byte offset of the line start. Store both: the offset makes resume O(1), the line number makes the log readable.
- For a huge array, the checkpoint is the index of the last completed element plus the decoder's byte offset if the library exposes it. Without one, resume means re-reading from the start — which is a reason to convert to NDJSON before the second run.
- Make per-record processing **idempotent** (upsert by the record's id), because a resume always reprocesses at least the record in flight.
- Parallelism: NDJSON parallelizes by splitting the file into N line ranges. A single array does not parallelize without first building an index of element offsets — usually more work than converting the file.

## Streaming Output

Building a large document in memory to write it once has the same ceiling as parsing:

- Write records as you produce them. For NDJSON, that is one serialize-and-write per record with no accumulation.
- For a JSON array, write `[`, then each element with separating commas, then `]` — most encoders expose a streaming writer for this; hand-rolling it means owning the comma logic, which is the one place a bug produces invalid output.
- Flush on a size or time boundary, not per record, or syscall overhead dominates.
- Compress on the way out (`gzip`/`zstd` stream), never to a temporary file first (Size and Speed Reflexes in SKILL.md).
- If the consumer is HTTP, this is chunked transfer encoding and the client must not buffer.

## Over HTTP

- **Chunked responses** stream a large array or NDJSON body. The trap is client-side: most HTTP clients buffer the whole body by default and undo the entire design.
- **Server-Sent Events** carry one JSON document per `data:` line — a streaming protocol with a JSON payload, not a JSON format. Multi-line `data:` fields are concatenated before parsing.
- Long-running exports are better as: request → job id → poll → download a compressed NDJSON file. A 20-minute streaming HTTP response dies to a proxy timeout.
- Proxies and gateways impose body limits and inactivity timeouts that a slow producer will hit; send data continuously or use the job pattern.

## Operations Bigger Than Memory

| Operation | Approach |
|---|---|
| Filter | Streaming pass, emit matching records; memory is one record |
| Map / reshape | Same, one record at a time |
| Count / aggregate by key | Streaming with a map of accumulators — memory is proportional to the *number of distinct keys*, which is the thing to bound |
| Sort | Extract the sort key plus the byte offset, sort that (small), then re-read records in order; or an external sort over NDJSON |
| Join | Load the smaller side into memory keyed by the join field, stream the larger side. If neither fits, sort both by key and merge |
| Deduplicate | A hash set of the id field only, never of the records |
| Validate | Per record against the schema, collecting error counts by type rather than error objects (`schema.md`) |

**After a large-file run**, write the measured size, record count, parse ratio and any structural quirk to `## Producers` in `memory.md` (`memory-template.md`). The next person's decision about whether to stream depends entirely on those numbers.
