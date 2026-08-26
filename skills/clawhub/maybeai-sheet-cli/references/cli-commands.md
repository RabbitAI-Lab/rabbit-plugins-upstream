# CLI Command Reference

## Runtime discovery is the command contract

Do not copy a static command tree from this skill. The installed CLI is the
source of truth for public commands and flags:

```bash
mbs --help
mbs <group> --help
mbs <group> <command> --help
```

Generate only commands listed by their parent `--help`. A directly callable
command that is absent from parent help is a hidden compatibility surface; do
not probe, recommend, or generate it for new work.

## Discover and identify the target

```bash
mbs workbook inspect --target "$WORKBOOK"
mbs worksheet list --target "$WORKBOOK" --output json
mbs table list --doc-id <DOC_ID> --output json
```

Use a Sheet target with `gid` for A1 range/cell work. Use a persistent `tid`
(and field or record IDs when required) for Base work. Do not infer the engine
from a worksheet name or visual appearance.

## Public operational patterns

### Read and inspect

```bash
mbs range inspect --target "$SHEET" --range A1:Z100
mbs range read --target "$SHEET" --range A1:D20 --output table
mbs table schema --target "$BASE_TABLE"
mbs table read --target "$BASE_TABLE" --limit 100 --output table
mbs table read --target "$BASE_TABLE" --all --order-by order_id --frame-out /tmp/orders.parquet
```

#### Complete table exports and pagination

`table read` currently defaults to 1000 records per request and accepts at
most 5000. Without `--all`, it performs exactly one bounded read, even if the
response says more records exist. Use a smaller explicit `--limit` for a
preview; use a frame for a complete result:

```bash
mbs table read \
  --target "$BASE_TABLE" \
  --all \
  --order-by order_id \
  --frame-out /tmp/orders.parquet \
  --output json
```

`--frame-out` requires `--all`. The CLI collects every page, then writes one
complete `.parquet`, `.csv`, or `.json` frame; it does not leave a partial
frame when pagination fails. It follows `next_cursor` / `nextCursor`. When a
backend instead returns `has_more: true` without a cursor, it requests the
next page with `offset += records_returned`. `has_more: false`, a reached
declared total, or an explicit completion marker ends the read.

Never infer completion from the number of returned rows. If a page fills the
requested limit but has no cursor, `has_more`, total, or completion marker,
the CLI exits with `backend.pagination_contract` rather than silently export a
truncated result. Repeated cursors, an empty page with `has_more: true`, and a
declared total larger than the rows received also fail. `--order-by` is a
backend capability: if the target cannot honor it, the CLI returns a capability
error instead of sorting locally. Complete reads do not pin a table snapshot;
avoid concurrent writes when an exact point-in-time export is required.

### Write table records

```bash
mbs table insert --target "$BASE_TABLE" --frame-in rows.json --verify
mbs table update \
  --target "$BASE_TABLE" \
  --frame-in corrected_rows.json \
  --key order_id \
  --expected-revision <REVISION> \
  --verify
```

`table insert` and `table update` are not an automatic replacement for an
atomic whole-table replacement operation. If the request requires deleting
missing records, preserving identities, or atomic replacement semantics, state
the capability gap and obtain an explicit product/API decision before composing
destructive calls.

### Write Sheet ranges, formulas, and notes

```bash
mbs range write --target "$SHEET" --range A1:C3 --values values.json --verify
mbs range style --target "$SHEET" --range B2:D4 --spec range-style.json --verify
mbs formula validate --target "$SHEET" --cell E2 --expression '=SUM(B2:D2)'
mbs formula set --target "$SHEET" --cell E2 --expression '=SUM(B2:D2)' --verify
mbs formula calculate --target "$SHEET" --cell E2 --save-result --verify
mbs range note read --target "$SHEET" --range B2:D4
mbs range note set --target "$SHEET" --range B2 --text "Reviewed" --verify
mbs range note clear --target "$SHEET" --range B2 --verify
```

Use `formula set` for formula writes and `range note read|set|clear` for Sheet
notes. Notes are not Base record notes. `range lineage` uses `--range`, not
`--cell`.

### Worksheet operations and styling

```bash
mbs worksheet calculate --target "$SHEET" --verify
mbs worksheet check-error --target "$SHEET" --range A1:Z100
mbs worksheet config --target "$SHEET" --spec worksheet-config.json --verify
mbs worksheet beautify --target "$SHEET" --verify
mbs range merge --target "$SHEET" --range A1:C1 --verify
mbs range unmerge --target "$SHEET" --range A1:C1 --verify
```

Run `mbs worksheet style --help` only when the task needs explicit worksheet
styling operations, then inspect the selected child with `--help`. Do not copy a
nested worksheet-style command list into this skill.

### Base fields and formulas

```bash
mbs column insert --target "$BASE_TABLE" --field new_status --field-type text --verify
mbs column rename --target "$BASE_TABLE" --field status --new-name Status --verify
mbs column config --target "$BASE_TABLE" --field amount --spec column-style.json --verify
mbs column batch-update --target "$BASE_TABLE" --updates base-field-updates.json --verify
mbs formula validate --target "$BASE_TABLE" --field gross_margin --expression 'revenue - cost'
mbs formula set --target "$BASE_TABLE" --field gross_margin --expression 'revenue - cost' --verify
mbs formula recalculate --target "$BASE_TABLE" --field gross_margin --verify
```

`column config` is a resource-style operation. For an in-place batch update of
existing Base field metadata, use public `column batch-update --updates` and
inspect its installed help for the accepted update-object contract. It does not
replace whole-schema migration: adding, deleting, or reordering fields may need
separate public column operations and has different atomicity/data-migration
semantics.

### SQL materialization

```bash
mbs sql query --target "$WORKBOOK?table=Sheet6" --sql-file result.sql --all --frame-out /tmp/query.parquet
mbs sql preview --target "$WORKBOOK?table=Sheet6" --sql-file result.sql --output table
mbs sql materialize \
  --target "$WORKBOOK?table=S_orders" \
  --sql-file result.sql \
  --mode create \
  --schema schema.json \
  --verify
```

Use `sql materialize` for public Base-table materialization. Use `sql config`
and `sql overwrite` only when the current help and selected target show a
Worksheet SQL Config workflow. `sql query --all --frame-out` is read-only and
writes a complete local Parquet, CSV, or JSON frame; it does not modify the
workbook.

`sql query` and `sql preview` accept a workbook target with
`?table=<WORKSHEET_NAME>` to select the worksheet used by the query. The CLI
resolves the worksheet selector before issuing the workbook SQL request. Do
not replace this with a Base-table `?tid=<TABLE_ID>` target; SQL query and
preview require a workbook target.

The canonical response operation for every public `table create` source is
`table.create`, including frame, SQL-query, and worksheet-range sources. The
source-specific implementation path does not change the operation name in
the response envelope.

### Other public groups

For chart, pivot, dashboard, image, media, history, file, share, and raw work,
start with the relevant parent help and then inspect the selected operation's
flags. Use `mbs image`, not a worksheet image compatibility alias.

## Mutation safety

For mutations, use `--dry-run` before unfamiliar or destructive work, preserve
`--expected-revision` and `--idempotency-key` when the workflow needs them, and
verify with a target-appropriate readback. `--output table|yaml` changes
rendering only; it does not alter the command contract.
