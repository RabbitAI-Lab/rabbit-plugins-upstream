# Read/Write Reference

## 1. Choose the target model first

Start every unfamiliar workbook operation with:

```bash
mbs workbook metadata --doc-id <DOC_ID> --output json
mbs workbook list-worksheets --doc-id <DOC_ID> --output json
```

Choose exactly one route before a write:

| Model | Identity to resolve | Valid write model |
|---|---|---|
| Excel Sheet | `worksheet_name`, optionally `gid` | A1/range/cell operations |
| Base Table | `table_id`, `field_id`, `record_id` or an explicit record key | field-mapped records and column Formula |
| Worksheet SQL Config | result worksheet plus SQL Config identity | raw SQL preview/config/materialization |

A worksheet name, a `gid`, a Base-looking table name, and a `db-table` alias
are not permission to use a cell address. If metadata cannot prove the model,
do not write.

## 2. Read safely

### Excel Sheet

```bash
mbs excel-worksheet read --doc-id <DOC_ID> --worksheet-name <SHEET> --output table
mbs excel-worksheet read --doc-id <DOC_ID> --worksheet-name <SHEET> --range A1:G20 --output table
mbs excel-table headers --doc-id <DOC_ID> --worksheet-name <SHEET> --table-id <PERSISTENT_TABLE_ID>
mbs excel-table metadata --doc-id <DOC_ID> --worksheet-name <SHEET> --table-id <PERSISTENT_TABLE_ID>
mbs excel-table sample --doc-id <DOC_ID> --worksheet-name <SHEET> --table-id <PERSISTENT_TABLE_ID> --limit 50
mbs excel-worksheet check-error --doc-id <DOC_ID> --worksheet-name <SHEET>
# Worksheet-backed table
mbs excel-table metadata --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID>
mbs excel-table sample --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID> --limit 50

# Base-backed table
mbs base-table metadata --doc-id <DOC_ID> --name orders_large --include-headers --output json
mbs base-table sample --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 50

# Workbook worksheet list
mbs workbook list-worksheets --doc-id <DOC_ID> --output table

# Workbook metadata
mbs workbook metadata --doc-id <DOC_ID>
```

Use an explicit `--worksheet-name`. A bounded A1 range is meaningful only for
a Sheet target.

### Base Table

```bash
mbs base-table metadata --doc-id <DOC_ID> --name <TABLE_NAME> --include-headers --output json
mbs base-table field list --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table schema --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table sample --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 50 --output table
mbs base-table read --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 100 --output table
```

Capture the returned table and field identities before writing. Use the sample
to identify a stable business key or returned record ID; never derive record
identity from a visual row number.

### Worksheet SQL Config

```bash
mbs sql config get --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --output json
mbs sql preview --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --sql-file query.sql --output table
```

The query must be raw SQL. SQL Config is neither a cell formula nor a Base
column Formula.

## 3. Write an Excel Sheet

An Excel Sheet full refresh is appropriate when:

- row 1 already contains the canonical worksheet headers
- all data rows from `start_row` onward should be replaced, not appended or merged
- existing header order and cell styles must remain in place
- formula columns omitted from the input should be filled from the row 2 formula template

Input must be a non-empty JSON array of objects. Every object key must exactly
match an existing header; matching is case-sensitive. The CLI calls
`/api/v1/excel/read_headers` before mutation and rejects unknown keys, empty
arrays, empty objects, mixed item types, and `start_row < 2`.

```json
[
  {"Name": "Alice", "Score": 88},
  {"Name": "Bob", "Score": 92}
]
```

Run a preflight before the real write:

```bash
mbs sheet update-data-keep-headers \
  --doc-id <DOC_ID> \
  --worksheet-name Students \
  --data students.json \
  --dry-run

mbs sheet update-data-keep-headers \
  --doc-id <DOC_ID> \
  --worksheet-name Students \
  --data students.json \
  --verify
```

Defaults are intentionally safe:

- `--start-row 2`: row 1 is never replaced
- `--preserve-formulas`: columns omitted from the first input object can reuse a row 2 formula template
- recalculation enabled: the backend rebuilds the workbook calculation chain
- `--verify`: opt-in bounded readback from row 1 through one row after the new dataset

