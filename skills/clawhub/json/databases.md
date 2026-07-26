# Databases — JSON Columns and Document Stores

A JSON column is a schema nobody wrote and everybody depends on. It is the right tool for genuinely variable data and the wrong one for fields you filter on — and the boundary is decidable.

**Contents:** [Column or Field](#column-or-field) · [PostgreSQL: json vs jsonb](#postgresql-json-vs-jsonb) · [Indexing jsonb](#indexing-jsonb) · [Write Amplification and TOAST](#write-amplification-and-toast) · [MySQL](#mysql) · [SQLite](#sqlite) · [MongoDB and Extended JSON](#mongodb-and-extended-json) · [Migrating JSON Data](#migrating-json-data) · [Loading and Exporting](#loading-and-exporting)

## Column or Field

Promote a JSON field to a real column when **any** of these is true:

| Signal | Why |
|---|---|
| It appears in `WHERE`, `JOIN` or `ORDER BY` regularly | Expression indexes exist, but a plain column is cheaper, simpler and always used by the planner |
| It needs a foreign key or a uniqueness constraint | JSON fields cannot carry either |
| It is present in ~100% of rows | Optionality was the reason to use JSON; if it is always there, it is a column |
| It has a fixed type the application depends on | JSON gives no type enforcement; a `"12"` will arrive eventually |
| It is aggregated (`SUM`, `AVG`) | Extraction plus a cast per row on every query |

Keep it in JSON when it is genuinely sparse across rows, arrives from an external producer whose shape you do not control, is written and read whole (a snapshot, a raw payload, an audit record), or is an implementation detail with no query pattern yet.

The stable hybrid: **queried fields as columns, the whole original document in one `raw`/`payload` column**. It keeps the source of truth intact for replay and signature verification (`signing.md`) while every query hits a real index.

## PostgreSQL: json vs jsonb

| | `json` | `jsonb` |
|---|---|---|
| Storage | The original text, verbatim | Parsed binary form |
| Whitespace and key order | Preserved | Discarded; keys reordered (by length, then bytes) |
| Duplicate keys | Preserved, all of them | Deduplicated, last one wins |
| Number literals | Preserved as written (`1.0` stays `1.0`) | Normalized through `numeric` |
| Indexing | Only expression indexes on extracted values | GIN over the whole document, plus expression indexes |
| Containment `@>`, existence `?` | Not available | Available |
| Write cost | Cheaper (no parse) | Higher (parse on write) |
| Read cost | Parses on every access | Cheap field access |

Default is **`jsonb`** for anything queried. `json` is the right choice for an audit or webhook table where the byte-exact document matters — the signature you may need to re-verify is over those exact bytes.

Operators: `->` returns JSON, `->>` returns text. Chaining a text result into another `->` is a type error, which is what most "operator does not exist" messages mean. `#>` and `#>>` take a path array. Postgres 12+ adds SQL/JSON path (`jsonb_path_query`, `@?`, `@@`) with filter expressions.

## Indexing jsonb

Three index shapes, and choosing wrong means the index exists and is never used:

| Query pattern | Index |
|---|---|
| Containment (`payload @> '{"status":"paid"}'`) or key existence | `GIN (payload)` — the default operator class, indexes keys and values |
| Containment only, smaller and faster | `GIN (payload jsonb_path_ops)` — no key-existence support, roughly half the size |
| Equality or range on one known field | `BTREE ((payload->>'status'))` — an expression index |
| Range on a numeric field | `BTREE (((payload->>'amount')::numeric))` — the cast must be in the index and in the query |

- **The expression in the query must match the index expression exactly**, cast included. `(payload->>'amount')::int` will not use an index built on `::numeric`.
- Expression indexes on a JSON field require the extraction to be immutable; casts to timestamp with a timezone are not, and the index creation fails — extract to text and cast on a stored generated column instead.
- A GIN index does not help `ORDER BY`. Sorting by a JSON field at scale needs a b-tree expression index or a real column.
- Index size is a real cost: a GIN index over a large document indexes every key and value. Index the field, not the document, unless containment queries are the actual pattern.

## Write Amplification and TOAST

- Postgres has no partial update of a `jsonb` value: `SET payload = jsonb_set(payload, …)` rewrites the **whole document** and creates a new row version. A 40 KB document updated on every request is 40 KB of write amplification per request plus vacuum work.
- Values above roughly 2 KB are compressed and moved out of line (TOAST); a document that crosses that boundary gets a compress/decompress cycle on every read and write.
- Consequence: **do not use one big JSON document as a mutable per-row state bag.** Frequently updated fields belong in columns; the JSON document should be mostly write-once.
- Counters inside JSON are the worst case: high-frequency updates to a large document. Move them out.

## MySQL

- The `JSON` type validates and stores a normalized binary form; key order is not preserved and duplicates are removed (last wins).
- **JSON columns cannot be indexed directly.** The pattern is a generated column plus an index on it:
  a stored or virtual generated column extracting the field, then a normal index over that column. Queries must reference the same expression the generated column uses for the optimizer to substitute it.
- `->` and `->>` exist as shorthand for `JSON_EXTRACT` and `JSON_UNQUOTE(JSON_EXTRACT(...))`. The unquoting difference is where string comparisons silently fail: `col->'$.a' = 'x'` compares a JSON string to a SQL string and never matches; `col->>'$.a' = 'x'` does.
- Partial in-place updates happen only under specific conditions (`JSON_SET`/`JSON_REPLACE`/`JSON_REMOVE` on same-or-smaller values in a column that has not been otherwise rewritten). Anything else rewrites the value.
- `JSON_TABLE` turns a document into rows and is the clean way to join array elements against tables.
- Multi-valued indexes (over an array inside a document) exist in 8.0.17+ and are the only way to index array membership.

## SQLite

- JSON functions are built in (the `json1` surface), with `->` and `->>` operators available in modern versions; `->>` returns SQL text, `->` returns JSON, the same distinction as elsewhere.
- Everything is stored as text unless the newer binary JSONB representation is used; validation happens in the functions, not in the column type, so add a `CHECK (json_valid(col))` constraint or the column will accept anything.
- Indexing works through generated columns plus a normal index, or directly through an expression index on `col ->> '$.field'`.
- `json_each` and `json_tree` expand documents into rows — the equivalent of `JSON_TABLE`.

## MongoDB and Extended JSON

- BSON is not JSON: it has types JSON does not (ObjectId, Date, Decimal128, Binary, int32 vs int64) and a 16 MB document limit.
- **Extended JSON** is the lossless text representation of BSON, in two flavors: *canonical* (`{"$numberLong":"9007199254740993"}` — type-explicit, round-trips exactly) and *relaxed* (`9007199254740993` as a plain number — readable, and lossy for large integers and decimals). Exports default to relaxed in several tools, which is a silent precision loss on the way out (`numbers.md`).
- `{"$oid": "…"}` and `{"$date": "…"}` in a document you received mean it came from a Mongo export, not from an API. Converting it to plain JSON drops the types.
- Field names starting with `$` or containing dots were historically forbidden and are still hazardous in query contexts — a document with a `$ne` key inside user data is an injection vector (`security.md`).
- Document design: unbounded arrays inside a document are the standard scaling mistake, because the document is rewritten and moved as it grows. Bound arrays, or model them as their own collection.
- Key order is preserved in BSON, which makes it possible to depend on it accidentally. Do not.

## Migrating JSON Data

- There is no `ALTER` for a document's shape: a shape change is a backfill, written as an idempotent, resumable job over batches, with a progress record (`streaming.md`).
- Version documents from day one with a `_v` field, and support reading the previous version until the backfill finishes. Otherwise the migration must be atomic, which at scale it cannot be.
- Validate before and after: count documents matching the old shape, run, count again, and assert that the sum is unchanged. A backfill that silently skips malformed documents is how a subset of rows ends up on a shape nobody supports.
- Add a `CHECK` constraint or an application-level schema at the same time as the backfill (`schema.md`), or the old shape reappears through a code path nobody migrated.

## Loading and Exporting

- NDJSON is the interchange format for bulk load and export: one record per line, resumable, splittable (`streaming.md`).
- Bulk load in batches (1,000-10,000 records per transaction is the usual sweet spot) rather than one transaction per record or one transaction for everything; the first is slow, the second holds locks and blocks vacuum.
- Escape and encoding pass through the database's client protocol, not through the shell: loading with a client library beats generating a giant `INSERT` script, which will eventually hit a quoting bug (`encoding.md`).
- Export with explicit types: a JSON export of a `numeric` column through a driver that uses doubles loses precision in the export, not in the database (`numbers.md`).

**When a storage decision is made** — column vs field, `json` vs `jsonb`, which index, which document version — write it to `~/Clawic/data/json/artifacts/<kebab-name>.md` with the reason and what was rejected, add its `## Boxes` line, and put the one-line decision in `~/Clawic/data/projects/<project>.md` if the work is tracked there (`memory-template.md`).
