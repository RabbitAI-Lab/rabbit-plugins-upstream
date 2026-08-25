# Base Mode Verification Runbook

Use this runbook before and after every Base Table mutation. Base Tables are
record/field objects, not worksheets with an alternate range implementation.

## 1. Detect the engine

```bash
mbs workbook metadata --doc-id <DOC_ID> --output json
mbs workbook list-worksheets --doc-id <DOC_ID> --output json
```

Locate the intended worksheet and confirm that its metadata identifies
`engine`/`data_engine` as `base`. Capture its worksheet name and `gid` for
human traceability, but do not use either as an A1 permission. If the response
does not contain the Base table identity, stop and resolve it through the
current Base metadata command or the service owner. Do not guess a table ID
from a name.

## 2. Capture table and field identity

Canonical commands can inspect a known Base table (the `table` forms are
compatibility aliases):

```bash
mbs table schema --target "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?tid=<TABLE_ID>" --output json
mbs table sample --target "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?tid=<TABLE_ID>" --limit 20 --output table
mbs table read --target "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?tid=<TABLE_ID>" --limit 100 --output table
mbs table inspect --doc-id <DOC_ID> --name <TABLE_NAME> --include-headers --output json  # compatibility resolver
mbs table schema --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs table sample --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 20 --output table
```

Record the returned `table_id`, every target `field_id`, field names/types, and
the record identity/key that the workflow will use. A column name is not a
stable substitute for `field_id`; a row position is not a substitute for
`record_id`.

## 3. Replace or upsert records

Use canonical table record commands with a field-ID JSON array:

```bash
mbs table replace-records --target "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?tid=<TABLE_ID>" --records records.json --verify
```

Use `replace` only when the ownership boundary is the complete target record
set. Use `upsert` only with an explicit stable record key/identity. Submit
values mapped to allowed `field_id`s, validate values against field types, and
exclude Formula and read-only fields. A successful operation must report the
resolved `table_id`, the record identities written, and field/record errors.

`records.json` is a JSON array of field-ID objects. For `upsert`, every record
must include the key field. Add `--expected-revision <REVISION>` when the caller
must enforce optimistic concurrency. Do not fall back to a Sheet command.

## 4. Set a column Formula

Use canonical Base Formula commands:

```bash
mbs formula compile --target "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?tid=<TABLE_ID>" --field-id <FIELD_ID> --expression '<EXPRESSION>'
mbs formula set --target "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?tid=<TABLE_ID>" --field-id <FIELD_ID> --expression '<EXPRESSION>'
mbs formula recalculate --target "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?tid=<TABLE_ID>" --field-id <FIELD_ID>
```

Formulas are attached to a `field_id` and evaluate for the table's records.
They are not placed in cells such as `E2`, copied down a range, or preserved by
a row-template write. Compile/validate the expression first, set it on the
intended `field_id`, then request recalculation at table scope.

Verification requires Formula execution evidence, not merely sampled values:

- resolved `table_id` and target `field_id`
- execution mode (`immediate` or `deferred`)
- executed field IDs or a dirty-table result
- field-level errors, if any
- a representative record read after execution

For deferred execution, retain the dirty-table evidence and do not claim that
computed values are current until a later table Formula recalculation returns
success.

## 5. Verify SQL Config materialization

SQL Config is a separate raw-SQL producer. It does not become a Base Formula
because its result happens to be materialized into a Base table.

```bash
mbs sql config set --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --sql-file result.sql --auto-refresh
mbs sql preview --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --sql-file result.sql --output table
mbs sql overwrite --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --confirm-overwrite
mbs sql config get --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --output json
```

Verify all of the following: stored query is raw SQL, preview succeeded, the
materialization reports its target model and result, and a bounded read/sample
matches the expected result shape. Raw SQL starts with `SELECT` or `WITH`; do
not wrap it in a cell formula.

## 6. Reject Sheet-only misuse

Stop and correct the route when a Base target is about to receive any of these:

- an A1 address, range, row number, or column letter as the write identity
- `range write/clear/set-formula/calculate`
- `sheet update-data-keep-headers`, `worksheet import --strategy replace`, or
  any row-2 template/preserve-formula behavior
- copy-range, cell Formula, chart, image, or Sheet formatting operations
- A1 row/column coordinates; Base row/column commands must use stable
  `record_id`/`field_id` selectors instead
- a legacy `table range set-formula` request

The canonical adapter defines `BASE_COLUMN_FORMULA_REQUIRED` for a missing Base
field selector and `SHEET_ONLY_OPERATION` for a Sheet-only route invoked on
Base. Treat those as guard contracts, not as a reason to retry with a different
`gid`, range, or keep-headers flag.