Use `--no-preserve-formulas` only when input JSON should own formula columns.
Use `--skip-recalculation` only when a later explicit calculate step is planned.
`--dry-run` and `--verify` are mutually exclusive.

Replacement semantics matter: the backend clears existing values from
`start_row` through the previous last row before writing the new objects. A
shorter input therefore clears stale trailing rows. Missing known keys and
`null` leave cells blank. Unknown keys never reach the update endpoint because
the CLI rejects them after header preflight.

### `written_unverified` after a full refresh

When `worksheet import --strategy replace --verify` exits nonzero but returns
`written_unverified` and `error: null`, treat the mutation result as unknown,
not failed. The response means the CLI's built-in verification was incomplete;
it does not prove that the online worksheet still has old values.

Before reporting failure, blocking, or asking the user to choose a fallback:

1. Read the replacement footprint: row 1 plus every submitted data row and
   every previously occupied trailing row that the refresh should have cleared.
   If a full read is too large, read header row plus known changed sentinel
   cells/rows, including at least one changed value and the previous last row.
2. Map source row-object values to the live header order. Compare text exactly;
   compare numeric and date-like values with a documented tolerance that
   accepts expected Excel normalization but not a wrong row or column.
3. Do not infer a mismatch from a changed service/entity set: row-object keys
   are worksheet headers (for example, date columns), not the service values.
4. If the coverage or sentinels match, report the refresh as successful with a
   CLI verification warning. If they do not match, recover automatically; do
   not offer the user a menu of implementation paths.

For a genuine mismatch, preserve the recorded worksheet identity:

1. Read the current used range, formula cells, required formatting/validation
   metadata, source dimensions, and the latest `mbs history list --limit 1`
   entry. Serialize source values in live header order. Re-read that history
   entry immediately before fallback; if it changed, or the workbook is
   actively edited by collaborators, stop rather than running a destructive
   automatic fallback: this CLI exposes no lock or revision precondition.
2. Immediately before each mutation, rerun `mbs workbook list-worksheets` and
   confirm the target name still maps to the recorded `gid`. Pass
   `--gid <RECORDED_GID>` (not only `--worksheet-name`) to every range clear,
   range write, calculate, and error-check command.
3. Partition source-owned value columns into contiguous ranges that exclude all
   formula cells. Never clear or raw-write a formula cell. When headers are
   unchanged, clear `A2:<max-old-or-new-value-column><old-last-row>` only in
   those value ranges and write the new values there. When headers or schema
   changed, clear the owned value/header ranges beginning at `A1`, including
   old trailing headers, then write new header/value matrices beginning at
   `A1`. Do not clear outside owned value ranges or pass `--clear-styles`.
4. If a schema change moves, removes, or changes the semantics of a formula
   column, stop the fallback and report that structural conflict; do not invent
   a formula, replace the worksheet, or claim success. For new value columns,
   preserve or explicitly apply any required formatting, validation, filter,
   and width configuration before completion.
5. Use `excel-worksheet range write --gid <RECORDED_GID> --verify`, then read
   back the same footprint plus sentinels, run
   `excel-worksheet calculate --gid <RECORDED_GID>`, and run
   `excel-worksheet check-error --gid <RECORDED_GID>` when formula/result cells
   depend on the refreshed values.
6. Run `mbs workbook list-worksheets` again and confirm that the target name
   still resolves to the recorded `gid`. A changed `gid` is a failed identity-
   preservation requirement even if the data and worksheet name look correct.

Numeric-looking strings follow this backend's USER_ENTERED-style parsing. A
value such as `"46215.95520833333"` can read back as `"46215.95521"`. Use
`excel-worksheet range write` for exact RAW text preservation instead of this
full-refresh command.

### `excel-table insert` (Sheet-backed tables only)

Best when:

- appending row objects to a known Sheet-backed Excel Table
- the target table metadata is already known
- you can verify with `excel-table read` or a targeted Sheet range read

For an `excel-table`, resolve the persistent ID and current range through
`excel-table metadata`, then build `rows.json` from the headers returned by
`excel-table schema` or `read`. The input must be a non-empty array of objects,
and every object must have exactly the same keys as the current header row. The
CLI converts the objects to header order and writes all rows in one
command immediately below the current Table range.

