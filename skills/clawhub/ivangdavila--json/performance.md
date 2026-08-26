# Performance — Speed, Size, and When to Leave JSON

Order of operations: measure where the time goes, remove double work, compress, and only then consider a different format. Most "JSON is slow" conclusions are reached before step one.

**Contents:** [Measure the Right Thing](#measure-the-right-thing) · [Orders of Magnitude](#orders-of-magnitude) · [Remove Double Work](#remove-double-work) · [Faster Parsing and Serialization](#faster-parsing-and-serialization) · [Compression](#compression) · [Making the Payload Smaller](#making-the-payload-smaller) · [Browser and Client Cost](#browser-and-client-cost) · [When to Leave JSON](#when-to-leave-json) · [Benchmarking Honestly](#benchmarking-honestly)

## Measure the Right Thing

The four costs are independent and confusing each other is the usual mistake:

1. **Serialization** on the producer (CPU, allocation).
2. **Transfer** (bytes over the wire, after compression).
3. **Parsing** on the consumer (CPU, and peak memory at 3-10× the document, Rule 6).
4. **Everything downstream** — validation, mapping to objects, database writes. This is frequently larger than all three above, and switching formats does nothing for it.

Instrument each separately before optimizing. A profile that shows "JSON" as 40% of a request usually resolves into 5% parse and 35% object mapping and validation.

## Orders of Magnitude

Ranges, not promises — hardware, document shape and library version each move these by more than 2×. Measure on your own payload; record the number in `## Producers` (`memory-template.md`).

| Operation | Order of magnitude |
|---|---|
| Native parser (C/C++/Rust-backed) parsing simple records | Hundreds of MB/s to a few GB/s; SIMD parsers are the top of that range |
| Pure-language parser (a JSON parser written in the scripting language itself) | Tens of MB/s — an order of magnitude slower |
| Serialization vs parsing | Serialization is usually the cheaper of the two for the same document |
| Schema validation, compiled | Comparable to parsing, often less; **compiling** the schema is 100-1000× a single validation (Rule 8) |
| gzip on record-shaped JSON | 5-10× smaller, at a few hundred MB/s compressing |
| Object mapping / reflection-based binding | Frequently exceeds parse time; source-generated or code-generated binding removes most of it |

The stable ratio worth remembering: for record data, **repeated key names dominate the size and compress away almost entirely**. That is why compression usually beats format changes.

## Remove Double Work

Before making anything faster, stop doing it twice:

- **Parse once per request.** A body parsed by middleware and again by a handler, or validated at three layers, is pure duplication (Rule 1).
- **Forward bytes, do not re-serialize.** A proxy or aggregator that parses a subdocument only to re-emit it should pass it through: `json.RawMessage` (Go), `Box<RawValue>` (Rust), `JsonElement`/`JsonDocument` (.NET), a string field (elsewhere). It also preserves signatures (Rule 5).
- **Cache the serialized bytes**, not the object, for anything served repeatedly and unchanged — including the ETag computed from them (`signing.md`).
- **Reuse the expensive objects**: compiled validators, serializer options, encoder/decoder instances, buffer pools. Constructing them per request is the single most common self-inflicted JSON cost.
- **Do not pretty-print machine-to-machine traffic** (`indent: 0`): indentation is 10-25% of a nested payload, and formatting costs CPU on both ends.
- **Do not log full bodies** at info level. Logging serializes the document a second time and writes it to three destinations (`security.md`).

## Faster Parsing and Serialization

- Swap in a faster library before changing anything structural: most ecosystems have a drop-in native parser that is several times the standard one, and the change is a line of code.
- Decode into **typed structures**, not generic maps: fewer allocations, lower peak memory (the 1-3× end of the ratio), and the type errors surface at the boundary.
- Avoid reflection at runtime where the language offers generated serializers (source generators, code-gen, derive macros). This is often a bigger win than the parser itself.
- Extract one field from a large document with a streaming scan rather than a full parse — a targeted extraction costs a fraction of materializing the whole tree (`streaming.md`).
- Skip work: many decoders can be told which fields to bind, and ignoring an enormous unused subtree is free if the parser can skip it rather than build it.
- Batch small documents into one NDJSON stream rather than one HTTP request each: per-request overhead dwarfs per-document parse cost at small sizes.

## Compression

- Enable it before considering anything else. `Content-Encoding: gzip` is the highest-value change in this file, and it is configuration.
- **Threshold**: compress above roughly 1 KB. Below that the header and CPU overhead can exceed the saving, and many servers default to a threshold in that range.
- **zstd** gives a better ratio at a similar or better speed than gzip and is widely available; **brotli** wins on static assets at high compression levels but is slow to compress at request time — use its cached, precompressed form.
- Compress at the edge, or in the application when the edge cannot: doing it in both places wastes CPU and can double-encode.
- Already-compressed payloads (an image as base64) do not compress again. That is an argument for not putting them in JSON at all.
- Storing compressed: a compressed JSON column is smaller but unqueryable; databases already compress large values transparently (`databases.md`).

## Making the Payload Smaller

In descending order of value per unit of damage:

| Change | Saving | Cost |
|---|---|---|
| Compression | 5-10× on record data | None worth mentioning |
| Remove fields nobody reads | Proportional | Requires knowing who reads what — sparse fieldsets make it the client's choice (`api-payloads.md`) |
| Pagination / streaming instead of whole collections | Bounded peak on both ends | Client complexity (`streaming.md`) |
| Compact output (no indentation) | 10-25% on nested data | None |
| Shortening key names | Large before compression, small after | Debuggability, forever. Rarely worth it |
| Columnar shape (arrays of values plus one header row) | Substantial for homogeneous records | A custom format everyone must implement; you have invented CSV with extra steps |
| Numbers as strings | Costs 2 bytes per value | Required for precision anyway (Rule 2) |
| Binary format | 10-30% raw, often ~0 after gzip | Debuggability and tooling (When to Leave JSON) |

## Browser and Client Cost

- `JSON.parse` blocks the main thread. Above roughly 1 MB, parse in a worker or stream the response — a 200 ms parse is a dropped frame budget of twelve.
- For large static data embedded in a bundle, a JSON string parsed with `JSON.parse` is measurably faster to load than the equivalent JavaScript object literal, because the JSON grammar is far cheaper to parse than JavaScript. This is a real, documented V8 optimization and applies to any large literal data blob.
- Mobile clients pay for bytes twice: transfer and memory. Pagination beats compression there.
- Do not re-serialize a response in the client to store it (localStorage, IndexedDB) if you can store the original text — one fewer round trip through the parser.

## When to Leave JSON

The threshold is a measurement, not a preference. Require gzipped-JSON numbers first (Where Experts Disagree in SKILL.md).

| Alternative | Wins | Costs |
|---|---|---|
| MessagePack / CBOR | Native binary values (no base64's +33%), faster parse, modestly smaller — frequently **not** smaller than gzipped JSON | Unreadable in a log or a browser; every tool needs a decoder |
| Protobuf / Avro / Thrift | 3-10× smaller and much faster; a real schema with generated types and enforced evolution rules | A build step, a schema registry, and no ad-hoc inspection |
| FlatBuffers / Cap'n Proto | Zero-copy access, no parse step at all | Rigid layout, awkward to produce by hand |
| Parquet | Analytical columnar storage; enormous wins for column scans | Not an interchange format for records or APIs |
| Plain CSV / NDJSON | Simpler and smaller for flat, homogeneous rows | No nesting, no types (`csv`) |

Sound reasons to switch: high-frequency internal service traffic where parse CPU is a measured bottleneck; payloads dominated by binary or numeric arrays; a strict evolution regime you want enforced by tooling. Unsound reasons: "JSON is slow" with no profile, and a size comparison that never applied compression.

Keep JSON at every boundary a human debugs: public APIs, webhooks, config, logs. The debuggability is the feature, and it is the one you miss at 3am.

## Benchmarking Honestly

- Benchmark with **your** payload, not a synthetic one: shape decides everything, and a document of many small objects behaves nothing like one of a few long strings.
- Report p50 and p99, not a mean — the tail is what breaks.
- Measure allocation and peak memory alongside time; a parser that is 20% faster and allocates twice as much loses under real concurrency.
- Warm up, and run long enough that JIT and garbage collection are represented.
- Compare like with like: gzipped JSON vs gzipped MessagePack, generated binding vs generated binding.
- Record the result, with the sample size and date, in `## Producers` or in `artifacts/` if it decided a format (`memory-template.md`). A benchmark nobody wrote down gets re-run with different assumptions in six months.
