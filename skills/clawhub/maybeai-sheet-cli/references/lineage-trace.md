# Formula Lineage and Computation Evidence

## 1. Select the model before tracing

A question about a computed value may concern three different producers:

| Target | Correct identity | Evidence to inspect |
|---|---|---|
| Excel Sheet formula | `worksheet_name` and A1 cell | `mbs formula lineage` |
| Base column Formula | `table_id`, `field_id`, record identity | Formula compile/recalculate evidence |
| Worksheet SQL Config | result worksheet and raw SQL config | stored SQL, preview, and materialization evidence |

Do not send a Base `field_id` to the A1 lineage command, and do not explain a
SQL Config result as though it were an ordinary formula cell.

## 2. Sheet formula lineage

`mbs formula lineage` is read-only A1-style dependency tracing for Sheet
targets and SQL result cells that the service exposes as cells.

```bash
mbs formula lineage --doc-id <DOC_ID> --worksheet-name Report --cell C2 --format tree --output yaml
mbs formula lineage --url <MAYBE_SHEET_URL> --worksheet-name Report --cell C2 --format node
```

`--cell` must be a concrete A1 address such as `C2` or `AE2`. Use
`--format tree` for a human explanation and `--format node` for a graph.

A tree result normally contains:

- `target`, `lineage`, and nested `depends_on`
- Sheet cells/ranges, column headers, and ordinary formula text
- an optional `produced_by` Worksheet SQL Config node
- SQL fingerprints, dependencies, and last-run state where SQL Config lineage
  is available

The trace is read-only. Read source values separately with
`excel-worksheet read` or `excel-table sample`.

## 3. Base column Formula evidence

Base Formula lineage is not an A1 dependency graph. Use the P5 Base Formula
surface:

```bash
mbs base-table field list --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table formula compile --doc-id <DOC_ID> --table-id <TABLE_ID> --field-id <FIELD_ID> --expression '<EXPRESSION>'
mbs base-table formula set --doc-id <DOC_ID> --table-id <TABLE_ID> --field-id <FIELD_ID> --expression '<EXPRESSION>'
mbs base-table formula recalculate --doc-id <DOC_ID> --worksheet-name <BASE_WORKSHEET> --table-id <TABLE_ID>
```

Retain the resolved `table_id`, target `field_id`, expression/compile result,
execution mode, executed fields or dirty-table result, field errors, and a
representative record read. These are the evidence for a Base computed column.

Do not substitute a cell lineage query, a range formula, or a row-2 template
for Base Formula evidence.

## 4. Worksheet SQL Config lineage

For an SQL-produced result, inspect the stored config and the materialized
output first:

```bash
mbs sql config get --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --output json
mbs sql preview --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --sql-file query.sql --output table
mbs sql overwrite --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --confirm-overwrite
```

Then use A1 lineage only when the target is a Sheet/SQL-result cell:

```bash
mbs formula lineage --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --cell C2 --format tree
```

Trace the `worksheet_sql_config`/SQL dependency nodes back to source
worksheets or Base tables. The authoritative query text is raw SQL in SQL
Config, not a cell formula.

## 5. Recovery

1. If metadata does not reveal the engine and object identity, stop and resolve
   it before tracing or writing.
2. If a Sheet A1 trace returns a source cell rather than a formula, inspect
   nearby cells and the source data.
3. If Base results are stale, obtain Formula execution evidence; a table sample
   alone cannot show whether recalculation ran.
4. If SQL output is stale or incomplete, inspect the saved config, preview the
   exact raw SQL, and validate the materialization result.
5. Existing legacy SQL wrapper cells are migration-only objects. Do not edit
   them through formula commands; use the SQL migration workflow.