```json
[
  {"id": "A-100", "amount": "100.00", "desc": "First row"},
  {"id": "A-101", "amount": "101.00", "desc": "Second row"}
]
```

```bash
mbs excel-table metadata --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID>
mbs excel-table insert --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID> --rows rows.json
mbs excel-table read --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID> --limit 20 --output table
```

The JSON example's keys are illustrative: replace them with the target table's
actual headers. `excel-table insert` does not have `--verify`. Do not reuse an
old `range_address` after structural row changes; call `metadata` again because
deleting an intermediate row shifts subsequent rows and the table end.

For a Base append or upsert, resolve `table_id`, writable `field_id`s, and a
stable key first, then use the Base record API:

```bash
mbs base-table field list --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table record upsert --doc-id <DOC_ID> --table-id <TABLE_ID> --key-field-id <KEY_FIELD_ID> --records records.json
```

`records.json` must use `field_id` keys. Do not append Base records through a
table-name or row-object convenience command.

### `worksheet convert-to-base`

Use this only to migrate one existing Sheet-backed worksheet to Base. It is a
one-way data migration, not a reversible engine setting: no Base-to-Sheet
conversion endpoint is available.

Before conversion, inspect the workbook and identify the worksheet by name or
gid. Run the backend-backed dry run before mutating the workbook:

```bash
mbs workbook list-worksheets --doc-id <DOC_ID> --output table

mbs worksheet convert-to-base \
  --doc-id <DOC_ID> \
  --worksheet-name Orders \
  --dry-run
```

After reviewing the preflight output, perform the conversion and verify the
selected worksheet's registered engine:

```bash
mbs worksheet convert-to-base \
  --doc-id <DOC_ID> \
  --gid <GID> \
  --yes \
  --verify
```

The operation requires `--yes` except for `--dry-run`; `--dry-run` and
`--verify` are mutually exclusive. `--verify` reads worksheet metadata and
fails when the selected worksheet does not report `data_engine: base`. Add
`--recalculate` if the Base worksheet should recalculate immediately after the
migration.

The default `--scrub-source-workbook` removes the old Sheet-engine cell content
after successful conversion while preserving styles. Use `--keep-sheet-source`
only when retaining that old source content is an explicit requirement. A URL
containing `?gid=<GID>` may be used in place of separate `--doc-id` and `--gid`
flags.

### `base-table create`

Best when:

- creating a new Base-backed logical table inside an existing workbook
- you have row-object JSON data and want the backend to materialize it as a DB table
- the table should be addressed later by native `table_id`

CLI:

```bash
mbs base-table create --doc-id <DOC_ID> --name Orders --rows orders.json
mbs base-table create --doc-id <DOC_ID> --name Orders --columns columns.json --rows rows.json --if-exists adopt --verify
mbs base-table metadata --doc-id <DOC_ID> --name Orders --include-headers --output json
mbs base-table sample --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 20 --output table
```

Use `base-table metadata --include-headers` when the next step needs exact header
text. The command is still a single-table lookup and requires `--name` or
`--backend-id`; use `workbook list-worksheets` first if the table name is
unknown.

`orders.json` must contain a JSON array of row objects. The CLI infers column
names and simple logical types (`text`, `number`, `boolean`) from the rows.
Pass `--columns columns.json` to provide an explicit schema, especially when
`rows.json` is empty or when the column order and logical types must be stable.
Use `--if-exists adopt` or `--adopt-existing` only for idempotent setup flows
where a matching Base-backed table may already exist; pair it with `--verify` so the CLI
confirms the registry adopted a Base-backed worksheet. Use `base-table create`
only for table-shaped data; use `excel-worksheet create` or `excel-worksheet
range write` for workbook-layout reports.

### `base-table field list` / `field update`

Use these commands when the user wants Base-backed column display metadata,
not row data mutation:

- formatter such as `$#,##0.00`, `0.00%`, `yyyy-mm-dd`
- data-cell text color or background color
- column width
- beautified header style metadata

