# Engine Selection When Creating Data Products

Choose the target model before creating a worksheet, table, or query output.
The models may coexist in one workbook but do not share a write API.

| Need | Create/use | Identity after creation |
|---|---|---|
| Visual report, merged cells, charts, images, or visible formulas | Excel Sheet | `worksheet_name`, `gid`, A1 addresses |
| Flat operational records and field-level computation | Base Table | `table_id`, `field_id`, record key/`record_id` |
| Persisted derived result from a query | Worksheet SQL Config | result worksheet and raw SQL config |

## Base Table

For a new durable Base handoff table, current CLI creation flows include:

```bash
mbs base-table create --doc-id <DOC_ID> --name cost_monthly --rows rows.json --verify
mbs base-table create-from-query --doc-id <DOC_ID> --name cost_monthly --sql-file <GOLD_SQL_FILE> --if-exists adopt --verify
mbs base-table metadata --doc-id <DOC_ID> --name cost_monthly --include-headers --output json
mbs base-table field list --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table sample --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 20 --output table
```

After creation, capture table/field identity. Do not update this Base Table by
writing a range, refreshing keep-headers data, or preserving a row-2 formula
template. Its desired mutation surface is P5 `base-table record replace/upsert`
and `base-table formula compile/set/recalculate`. These commands are available;
use `mbs base-table --help` to confirm flags and follow the verification
runbook before use.

## Worksheet SQL Config

Use this when the query itself must remain visible, auditable, and refreshable
as a distinct producer:

```bash
mbs sql config set --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --sql-file <GOLD_SQL_FILE> --auto-refresh
mbs sql preview --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --sql-file <GOLD_SQL_FILE> --output table
mbs sql overwrite --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --confirm-overwrite
mbs sql config get --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --output json
```

SQL Config takes raw SQL; it is not a Formula field and it must not be created
as a legacy cell SQL wrapper. A Base table can be an SQL materialization target
without changing its record/field semantics.

## Excel Sheet

Use Sheet only for layout-oriented outputs:

```bash
mbs excel-worksheet create --doc-id <DOC_ID> --name <REPORT_WORKSHEET> --output json
mbs excel-worksheet range write --doc-id <DOC_ID> --worksheet-name <REPORT_WORKSHEET> --range A1:D20 --values <VALUES_JSON> --verify
mbs excel-worksheet range set-formula --doc-id <DOC_ID> --worksheet-name <REPORT_WORKSHEET> --cell E2 --formula '=<FORMULA>'
mbs excel-worksheet calculate --doc-id <DOC_ID> --worksheet-name <REPORT_WORKSHEET>
mbs excel-worksheet check-error --doc-id <DOC_ID> --worksheet-name <REPORT_WORKSHEET>
```

Verify the assigned engine after creation with `mbs workbook list-worksheets --doc-id <DOC_ID> --output json`. If the result is Base, stop using A1/range
or cell formula instructions and switch to the Base verification runbook.