```bash
mbs base-table field list --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table field update --doc-id <DOC_ID> --table-id <TABLE_ID> --field-id <FIELD_ID> --formatter "#,##0.00" --verify --output json
```

`field update` accepts native `--table-id --field-id` values, or resolves
`--name --field` to those IDs before calling the native field API. With
`--verify`, the command returns the updated field property. Width is stored as
`field.property.style.width`. The legacy
`db-table field batch-update` command is compatibility-only and is not part of
new examples.

### `base-table create-from-range`

Best when:

- a source worksheet lives in one document and the target Base-backed raw
  surface must land in another document
- you need a raw `R_*` surface from a bounded worksheet range without writing
  per-run Python import drivers
- merged-title sheets need a semantic header row inside the readback matrix

CLI:

```bash
mbs base-table create-from-range \
  --doc-id <TARGET_DOC_ID> \
  --name R_OrderLines_Store1 \
  --source-doc-id <SOURCE_DOC_ID> \
  --worksheet-name "1店" \
  --range A2:AR423 \
  --header-row 0 \
  --use-header-names \
  --if-exists adopt \
  --verify \
  --output json

mbs base-table metadata --doc-id <TARGET_DOC_ID> --name R_OrderLines_Store1 --output json
mbs base-table sample --doc-id <TARGET_DOC_ID> --table-id <TABLE_ID> --limit 20 --output table
```

The command is CLI-composed: it reads the source range through
`/api/v1/excel/read_sheet`, reshapes the values matrix, then creates the named
Base-backed table on the target workbook through `/api/v1/excel/db_table/create`.
`--header-row` is a 0-based index inside the returned `values` matrix, not an
Excel row number. For Shein-style merged titles, start `--range` at the
semantic header row (`A2:...`) and keep `--header-row 0`. Use
`--use-header-names` for semantic column names (blank header cells become
`col_NNN`); omit it for positional `raw_col_NNN` columns. Entirely blank rows
are dropped. JSON output includes source doc/sheet/range plus row/column
counts in `context`.

### `base-table create-from-query`

Best when:

- a SQL template should materialize a reusable Base-backed handoff table
- the source tables already exist in MaybeSheet
- the output should be addressed later by native `table_id`
- an ETL skill needs an auditable `--sql-file` command instead of Python-side planning

CLI:

```bash
mbs base-table create-from-query \
  --doc-id <DOC_ID> \
  --name S1_RevenueStructureInput \
  --sql-file s1_revenue_structure_input.sql \
  --if-exists adopt \
  --verify

mbs base-table metadata --doc-id <DOC_ID> --name S1_RevenueStructureInput --output json
mbs base-table schema --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table sample --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 20 --output table
```

The command executes raw SQL, infers source tables from `FROM` and `JOIN`, and
creates the named output Base table. `--name` is required and identifies the
output only. It does not accept `--worksheet-name`; `--gid` is optional
compatibility context and does not select a SQL source. Use a raw `SELECT` or
`WITH ... SELECT` body, never legacy `=SQL(...)` syntax; that wrapper is
migration-only compatibility. For a Base source,
reference quoted field display names, never `field_id` values such as
`col_000001`; `SELECT *` returns each display column once.

### Sheet formula writes

Use these only after confirming a Sheet target:

```bash
mbs excel-worksheet range set-formula --doc-id <DOC_ID> --worksheet-name <SHEET> --cell E2 --formula '=SUM(B2:D2)'
mbs excel-worksheet range set-formula --doc-id <DOC_ID> --operations formulas.json --recalculate-mode worksheet
```

Use `excel-worksheet range set-formula` for ordinary worksheet formula writes.
Use `formula read`, `formula batch-set`, and `formula lineage` for the
formula-focused Sheet workflow. For a Base formula, use `base-table formula`
with a resolved `table_id` and `field_id` instead.

For direct one-cell calculation, `mbs formula calculate` and
`mbs excel-worksheet range calculate` both call `/api/v1/excel/calc-formula`.
Pass `--no-save-result` for preview-only checks, `--save-result` when the
formula/result should persist, and omit the flag only when relying on the
backend default deliberately.

### Legacy `sheet upsert`

Best when:

- syncing business records by key
- updating existing rows
- appending missing rows automatically
- you have confirmed the gid and key column

Common keys include `Order ID`, `SKU`, and `ID`.

The following commands are Sheet-only:

```bash
mbs excel-worksheet range write --doc-id <DOC_ID> --worksheet-name <SHEET> --range A1:C3 --values values.json --verify
mbs excel-worksheet range clear --doc-id <DOC_ID> --worksheet-name <SHEET> --range D1:F10
mbs excel-table metadata --doc-id <DOC_ID> --worksheet-name <SHEET> --table-id <PERSISTENT_TABLE_ID>
mbs excel-table insert --doc-id <DOC_ID> --worksheet-name <SHEET> --table-id <PERSISTENT_TABLE_ID> --rows rows.json
mbs excel-worksheet range set-formula --doc-id <DOC_ID> --worksheet-name <SHEET> --cell E2 --formula '=SUM(B2:D2)'
```

Value handling:

- `excel-worksheet range write` defaults to `RAW`; numeric-looking strings such as `"5.53%"` and `"9,007,000"` stay strings.
- Current `mbs` range-write exposes no `USER_ENTERED` or `value_input_option` flag. Do not pass one or infer `parse_result` fields; use a command that explicitly exposes parsing semantics if they are required.

### `clear_range`

Best when:

- you need to clear a specific range
- you want a local reset before a write

For a complete Sheet data-row refresh, use:

```bash
mbs worksheet import ./rows.json --strategy replace --doc-id <DOC_ID> --worksheet-name <SHEET> --dry-run
mbs worksheet import ./rows.json --strategy replace --doc-id <DOC_ID> --worksheet-name <SHEET> --verify
```

This route preserves the existing Sheet header row, styles, and Sheet formula
columns. It can reuse a formula template from Sheet row 2 for omitted formula
columns. That behavior is deliberately confined to Sheet targets; it must not
be applied to a Base Table.

## 4. Write a Base Table

Base writes are field-mapped record operations. They must resolve `table_id`,
allowed `field_id`s, and the record key or `record_id` before mutation. Formula
and read-only fields must be excluded from the data payload.

Use the P5 Base command group with field-ID record JSON:

```bash
mbs base-table read --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 100 --output table
mbs base-table field list --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table record replace --doc-id <DOC_ID> --table-id <TABLE_ID> --records records.json
mbs base-table record upsert --doc-id <DOC_ID> --table-id <TABLE_ID> --key-field-id <KEY_FIELD_ID> --records records.json
```

`records.json` is a JSON array whose object keys are `field_id` values, not
display headers. `replace` owns the complete target record set. `upsert` requires
each object to include its `--key-field-id`; it updates matching `record_id`s
and creates records for absent keys. Add `--expected-revision <REVISION>` when
the caller holds an optimistic-concurrency revision.

Do not perform a Base replace/upsert through `worksheet import --strategy
replace`, `sheet update-data-keep-headers`, A1/range commands, or cell formula
commands.

Current `base-table create`, `create-from-range`, and `create-from-query` create
a Base table. They do not change the rule above: none is a general record
replace/upsert API.

## 5. Write Worksheet SQL Config

```bash
mbs sql config set --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --sql-file query.sql --auto-refresh
mbs sql preview --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --sql-file query.sql --output table
mbs sql overwrite --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --confirm-overwrite
```

Preview before materialization. Confirm the saved config and materialized
result afterward. Use `mbs base-table create-from-query` only when the desired
outcome is creation of a reusable Base handoff table from raw SQL; it is not a
column Formula command.

## 6. Verification and rejection rules

Use the verification method that matches the model:

- Sheet: targeted `excel-worksheet read`, then `excel-worksheet check-error`
  after formula or SQL-result changes.
- Base: inspect the record result, `table_id`, `field_id` mapping, and Formula
  execution evidence; a sample alone is not enough for computed columns.
- SQL Config: inspect stored raw SQL, preview/materialization status, and a
  bounded result read or Base sample.

Reject a route when a Base target receives a range, cell, row/column position,
row-template preservation, keep-headers refresh, or cell formula operation.
The full procedure is in [base-mode-verification.md](base-mode-verification.md).
